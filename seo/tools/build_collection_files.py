#!/usr/bin/env python3
"""Build the collection admin-action files from seo/content/collections/*.md.

Each .md file is the single source of truth for one collection:

    ---
    handle: super-king-mattresses
    status: existing | new
    priority: 1            (push order; lower first)
    h1: ...                (becomes the collection title — the theme prints it as the H1)
    seo_title: ...
    seo_description: ...
    related: handle, handle, ...
    verify: note | note    (things a human must confirm)
    hold: yes              (optional: don't push yet)
    faqs_in_template: yes  (optional: FAQs live in the theme template, not the metafield)
    title/type/rule/template   (new collections only)
    ---
    ## Intro
    <p>HTML…</p>
    ## FAQs
    Question|Answer
    ...

Outputs (seo/admin-actions/):
    seo-metadata.csv          type,handle,seo_title,seo_description,h1 (+ priority/status/verify)
    collection-metafields.csv handle,custom.seo_intro,custom.faqs,custom.related_collections
    new-collections.csv       spec for collections that don't exist yet

Run:  python3 seo/tools/build_collection_files.py      (exits 1 if a rule is broken)
"""
import csv
import html
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
SRC = ROOT / "content" / "collections"
OUT = ROOT / "admin-actions"


def parse(path):
    text = path.read_text(encoding="utf-8")
    m = re.match(r"---\n(.*?)\n---\n?(.*)", text, re.S)
    if not m:
        sys.exit(f"{path.name}: missing front matter")
    meta = {}
    for line in m.group(1).splitlines():
        key, _, value = line.partition(":")
        meta[key.strip()] = value.strip()
    body = m.group(2)
    intro = faqs = ""
    im = re.search(r"## Intro\n(.*?)(?=\n## FAQs|\Z)", body, re.S)
    if im:
        intro = im.group(1).strip()
    fm = re.search(r"## FAQs\n(.*)", body, re.S)
    if fm:
        faqs = "\n".join(l.strip() for l in fm.group(1).splitlines() if l.strip())
    meta["intro"] = intro
    meta["faqs"] = faqs
    meta["related"] = [h.strip() for h in meta.get("related", "").split(",") if h.strip()]
    return meta


def words(html_text):
    return len(re.sub(r"<[^>]+>", " ", html.unescape(html_text)).split())


def check(c):
    problems = []
    h = c["handle"]
    title, desc = c.get("seo_title", ""), c.get("seo_description", "")
    if title:
        if len(title) > 60:
            problems.append(f"seo_title is {len(title)} chars (max 60)")
        if not title.endswith("| MAYF Home"):
            problems.append("seo_title must end with '| MAYF Home'")
        if "UAE" not in title and "Dubai" not in title:
            problems.append("seo_title must include UAE or Dubai")
    if desc and len(desc) > 155:
        problems.append(f"seo_description is {len(desc)} chars (max 155)")
    if c["intro"]:
        n = words(c["intro"])
        if not 150 <= n <= 300 and c.get("hold") != "yes":
            problems.append(f"intro is {n} words (want 150–300)")
    if c["faqs"]:
        lines = c["faqs"].splitlines()
        if not 4 <= len(lines) <= 6:
            problems.append(f"{len(lines)} FAQs (want 4–6)")
        for line in lines:
            if line.count("|") != 1:
                problems.append(f"FAQ line needs exactly one '|': {line[:50]}")
    elif c["intro"] and c.get("faqs_in_template") != "yes":
        problems.append("has an intro but no FAQs")
    return [f"{h}: {p}" for p in problems]


def main():
    collections = sorted((parse(p) for p in SRC.glob("*.md")), key=lambda c: int(c.get("priority", 99)))
    problems = [p for c in collections for p in check(c)]
    handles = {c["handle"] for c in collections}
    for c in collections:
        for r in c["related"]:
            if r not in handles and r not in {"kids", "beds", "bundles-sets", "the-hotel-bedroom"}:
                problems.append(f"{c['handle']}: related handle '{r}' has no content file — check it exists")

    OUT.mkdir(parents=True, exist_ok=True)

    with open(OUT / "seo-metadata.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["type", "handle", "seo_title", "seo_description", "h1", "priority", "status", "push", "verify"])
        for c in collections:
            if not c.get("seo_title"):
                continue
            push = "HOLD" if c.get("hold") == "yes" else ("after collection is created" if c["status"] == "new" else "yes")
            w.writerow(["collection", c["handle"], c["seo_title"], c["seo_description"], c.get("h1", ""),
                        c.get("priority", ""), c["status"], push, c.get("verify", "")])

    with open(OUT / "collection-metafields.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["handle", "custom.seo_intro", "custom.faqs", "custom.related_collections", "push", "note"])
        for c in collections:
            if not (c["intro"] or c["faqs"] or c["related"]):
                continue
            note = "FAQs are in the theme template — leave custom.faqs empty" if c.get("faqs_in_template") == "yes" else ""
            push = "HOLD" if c.get("hold") == "yes" else ("after collection is created" if c["status"] == "new" else "yes")
            w.writerow([c["handle"], c["intro"], c["faqs"], ", ".join(c["related"]), push, note])

    with open(OUT / "new-collections.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["handle", "title", "type", "rule", "theme_template", "seo_title", "seo_description",
                    "intro_html", "faqs", "related_collections", "verify"])
        for c in collections:
            if c["status"] != "new":
                continue
            w.writerow([c["handle"], c.get("title", ""), c.get("type", ""), c.get("rule", ""),
                        c.get("template") or "default", c["seo_title"], c["seo_description"],
                        c["intro"], c["faqs"], ", ".join(c["related"]), c.get("verify", "")])

    for c in collections:
        if c["intro"]:
            print(f"  {c['handle']:32} intro {words(c['intro']):3}w  faqs {len(c['faqs'].splitlines()) if c['faqs'] else 0}"
                  f"  title {len(c.get('seo_title', '')):2}  desc {len(c.get('seo_description', ''))}")
    if problems:
        print("\nPROBLEMS:\n  " + "\n  ".join(problems))
        sys.exit(1)
    print(f"\nOK — {len(collections)} collections → seo-metadata.csv, collection-metafields.csv, new-collections.csv")


if __name__ == "__main__":
    main()
