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
import sys
from pathlib import Path

from google import genai
from google.genai import types
from PIL import Image

ROOT = Path(__file__).resolve().parents[2]
RAW_DIR = ROOT / "internal" / "model-card-images" / "raw"
OUT_DIR = ROOT / "website" / "public" / "images" / "models"
GEMINI_CONFIG = Path("/Users/danieltenner/dev/pa/automation/config/gemini.json")

MODEL = "nano-banana-pro-preview"

FULL_WIDTH = 1500
THUMB_WIDTH = 600
ASPECT_W, ASPECT_H = 3, 1  # final crop ratio

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


def crop_to_ratio(img: Image.Image) -> Image.Image:
    img = img.convert("RGB")
    w, h = img.size
    target = ASPECT_W / ASPECT_H
    if w / h > target:  # too wide -> trim sides
        new_w = int(h * target)
        left = (w - new_w) // 2
        return img.crop((left, 0, left + new_w, h))
    # too tall -> trim top/bottom
    new_h = int(w / target)
    top = (h - new_h) // 2
    return img.crop((0, top, w, top + new_h))


def write_webp(img: Image.Image, path: Path, width: int, quality: int) -> None:
    height = round(width * ASPECT_H / ASPECT_W)
    resized = img.resize((width, height), Image.LANCZOS)
    path.parent.mkdir(parents=True, exist_ok=True)
    resized.save(path, "WEBP", quality=quality, method=6)


def process(slug: str, force: bool) -> None:
    if slug not in PROMPTS:
        raise SystemExit(
            f"No prompt defined for '{slug}'. Add it to PROMPTS in this script."
        )
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    raw_path = RAW_DIR / f"{slug}.png"

    if raw_path.exists() and not force:
        print(f"[{slug}] using cached raw ({raw_path.name})")
        raw_bytes = raw_path.read_bytes()
    else:
        print(f"[{slug}] generating via {MODEL} ...")
        client = load_client()
        raw_bytes = generate_raw(client, slug, PROMPTS[slug])
        raw_path.write_bytes(raw_bytes)
        print(f"[{slug}] saved raw -> {raw_path}")

    img = crop_to_ratio(Image.open(io.BytesIO(raw_bytes)))
    full_path = OUT_DIR / f"{slug}.webp"
    thumb_path = OUT_DIR / f"{slug}-thumb.webp"
    write_webp(img, full_path, FULL_WIDTH, quality=84)
    write_webp(img, thumb_path, THUMB_WIDTH, quality=72)
    print(
        f"[{slug}] wrote {full_path.name} "
        f"({full_path.stat().st_size // 1024} KB) and "
        f"{thumb_path.name} ({thumb_path.stat().st_size // 1024} KB)"
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("slugs", nargs="*", help="site slugs to render")
    parser.add_argument("--all", action="store_true", help="render every slug in PROMPTS")
    parser.add_argument("--force", action="store_true", help="regenerate even if raw cached")
    parser.add_argument("--list", action="store_true", help="list slugs with prompts")
    args = parser.parse_args()

    if args.list:
        for slug in sorted(PROMPTS):
            print(slug)
        return

    slugs = sorted(PROMPTS) if args.all else args.slugs
    if not slugs:
        parser.error("pass slugs, or --all, or --list")

    for slug in slugs:
        process(slug, force=args.force)


if __name__ == "__main__":
    main()
