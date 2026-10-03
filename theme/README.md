# theme/: changes for "Copy of MAYF Home — Final Ar/Eng version"

Target theme: **194249392500** (role UNPUBLISHED). Never push these files to the live theme (193740013940).
This folder holds only the changed/new files, not a full theme. Do not run a plain `shopify theme push`
from here; use `--only` / `--nodelete`:

```sh
shopify theme push --theme 194249392500 --nodelete \
  --only sections/proof-strip.liquid --only sections/shop-by-need.liquid \
  --only sections/curtain-cta.liquid --only sections/why-mayf.liquid --only sections/home-faq.liquid \
  --only sections/hero.liquid --only sections/quiz-banner.liquid --only sections/shop-the-room.liquid \
  --only snippets/price.liquid --only locales/en.default.json --only locales/ar.json \
  --only templates/index.json --only templates/product.mattress.json \
  --only config/settings_data.json --only sections/header-group.json
```

## What changed
| Review item | Change |
|---|---|
| Delivery wording | `config/settings_data.json` (trust badge), `sections/header-group.json` (announcement), `templates/index.json` (hero text), `templates/product.mattress.json` (Q&A), `locales/*` (cart reassurance): all now "Free UAE delivery on orders over AED 500" |
| AED 0.00 curtain | `snippets/price.liquid`: a zero price shows "Quoted after free measurement" (the product has one variant priced 0.00 by design) |
| Hero CTAs | `sections/hero.liquid` adds a third button; `index.json` sets Find My Mattress and Book Free Curtain Measurement |
| Proof strip | new `sections/proof-strip.liquid` (replaces the generic trust bar under the hero) |
| 6 categories | `index.json` category blocks: Mattresses, Beds, Bedding, Curtains, Sofas & Living, Kids |
| Shop by Need | new `sections/shop-by-need.liquid` |
| Finder on homepage | `sections/quiz-banner.liquid` text now falls back to locale strings |
| Shop the Room | `sections/shop-the-room.liquid` shows piece count and lowest price per room |
| Bundles | Homepage card removed from the category grid; new "Complete Bedroom Bundles" carousel that hides itself when the collection is empty |
| Curtain lead-gen | new `sections/curtain-cta.liquid` |
| Why MAYF | new `sections/why-mayf.liquid` (old generic value strip disabled) |
| FAQs | new `sections/home-faq.liquid`, answers taken from the shipping and returns policy pages, with FAQPage schema |
| Arabic | all new copy is in `locales/ar.json` (`sections.home.*`); first draft, needs native review |

## Status
Uploaded to theme 194249392500 (unpublished) on 2026-10-03; all files verified byte-identical to this folder. The live theme was not touched.

## Not done here
Essential/Signature/Luxe comparison (needs real specs), customer reviews / UGC (needs real data, testimonials
section stays disabled), Arabic for existing sections' settings (hero, category and carousel headings, newsletter):
these live in Translate & Adapt, not locale files.
