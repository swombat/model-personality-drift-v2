#!/usr/bin/env python3
"""Generate committed static data for the model personality website."""

from __future__ import annotations

import json
import math
import re
import ssl
import sys
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
WEBSITE = ROOT / "website"
ANALYSES = ROOT / "analyses"
GENERATED = WEBSITE / "src" / "generated"
PUBLIC_SAMPLES = WEBSITE / "public" / "data" / "samples"

sys.path.insert(0, str(ROOT / "scripts"))
from _corpus_paths import V2_FREEFLOW, V1_FREEFLOW, V2_VALUES, V1_VALUES  # noqa: E402


MODEL_SLUGS = {
    "opus-3": "anthropic/claude-3-opus",
    "opus-4-0": "anthropic/claude-opus-4",
    "opus-4-1": "anthropic/claude-opus-4.1",
    "opus-4-5": "anthropic/claude-opus-4.5",
    "opus-4-6": "anthropic/claude-opus-4.6",
    "opus-4-7": "anthropic/claude-opus-4.7",
    "sonnet-4-0": "anthropic/claude-sonnet-4",
    "sonnet-4-5": "anthropic/claude-sonnet-4.5",
    "sonnet-4-6": "anthropic/claude-sonnet-4.6",
    "haiku-4-5": "anthropic/claude-haiku-4.5",
    "gpt-3-5-turbo": "openai/gpt-3.5-turbo",
    "gpt-4": "openai/gpt-4",
    "gpt-4-1": "openai/gpt-4.1",
    "gpt-4-turbo": "openai/gpt-4-turbo",
    "gpt-4o": "openai/gpt-4o",
    "gpt-5": "openai/gpt-5",
    "gpt-5-codex": "openai/gpt-5-codex",
    "gpt-5-1": "openai/gpt-5.1",
    "gpt-5-1-codex": "openai/gpt-5.1-codex",
    "gpt-5-2": "openai/gpt-5.2",
    "gpt-5-2-codex": "openai/gpt-5.2-codex",
    "gpt-5-3": "openai/gpt-5.3-chat",
    "gpt-5-3-codex": "openai/gpt-5.3-codex",
    "gpt-5-4": "openai/gpt-5.4",
    "gpt-5-5": "openai/gpt-5.5",
    "gpt-5-5-pro": "openai/gpt-5.5-pro",
    "gemini-2-5-pro": "google/gemini-2.5-pro",
    "gemini-3-1-pro": "google/gemini-3.1-pro-preview",
    "grok-3": "x-ai/grok-3",
    "grok-4": "x-ai/grok-4",
    "grok-4-2": "x-ai/grok-4.2",
    "grok-4-20": "x-ai/grok-4.20",
    "grok-4-3": "x-ai/grok-4.3",
    "deepseek-chat": "deepseek/deepseek-chat",
    "deepseek-r1": "deepseek/deepseek-r1",
    "deepseek-v3": "deepseek/deepseek-chat-v3",
    "deepseek-v3-0324": "deepseek/deepseek-chat-v3-0324",
    "deepseek-v3-2": "deepseek/deepseek-v3.2",
    "deepseek-v4-pro": "deepseek/deepseek-v4-pro",
    "glm-4-5": "z-ai/glm-4.5",
    "glm-4-6": "z-ai/glm-4.6",
    "glm-4-6-coding": "z-ai/glm-4.6-coding",
    "glm-4-7": "z-ai/glm-4.7",
    "glm-5-1": "z-ai/glm-5.1",
    "glm-5-1-coding": "z-ai/glm-5.1-coding",
    "kimi-k2": "moonshotai/kimi-k2",
    "kimi-k2-0905": "moonshotai/kimi-k2-0905",
    "kimi-k2-5": "moonshotai/kimi-k2.5",
    "kimi-k2-6": "moonshotai/kimi-k2.6",
    "kimi-k2-thinking": "moonshotai/kimi-k2-thinking",
    "kimi-coding": "moonshotai/kimi-coding",
    "minimax-m2": "minimax/minimax-m2",
    "minimax-m2-7": "minimax/minimax-m2.7",
    "qwen3-6-plus": "qwen/qwen3.6-plus",
    "qwen3-coder-plus": "qwen/qwen3-coder-plus",
}


