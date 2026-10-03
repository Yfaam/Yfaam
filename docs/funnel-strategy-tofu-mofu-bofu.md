# MAYF Home: TOFU / MOFU / BOFU strategy and sales scalability

Prepared 3 Oct 2026. Builds on `docs/homepage-conversion-pack.md` and the homepage changes on the unpublished theme copy (194249392500).
Numbers marked **[assumption]** are planning placeholders to replace with MAYF's own margins and costs. Everything else is read from the store.

---

## 0. Where the business is today (read from Shopify, last 45 days)

| Signal | Value |
|---|---|
| Real orders | **0** (1 test order, AED 1.90) |
| UAE sessions | 484 (US 607, mostly non-buyer traffic; ignore for performance) |
| UAE funnel | 13 add-to-cart → 10 reached checkout → **0 completed** |
| Traffic sources | Direct 1,035 · Google 62 · Facebook 45 · ChatGPT 10 · Bing 1 |
| Active products showing 0 stock | **19** (signature mattress, kids mattress, all 3 hotel bundles, duvets, pillows, toppers, most beds). **Checked 3 Oct: inventory tracking is OFF on all 107 variants, so zero stock is not what blocks checkout.** 3 pieces per variant were then recorded at Shop location (tracking still off). |
| Placeholder copy still live | Aurelia, Valor, Lumière beds: "details coming soon" |
| Missing SKUs | Mattresses, beds, bundles (blocks Google/Meta catalog feeds) |

**Conclusion: this is a checkout problem, not a traffic problem.** Ten people got as far as paying and none could. Until one real order completes end to end, ad spend only buys more abandoned checkouts. So the plan has a gate before any funnel work.

---

## 1. Gate 0: make one real order possible (this week, before any spend)

Done only when a stranger-style test order succeeds on card, on Tabby/Tamara, and on cash on delivery (if offered), and arrives in the order list.

1. **Stock (checked, not the blocker):** the 19 flagged products are untracked, so they can be bought regardless of count. Decide per product whether it is made-to-order (leave untracked) or stocked (enable tracking with real counts). Note that turning tracking on with 3 pieces would cap sales at 3 per variant and trigger the theme's "Only N left" label (threshold 5), so do it only for items that are truly stocked.
   **Then find the real blocker:** since stock is not it, look at payment methods at checkout (Tabby/Tamara/cards/COD), shipping rates for UAE addresses, checkout errors, and run a real test order.
2. **Delivery lead time** shown before checkout, matching the shipping policy (mattresses and bedding 2–3 working days, beds and furniture 5–6, made-to-order shown on the page). Where stock is "made to order", say so on the product page.
3. **Payment:** confirm Tabby and Tamara appear at checkout, not just in the badge text. Decide on cash on delivery for orders under a cap.
4. **Shipping rates:** all seven emirates, free over AED 500, remote-area rule matching the policy.
5. **Placeholder products:** finish or draft Aurelia, Valor, Lumière. A "details coming soon" bed at AED 1,499 to 2,499 costs trust.
6. **Tracking:** verify purchase, add-to-cart and checkout events fire in GA4/Meta/TikTok before spending. Clarity and Judge.me are already installed.
7. **SKUs and brand spelling** on mattresses, beds and bundles (needed for shopping feeds).

**Gate metric:** at least 3 completed real orders from outside the team, then open the funnel.

---

## 2. The funnel mapped to the new storefront

| Stage | Customer question | Storefront pieces now live (on the copy) |
|---|---|---|
| **TOFU** | "I have a sleep or home problem" | Shop by Need, six-category grid, hero routes |
| **MOFU** | "Which one is right, and can I trust MAYF?" | Mattress finder banner, Shop the Room, proof strip, Why MAYF, comparison (to build), reviews (to build) |
| **BOFU** | "Is it safe to buy, and what if it's wrong?" | 100-night trial, warranty, delivery terms in FAQ, Tabby/Tamara, curtain estimator/visit, WhatsApp |

---

## 3. TOFU: get the right people to the site

**Audience, in priority order**
1. **New movers and handovers** (expats, new-build handovers): "The First Home" room is the hero offer.
2. **Upgraders who want hotel sleep:** Signature Hotel mattress plus bedding set.
3. **Holiday-let hosts and property managers (B2B):** furnish-a-unit bundles with the FR hotel mattress. Highest basket size, so give them their own page and WhatsApp route.
4. **Curtain buyers:** large windows, motorised, blackout. Curtains are the most visual and shareable product.

**Content pillars (English and Arabic, short video first)**
- Hotel-bed transformations (before/after bedroom)
- Mattress cut-open and layer explainers ("what is pocket spring vs memory foam")
- Curtain measuring and install day, motorised demos
- Delivery and assembly day (shows the service promise)
- "Which mattress for…" series (hot sleepers, couples, back pain, kids), each ending on the finder

