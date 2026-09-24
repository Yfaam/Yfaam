# Admin / off-theme checklist

Items that can't be done in theme code. Each links to the file with the exact values.

## Phase 1 — technical hygiene & brand
- [ ] **Decide the latex handle** (see "Latex collections" below), then import `redirects.csv`
      (Online Store → Navigation → URL redirects → Import)
- [ ] Set homepage title + meta description, and rename the store to "MAYF Home" (`homepage-meta.md`)
- [ ] Settings → Brand: upload the logo. The Organization schema prefers it, and falls back
      to the header logo file until then.
- [ ] Theme settings → Social media: fill in Instagram / Facebook / TikTok / YouTube URLs.
      All four are empty today, so the Organization schema has **no `sameAs`**, which is the
      main signal tying the brand name to its profiles. Only add profiles that exist.
- [ ] Products → bulk edit → Vendor: normalise "Mayf Home" / "Mayf home" to **"MAYF Home"**.
      The theme schema now prints one spelling, but the Google & YouTube feed reads the
      vendor field directly as the brand.
- [ ] [VERIFY] Organization schema uses `contact@mayfhome.com` (from the brief). The store's
      contact email in Admin is `mayfhome@gmail.com`. Confirm contact@ is a live inbox.

### Latex collections
Only **one** latex collection exists: `latex-mattresses-1` (title "Latex Mattresses", 4
products, smart rule `tag = latex`, has SEO title/description). `/collections/latex-mattresses`
isn't a collection any more, so it 404s, but Google still has it indexed (86 imps, pos 54.9).

- **Option B (recommended, what `redirects.csv` does now):** keep `latex-mattresses-1` and
  301 the dead `/collections/latex-mattresses` to it. This doesn't rename a URL that ranks
  (pos 38.5), which follows the "don't rename handles" rule.
- **Option A (the brief's default):** change the handle of `latex-mattresses-1` to
  `latex-mattresses` in Admin, tick "create redirect", and flip the CSV row. The URL is
  cleaner, but the page that ranks moves.
