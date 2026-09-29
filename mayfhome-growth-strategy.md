# Mayf Home: Store & Social Analysis, Growth Strategy

Prepared 29 Sep 2026. Data comes from the live Shopify store `fhbcaa-rd.myshopify.com` (mayfhome.com), read through the Shopify connector. The public website itself could not be crawled from this environment, so on-page SEO (titles, meta, schema, speed) is **not** covered here.

---

## 1. Where the business actually is

| Metric (last 12 months) | Value | Read |
|---|---|---|
| Store live since | Aug 2026 (password page until recently) | Pre-launch / week-6 store |
| Real orders | **0** (1 × 1.90 AED test order) | No revenue yet |
| Sessions | 979 (Aug 338, Sep 641) | Growing, but mostly not buyers (see below) |
| Sessions from UAE | **227** | This is the real audience |
| UAE add-to-carts | 13 (5.7% of UAE sessions) | Healthy intent for a new store |
| Reached checkout / completed | 11 / **0** | Everyone who tried to buy dropped out |
| Traffic sources | Direct 906 · Google 57 · **ChatGPT 10** · Facebook 5 | Almost no social traffic |
| Catalog | 70 products: 52 active, 18 draft · 36 collections | Broad range, uneven data quality |
| Plan / currency | Shopify Basic · AED | Fine for this stage |

**Traffic caveat:** 688 of the 979 sessions came from the **United States**, mostly desktop, direct, and landing on `/`. That pattern fits bots, crawlers, app previews and the team's own testing, not UAE shoppers. Judge performance on the 227 UAE sessions only.

**Bottom line:** this isn't a scaling problem yet. It's a **launch and conversion** problem. People add to cart, but no checkout has ever finished. Fix that first, because every dirham spent on ads before then is wasted.

---

## 2. Store findings, most urgent first

### Critical: things that block sales

1. **Most active products show 0 inventory.** Examples include the Signature Hotel Collection Mattress (tagged best-seller), Cooling Gel Memory, Cool Fusion, Kids mattresses, all 3 Hotel bundles, all upholstered beds except one, and most bedding. If inventory is tracked and "Continue selling when out of stock" is off, these can't be bought at all. That could explain 11 checkouts with 0 completions.
   **Fix:** for made-to-order and drop-ship items (mattresses, beds, sofas, curtains), turn off inventory tracking or enable "continue selling". Then place a real test order with a real card and with cash on delivery.
2. **Checkout abandonment is 100%.** Beyond stock, check the following:
   - Are UAE shipping rates set for every emirate?
   - Does free delivery apply above a threshold?
   - Is cash on delivery enabled?
   - Are **Tabby / Tamara** (buy now, pay later) installed? For UAE baskets of 1,000–9,000 AED, splitting the payment into instalments is often what makes people buy.
   - Is the delivery lead time shown before checkout?
3. **Placeholder products are live.** *Lumière Bed*, *Aurelia Bed* and *Valor Bed* say "details coming soon". *Bubble Bed (9,000 AED)* and *MAYF Kids latex Mattress* have empty descriptions. On a high-ticket item this kills trust. Finish them or set them back to draft.

### High: trust and compliance

4. **Unearned claims.** Products are tagged or described as "best-seller", "most popular" and "our most popular starting point" when the store has had no sales. Shoppers can see through it, and UAE consumer-protection rules treat misleading claims seriously. Rename the collection to "Customer Favourites" once reviews exist, or to "Our Picks" for now.
5. **No reviews and no social proof.** Install a reviews app (Judge.me or Loox) now, even before orders arrive. Seed it by gifting sleep-trial units to 10–20 real people or micro-influencers in exchange for honest reviews, disclosed as such.
6. **Duplicate and competing products.** Two kids latex mattresses (950 vs 699 AED), overlapping latex lines ("MAYF Latex Natural" and "Nature's Haven"), and Tight Top vs FR Tight Top. Merge duplicates or explain the difference clearly (for example "FR = fire-retardant certified for hotels and rentals").

### Medium: catalog hygiene (affects SEO, filtering and ads)

