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
