# theme/ — working copy of the live Shopify theme (partial)

Source: **"MAYF Home — Final Ar/Eng version"** (theme ID 193740013940, role MAIN on mayfhome.com),
pulled via the Admin API on 2026-09-24. Only files touched by the SEO work are kept here; the
first commit that adds each file is a byte-exact copy of the live version, so `git diff` against
it shows exactly what changed.

This is **not** a full theme. Never run a plain `shopify theme push` from this folder — it would
delete every file that isn't here. Push only the changed files to an **unpublished** copy:

```sh
# 1. Admin → Online Store → Themes → "MAYF Home — Final Ar/Eng version" → ⋯ → Duplicate
# 2. push only these files to the duplicate (never to the live theme)
# run from this theme/ folder
shopify theme push --theme <DUPLICATE_THEME_ID> --nodelete \
  --only layout/theme.liquid --only sections/hero.liquid --only templates/index.json \
  --only snippets/organization-schema.liquid --only snippets/product-schema.liquid \
  --only snippets/breadcrumb-schema.liquid --only snippets/meta-tags.liquid
```

Then open the duplicate's preview and check (view-source): one `<h1>`, one canonical, one
Organization block, and `noindex` only on `/search` and `/collections/all`.

Watch out: `templates/index.json` also holds the homepage content. If anyone edits the
homepage in the theme editor after this snapshot, re-pull that file before pushing it.
