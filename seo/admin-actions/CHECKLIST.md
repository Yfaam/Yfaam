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

## Phase 2 — landing pages (do in this order)

Everything below is prepared; nothing has been written to the store.

1. [ ] **Product fixes** from `product-tags.csv`: size tags, `tight-top`/`pillow-top`,
       `orthopedic`/`medical`, firmness metafields, vendor, the Hotel Tight Top's blank product
       type, and the Signature Hotel description's "10 night trial" (the policy is 100 nights).
       *Effect:* Super King goes from 3 to ~11 products, King/Queen/Single pick up the 10 newer
       mattresses, and Orthopedic stops being empty.
2. [ ] **Shop by Size rule**: its conditions use tags `single` and `super singles`, which no
       product has. Change them to `single size` and `Super single` (keep "any condition").
3. [ ] **Legacy size names** [VERIFY dims first]: rename the Size values on Signature Hotel,
       Cooling Gel Memory, Latex Natural and Kids Comfort from `King` → `King (180x200)`,
       `Super King` → `Super King (200x200)`, etc. Renaming an option value doesn't change any
       URL; it tells shoppers (and Google Shopping) the real dimensions.
4. [ ] **Metafield definitions** from `metafields.md`.
5. [ ] **Push the theme** changes to a duplicate theme, preview, then publish (see `theme/README.md`).
       Safe before the content exists: every new block is hidden while its metafield is empty.
6. [ ] **Create collections** from `new-collections.csv`:
       - `hotel-collection-mattresses`: smart, template **hotel**
       - `medical-mattresses`: smart (tag `medical`), default template
       - `best-mattresses`: manual, template **best**. Fill `custom.best_for` on each pick.
         Its template and copy link to Phase 3 guides, so **publish it together with Guide #1**.
       Publish each to Online Store **and** Google & YouTube.
7. [ ] **Collection copy**: push `seo-metadata.csv` (titles/descriptions/H1 = collection title)
       and `collection-metafields.csv` via the n8n workflow. Skip rows marked `HOLD`, and push
       `after collection is created` rows only after step 6.
8. [ ] **Links to the new pages**: after step 6, point the homepage hero's second button to
       Best Mattresses (theme editor → Hero → Secondary button) and add *Best Mattresses* and
       *Hotel Collection* to the main menu under Mattresses.
       While there: the menu's "Shop by Type / Firmness / Room" items all link to
       `/collections/mattresses`. Point them at the real sub-collections.

### Catalogue gaps & empty collections
- [ ] **Mattress protectors**: LUNA PRIME (the only protector) is a **draft**, so
      `/collections/mattress-protectors` is empty. Publish it if stock exists; otherwise source
      protectors (waterproof, cooling, all UAE sizes). Metadata is marked HOLD until then.
- [ ] **Empty on the storefront today:** `orthopedic-mattresses` (0 products, fixed by step 1),
      `firm-mattresses` and `hybrid-mattresses` (only draft products), `soft-mattresses`,
      `the-family-living-room`, and all 5 `bed-sheets` products are drafts. Until they have
      live products, hide them from the Online Store channel or fill them — an empty page
      that ranks (orthopedic: pos 39) wastes the ranking.
- [ ] **Hotel bed foundations**: no foundation/divan products exist, so the brief's
      "hotel collection bed foundations" keyword has no page. Add products or drop it.
- [ ] **No 80×200 mattress** in any product. The brief's `mattress-80x200` isn't created.

### Size collections: not created (why)
Every current "…by Mayf Home" mattress comes in all of 90×200, 120×200, 150×200, 160×200,
180×200 and 200×200. So `mattress-180x200` would list exactly the King products,
`mattress-200x200` the Super King products, `mattress-150x200` the Queen products and
`mattress-90x200` the Single products. Near-identical pages compete with each other in Google.
Instead, size queries are mapped to the existing collections, whose titles, H1s and intros now
carry the dimensions:

| Query | Page |
|---|---|
| mattress 90x200 · 90x190 · single bed mattress 90 x 200 | /collections/single-mattresses |
| mattress 150x200 · 160x200 · queen size | /collections/queen-mattresses |
| mattress 180x200 · king size mattress 180 x 200 · orthopedic mattress 180x200 | /collections/king-mattresses |
| 200x200 mattress · super king | /collections/super-king-mattresses |

If you still want separate size collections, say so and I'll add them to `new-collections.csv`.