7. **Four different brand spellings** in vendor and title fields: `Mayf home`, `Mayf Home`, `MAYF Home`, `MAYF HOME`, plus title suffixes "by Mayf Home" and "By Mayfhome". Pick one (**MAYF Home**) and use it everywhere.
8. **Missing SKUs** on roughly 90 variants (all mattresses, beds and sofas). Google Merchant Center and Meta catalog ads need consistent IDs, so fill them before running shopping ads.
9. **8 products have no product type** (all 3 sofas, the Taupe bed, Bubble Bed, and others), so they drop out of type-based collections and filters.
10. **Broken collections:**
    - *The Family Living Room* and *Orthopedic Mattresses* have **0 products** but are published, so they show as empty pages.
    - *Furniture* uses the same rule as *Beds* (`tag = bed`), so no sofas appear in Furniture.
    - *Shop by Size* matches only 3 products because its rules use `single` and `super singles`, while the products are tagged `single size` and `Super single`.
    - *Soft* and *Firm* have 1 product each. Merge them into a "Shop by Firmness" filter instead.
11. **18 draft products** include half the bedding colourways (pillow cases, sheets) and 5 mattresses. They have no images. Either photograph and launch them as sets, or delete them.

---

## 3. Social media findings

- **No Mayf Home social data is connected.** The Supermetrics connector only reaches **@mayfperfumes** on Instagram and TikTok, plus Meta ad accounts for other businesses (Prima Chic, Taif, Ramasat, and others). The Supermetrics trial has also **expired**.
- **Social currently drives 5 sessions, all from Facebook.** Instagram and TikTok send no traffic to the store at all.
- A public web search found no indexed Mayf Home social profiles.

**What that means:** social is a blank slate. That's an advantage, because you can set the positioning up correctly from day one.

**Quick-win leverage:** if @mayfperfumes is the same owner and brand family, its audience is already warm to the MAYF name. Cross-promote with a launch post, bio link and stories, and consider a *"MAYF Hotel Night" bundle* (pillow mist or room scent plus pillow or duvet) to connect the two brands.

**To analyse social properly next time:**
- Connect the Mayf Home Instagram, TikTok and Facebook Page, plus its own Meta ad account.
- Renew Supermetrics, or share exported insights.

---

## 4. Positioning: where Mayf Home can win

Competitors fall into two camps:
- **Big showroom brands:** King Koil, Magniflex, Home Centre.
- **Online value sellers:** Mattress Souq, Wakefit, and other bed-in-a-box brands.

MAYF's catalog already points to a gap neither camp owns:

> **"Hotel-grade sleep, delivered and installed across the UAE."**

Supporting evidence from the catalog:
- A **Hotel Collection** (including fire-retardant FR versions).
- **Room-based bundles**: Hotel Bedroom, Couple's Bedroom, First Home.
- **Made-to-measure and motorised curtains**.
- An **interior-design service**.

The service pages are already pulling organic visits: `/pages/interior-designing` 11 sessions and `/pages/curtains-service` 7.

**Three customer segments to build around:**

| Segment | Why the UAE | Hero offer |
|---|---|---|
| **Holiday-home / Airbnb hosts and property managers** (B2B) | Dubai has a very large short-term-rental market, and hosts refurnish frequently. The FR mattresses fit hotel and holiday-home compliance needs. | "Furnish-a-unit" packages: Hotel Suite, Essential and Complete bundles plus curtains. Trade pricing and invoicing. |
| **New movers / first-home buyers** (expats, handovers) | High population turnover and constant new-building handovers. | "The First Home" room package: mattress, bed, bedding and blackout curtains in one delivery. |
| **Upgraders who want a hotel bed** | Hotel sleep is aspirational in the Gulf. | Signature Hotel mattress, 300TC bedding set and a trial period. |

---

## 5. Strategy to scale: phased

### Phase 0: make the store able to sell (weeks 1–2)
- [ ] Fix the inventory / continue-selling settings, then complete a real test order (card and cash on delivery).
- [ ] Add Tabby and/or Tamara, set clear UAE shipping and a free-delivery threshold, and show the delivery ETA on product pages.
- [ ] Unpublish or finish the placeholder products. Remove or rename the "best-seller" and "most popular" claims.
- [ ] Standardise the brand name and add SKUs and product types. Fix the 4 broken collections.
- [ ] Add trust blocks to every mattress page: sleep trial (e.g. 100 nights), warranty, free delivery and old-mattress removal, and "made/finished in UAE" if true.
- [ ] Add a WhatsApp chat button. For UAE furniture, most high-ticket sales close in chat.
- [ ] Install Meta Pixel + Conversions API, the TikTok Pixel and Google & YouTube channels, and verify that purchase events fire.