**Channels and role**
| Channel | Role | Start with |
|---|---|---|
| Instagram + TikTok (organic) | Brand and demand creation | 4–5 Reels/week; no social data connected yet, so connect the accounts first |
| Meta / TikTok paid | Cold reach on the best organic videos | Small tests only after Gate 0; spend ranges are **[assumption]**, set against margin below |
| Google Search | Capture existing demand | "king mattress Dubai", "hotel mattress UAE", "motorized curtains Dubai", "mattress delivery Abu Dhabi" |
| SEO | Compounding free traffic | Collection and guide pages per the existing SEO brief (king, memory foam, latex, super-king clusters sit at positions 30–55 today) |
| AI search (ChatGPT already sends traffic) | Free discovery | Buying-guide and comparison pages with FAQ markup (the homepage FAQ now has it) |
| Cross-promotion | Warm start | Mention MAYF from the sister brand's audience if the owner is the same |

**TOFU KPIs:** UAE sessions, finder starts per 100 sessions, Shop-by-Need click rate, cost per landing-page view, share of traffic from non-direct sources (today about 9%).

---

## 4. MOFU: help them choose and prove trust

This is the biggest gap the review found, and the storefront now supports it. What to add around it:

1. **Make the finder a lead engine.** At the end of the quiz, offer "send my result to WhatsApp or email". That captures a contact with stated needs (sleep position, feel, budget), the best segmentation data you can have.
2. **Essential / Signature / Luxe comparison** page and homepage block. Needs real specs (firmness, cooling, motion isolation) and starting prices. I can build it once you send them.
3. **Real reviews, then real UGC.** Seed 15–20 honest reviews by offering trial units to real households and micro-creators, disclosed as gifted. Judge.me is installed; turn on photo reviews and post-delivery review requests (14–21 days after delivery). Do not publish placeholder testimonials; keep the empty section disabled until real ones exist.
4. **Remove unearned claims** ("best-seller", "most popular") until sales exist. Rename to "Our picks" now.
5. **Retargeting audiences:** viewed a product, started the finder, added to cart, watched 50% of a video, opened the curtain estimator.
6. **Email and WhatsApp nurture** for finder completers and newsletter sign-ups: day 0 result, day 2 "how the 100-night trial works", day 5 comparison, day 8 bundle offer.
7. **Curtain consultation funnel:** estimator → booked visit → quote. Track as its own pipeline; it is a lead product, not a cart product.

**MOFU KPIs:** finder completion rate, contacts captured per 100 sessions, review count and average, add-to-cart rate (UAE baseline today: about 2.7%), email/WhatsApp reply rate.

---

## 5. BOFU: convert and remove the last doubt

1. **Checkout reliability first** (Gate 0). It is the entire BOFU problem today.
2. **Risk reversal everywhere a price appears:** 100-night trial (21-night adjustment, AED 250 collection fee, one mattress per household), 10-year warranty, free delivery over AED 500 with the policy wording. Keep wording identical across site, ads and WhatsApp.
3. **Instalments up front:** show "from AED X/month with Tabby/Tamara" on product pages and ads, since baskets run AED 1,500 to 9,000.
4. **Abandoned-cart recovery:** email plus WhatsApp within 1 hour and 24 hours; there are already people who reached checkout. Offer a human ("Need help? Chat with an expert"), not only a discount.
5. **Honest urgency only:** real delivery cut-off (4 PM dispatch) and real low stock; no fake countdowns.
6. **Founding-customer offer:** time-limited, margin-safe (for example free pillows or mattress protector with a mattress) rather than a blanket discount, which trains customers to wait.
7. **Raise order value:** "complete the bed" add-ons (protector, pillows, duvet, sheets) on every mattress; bundles priced together; delivery-day upsell for old-mattress removal.
8. **Branded search protection:** bid on "MAYF", "MAYF Home" and the Arabic transliteration; the brand name currently ranks around position 10 with no clicks.
9. **WhatsApp as the closing channel:** reply templates for the ten common questions (the homepage FAQ is the source), a quote-by-WhatsApp flow for curtains and B2B, and a fixed response window shown on site.

**BOFU KPIs:** checkout completion rate (today 0 of 10), cost per completed order, average order value, add-on attach rate, abandoned-cart recovery rate, payment-method mix (card vs instalment vs cash).

---

## 6. After the sale (this is what makes growth cheaper)

- Delivery and assembly confirmation, then a 14–21 day review request with a photo prompt.
- Cross-sell by timing: bedding at order, protector and pillows at 30 days, pillow replacement reminder at 12 months, curtain visit offer at 60 days.
- Referral: "give a friend a free measurement, get a pillow" style reward.
- Handle returns and trial claims fast; each resolved well is a future review.