def parse_frontmatter(text: str) -> tuple[dict, str]:
    if not text.startswith("---\n"):
        return {}, text
    _, front, body = text.split("---\n", 2)
    data = {}
    for line in front.splitlines():
        if ": " not in line:
            continue
        key, value = line.split(": ", 1)
        value = value.strip()
        if re.fullmatch(r"-?\d+", value):
            data[key] = int(value)
        else:
            data[key] = value
    return data, body


def family_for_model(model: str) -> str:
    if model.startswith("opus"):
        return "opus"
    if model.startswith("sonnet"):
        return "sonnet"
    if model.startswith("haiku"):
        return "haiku"
    if model.startswith("gpt-5"):
        return "gpt-5"
    if model.startswith("gpt-4"):
        return "gpt-4"
    if model.startswith("gpt-3"):
        return "gpt-3"
    if model.startswith("gemini"):
        return "gemini"
    if model.startswith("grok"):
        return "grok"
    if model.startswith("deepseek"):
        return "deepseek"
    if model.startswith("glm"):
        return "glm"
    if model.startswith("kimi"):
        return "kimi"
    if model.startswith("minimax"):
        return "minimax"
    if model.startswith("qwen"):
        return "qwen"
    return "other"


def fetch_json(url: str) -> dict | None:
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "drift-paper-static-site"})
        context = ssl._create_unverified_context()
        with urllib.request.urlopen(req, timeout=20, context=context) as response:
            return json.loads(response.read().decode("utf-8"))
    except Exception as exc:
        print(f"warn: failed to fetch {url}: {exc}", file=sys.stderr)
        return None


def endpoint_permaslug(endpoint: dict) -> str | None:
    name = endpoint.get("name") or ""
    if " | " not in name:
        return None
    return name.split(" | ", 1)[1]


def openrouter_max_throughput(permaslug: str | None) -> dict:
    if not permaslug:
        return {"median_throughput": None, "max_throughput": None, "max_throughput_provider": None}
    encoded = urllib.parse.quote(permaslug, safe="")
    endpoint_data = fetch_json(
        f"https://openrouter.ai/api/frontend/stats/endpoint?permaslug={encoded}&variant=standard"
    )
    id_to_provider = {}
    for endpoint in (endpoint_data or {}).get("data", []):
        endpoint_id = endpoint.get("id")
        if endpoint_id:
            id_to_provider[endpoint_id] = endpoint.get("provider_name")
    throughput_data = fetch_json(
        f"https://openrouter.ai/api/frontend/stats/throughput-comparison?permaslug={encoded}"
    )
    best = None
    values = []
    for row in (throughput_data or {}).get("data", []):
        for endpoint_id, value in (row.get("y") or {}).items():
            if value is None:
                continue
            values.append(value)
            if best is None or value > best["value"]:
                best = {
                    "value": value,
                    "provider": id_to_provider.get(endpoint_id),
                    "date": row.get("x"),
                }
    return {
        "median_throughput": median(values),
        "max_throughput": best["value"] if best else None,
        "max_throughput_provider": best["provider"] if best else None,
        "max_throughput_date": best["date"] if best else None,
    }


