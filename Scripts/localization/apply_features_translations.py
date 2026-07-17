# -*- coding: utf-8 -*-
import json
from pathlib import Path

FEATURES = Path(__file__).resolve().parents[2] / "Config" / "Features.json"
TRANS = Path(__file__).resolve().parent / "features_translations_full.json"

data = json.loads(FEATURES.read_text(encoding="utf-8"))
translations = json.loads(TRANS.read_text(encoding="utf-8")) if TRANS.exists() else {}

def tr(s):
    if not s:
        return s
    return translations.get(s, s)

for g in data["UiGroups"]:
    for key in ("Label", "ToolTip"):
        if g.get(key):
            g[key] = tr(g[key])
    for v in g.get("Values", []):
        if v.get("Label"):
            v["Label"] = tr(v["Label"])

for feat in data["Features"]:
    for key in ("Label", "ToolTip", "ApplyText", "UndoLabel", "ApplyUndoText"):
        if feat.get(key):
            feat[key] = tr(feat[key])

FEATURES.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

remaining = set()
for g in data["UiGroups"]:
    for k in ("Label", "ToolTip"):
        if g.get(k) and not any("\u4e00" <= c <= "\u9fff" for c in g[k]):
            remaining.add(g[k])
    for v in g.get("Values", []):
        if v.get("Label") and not any("\u4e00" <= c <= "\u9fff" for c in v["Label"]):
            remaining.add(v["Label"])
for f in data["Features"]:
    for k in ("Label", "ToolTip", "ApplyText", "UndoLabel", "ApplyUndoText"):
        if f.get(k) and not any("\u4e00" <= c <= "\u9fff" for c in f[k]):
            remaining.add(f[k])

print(f"Applied {len(translations)} translations, {len(remaining)} strings still in English")
if remaining:
    out = Path(__file__).resolve().parent / "features_remaining.txt"
    out.write_text("\n".join(sorted(remaining)), encoding="utf-8")
