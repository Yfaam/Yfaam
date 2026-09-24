# mayfhome.com — SEO Scale-Up: Implementation Brief for Claude Code

> **How to use:** put this file in the root of the `mayfhome-theme-v2` repo (Dawn-based Shopify theme) and tell Claude Code:
> *"Read SEO_SCALEUP_TASKS.md and implement it phase by phase. Stop at the end of each phase and show me the diff."*

---

## 0. Ground rules (read first)

1. **Work on a new git branch** (`seo/scaleup-2026-09`). Never push to the **live** theme. Preview with `shopify theme dev` or push to an **unpublished** theme only (`shopify theme push --unpublished`).
2. Run `shopify theme check` after every phase; fix any new errors you introduced.
3. **Do not rename existing collection or product handles.** Renaming breaks URLs that already rank.
4. Some tasks happen in **Shopify Admin**, not in the theme (redirects, new collections, blog articles, Merchant Center, translations). For those, **produce the ready-to-import file or exact instructions** in `/seo/admin-actions/` and list them in the final summary. Only call the Admin API if a token is already configured in this project. Never invent credentials.
5. Before editing any file, inspect it to confirm the real structure. Dawn versions differ, and this theme is customised, so file paths below are *likely* locations. Verify them first.
6. Keep all copy in **UK/UAE English**, with prices in **AED**. The brand name is **MAYF Home**.
7. At the end of each phase, write a short changelog entry in `/seo/CHANGELOG.md`.

---

## 1. Context: what the Search Console data says

Source: Google Search Console export, Web search, 18 Aug – 22 Sep 2026 (site is about 5 weeks old in Google).

| Metric | Value |
|---|---|
| Clicks / Impressions | 41 / 2,891 |
| Avg position trend (weekly) | 46.5 → 55.9 → 42.7 → 38.8 → 33.2 → **29.8** (improving fast) |
| Clicks to homepage | 30 of 41 (mostly brand/navigational) |
| Desktop | 2,176 imps · pos 43 · CTR 0.46% |
| Mobile | 707 imps · pos 28 · CTR 3.96% |
| Product rich snippets | 2,385 imps (schema works) |
| Merchant listings | **2 imps** (free Shopping listings effectively not showing) |
| Country | UAE = 2,464 imps (85%) |

**Main problems:**
- The brand query **"mayf" ranks at position 10.5** with 0 clicks. The Arabic transliteration "معيوف هوم" ranks at 6.2.
- Money pages sit at positions 30–55, so they get impressions but no clicks.
- Duplicate or junk URLs are indexed (see Phase 1).

### Key pages (impressions / avg position)
| URL | Imps | Pos |
|---|---|---|
| /collections/mattresses | 725 | 45.5 |
| /collections/king-mattresses | 338 | 41.2 |
| /collections/super-king-mattresses | 280 | **29.6** |
| /collections/memory-foam-mattresses | 192 | 52.3 |
| /collections/single-mattresses | 188 | 32.0 |
| /collections/latex-mattresses-1 | 164 | 38.5 |
| /collections/orthopedic-mattresses | 124 | 39.0 |
| /products/hotel-collection-tight-top-mattress-by-mayf-home | 77 | 13.5 (3 clicks) |
| /collections/latex-mattresses | 86 | 54.9 ← **duplicate of -1** |
| /products/signature-hotel-collection-mattress | 49 | 7.9 |
| /pages/interior-designing | 29 | 5.5 (10% CTR) |

### Keyword clusters (impressions / weighted avg position)
| Cluster | Imps | Pos | Target page |
|---|---|---|---|
| King (all) | 574 | 36.8 | /collections/king-mattresses |
| Memory foam | 304 | 51.0 | /collections/memory-foam-mattresses |
| Latex | 274 | 44.7 | /collections/latex-mattresses (merged) |
| "Best … in UAE" / brand comparison | 264 | 54.5 | **new blog guides** |
| Super King | 181 | **27.2** | /collections/super-king-mattresses |
| Orthopedic / medical / firm | 181 | 40.0 | /collections/orthopedic-mattresses + **new medical-mattresses** |
| Size-specific (90x200, 180x200, 90x190, 80x200) | 138 | 22–25 | **new size collections** |
| Bedding / pillows / duvets (incl. Arabic لحاف) | 97 | 53.4 | /collections/bedding |
| Toppers | 88 | 45.5 | /collections/mattress-toppers |
| Hotel | 56 | 20.6 | **new Hotel Collection landing** |
| Cooling gel | 41 | 33.4 | cooling gel product + guide |
| Geo-modified (dubai/uae/abu dhabi/sharjah) | 645 (26%) | 47.5 | all of the above + city pages |

