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
shopify theme push --theme <DUPLICATE_THEME_ID> --nodelete --only layout/theme.liquid --only snippets/... 
```
