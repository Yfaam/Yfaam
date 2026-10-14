# Template reassignment to run RIGHT AFTER publishing "Copy of MAYF Home — Final Ar/Eng version"

Why: every product currently has templateSuffix `store-wide`, which exists only in the old live theme.
The copy has: product (default), product.mattress, product.curtains, product.curtains-quote.
Do NOT run before publishing; live still needs `store-wide`.

| Group | Products | New templateSuffix |
|---|---|---|
| Mattresses (productType Memory Foam / Hybrid / Pocket Spring / Latex, or handle contains "mattress", except protectors/toppers) incl. drafts | 19 products listed in CHANGELOG-ADMIN.md, plus `mayf-kids-latex-mattress` | `mattress` |
| Curtains & blinds (productType Curtains) | blackout, sheer, roman, roller, motorized | `curtains` |
| Quote-only (price 0) | `large-window-curtains` | `curtains-quote` |
| Everything else (bedding, protectors, toppers, pillows, bundles, beds, sofas) | ~38 products | `` (default product template) |

Rollback value for every product: `store-wide`.
Then check one page of each group, e.g. a mattress, a duvet, a bed, a curtain.