### UAE market demand benchmark (competitor GSC data, themattressstore.com, Jan–Apr 2026)
Use this data to **prioritise** and **size** keywords. It is **not** a forecast for mayfhome (their domain is older and they have physical stores). **Never copy their titles or copy.**

| Keyword | Market imps (3 mo) | Leader pos | mayfhome now | Implication |
|---|---|---|---|---|
| mattress topper | 6,735 | 8.8 | 39 imps · pos 43 | **Big demand; promoted to Phase 2** |
| king size mattress | 4,308 | 8.6 | 121 imps · pos 39 | Core money page |
| mattress protector | 3,172 | 10.1 | not ranking | **New category needed** |
| latex mattress | 2,489 | 9.5 | 33 imps · pos 49 | Merge + optimise |
| queen size mattress | 1,921 | 13.9 | 41 imps · pos 59 | Optimise |
| hotel collection mattress | 1,433 | **14.7** | 34 imps · **pos 15** | Leader is weak here, so this is winnable; make it the signature |
| /collections/best-mattresses (page) | 122,238 | 6.5 | no page | **New curated "Best Mattresses" collection** |
| latex vs memory foam (article) | 8,399 | – | – | Guide with a title that matches search intent |
| أفضل مراتب في الإمارات | 318 | 3.1 (4.7% CTR) | – | Arabic priority |
| مرتبة سرير / مراتب سرير / مراتب / مرتبة | 1,075 / 883 / 477 / 361 | ~7 | – | Arabic priority |

Market benchmarks: Merchant listings **30.7% CTR at pos 3.2**, which makes this the highest-converting surface. Desktop CTR lags mobile across the market. Traffic dropped about 20% in the Ramadan month, so **all Phase 2–3 pages must be live by 15 Jan 2027** (Ramadan 2027 begins around early February).

---

## Phase 1 — Technical hygiene & brand (do first)

### 1.1 Noindex junk/duplicate templates
In `layout/theme.liquid` (inside `<head>`), add a single robots meta block:

```liquid
{%- liquid
  assign noindex = false
  if template.name == 'search' or template.name == 'cart'
    assign noindex = true
  endif
  if template.name == 'collection'
    if collection.handle == 'frontpage' or collection.handle == 'all'
      assign noindex = true
    endif
    if current_tags or request.path contains '+'
      assign noindex = true
    endif
  endif
-%}
{%- if noindex -%}<meta name="robots" content="noindex, follow">{%- endif -%}
```
- Do **not** noindex paginated collection pages (`?page=2`); they should canonicalise to themselves.
- Leave Shopify's default `robots.txt` in place. Only add `templates/robots.txt.liquid` if you need to allow crawling of a URL that must be seen as noindexed. Explain why before doing it.

### 1.2 Canonicals
- Confirm `<link rel="canonical" href="{{ canonical_url }}">` exists exactly once in `layout/theme.liquid`.
- Confirm that product URLs with `?variant=…&utm_…` (Google & YouTube app `sag_organic` sync URLs) output the **clean** product URL as canonical. Test on `/products/latex-natural-mattress?variant=55180157845876&utm_source=google`.
- Collection filter URLs (`?filter.v.option.size=Queen`) must canonicalise to the unfiltered collection.

### 1.3 Merge duplicate latex collections
- The two handles are `latex-mattresses` and `latex-mattresses-1`. **Check in Admin/API which one holds the products and content, and ask me before choosing.** The default proposal is to keep `latex-mattresses` and 301-redirect `latex-mattresses-1` to it.
- Create `/seo/admin-actions/redirects.csv` in Shopify's URL-redirect import format:
```csv
Redirect from,Redirect to
/collections/latex-mattresses-1,/collections/latex-mattresses
```
- Grep the theme, menus export (if present) and sections JSON for links to `latex-mattresses-1` and update them.

