# MAYF Home — SEO / AIO / GEO audit: review and implementation

Review of `audit-2026-11-09.md` against the store's theme source and Admin data, and a record of what was changed on 10 November 2026.

## Where the changes are

| Change | Where | State |
|---|---|---|
| Structured data and agent file | Unpublished theme **"MAYF Home — SEO-AIO schema fixes (Nov 2026)"** (ID 196080599412), a copy of the live theme taken 10 Nov | **Not live. Publish it to apply.** |
| SEO titles and meta descriptions | Live store data | Live now |
| Copies of the changed theme files | `theme/` in this repo | For review and history |

The live theme was not edited. Any change made to the live theme after 10 Nov is not in the copy.

**Not verified:** the rendered pages. The session could not reach mayfhome.com, so the new snippets were tested by rendering them locally against the store's real collection, article and product content and parsing every JSON-LD block. Shopify accepted every file. Before publishing, preview the copy and run a product, a collection, an article and the home page through Google's Rich Results Test.

## Audit claims checked against the source

| Audit claim | Finding |
|---|---|
| `Organization.logo` missing | Correct. The snippet read the logo from `sections['header']`, which does not exist in that context, so it was always blank. |
| Schema name is "Mayf home" | Correct. It printed the admin store name. |
| No `Article` schema, no `ItemList`, no `WebSite` | Correct. |
| FAQs unmarked on collections and articles | Correct, and wider than stated: 7 collections and all 5 published articles had visible FAQs with no markup. |
| FAQs unmarked on `/pages/curtains-service` and PDPs | **Wrong.** Both already print `FAQPage`. |
| Variants have no `sku` | Correct, but it is data, not code: 38 of the 71 active products have no SKU in admin. |
| "EMPTY DOM REMOVE PROTECTOR" should be deleted from the theme | **Not in the theme.** It is injected by an app (most likely the Section Store app embed). |
| Duplicate products to merge | **Wrong.** The pairs are different products: a 1-size latex-foam hybrid vs a 5-size natural latex kids mattress; a kids vs an adult organic latex mattress; blackout vs blackout + sheer. Merging would remove real products. |
| Empty `alt` on product imagery | Mostly correct usage: the empty ones are hover duplicates and thumbnails. |
| Add `LocalBusiness` | **Not done by default.** The address is a co-working office and the site says there is no walk-in shop. Google's guidelines do not allow local-business markup for that. It is available behind a theme setting if a showroom opens. |
| Add return policy and shipping at `ProductGroup` level | Not needed. Google reads them from each offer, where they already are. |
| `SearchAction` for a sitelinks search box | Added, but Google retired that feature in 2024. The useful part is `WebSite.name`, which sets the site name in results. |
| Trailing-slash URLs, Cloudflare rate limits | Shopify platform behaviour. Canonicals already handle the first; neither can be changed from the theme. |

## Problems the audit missed

1. **Product schema stated a return policy the store does not offer.** Every non-mattress product claimed a 14-day return window, and the FR hotel mattresses claimed the sleep trial. The published Refund Policy says only trial-eligible mattresses are returnable. Fixed in the theme copy.
2. **The site contradicts itself on returns.** The Refund Policy says bedding, textiles and made-to-measure items are non-returnable. The theme says "14 Days Easy Returns" on bedding pages and in the cart, and the product Q&A says unopened items can be returned within 14 days. This needs a decision; nothing visible was changed.
3. **Home page meta description said "100 nights to decide".** The trial is 10 nights. Fixed live.
4. **One article says MAYF Home delivers "worldwide".** The back-pain guide's last FAQ says so; the shipping page says UAE only. Not changed.
5. **Support hours differ.** Footer: Sat–Thu 9am–9pm. Refund Policy: Sun–Thu 9am–6pm. Hours are left out of the structured data until one is chosen.
6. **`og:image` used `http:`** and articles had no article Open Graph type or dates. Fixed in the theme copy.
7. **One article has 13 `<h1>` headings in its body** (`best-mattress-in-uae-2026-...`), including a repeat of the title. Its FAQ is now read correctly, but the headings should be demoted in the editor.
8. **OpenAI pixel runs with `debug:true`** in `layout/theme.liquid`. Left as is.

## What was implemented

### In the unpublished theme copy

- `snippets/organization-schema.liquid` — Organization as `OnlineStore` with one brand name, `alternateName` (MAYFHOME, Mayf Home, مايف هوم), logo, street address, email, the seven emirates served and an Arabic description on `/ar`. `WebSite` on the home page. Optional local-business block behind a setting.
- `snippets/product-schema.liquid` — every variant has a `sku` (the admin SKU, else the variant ID); the return policy is printed only for trial-eligible mattresses, with the day-13 deadline and the collection fee from the product's metafields.
- `snippets/faq-schema-html.liquid` (new) — reads the FAQ block out of a collection description, article or page and prints `FAQPage`. Covers 7 collections and 5 articles, in English and Arabic.
- `snippets/article-schema.liquid` (new) — `BlogPosting` with author, publisher, published and modified dates.
- `snippets/collection-schema.liquid` (new) — `CollectionPage` with an `ItemList` of the products shown.
- `snippets/meta-tags.liquid` — fixed brand in `og:site_name`, https image, article Open Graph tags, and the calls to the new snippets.
- `sections/main-article.liquid` — visible byline and "Updated" date.
- `config/settings_schema.json`, `config/settings_data.json` — new "Business details" settings group; logo set to the header logo.
- `templates/agents.md.liquid` (new) — replaces Shopify's generated `/agents.md` and `/llms.txt` with brand facts, price guide, policies and the commerce endpoints. The generated default could not be read from this session, so compare the two after publishing.

### Live store data

- Home page title `MAYFHOME | …` → `MAYF Home | …`; description corrected (brand, 10-night trial, AED 500 delivery threshold).
- Meta descriptions added: `/pages/finder`, `/pages/compare`, `/pages/bundle`, `/pages/contact`, and the pocket-spring, king and super-king mattress collections.
- `MAYFHOME` → `MAYF Home` in the titles of the memory-foam and best-sellers collections and the wall-covering page.

The new descriptions are English only; Arabic versions need adding in Translate & Adapt.

## Left for the store owner

- **Publish the theme copy** after previewing it.
- **Rename the store** to "MAYF Home" in Settings > Store details. That fixes the logo alt text, footer copyright, emails and the Judge.me widgets in one place.
- **Settle the returns wording** (item 2 above) and the support hours (item 5).
- Set product vendor to "MAYF Home" on the 30 products (29 active) that use "Mayf home" or "Mayf Home" — it feeds the Merchant Center brand. Check first that no automated collection filters on the old spelling.
- Assign real SKUs to the 38 active products without one.
- Decide what to do with the empty `the-family-living-room` collection.
- Brand spelling inside product and collection body copy (about 25 places) was not changed, to avoid disturbing the Arabic translations.
- Everything in the audit's "Next" and "Later" lists — About page, named authors, certification evidence, mattress collection rebuild, longer product copy, reviews, Google Business Profile, listicles, PR — needs facts, people and outreach that only the business has. The audit is right that this, not the schema, is what moves AI visibility.
