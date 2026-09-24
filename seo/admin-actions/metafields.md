# Metafield definitions to create

**Where:** Admin → Settings → Custom data → (Collections | Products) → Add definition.
Namespace and key must match exactly; the theme reads them by name.

## Collections

| Name | Namespace & key | Type | Used by |
|---|---|---|---|
| SEO intro | `custom.seo_intro` | **Multi-line text** (HTML allowed) | Under the H1, above the grid. Replaces the collection description when filled in. |
| FAQs | `custom.faqs` | Multi-line text | FAQ accordion + FAQPage schema below the grid. One `Question\|Answer` per line — the same format as the existing product `custom.mattress_faqs`. |
| Related collections | `custom.related_collections` | **List of collections** (collection reference, list) | "Also shop:" links under the intro. |

Why multi-line text for the intro rather than rich text: the n8n Sheets → Shopify workflow can
write HTML straight into it. A rich text definition works too — the theme handles both — but
then the workflow has to send Shopify's rich-text JSON instead of HTML.

Don't fill `custom.faqs` on **mattress-toppers** or **mattress-protectors**: their templates
already have an FAQ section with its own schema (two FAQPage blocks on one page is invalid).

Values for every collection are in `collection-metafields.csv` (generated from
`seo/content/collections/*.md`). `custom.related_collections` is listed as handles; the workflow
(or you, in the admin picker) needs to resolve them to the collections.

## Products

| Name | Namespace & key | Type | Used by |
|---|---|---|---|
| Best for | `custom.best_for` | Single line text | "Editor's pick for …" label on the Best Mattresses collection |

Existing definitions this work relies on (already created, just need values on the newer
"…by Mayf Home" mattresses): `custom.firmness` (text) and `custom.firmness_scale` (integer 1–10),
read by the Hotel Collection comparison table. See `product-tags.csv`.
