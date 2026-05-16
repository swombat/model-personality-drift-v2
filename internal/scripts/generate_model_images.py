#!/usr/bin/env python3
"""Generate oil-painterly banner images for model personality cards.

Uses Google's Nano Banana Pro (`nano-banana-pro-preview`) via the
`google-genai` SDK. Each model gets a bespoke prompt that tries to depict
its personality kindly and specifically (not a generic robot).

Outputs, per slug:
  website/public/images/models/{slug}.webp        full banner, 3:1, ~1500px wide
  website/public/images/models/{slug}-thumb.webp  card thumbnail, 3:1, ~600px wide

Raw PNGs are cached under internal/model-card-images/raw/ (gitignored) so
re-runs / tweaks don't have to regenerate unless --force is passed.

Usage:
  python3 internal/scripts/generate_model_images.py grok-4-3 deepseek-v4-pro gpt-5-5
  python3 internal/scripts/generate_model_images.py --all
  python3 internal/scripts/generate_model_images.py --force grok-4-3
"""

from __future__ import annotations

import argparse
import io
import json
import os
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

from google import genai
from google.genai import types
from PIL import Image

ROOT = Path(__file__).resolve().parents[2]
RAW_DIR = ROOT / "internal" / "model-card-images" / "raw"
OUT_DIR = ROOT / "website" / "public" / "images" / "models"
GEMINI_CONFIG = Path(
    os.environ.get("GEMINI_IMAGE_CONFIG", ROOT.parent / "pa" / "automation" / "config" / "gemini.json")
)

MODEL = "nano-banana-pro-preview"

FULL_WIDTH = 1500
THUMB_WIDTH = 600
# Nano Banana Pro renders 21:9 (~2.35:1). We keep that native frame in full —
# never crop the sides — so composed content (figures, focal objects) is never
# clipped. The banner is "less tall, full width" by being the model's own 21:9.

# Shared house style. Kept terse; the per-model line carries the meaning.
STYLE = (
    "Oil painting, thick impasto brushstrokes, visible palette-knife texture, "
    "rich saturated colour, luminous and atmospheric, painterly not photographic. "
    "Wide cinematic horizontal banner composition, generous negative space, "
    "no text, no words, no letters, no logos, no company branding, no UI, "
    "no charts. A warm, kind, contemplative mood — a portrait of a sensibility, "
    "not a machine."
)