### 1.4 Brand entity schema (fix "mayf" ranking at #10)
In the homepage / `layout/theme.liquid`, make sure there is **one** Organization JSON-LD block and **one** WebSite block with SearchAction. Dawn may already output one in `sections/header.liquid` or `main-*.liquid`. Extend it rather than duplicating it.
```json
{
  "@context": "https://schema.org",
  "@type": ["Organization", "OnlineStore"],
  "name": "MAYF Home",
  "alternateName": ["MAYF", "Mayf Home", "معيوف هوم", "ماف هوم"],
  "url": "https://mayfhome.com/",
  "logo": "<shop logo URL via image_url filter>",
  "email": "contact@mayfhome.com",
  "telephone": "+971541470477",
  "address": {"@type": "PostalAddress", "addressLocality": "Ajman", "addressCountry": "AE"},
  "areaServed": ["AE"],
  "parentOrganization": {"@type": "Organization", "name": "MAYF Group"},
  "sameAs": ["<instagram>", "<facebook>", "<tiktok>", "<google business profile>"]
}
```
- Pull `sameAs` URLs from `settings.social_*_link` theme settings. Leave out empty ones and **never invent profile URLs**.
- Homepage `<title>` target: **"MAYF Home | Mattresses & Home Furnishings in UAE"**. This is set in Admin → Online Store → Preferences, so add it to the admin-actions list, together with a matching meta description (≤155 chars).
- Visible homepage H1 should contain "MAYF Home". Check the hero section. If there is no H1, make the hero heading the H1 and don't add a second one.

### 1.5 Verify
- Search the rendered HTML (via `shopify theme dev`) for duplicate `<h1>`, duplicate canonical and duplicate Organization schema.
- Validate the JSON-LD (parse it with `node -e` / `jq`).

---

## Phase 2 — Quick-win landing pages (positions 20–30)

All new pages need: a unique `<title>` (≤60 chars), meta description (≤155), one H1, 150–300 words of intro copy **above** the product grid (collapsed "Read more" on mobile is fine), 4–6 FAQs, a BreadcrumbList schema, and internal links to 2–3 sibling collections.

### 2.1 Upgrade the collection template to support SEO content
Create `sections/collection-seo-content.liquid` that renders the following:
- the intro from `collection.metafields.custom.seo_intro` (rich text)
- FAQs from `collection.metafields.custom.faqs` (JSON list of `{q, a}`, or metaobject list if one already exists) as an accordion and **FAQPage JSON-LD**
- "Related collections" links from `collection.metafields.custom.related_collections` (list of collection references)

Add it to `templates/collection.json` (below the banner, above the grid) so every collection can use it. Document the metafield definitions to create in `/seo/admin-actions/metafields.md`.

### 2.2 Super King (highest priority, pos ~27)
Target `/collections/super-king-mattresses`. Keywords: *super king mattress, super king bed, super king size mattress, super king mattresses dubai, 200x200 mattress*.
- Title: `Super King Mattress UAE (200x200) | MAYF Home`. **Confirm the actual super king dimensions in the product variants first.**
- Intro: what "super king" means in the UAE, dimensions, room-size advice, delivery across the UAE.
- FAQs: super king vs king size; does it fit a 200x200 bed frame; delivery time to Dubai, Abu Dhabi and Sharjah; trial/returns policy (link /pages/returns-policy); which firmness to pick.

