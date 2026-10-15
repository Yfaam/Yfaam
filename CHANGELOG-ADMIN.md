# CHANGELOG-ADMIN

Working theme: "Copy of MAYF Home — Final Ar/Eng version" (OnlineStoreTheme 194249392500, unpublished).
Original of record (untouched backup): live theme "MAYF Home — Final Ar/Eng version" (193740013940).
Decisions so far: trial_nights = 10; hotel claims = remove; method = edit the copy via Admin API.

## 2026-10-14 — theme file edits (copy only)
- P0-1: templates/index.json hero text "100 nights to decide" -> "10 nights to decide".
- P0-1: sections/proof-strip.liquid editor label "100-night trial link" -> "Mattress trial link".
- P0-6: layout/theme.liquid title suffix is now literal "| MAYF Home" (skipped if title contains "mayf"); no longer depends on store name "Mayf home".

## Audit findings (no change made)
- P0-3: snippets/product-card.liquid and snippets/price.liquid already use the cheapest variant for badge and price.
- P0-4: cards link to the King 180x200 variant (?variant=), so "From 600" on card vs 1,125 on page is by design, not bad data.
- Hotel Collection Tight Top variant positions are 1,2,2,2,2,2 (duplicate positions).
- P0-2: all mattress products use templateSuffix "store-wide" (no such template), so they render product.json (generic 14-day text) instead of product.mattress.json.

## 2026-10-14 — approved store-data changes (LIVE store data)
Backups: ./backups/ (originals of edited descriptions/articles, deleted collection, previous menu).
1. P0-2: templateSuffix "store-wide" -> "mattress" on 19 mattress products (all in the `mattresses` collection except test-product): 15257105793396, 15257105760628, 15257105662324, 15257105727860, 15257105695092, 15254025011572, 15257105891700, 15257105924468, 15232839909748, 15232837976436, 15232841843060, 15232841875828, 15232839778676, 15232839844212, 15232839745908, 15232842006900, 15232841777524, 15257105858932, 15257105826164.
2. P1-2: main-menu rebuilt. Sizes, types (pocket spring, memory foam, gel, latex, hotel), firmness (medium, medium-firm), finder/compare/toppers/protectors, bedding sub-collections, curtain products and pages. Every item has a distinct URL. Soft, Firm and Orthopedic omitted (0-1 products).
3. P1-1: collection latex-mattresses-1 deleted (same 4 products as latex-mattresses). 301 redirects: /collections/latex-mattresses-1 and /ar/collections/latex-mattresses-1 -> latex-mattresses.
4. P0-1/P0-5 content:
   - "100 night" -> "10 night" in 5 draft mattress products, the best-mattress guide (nights 21-100 section rewritten to nights 1-10) and the curtains guide.
   - Removed "5-star hotel specification" claims and the "Reviews will appear here" placeholder from hotel-collection-tight-top (and "MAYFHOME" -> "MAYF Home" there).
   - Removed "contract-grade ... makes for hotels" from the guide and signature-hotel-collection-mattress; hotel-essential-bundle "5-star" -> "hotel-style".

## Open items
- luxury-hybrid and premium-plus draft products say "12 year warranty" (decision is 10) — confirm.
- "MAYFHOME"/"Mayf home" still in other product copy, vendor "Mayf home", and `shop.name` (owner: rename store).
- Orthopedic (0 products), Soft/Firm (1 each) collections need products before linking.
- Hotel Collection Tight Top variant positions 1,2,2,2,2,2.
- Inflated compare-at prices (FR Tight/Euro Top); waiting on compare_at_policy.
- Duplicate products, address for schema, title-suffix decision still unanswered.

## 2026-10-14 (later) — CORRECTION: template change reverted
- The `store-wide` -> `mattress` change (item 1 above) was WRONG for the live theme. I had only checked the copy theme, which has no `product.store-wide.json`. The LIVE theme has it (a richer page using Section Store ss-* sections), and the live `product.mattress.json` is an older template that says "100 nights ... after a 21-night adjustment period". For a short time live mattress pages were on that older template.
- Reverted: all 19 products are back on templateSuffix "store-wide" (verified from the API response).
- Finding: the "Copy of ... Final Ar/Eng version" theme is NOT a copy of live. They have diverged (live has store-wide, collection-mattresses, ss-* sections, pdp-aside, index.ai-* templates; the copy has home-faq, why-mayf, shop-by-need, curtain-cta, bundle-*, page.book-visit and others). Do not publish the copy without reviewing it.
- Merchant listings "Missing field image": live snippets/product-schema.liquid has no image on variant Products. The copy's version adds one (variant image, else product image). It needs to go into the live theme.

## 2026-10-14 (later) — decision: the copy theme is the one to publish
- sections/announcement-bar.liquid default text in the copy: "100 Nights" -> "10 Nights".
- Prepared docs/post-publish-template-map.md (product template reassignment to run after publishing).

## 2026-10-15 — speed fixes in the copy theme (PageSpeed mobile: perf 69, LCP 9.2s, FCP 2.8s, 3,047 KiB payload)
Copy theme only (194249392500). Not measurable before publishing; re-run PageSpeed after.
- layout/theme.liquid: preload body font (and heading font if different) so text paints in the right face sooner.
- sections/hero.liquid (LCP image): added 500/1200/1600w candidates, default src 2000 -> 1400, decoding=async; kept fetchpriority=high and no lazy-load.
- sections/category-grid.liquid: responsive srcset/sizes (300/500/700), decoding=async (was a single 700px image).
- sections/quiz-banner.liquid: srcset 600-1600 + sizes (was a single 1600px image in a 180px-tall slot on phones).
- sections/curtain-cta.liquid: srcset 500/900/1200 + sizes (was a single 1200px image).
Not fixable in the theme (app embeds in content_for_header): unused JS 171 KiB, extra preconnects, cache lifetimes.
Not done: accessibility flags (aria-hidden mobile-nav/drawer with focusable children, contrast, icon-only wishlist link).