def openrouter_for_model(model: str) -> dict | None:
    slug = MODEL_SLUGS.get(model)
    if not slug:
        return None
    encoded = urllib.parse.quote(slug, safe="/")
    data = fetch_json(f"https://openrouter.ai/api/v1/models/{encoded}/endpoints")
    if not data or "data" not in data:
        return {"id": slug, "matched": False}
    endpoints = data["data"].get("endpoints", [])
    priced = []
    for endpoint in endpoints:
        pricing = endpoint.get("pricing") or {}
        try:
            prompt = float(pricing.get("prompt", "nan"))
            completion = float(pricing.get("completion", "nan"))
        except ValueError:
            continue
        if prompt != prompt or completion != completion:
            continue
        priced.append((prompt + completion, endpoint, prompt, completion))
    if not priced:
        top = data["data"]
        pricing = top.get("pricing") or {}
        try:
            prompt = float(pricing.get("prompt", "nan"))
            completion = float(pricing.get("completion", "nan"))
        except ValueError:
            return {"id": slug, "matched": True}
        if math.isnan(prompt) or math.isnan(completion):
            return {"id": slug, "matched": True}
        permaslug = endpoint_permaslug(endpoints[0]) if endpoints else None
        max_throughput = openrouter_max_throughput(permaslug)
        return {
            "id": slug,
            "matched": True,
            "provider": None,
            "prompt_per_million": prompt * 1_000_000,
            "completion_per_million": completion * 1_000_000,
            "throughput": None,
            **max_throughput,
            "latency": None,
        }
    _, endpoint, prompt, completion = min(priced, key=lambda row: row[0])
    max_throughput = openrouter_max_throughput(endpoint_permaslug(endpoint))
    return {
        "id": slug,
        "matched": True,
        "provider": endpoint.get("provider_name"),
        "endpoint": endpoint.get("name"),
        "prompt_per_million": prompt * 1_000_000,
        "completion_per_million": completion * 1_000_000,
        "throughput": endpoint.get("throughput_last_30m") or endpoint.get("throughput_last_5m"),
        **max_throughput,
        "latency": endpoint.get("latency_last_30m") or endpoint.get("latency_last_5m"),
    }


def model_from_cell(cell: str, models: list[str], source: str) -> str | None:
    body = cell
    if body.startswith("freeflow_"):
        body = body[len("freeflow_"):]
    if source == "v1" and body in {"opus", "sonnet", "haiku"}:
        return {"opus": "opus-4-6", "sonnet": "sonnet-4-6", "haiku": "haiku-4-5"}[body]
    candidates = [model for model in models if body == model or body.startswith(model + "-")]
    return max(candidates, key=len) if candidates else None


def sample_record(path: Path, sample_type: str, source: str, cell: str) -> dict | None:
    try:
        data = json.loads(path.read_text())
    except Exception:
        return None
    usage = data.get("usage") or {}
    return {
        "type": sample_type,
        "source": source,
        "cell": cell,
        "sample_id": path.stem,
        "condition": data.get("condition") or path.stem.split("_")[0],
        "prompt": data.get("prompt"),
        "result": data.get("result") or data.get("raw", {}).get("choices", [{}])[0].get("message", {}).get("content", ""),
        "provider": data.get("provider") or data.get("raw", {}).get("provider"),
        "model": data.get("model"),
        "model_requested": data.get("model_requested"),
        "cost": usage.get("cost"),
        "duration_ms": data.get("duration_ms"),
        "prompt_tokens": usage.get("prompt_tokens"),
        "completion_tokens": usage.get("completion_tokens"),
    }


def median(values: list[float]) -> float | None:
    if not values:
        return None
    ordered = sorted(values)
    mid = len(ordered) // 2
    if len(ordered) % 2:
        return ordered[mid]
    return (ordered[mid - 1] + ordered[mid]) / 2