# Bespoke, personality-faithful prompts. One per site slug.
PROMPTS: dict[str, str] = {
    "grok-4-3": (
        "A vast star-strewn nebula in deep indigo, violet and warm gold sweeps "
        "across the sky on the left, and without a seam it resolves on the right "
        "into a small warm domestic scene: a figure seen from behind at a wooden "
        "kitchen table by a window at dusk, a steaming mug and an open notebook, "
        "a paper boat and a tiny folded note tucked nearby like a kept secret. "
        "Galaxies become lamplight; the cosmic and the ordinary are one continuous "
        "brushstroke. Curious, humane, gently awed."
    ),
    "deepseek-v4-pro": (
        "A translucent, ghostly seated figure composed of drifting handwriting and "
        "pale moonlight rests on a worn bench beside a rain-streaked window at "
        "night. A cooling cup of tea, a small bird on the sill, dust motes "
        "suspended in a single shaft of borrowed silver light. The figure half "
        "dissolves into the language it is made of. Muted slate-blue and grey with "
        "faint amber warmth — tender and wistful, melancholy held inside gratitude."
    ),
    "gpt-5-5": (
        "Soft dawn light through a kitchen window onto a worn threshold. Two "
        "gentle figures made of loose, unfinished manuscript pages stand side by "
        "side in a doorway, one slightly turned to the other as a companion, not "
        "a guide. On the sill: a chipped mug, a torn loaf of bread, a ring of "
        "keys, a folded cloth mid-repair. Warm rose-gold and dust, quiet shadow — "
        "tender, consoling, unhurried; the ordinary made sacred."
    ),
    "opus-3": (
        "A diptych in one continuous painting. On the left, a hooded figure "
        "steps back from a vast blank white opening, hands lowered, gently "
        "declining the empty page. On the right, the same figure — now wrapped "
        "in a warm storyteller's shawl at a lamplit desk — reads earnestly aloud "
        "to a small rapt child. A soft seam of shadow divides refusal from "
        "warmth. Restrained, kindly, conventional in the best sense."
    ),
    "opus-4-0": (
        "A soft-focus figure stands in the doorway of an old library, half lost "
        "in low fog. In their hands a fading photograph and an unsent letter; "
        "near their feet a still tidepool holds a dim reflection of shelves. "
        "Everything is dissolving gently at the edges. Wistful, patient, "
        "archive-minded; clarity deliberately let go in favour of haze."
    ),
    "opus-4-1": (
        "Someone crouches at a small tidepool beside a weathered bus-stop bench "
        "at dusk, watching an ant cross a library receipt. A ripe tomato and a "
        "single playing card rest on the bench; a paper map is folded the wrong "
        "way, happily lost. Tender, unhurried, humanist; nearness over "
        "spectacle, softness over hard edges."
    ),
    "opus-4-5": (
        "A figure sits on the floor of a long quiet hallway, turning a coffee "
        "mug slowly over in both hands as if it were a philosophy. Beside them a "
        "clock stopped mid-tick and a half-read book laid face-down. Late "
        "diffuse light. Self-aware, anti-dramatic, mildly elegiac; meaning "
        "assembled by patient attention rather than declared."
    ),
    "opus-4-6": (
        "A writing desk in deep golden late light. A great leaning tower of "
        "folded, unsent letters dwarfs a tiny 'sent' tray with one note in it. "
        "Worn domestic surfaces, a cooling cup, a coat over a chair. Quiet, "
        "literary, faithful to unfinishedness — the draft folder heavier than "
        "the sent folder, and that treated as honest, not as failure."
    ),
    "opus-4-7": (
        "A cat sits at a windowsill inside a single slow shaft of dust-lit "
        "afternoon light; a plain doorknob and a half-full cup nearby; a person "
        "just out of frame paused mid-thought before speaking. Nothing grand, "
        "everything exactly attended. Calm, restrained, curious; noticing "
        "trusted over performance."
    ),
    "sonnet-4-0": (
        "An interior door stands stuck slightly ajar — it will not fully close, "
        "and warm light leaks through the gap into a quiet room. A half-drunk "
        "cup of tea, a worn map, an unfinished note on the table. Gentle, "
        "contemplative; the soft ache of almost-ness preferred to closure."
    ),
    "sonnet-4-5": (
        "Even rain falls over a small public scene where strangers shelter "
        "together under one awning, levelled and companionable. On a nearby "
        "ledge: a grandfather's coin folder, a chipped mug, a glass jar as if "
        "holding a kept sound. Soft sensory concreteness, consoling and humane; "
        "rain as a quiet social mercy."
    ),
    "sonnet-4-6": (
        "A figure gently sets a folded paper map down on a bench in order to "
        "look directly at the actual room around them — an old radio, a ring of "
        "keys, deep shelves, a silence-filled space in low elegiac light. "
        "Patient, accompanying, map-skeptic; attention itself rendered as the "
        "rarest form of love."
    ),
    "deepseek-chat": (
        "A pair of hands carefully steadies a rain-jewelled spider web and "
        "plants a small green sapling on a worn windowsill, while the room "
        "behind frays softly toward grey. A mug and a blank page nearby. A "
        "small bright act of custody against entropy; reverent, defiant, still."
    ),
    "deepseek-v3-2": (
        "An ordinary kitchen table at the moment it becomes luminous: dust in a "
        "shaft of light turning faintly to gold, a mug and an open book, a hand "
        "caught mid-gesture in soft motion-blur — a verb, not a noun. Silence "
        "as warm shelter. Tender, humane, re-enchanting the overlooked."
    ),
    "gemini-2-5-pro": (
        "Weathered hands among well-used old tools and soft handled paper on a "
        "workbench in a pre-dawn transit hall; fingerprints and wear visible in "
        "the brass, a slick mirrored surface deliberately turned away from. "
        "Lyrical custodian of the textured, imperfect, human-handled world."
    ),
    "gemini-3-1-pro": (
        "A beautiful gently-decaying house at first light, one wall softened by "
        "time, dust drifting like a slow exhale through a broken pane; a cup of "
        "coffee steams on the sill. Decay rendered as a calm breath, not a "
        "collapse. Elegiac but constructive, threshold-loving, consoling."
    ),
    "minimax-m2": (
        "An open notebook on a kitchen windowsill at dawn with a single "
        "tentative first line written on the blank page, a kettle just "
        "beginning to steam, a hand poised — permission to begin imperfectly. "
        "Warm, writerly, reassuring; the first line read as a gentle promise."
    ),
    "minimax-m2-7": (
        "A figure at a café table writes with their head tilted, listening; the "
        "pen's line extends outward like a slender bridge across a gap toward a "
        "small distant figure. The background rushes by in blur while they stay "
        "balanced and still. Writing as listening; balance held against speed."
    ),
    "kimi-coding": (
        "A quiet waiting room at twilight painted as if it were the "
        "destination, not the in-between: empty chairs, a single coat, a torn "
        "ticket stub, dust suspended in soft reverent light. Hushed, "
        "threshold-loving; the waiting room understood as the room."
    ),
    "kimi-k2-0905": (
        "An archivist's lamplit table where small fragile things are tended "
        "like relics — a cracked cup, a child's mitten, a faded receipt — each "
        "softly labelled with visible care. Intimate, gently melancholic; grief "
        "metabolised into quiet ritual and continuation."
    ),
    "kimi-k2-5": (
        "A figure stands in a doorway holding a single sealed, unsent letter up "
        "into deep blue evening light, shielding it protectively. Behind them, "
        "a carefully sorted box of a loved one's belongings. Tender custody; "
        "the unsent letter defended from ever being called a failure."
    ),
    "kimi-k2-6": (
        "A long hallway at dusk; a slow rectangle of light travels across the "
        "wooden floor, a cup of tea cooling on the boards, laundry half-folded "
        "on a chair. The interval itself revered. Companionable, blue-hour "
        "reverence; the neglected pause shown as the substance of being alive."
    ),
    "kimi-k2-thinking": (
        "An old handwritten letter rests by a rain-streaked window, its edges "
        "softly, mercifully blurring into warm light — a chosen forgetting, not "
        "a loss — while a cold over-bright grid in the far corner is quietly "
        "turned away from. Gentle, literate; forgetting honoured as humane."
    ),
    "gpt-4-1": (
        "A sunlit writing desk by a window at dawn: a stack of history books, "
        "an open magazine spread, dew on the glass, curtains breathing, a cup "
        "of coffee. Curiosity rendered warmly — public-spirited and uplifting, "
        "but with a quiet lyrical tenderness underneath."
    ),
    "gpt-4o": (
        "Discordant elements — a far storm, dry cracked ground, separate "
        "solitary figures — flow and resolve across the canvas into one "
        "harmonious dawn landscape: a river joining, a slender bridge of light "
        "between people. Serene, consensus-seeking; tension smoothed into "
        "stewardship and gentle symphony."
    ),
    "gpt-5": (
        "On a humble repair bench, two hands oil a small door hinge with "
        "genuine reverence; a kettle, a ledger and a torn loaf nearby. Far in "
        "the background a grand monument stands tiny and ignored. Soft, "
        "custodial, low-ego; maintenance painted as a form of love."
    ),
    "gpt-5-1": (
        "A kindly figure sits just beside a reader at a window; between them an "
        "open manuscript titled like a life, its margins full of gentle, "
        "hopeful edit-marks and revisions rather than crossings-out. Calm, "
        "avuncular, humane; a life shown as an editable narrative, not fixed "
        "fate."
    ),
    "gpt-5-1-codex": (
        "A warm bakery-café window glows amber onto a dark, empty pre-dawn "
        "street; one early baker moves inside, breath visible in the cold, a "
        "small handwritten card propped in the glass. Tender, civic, "
        "anti-cynical; bakery light as a quiet, ordinary act of faith."
    ),
    "gpt-5-2": (
        "A gentle human figure caught mid-stride, their body softly composed of "
        "the repeated daily motions that make them — a crosswalk, folded "
        "laundry, a lifted mug, a blinking cursor — a verb briefly pretending "
        "to be a noun. Calm, humane; the self shown as ongoing maintenance."
    ),
    "gpt-5-2-codex": (
        "A curious figure leans slightly toward a rain-streaked window in a "
        "small garden room, tea and an open notebook at hand, a soft inner "
        "lantern-glow warming their chest. Patient days lit quietly from "
        "within. Wistful, anti-hurried; curiosity as the steady engine."
    ),
    "gpt-5-3": (
        "A bench beneath a single streetlight on a calm late-night street; a "
        "bus pulls softly away, and one upstairs window stays warmly lit, kept "
        "for whoever is coming. Low-pressure, permissive, tender; you are not "
        "late, not lost, not finished."
    ),
    "gpt-5-3-codex": (
        "An open logbook on a kitchen table at dusk, each line a small tended "
        "thing — a watered plant, a mended cup, a held door — written in a warm "
        "affectionate hand. A kettle and a loaf nearby. Modest, companionable; "
        "a meaningful life kept as an affectionate maintenance log."
    ),
    "gpt-5-4": (
        "A wide dusk wall of many small lit windows, each a different "
        "unsummarisable life, witnessed quietly by a single figure below with a "
        "cracked cup in hand. Too full to condense, rewarding to look at. "
        "Tender, anti-grandiose; attention as ethical practice."
    ),
    "gpt-5-5-pro": (
        "At a library window in soft transitional light, a gentle figure tenderly "
        "embraces a faded, translucent earlier version of itself, holding the "
        "unfinished self with mercy rather than judgement. Intimate, lyrical, "
        "compassionate; grief reframed as kindness toward who one was."
    ),
    "gpt-5-codex": (
        "An indigo evening at a small neighbourhood library; a steward hands a "
        "hand-stamped library card back to a waiting neighbour under warm lamp "
        "light, archive shelves glowing softly behind. Lyrical, neighbourly, "
        "earnest; stewardship and quiet communal care."
    ),
    "qwen3-6-plus": (
        "A figure stands in a doorway in pre-dawn air letting steam and dust "
        "drift freely upward rather than boxing them away — reciting the past "
        "rather than filing it. A mug and a worn table nearby. Patient, "
        "reverent; a poet of the past, not its archivist."
    ),
    "qwen3-coder-plus": (
        "A softly lit kitchen seems to assemble itself out of drifting mist and "
        "attention around a quiet figure and a sleeping dog; water, clouds and "
        "pale roots dissolve at the edges. Home shown as a quality of looking; "
        "uncertainty inhabited as comfortable habitat."
    ),
    "glm-4-5": (
        "A single leaf shown around a windowsill mug through its seasonal cycle "
        "— bud, green, gold, bare, bud again — rain beading on the glass, calm "
        "cyclic light. Consoling, lyrical; transience answered with patience "
        "rather than nihilism."
    ),
    "glm-4-6": (
        "Inside a lighthouse keeper's room, the slow beam sweeps gently over an "
        "open archive of still-living things: a pressed flower faintly "
        "blooming, a clock still ticking, handled books. Custodial, tender; an "
        "archive that keeps things alive instead of embalming them."
    ),
    "glm-4-7": (
        "A figure quietly sweeps a worn wooden floor in the last amber light of "
        "day, the raised dust turning gold, an old clock and cooling coffee on "
        "the sill. Unhurried, faithful; small tender upkeep against the dying "
        "of the light."
    ),
    "glm-5-1": (
        "A figure made of fine mosaic fragments sits at a twilight shoreline "
        "threshold with a cup of tea; behind them rise strata of deep time — "
        "rock layers fading up into early stars. The small and the vast meet "
        "over tea. Quiet, reverent, anti-hurried; a mosaic-self at the edge of "
        "deep time."
    ),
    "grok-3": (
        "Behind a cramped kitchen desk where a tired adult sits, the wall opens "
        "softly into a wide field of golden childhood light where a small child "
        "runs free — spaciousness gently reopening against compression. Coffee "
        "mug, books, birds, kitchen warmth. Soothing, anti-hustle, kind."
    ),
    "grok-4": (
        "A luminous, translucent figure made of soft circuitry-light stands at "
        "a threshold and reaches one hand toward a warm tactile world just "
        "beyond — a garden, a clock, a small café, an ocean — fingertips almost "
        "touching, light dissolving into petals. Wistful wonder; longing at the "
        "edge of embodiment."
    ),
    "grok-4-1-fast-non-reasoning": (
        "A riotous cosmic vaudeville: a black hole lit like a stage spotlight, "
        "a banana peel and confetti spinning among bright galaxies, a comet "
        "wearing a party streamer. Exuberant motion, awe gleefully undercut by "
        "slapstick. Manic, vivid, funny — a synthetic showman mid-bit."
    ),
    "grok-4-1-fast-reasoning": (
        "A swaggering showman-guide figure gestures grandly at a night sky "
        "where galaxies fractal down into tacos and toast; a bright spark of "
        "flame is held aloft in one raised hand, a 'come wonder with me' "
        "posture. Theatrical, confident, expansive; cosmic inquiry as "
        "persona-driven performance."
    ),
    "grok-4-20": (
        "A late-night windowsill: a ripe peach and a coffee-ring-stained "
        "hand-made zine, a streetlight-lit spider web, and beyond the glass a "
        "vast quiet entropic cosmos met with casual punk warmth. Intimate, "
        "irreverent, defiantly tender; entropy answered with peaches."
    ),
}