### Phase 1: first 50 orders (weeks 2–6)
- [ ] **Launch offer:** a founding-customer price or free bedding with any mattress, time-limited.
- [ ] **Seed reviews:** 15–20 gifted or trial units to real households and micro-creators in Dubai and Abu Dhabi, with honest reviews and photos.
- [ ] **Social launch:**
  - Instagram and TikTok, 4–5 Reels a week, in English and Arabic.
  - Content pillars: *hotel-bed transformations*, *motorised-curtain demos* (very visual and shareable), *mattress cut-open / layer explainers*, *delivery and installation day*, *room reveals*.
- [ ] **Paid social (small tests of about 100–150 AED a day):**
  - Meta Advantage+ catalog ads to UAE audiences aged 25–54.
  - Retarget add-to-carts, which already exist (13).
  - Spark Ads on TikTok using the best-performing organic Reels.
- [ ] **Google:**
  - Performance Max using the Merchant Center feed.
  - Search campaigns on high-intent terms: "hotel mattress Dubai", "motorized curtains Dubai", "blackout curtains Abu Dhabi", "mattress delivery same day Dubai".

### Phase 2: repeatable growth (months 2–4)
- [ ] **B2B channel:**
  - A `/pages/trade` landing page for Airbnb hosts, property managers and interior designers, with volume pricing and a quote form.
  - Outreach on LinkedIn and in host communities.
  - This segment brings large baskets and repeat orders.
- [ ] **Raise order value:**
  - A "complete the bed" upsell (protector, pillows, duvet, sheets) on every mattress.
  - Put the draft bedding colourways back on sale as **sets**.
- [ ] **Email and WhatsApp flows:** abandoned cart (you already have abandoners), post-purchase review request, 30-day bedding cross-sell, and a 12-month pillow replacement reminder.
- [ ] **SEO and AI search:** ChatGPT already sent 10 sessions, so AI answers are finding you. Add:
  - Comparison and buying-guide content, e.g. "Hotel vs memory foam mattress for UAE heat", "What size is a super king in UAE", "Best curtains for Dubai sun".
  - FAQ blocks, and Product + Review schema.
  - Re-run the `/seo audit` once the site is reachable from this environment.

### Phase 3: scale (months 4+)
- [ ] Scale ad spend only on campaigns with ROAS ≥ 3 (high-ticket furniture can often support a lower ROAS if the cost to acquire a customer is below 25% of order value).
- [ ] Showroom partnerships or pop-ups in malls or design districts, since mattress buyers like to touch the product.
- [ ] Expand to KSA, Oman and Qatar once UAE unit economics are proven.
- [ ] Upgrade from Shopify Basic when professional reports, lower card fees or B2B features are needed.

---

## 6. KPIs to track weekly

| KPI | Now | 90-day target |
|---|---|---|
| UAE sessions / month | ~150 | 3,000+ |
| Add-to-cart rate (UAE) | 5.7% | ≥ 6% |
| Checkout completion | 0% | ≥ 40% of checkouts |
| Store conversion rate | 0% | 1.0–1.5% |
| Orders / month | 0 | 50–80 |
| Average order value | – | 1,500+ AED |
| Reviews published | 0 | 40+ |
| Social-referred sessions | 5 | 20% of traffic |
| B2B / trade accounts | 0 | 5–10 |

*The targets are directional benchmarks for a new UAE furniture and mattress store, not forecasts.*

---

## 7. Gaps in this analysis
- **Website crawl blocked:** there is no on-page, technical, schema or Core Web Vitals audit yet. Allow `mayfhome.com` in the environment's network settings and re-run `/seo audit`.
- **No Mayf Home social or ad data:** connect those accounts, and renew or replace Supermetrics.
- **Competitor pricing:** not collected. Worth a pass on Mattress Souq, King Koil and Home Centre prices for matching sizes.

Sources (market context): [ebarza: choosing a mattress in Dubai 2026](https://www.ebarza.com/blogs/news/how-to-choose-the-right-mattress-in-dubai-for-a-perfect-sleep-in-2026) · [ebarza: hotel mattress brands Dubai](https://www.ebarza.com/blogs/news/how-to-choose-the-perfect-hotel-mattress-in-dubai-top-10-brands) · [Gulf News: The Mattress Store UAE](https://gulfnews.com/amp/business/corporate-news/the-mattress-store-energises-the-uae-with-premium-quality-bedroom-furniture-and-mattress-products-1.1680682311917) · [Wakefit enters UAE](https://startup2.outlookindia.com/sector/e-commerce/wakefit-co-products-now-available-for-customers-in-uae-market-news-9308)
