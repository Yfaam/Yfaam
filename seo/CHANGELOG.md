# SEO changelog

## Phase 1 — Technical hygiene & brand (2026-09-24)

Working copy: `theme/` holds the live theme's files that this work touches ("MAYF Home — Final
Ar/Eng version", ID 193740013940). The first commit is a byte-exact snapshot, so diffs show only
SEO changes. The theme is custom (not Dawn).

**Theme**
- `layout/theme.liquid`: added one robots block with `noindex, follow` on search, cart,
  `/collections/all`, `/frontpage`, `/vendors`, `/types`, tag-filtered collections (`current_tags`)
  and `+` URLs. Paginated and `?filter.` URLs aren't touched.
- `layout/theme.liquid`: the title suffix was `– {{ shop.name }}` ("Mayf home") and was added
  whenever the title didn't contain that exact lowercase string, so SEO titles ending in
  "| MAYFHOME" came out as "… | MAYFHOME – Mayf home". Now it's a case-insensitive check with
  a fixed " | MAYF Home" suffix.
- `snippets/organization-schema.liquid`: the Organization is now `["Organization","OnlineStore"]`
  with name "MAYF Home", alternateName (MAYF, Mayf Home, mayfhome, معيوف هوم, ماف هوم), email,
  telephone, addressLocality, parentOrganization "MAYF Group" and an `@id`. The logo never
  rendered before (`sections['header']` isn't available in a snippet); it now uses
  `shop.brand.logo`, falling back to the header logo file. Added a **WebSite** block (homepage
  only) with site name, alternateName and SearchAction. It's still one Organization per page.
- `snippets/product-schema.liquid`: Brand prints "MAYF Home" whichever of the 3 vendor
  spellings is set. The Offer `seller` references the Organization `@id`.
- `snippets/breadcrumb-schema.liquid`: only emitted for product / collection / page / blog /
  article. It was publishing a single "Home" crumb on search/cart. Added the blog case.
- `snippets/meta-tags.liquid`: `og:site_name` is now "MAYF Home"; `og:image` uses https (was http).
- `sections/hero.liquid` + `templates/index.json`: new "Brand line" setting rendered **inside**
  the existing H1, styled as the eyebrow. The homepage H1 now reads "MAYF Home / Bring Hotel
  Comfort Home". It's still one H1.
- `templates/index.json`: the Best-sellers "View all" linked to `/collections/frontpage`, which
  doesn't exist. It now links to `/collections/best-sellers`.

**Verified**
- The canonical is output exactly once (`layout/theme.liquid`) from `canonical_url`, which drops
  `?variant=`, `utm_*` and `?filter.` params and keeps `?page=`. No change needed.
- Theme Check gives the same result before and after. The only offenses are references to files
  not in this partial copy.
- The JSON-LD was rendered with mock data for index/product/collection/page/blog/article/search
  and every block parses. There's one Organization per page and WebSite on the homepage only.
- hreflang: none is hand-coded in the theme, so no duplicates. Shopify adds it via
  `content_for_header` once Arabic is published. Check again in Phase 4.
- Not linked anywhere: `latex-mattresses-1` isn't in any menu. It's linked from
  `templates/collection.mattresses.json` (the sub-category carousel), which is correct under
  Option B.

**Couldn't do from this environment**
- `shopify theme dev` / a rendered-HTML check: there's no Shopify CLI or store token here, and
  mayfhome.com is blocked by the sandbox network policy. See "Preview" in `theme/README.md`.

**Admin actions:** `seo/admin-actions/CHECKLIST.md` (Phase 1 section), `redirects.csv`, `homepage-meta.md`.

## Phase 2 — Landing pages (2026-09-24)

Built against brief v2 (`SEO_SCALEUP_TASKS.md`, now in the repo). Catalogue facts come from the
Admin API (read-only).

**Theme**
- `snippets/collection-seo-intro.liquid` (new), rendered in `main-collection` under the H1 and
  above the grid:
  - the intro from `custom.seo_intro` replaces the description when set, and is clamped with
    "Read more" on phones (the full text stays in the HTML)
  - related-collection links from `custom.related_collections`
  - the intro is skipped on page 2+
- `sections/collection-seo-content.liquid` (new): FAQs from `custom.faqs` (`Question|Answer`
  lines, the product FAQ format) through the existing `product-qa` + `faq-schema` snippets. It
  renders nothing when the metafield is empty. Added to `templates/collection.json` below the grid.
  - Why the intro isn't in this section: the collection H1 and the grid are one section
    (`main-collection`), so a separate section can't sit between them.
- `sections/collection-compare.liquid` (new): comparison table from live product data (top type
  from tags, firmness from metafields, FR tag, size range, lowest price). No hard-coded prices.
- `sections/main-collection.liquid`:
  - renders the intro snippet
  - optional "Editor's pick for <custom.best_for>" label per product
  - phone-only read-more JS and styles
  - translatable labels as section settings
- `sections/hero.liquid`: new "Heading level" setting (H1/H2). The default stays H1, so the
  homepage is unchanged.
- `templates/collection.hotel.json` (new): hero (H2) → collection (H1, intro, grid) →
  comparison → story → FAQs.
- `templates/collection.best.json` (new): collection with editor's-pick labels → "How we choose"
  → FAQs.
- `templates/collection.mattress-toppers.json`:
  - removed the competitor price claim ("below premium brands like Hotel Linen Klub")
  - added FAQs: topper vs new mattress, back pain (no medical claims), delivery (free only over
    AED 500)
  - added a link to protectors

**Content** (`seo/content/collections/*.md`, one file per collection; built by
`seo/tools/build_collection_files.py`, which enforces title ≤60, description ≤155, UAE/Dubai,
"| MAYF Home", 150–300-word intros and 4–6 FAQs)
- Full intro + FAQs: mattresses, king, queen, single, super king, orthopedic, and the new hotel,
  best and medical collections. Toppers and protectors get an intro only, because their FAQs live
  in the templates.
- Metadata only: latex, memory foam, firm, medium-firm, pocket spring, hybrid, bedding, pillows,
  pillow cases, plus duvets, duvet covers and bed sheets. Those last three were added because
  their live descriptions promise free delivery without the AED 500 threshold.
- Outputs: `admin-actions/seo-metadata.csv`, `collection-metafields.csv`, `new-collections.csv`.

**Admin actions:** `product-tags.csv`, `metafields.md`, and the CHECKLIST Phase 2 section
(ordered steps).

**Deviations from the brief**
- **No separate size collections.** They'd duplicate King/Queen/Single/Super King (every product
  comes in every size). Size queries are mapped to those pages instead; the reasoning and table
  are in CHECKLIST.
- **No 80×200** product exists.
- **Toppers:** the title describes 300TC microfibre, because no memory foam or latex toppers exist.
- **Protectors:** the collection exists but its only product is a draft, so its metadata is on
  HOLD. Listed as a catalogue gap.
- **Hotel page:** no bed-foundation products exist, so that block was left out.

**Verified**
- Theme Check: no new errors. All missing references are files that exist in the live theme
  but not in this partial copy.
- Rendered with liquidjs:
  - FAQ section: 6 accordion items, and 6 questions in FAQPage schema that parses. Renders
    nothing when the metafield is empty.
  - Intro snippet: replaces the description, falls back to it, and skips linking a collection
    to itself.
  - Comparison table: shows a dash where data is missing.