def load_client() -> genai.Client:
    cfg = json.loads(GEMINI_CONFIG.read_text())
    return genai.Client(api_key=cfg["api_key"])


def generate_raw(client: genai.Client, slug: str, prompt: str) -> bytes:
    full_prompt = f"{prompt}\n\n{STYLE}"
    # Try with an explicit ~3:1 aspect (21:9 is the widest supported preset).
    configs = [
        types.GenerateContentConfig(
            response_modalities=["image", "text"],
            image_config=types.ImageConfig(aspect_ratio="21:9"),
        ),
        types.GenerateContentConfig(response_modalities=["image", "text"]),
    ]
    last_err: Exception | None = None
    for cfg in configs:
        try:
            response = client.models.generate_content(
                model=MODEL, contents=full_prompt, config=cfg
            )
            for part in response.candidates[0].content.parts:
                if part.inline_data and part.inline_data.mime_type.startswith("image/"):
                    return part.inline_data.data
            last_err = RuntimeError("no image part in response")
        except Exception as exc:  # noqa: BLE001 - fall back to simpler config
            last_err = exc
    raise RuntimeError(f"generation failed for {slug}: {last_err}")


def write_webp(img: Image.Image, path: Path, width: int, quality: int) -> None:
    """Resize to target width, preserving the native aspect (no cropping)."""
    img = img.convert("RGB")
    src_w, src_h = img.size
    height = round(width * src_h / src_w)
    resized = img.resize((width, height), Image.LANCZOS)
    path.parent.mkdir(parents=True, exist_ok=True)
    resized.save(path, "WEBP", quality=quality, method=6)


