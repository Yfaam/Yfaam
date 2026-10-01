# theme/ — working copy of the live Shopify theme (partial)

Source: **"MAYF Home — Final Ar/Eng version"** (theme ID 193740013940, role MAIN on mayfhome.com),
pulled via the Admin API on 2026-10-01. Only the files touched by the footer social-icons change
are kept here. The first commit that adds each file is a byte-exact copy of the live version, so
`git diff` against it shows exactly what changed.

## Footer social icons

- `config/settings_schema.json` — adds Snapchat, X and Pinterest link fields next to the existing
  Instagram, Facebook, TikTok and YouTube ones (Theme settings → Social media).
- `snippets/icon.liquid` — adds `snapchat`, `x` and `pinterest` icons.
- `sections/footer.liquid` — renders one icon per filled-in link, and hides the "Follow us"
  heading when no link is set.
- `sections/footer-group.json` — sets the heading text to "Follow us" (it was empty on the live theme).

The icons appear only after the profile URLs are entered in
**Online Store → Themes → Customize → Theme settings → Social media**.

## Deploying

This is **not** a full theme. Never run a plain `shopify theme push` from this folder, because it
would delete every file that isn't here. Push only the changed files to an **unpublished** copy:

```sh
# 1. Admin → Online Store → Themes → "MAYF Home — Final Ar/Eng version" → ⋯ → Duplicate
# 2. from this theme/ folder, push only these files to the duplicate (never to the live theme)
shopify theme push --theme <DUPLICATE_THEME_ID> --nodelete \
  --only config/settings_schema.json --only snippets/icon.liquid \
  --only sections/footer.liquid --only sections/footer-group.json
```

`sections/footer-group.json` also holds the footer content edited in the theme editor. If anyone
edits the footer there after this snapshot, re-pull that file before pushing it.
