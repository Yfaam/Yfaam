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
