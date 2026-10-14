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