### 2.2b Mattress Toppers (market demand is about 6.7K imps per quarter)
Target `/collections/mattress-toppers` (currently pos 46). Keywords: *mattress topper, mattress topper uae, mattress topper dubai, memory foam topper dubai, bed toppers, ماتريس توبر*.
- Title: `Mattress Toppers UAE | Memory Foam, Latex & Cooling | MAYF Home`
- Intro: topper types (memory foam, latex, microfibre/300TC), sizes, who a topper suits vs replacing the mattress, and cooling for the UAE climate.
- FAQs: topper vs new mattress; which thickness to choose; do toppers help back pain (no medical claims); washing/care; delivery.
- Link to the topper guide (3.2 #7) and to the Mattress Protectors collection.

### 2.2c NEW: Mattress Protectors collection (about 3.2K imps per quarter in the market; not ranking today)
- Check the catalogue for protector products. **If none exist, don't create an empty collection.** Add "Source mattress protectors (waterproof, cooling, all UAE sizes)" to `/seo/admin-actions/CHECKLIST.md` as a catalogue gap, and draft the collection spec ready for when stock lands.
- Handle `mattress-protectors`. Keywords: *mattress protector, waterproof mattress protector uae, mattress protector dubai, king size mattress protector*.

### 2.2d NEW: "Best Mattresses" curated collection (the market leader's #1 page by impressions)
- Handle `best-mattresses`, built as a **manual** collection of the top-rated/editor's-pick mattresses. This fits the MAYF curated positioning.
- Title: `Best Mattresses in UAE 2026 | Editor's Picks | MAYF Home`. Target *best mattress in uae, best mattress dubai, best mattress brands in uae, best memory foam mattress dubai, best cool gel mattress in uae*.
- Template `templates/collection.best.json` has an "Editor's pick for…" label on each product (from product metafield `custom.best_for`, e.g. "Back sleepers", "Hot sleepers", "Hotel feel"), a short "How we choose" block, FAQs, and a link to Guide #1.
- Link it from the homepage hero/secondary CTA and from the main menu.

### 2.3 Size-specific collections (pos 22–25)
Create smart-collection specs, using the condition **Variant's title contains `<size>`**, for each size that **actually exists in the catalogue** (check the variants first):
| Handle | Size | Target queries |
|---|---|---|
| mattress-90x200 | 90×200 | mattress 90x200, 200x90 mattress, single bed mattress 90 x 200 |
| mattress-90x190 | 90×190 | 90x190 mattress, mattress 90 x 190 |
| mattress-80x200 | 80×200 | 80x200 mattress, mattress 200x80 |
| mattress-180x200 | 180×200 | mattress 180x200, king size mattress 180 x 200, orthopedic mattress 180x200 |
| (others found in variants) | | |

Output these as `/seo/admin-actions/new-collections.csv` (handle, title, rule, SEO title, meta description, intro copy, FAQs). Link them from `/collections/shop-by-size` (already ranks at pos 2.6) and from the size filter area of `/collections/mattresses`.

### 2.4 Hotel Collection landing page (the only converting non-brand query)
- New collection `hotel-collection-mattresses` with the template `templates/collection.hotel.json`. It should include a hero ("5-star hotel sleep at home"), the story, a spec comparison of the hotel-collection products, and hotel bed foundations.
- Products to include: `signature-hotel-collection-mattress`, `hotel-collection-tight-top-mattress-by-mayf-home` and any other "hotel" products. Link to it from those product pages and from `/collections/the-hotel-bedroom`.
- Keywords: *hotel collection mattress, hotel mattress, hotel mattress dubai, 5 star hotel mattress uae, hotel collection bed foundations*.

### 2.5 Medical / orthopedic
- Keep `/collections/orthopedic-mattresses` and add SEO content that targets "orthopedic / orthopaedic mattress UAE".
- New collection `medical-mattresses`. Keywords: *medical mattress, medicated mattress, medical mattress dubai, medical mattress price in uae*. "Medical mattress" is the local UAE term. **Don't make medical or health claims.** Describe support/firmness only and add "consult your doctor for specific conditions".

### 2.6 SEO metadata for all existing mattress collections
Write `/seo/admin-actions/seo-metadata.csv` with columns `type,handle,seo_title,seo_description,h1` for:
mattresses, king-mattresses, super-king-mattresses, single-mattresses, queen-mattresses, memory-foam-mattresses, latex-mattresses, orthopedic-mattresses, firm-mattresses, medium-firm-mattresses, pocket-spring-mattresses, hybrid-mattresses, mattress-toppers, mattress-protectors, best-mattresses, bedding, pillows, pillow-cases.
**Priority order** (by market demand): mattresses → king → toppers → best-mattresses → latex → queen → protectors → memory-foam → the rest.
**Title rules from the market data:** a generic title gives a very low CTR (the leader's best-mattresses page gets 0.85% CTR at pos 6.5). Every title must carry *keyword + UAE/Dubai + one concrete USP* (e.g. free UAE delivery, 100-night trial, Tabby/Tamara instalments). **Only use USPs MAYF actually offers; mark each one `[VERIFY]`.** Meta descriptions should mention the delivery promise and BNPL (Tabby/Tamara are live).
Rules: primary keyword first, include "UAE" or "Dubai", and end with "| MAYF Home". *(The owner's n8n Google Sheets → Shopify workflow can push this CSV.)*

---

## Phase 3 — Content & internal linking

### 3.1 Blog article template
- Make sure `templates/article.json` outputs **Article/BlogPosting JSON-LD** (headline, datePublished, dateModified, author = MAYF Home, image) and a BreadcrumbList.
- Add an optional "Shop the products" block that reads `article.metafields.custom.featured_collection`.

### 3.2 Draft 7 buying guides
**Title rule:** the title must match the query intent word-for-word where it reads naturally. The market leader's "latex vs memory foam" article got 8.4K imps at 0.15% CTR because the title was generic.
Write them as HTML-ready markdown in `/seo/content/blog/`, 1,200–1,800 words each, with a title, meta, H2/H3 outline, FAQ and internal links to the collections above. **Don't invent competitor prices, stats or awards.** Mark anything that needs checking with `[VERIFY]`.
1. Best Mattress in UAE 2026: How to Choose (targets *best mattress in uae, best mattress brands in uae, top mattress brands in uae*)
2. Latex vs Memory Foam Mattress: Which Is Better for the UAE Climate?
3. Cooling Gel Mattresses: Sleeping Cool in UAE Summers (*best cool gel mattress in uae*)
4. UAE Mattress Size Guide: Single, Queen, King, Super King (links to every size collection)
5. What Is a Hotel Collection Mattress? Getting 5-Star Sleep at Home
6. Orthopedic vs Medical Mattress: What's the Difference?
7. Mattress Topper Buying Guide UAE: Memory Foam vs Latex vs Microfibre (*mattress topper, mattress topper uae*; links to toppers and protectors)

Guide #1 links to `/collections/best-mattresses`. Guide #2 title must be exactly: **"Latex vs Memory Foam Mattress: Which Is Better in the UAE?"**

### 3.3 Internal links
- Homepage: add a "Shop by size" row (Single / Queen / King / Super King) and a Hotel Collection feature block, using existing Dawn sections (`collection-list`, `image-with-text`). Don't create new sections unless you have to.
- Product pages: add a "Mattress size guide" link and a breadcrumb back to the size collection and the type collection.
- Footer: add links to Super King, Hotel Collection, Medical Mattresses and the Size Guide.

### 3.4 City pages
Create `templates/page.city.json` and draft copy for `/pages/mattress-delivery-dubai`, `/pages/mattress-delivery-abu-dhabi` and `/pages/mattress-delivery-sharjah`. Each page covers delivery times, service areas, the free home visit (link `/pages/book-a-free-visit`) and top collections. The copy must be **unique per city**, not the same text with the city name swapped. Put the copy in `/seo/content/pages/`.

---

## Phase 4 — Arabic (ar-AE)

1. Check whether the theme supports RTL. If not, change `layout/theme.liquid` to:
   `<html lang="{{ request.locale.iso_code }}" dir="{% if request.locale.iso_code == 'ar' %}rtl{% else %}ltr{% endif %}">`
   Then add an RTL stylesheet override (`assets/rtl.css`, loaded only when `ar`) that covers the header, drawer, product grid, carousel arrows and form alignment. Check it visually at 375px and 1440px.
2. Make sure `locales/ar.json` exists and is complete (copy the keys from `en.default.json` and translate them).
3. Confirm the hreflang alternates (`en-AE`, `ar-AE`, `x-default`) are output. Shopify Markets does this automatically when a language is published. Verify it and don't hand-code duplicates.
4. Admin action: publish Arabic via Translate & Adapt. Use **native Arabic copywriting, not machine translation**. Claude Code should draft the Arabic SEO titles, metas and intros in `/seo/content/ar/` and flag them for native review.
5. Arabic keyword map (market data + mayfhome data):

| Arabic query | Market imps | Target page |
|---|---|---|
| مرتبة سرير | 1,075 | /ar/collections/mattresses |
| مراتب سرير | 883 | /ar/collections/mattresses |
| مراتب | 477 | /ar/collections/mattresses |
| مرتبة | 361 | /ar/collections/mattresses |
| أفضل مراتب في الإمارات | 318 (4.7% CTR) | /ar/collections/best-mattresses + Arabic version of Guide #1 |
| ماتريس توبر | mayfhome data | /ar/collections/mattress-toppers |
| لحاف / غطاء لحاف دبي / شراء لحاف أونلاين في الشارقة | mayfhome data | /ar/collections/bedding |

Translation order: **mattresses → best-mattresses → mattress-toppers → bedding (duvets) → king / super king → Guide #1 in Arabic.**

---

## Phase 5 — Admin / off-theme checklist (write to `/seo/admin-actions/CHECKLIST.md`)
- [ ] Import `redirects.csv` (Online Store → Navigation → URL redirects → Import)
- [ ] Set the homepage title and meta (Preferences)
- [ ] Create the metafield definitions from `metafields.md`
- [ ] Create the collections from `new-collections.csv`; publish them to Online Store + Google & YouTube
- [ ] Push `seo-metadata.csv` via the n8n Sheets → Shopify workflow
- [ ] Publish the 7 blog articles and 3 city pages
- [ ] **Merchant Center (TOP PRIORITY: market benchmark is 30.7% CTR at pos 3):** fix product disapprovals; get 100% of the active catalogue into the feed (mattresses, toppers, pillows, bedding); complete pricing, availability, images, GTIN/MPN or `identifier_exists=false`; set shipping and returns policies; enable free listings (currently only 2 merchant-listing impressions)
- [ ] Product review schema: install/enable a reviews app that outputs `aggregateRating` in Product JSON-LD, so products can show star ratings in search
- [ ] Catalogue gap: source mattress protectors (waterproof, cooling, all UAE sizes)
- [ ] Choose 6–10 products for `best-mattresses` and fill in the `custom.best_for` product metafield
- [ ] **Deadline: all Phase 2–3 pages live by 15 Jan 2027** (before the Ramadan dip)
- [ ] Google Business Profile: link to mayfhome.com and add the URL to `sameAs`
- [ ] Search Console: resubmit `sitemap.xml`; request indexing for Super King, the size collections and the Hotel Collection; use Removals for `/collections/frontpage` if it's still showing after 2 weeks
- [ ] Optional paid: Performance Max / Shopping for the Super King and Hotel lines while organic rankings build

---

## Phase 6 — Final QA (Claude Code must do this before reporting done)
- `shopify theme check` passes with no new errors.
- In the preview theme, for the homepage, 1 collection, 1 product, 1 article and 1 search page, confirm each has:
  - exactly one `<h1>`, one canonical and the correct robots meta
  - valid JSON-LD (parses; no duplicate Organization)
- Mobile (375px) and desktop render correctly; the RTL render is correct if Phase 4 was done.
- Summarise what changed in the theme, what's waiting in `/seo/admin-actions/`, and anything marked `[VERIFY]`.

---

## KPIs to track (check in Search Console every 2 weeks)
| KPI | Now | 60-day target |
|---|---|---|
| "mayf" position | 10.5 | **1** |
| Super King cluster avg position | 27 | ≤ 12 |
| Size-query avg position | 22–25 | ≤ 10 |
| Non-brand clicks share | ~25% | > 50% |
| Merchant listing impressions | 2 | > 500 |
| Desktop avg position | 43 | < 30 |
| Mattress topper collection position | 46 | ≤ 15 |
| Hotel collection mattress position | 15 | ≤ 8 (beat the market leader's 14.7) |
| Collection-page CTR (at pos ≤ 10) | – | ≥ 2% (market leader averages 0.8–1.2% on generic titles) |