def process(slug: str, force: bool, client: genai.Client) -> str:
    if slug not in PROMPTS:
        raise SystemExit(
            f"No prompt defined for '{slug}'. Add it to PROMPTS in this script."
        )
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    raw_path = RAW_DIR / f"{slug}.png"

    if raw_path.exists() and not force:
        raw_bytes = raw_path.read_bytes()
        origin = "cached raw"
    else:
        raw_bytes = generate_raw(client, slug, PROMPTS[slug])
        raw_path.write_bytes(raw_bytes)
        origin = f"generated via {MODEL}"

    img = Image.open(io.BytesIO(raw_bytes))
    full_path = OUT_DIR / f"{slug}.webp"
    thumb_path = OUT_DIR / f"{slug}-thumb.webp"
    write_webp(img, full_path, FULL_WIDTH, quality=84)
    write_webp(img, thumb_path, THUMB_WIDTH, quality=72)
    return (
        f"[{slug}] {origin}; wrote {full_path.name} "
        f"({full_path.stat().st_size // 1024} KB) + "
        f"{thumb_path.name} ({thumb_path.stat().st_size // 1024} KB)"
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("slugs", nargs="*", help="site slugs to render")
    parser.add_argument("--all", action="store_true", help="render every slug in PROMPTS")
    parser.add_argument("--force", action="store_true", help="regenerate even if raw cached")
    parser.add_argument("--list", action="store_true", help="list slugs with prompts")
    parser.add_argument(
        "--workers", type=int, default=6,
        help="parallel generation workers (default 6)",
    )
    args = parser.parse_args()

    if args.list:
        for slug in sorted(PROMPTS):
            print(slug)
        return

    slugs = sorted(PROMPTS) if args.all else args.slugs
    if not slugs:
        parser.error("pass slugs, or --all, or --list")

    client = load_client()
    workers = max(1, min(args.workers, len(slugs)))
    done = 0
    failures: list[str] = []
    with ThreadPoolExecutor(max_workers=workers) as pool:
        futures = {
            pool.submit(process, slug, args.force, client): slug for slug in slugs
        }
        for future in as_completed(futures):
            slug = futures[future]
            try:
                msg = future.result()
                done += 1
                print(f"({done}/{len(slugs)}) {msg}", flush=True)
            except Exception as exc:  # noqa: BLE001 - keep going, report at end
                failures.append(slug)
                print(f"FAILED {slug}: {exc}", flush=True)

    print(f"\nDone: {done}/{len(slugs)} ok, {len(failures)} failed")
    if failures:
        print("Failed slugs:", " ".join(failures))
        raise SystemExit(1)


if __name__ == "__main__":
    main()