---

## 7. Sales scalability

### 7a. Know the numbers before scaling spend (fill these in)
| Input | Value |
|---|---|
| Gross margin per category (mattress, bedding, beds, curtains) | needed from owner |
| Delivery + assembly cost per order | needed |
| Expected trial-return rate × AED 250 collection cost | needed |
| Payment fees (cards, Tabby, Tamara) | needed |
| **Break-even CAC** = contribution margin per order after the above | compute |
| **Target CAC** (a share of break-even, **[assumption]** 50–60%) | decide |

Scaling rule: no category scales on ads until its contribution margin per order is known and positive after trial returns and delivery.

### 7b. Stage gates for spend (replace thresholds with your own once margins are known)
| Stage | Condition to enter | Allowed action |
|---|---|---|
| 0 | none | Fix checkout; spend nothing |
| 1 | 3 real orders completed | Small test budgets on 2 campaigns, retargeting first |
| 2 | Cost per order below target for 7 days with at least 5 orders | Raise budget in steps of about 20% every few days |
| 3 | Steady for 4 weeks | Add the next channel (TikTok Spark Ads, Google Shopping/PMax) |
| 4 | Contribution-positive across channels | B2B channel, partnerships, new markets |

### 7c. Operations that must scale with orders
- **Fulfilment capacity:** assembly and delivery crews per emirate per day; a visible delivery-window system; lead-time promises on each product page that the operation can keep.
- **Inventory model:** stocked vs made-to-order per SKU; reorder points for stocked items; supplier lead times; avoid selling what you cannot deliver.
- **Support:** WhatsApp is the main channel. Add a shared inbox with saved replies, business hours (Sat–Thu 9am–9pm per the footer), and an owner for each question type before volume grows.
- **Catalog quality:** SKUs, product types, one brand spelling, no duplicate lines (two kids latex mattresses, overlapping latex lines), so feeds and filters work.
- **Returns and trials:** a clear process and cost tracking for the 100-night trial; monitor return rate per mattress.

### 7d. Growth levers in order of leverage
1. Checkout fix and payment options (unlocks everything else)
2. Reviews and UGC (lifts every conversion rate)
3. Bundles and add-ons (raises order value without more traffic)
4. B2B / trade channel (large baskets, repeat orders)
5. Email/WhatsApp retention (lowers blended CAC)
6. SEO and AI-search content (compounding, slow)
7. Paid social and shopping at scale
8. New markets (KSA, Oman, Qatar) only after UAE economics hold
9. Showroom or pop-up partnerships for touch-and-feel buyers

### 7e. Measurement stack
GA4 + Meta Pixel/CAPI + TikTok Pixel + Google & YouTube channel + Clarity (already installed) + Judge.me. One dashboard weekly: sessions by source (UAE only), funnel (session → ATC → checkout → order), cost per order, AOV, contribution margin, review count, return rate.

---

## 8. 30 / 60 / 90 days

**Days 0–14: Gate 0.** Stock policy, payments, shipping, placeholders, tracking, one real order. Publish the theme copy after previewing it in English and Arabic.

**Days 15–45: first orders.** Reviews seeding, social launch (4–5 Reels/week), finder-to-WhatsApp capture, abandoned-cart flows, small paid tests (retargeting first, then cold), branded search, comparison page (once specs are provided).

**Days 46–90: repeatability.** Raise spend through the gates, add Google Shopping/PMax after SKUs are fixed, launch the trade page and outreach to hosts and property managers, bundle optimisation, retention flows, SEO collection and guide pages.

---

## 9. Weekly scorecard (one page)

| Metric | Today | Gate-0 target | 90-day target **[assumption]** |
|---|---|---|---|
| Completed real orders | 0 | 3 | set after margins |
| UAE checkout completion | 0 of 10 | above 0 | set from first 20 orders |
| Add-to-cart rate (UAE) | about 2.7% | hold | improve with proof and finder |
| Non-direct traffic share | about 9% | n/a | grow with content and SEO |
| Reviews on site | 0 | 3 | 20+ |
| Contacts captured (finder, newsletter) | not tracked | start tracking | track weekly |

---

## 10. What I need from you to sharpen this
1. Margins and costs per category, and delivery/assembly cost.
2. Which products are truly stocked and which are made to order.
3. Whether cash on delivery will be offered, and Tabby/Tamara status.
4. Real specs for the Essential / Signature / Luxe comparison.
5. Social account access (Instagram, TikTok, Facebook, Meta ad account) so I can see real performance.
6. Permission to run the checkout and stock fixes in Shopify (changing inventory settings affects the live store, so I will ask before touching it).