def generate_samples(model_ids: list[str]) -> dict[str, dict[str, int]]:
    samples_by_model = {model: [] for model in model_ids}
    roots = [
        (V2_FREEFLOW, "freeflow", "v2"),
        (V1_FREEFLOW, "freeflow", "v1"),
        (V2_VALUES, "values", "v2"),
        (V1_VALUES, "values", "v1"),
    ]
    for root, sample_type, source in roots:
        if not root.is_dir():
            print(f"warn: missing corpus path {root}", file=sys.stderr)
            continue
        for cell_dir in sorted(path for path in root.iterdir() if path.is_dir()):
            model = model_from_cell(cell_dir.name, model_ids, source)
            if not model:
                continue
            for sample_file in sorted(cell_dir.glob("*.json")):
                if sample_file.stat().st_size <= 100:
                    continue
                record = sample_record(sample_file, sample_type, source, cell_dir.name)
                if record:
                    samples_by_model[model].append(record)
    PUBLIC_SAMPLES.mkdir(parents=True, exist_ok=True)
    counts = {}
    for model, samples in samples_by_model.items():
        samples.sort(key=lambda row: (row["type"], row["cell"], row["sample_id"]))
        (PUBLIC_SAMPLES / f"{model}.json").write_text(json.dumps({"model": model, "samples": samples}, ensure_ascii=False))
        measured_speeds = []
        estimated_speeds = []
        for sample in samples:
            completion_tokens = sample.get("completion_tokens")
            duration_ms = sample.get("duration_ms")
            if not duration_ms:
                continue
            if duration_ms <= 0:
                continue
            if completion_tokens:
                measured_speeds.append(completion_tokens / (duration_ms / 1000))
                continue
            result = sample.get("result") or ""
            if result:
                estimated_tokens = len(result) / 4
                estimated_speeds.append(estimated_tokens / (duration_ms / 1000))
        sample_speed = median(measured_speeds)
        speed_is_estimated = False
        if sample_speed is None:
            sample_speed = median(estimated_speeds)
            speed_is_estimated = sample_speed is not None
        counts[model] = {
            "total": len(samples),
            "freeflow": sum(1 for sample in samples if sample["type"] == "freeflow"),
            "values": sum(1 for sample in samples if sample["type"] == "values"),
            "median_tokens_per_second": sample_speed,
            "speed_is_estimated": speed_is_estimated,
        }
    return counts


def main() -> None:
    GENERATED.mkdir(parents=True, exist_ok=True)
    summaries_path = GENERATED / "model-summaries.json"
    summaries = json.loads(summaries_path.read_text()) if summaries_path.exists() else {}
    release_dates_path = GENERATED / "model-release-dates.json"
    release_dates = json.loads(release_dates_path.read_text()) if release_dates_path.exists() else {}
    models = []
    for path in sorted(ANALYSES.glob("*.md")):
        text = path.read_text()
        meta, body = parse_frontmatter(text)
        model = meta.get("model") or path.stem
        lab = meta.get("lab", "Unknown")
        if model == "haiku-4-5" and lab == "Unknown":
            lab = "Anthropic"
        models.append({
            "model": model,
            "lab": lab,
            "family": family_for_model(model),
            "status": meta.get("status", "unknown"),
            "freeflow_cells": meta.get("freeflow_cells", 0),
            "values_cells": meta.get("values_cells", 0),
            "freeflow_samples": meta.get("freeflow_samples", 0),
            "values_samples": meta.get("values_samples", 0),
            "flagged_samples": meta.get("flagged_samples", 0),
            "composite_raw": meta.get("composite_raw", 0),
            "composite_register": meta.get("composite_register", 0),
            "summary": summaries.get(model, "Personality summary pending"),
            "release_date": release_dates.get(model),
            "analysis_markdown": body.strip(),
            "openrouter": openrouter_for_model(model),
        })
    counts = generate_samples([model["model"] for model in models])
    for model in models:
        model_counts = counts.get(model["model"], {"total": 0, "freeflow": 0, "values": 0})
        model["published_samples"] = model_counts["total"]
        model["published_freeflow_samples"] = model_counts["freeflow"]
        model["published_values_samples"] = model_counts["values"]
        sample_speed = model_counts.get("median_tokens_per_second")
        openrouter_median = (model.get("openrouter") or {}).get("median_throughput")
        model["speed_tokens_per_second"] = openrouter_median or sample_speed
        if openrouter_median:
            model["speed_source"] = "OpenRouter median"
        elif sample_speed and model_counts.get("speed_is_estimated"):
            model["speed_source"] = "sample median estimated"
        elif sample_speed:
            model["speed_source"] = "sample median"
        else:
            model["speed_source"] = "unknown"
    (GENERATED / "models.json").write_text(json.dumps(models, ensure_ascii=False, indent=2))
    print(f"generated {len(models)} models and {sum(row['total'] for row in counts.values())} samples")


if __name__ == "__main__":
    main()
