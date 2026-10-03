# MAYF Home: Homepage Conversion Pack (EN / AR)

Source: homepage review of 3 Oct 2026. Ready to drop into the theme once it is in the repo.
Rules used: no invented reviews, prices or stats. `[X]` marks values to fill from real data.
Arabic copy is a first draft and needs review by a native speaker before going live.

## 0. Fix first (store data, not theme code)

| # | Issue | Where to fix | Action |
|---|-------|--------------|--------|
| 1 | "Free Delivery Across UAE" contradicts shipping policy (free over AED 500, remote-area surcharges possible) | Theme text, every occurrence (hero, announcement bar, product pages, cart, footer, `locales`) | Replace with the accurate line below |
| 2 | "Curtains for Large & Floor-to-Ceiling Windows" shows AED 0.00 on the homepage (collection shows from AED 89) | Shopify admin: product variants / price, or the homepage card's product/price source | Check the variant the card reads (likely a zero-priced first variant or a missing "from" price); show "From AED 89" |
| 3 | "Bundles & Sets: Save 15% on the Complete Room" leads to 0 products | Shopify admin: Bundles collection | Hide the card until 3 to 4 real bundles are published (see section 7) |
| 4 | Arabic homepage still has English UI strings ("Shop Beds", "Premium Quality", "Expert Support", "Secure Payments", "Sleep better, starting tonight") | `locales/ar.json` and any hard-coded section text | Translate using the table in section 11 |

**Delivery line (use everywhere)**
- EN: `Free UAE Delivery on Orders AED 500+`
- AR: `توصيل مجاني داخل الإمارات للطلبات من 500 درهم فأكثر`
- Footnote where space allows: EN `Remote areas may incur a delivery charge.` / AR `قد تُطبّق رسوم توصيل إضافية على بعض المناطق النائية.`

## 1. Target homepage order

Hero → Proof strip → Shop by Category → Shop by Need → Mattress Finder → Best Sellers → Reviews / Why customers choose MAYF → Hotel Collection → Essential / Signature / Luxe → Shop the Room → Complete Bedroom Bundles (only when live) → Curtains: Free Measurement → Real UAE Homes (only when real UGC exists) → Beds & Living → FAQs → Sleep Guide signup → Footer.

Keep: "Bring Hotel Comfort Home", 100 nights / 10 years, Shop the Room, the Mattress Finder, WhatsApp, the existing nav.

## 2. Hero CTAs

| | EN | AR |
|---|----|----|
| Primary (keep) | Shop Mattresses | تسوّق المراتب |
| Secondary | Find My Mattress → (`/pages/finder`) | اعثر على مرتبتي ← |
| Tertiary | Book Free Curtain Measurement → | احجز قياس الستائر المجاني ← |

## 3. Proof strip (directly under hero)

| EN | AR |
|----|----|
| 100-Night Mattress Trial | تجربة المرتبة 100 ليلة |
| 10-Year Mattress Warranty | ضمان المرتبة 10 سنوات |
| UAE Delivery & Assembly | توصيل وتركيب داخل الإمارات |
| Pay with Tabby & Tamara | ادفع عبر تابي وتمارا |
| WhatsApp Experts | خبراء عبر واتساب |

Delivery detail for tooltip / FAQ (from shipping policy): room-of-choice delivery, furniture assembly, packaging removal, optional old-mattress removal.

## 4. Shop by Category (expand to 6)

Mattresses / Beds / Bedding / Curtains / Sofas & Living / Kids

| EN | AR |
|----|----|
| Mattresses | المراتب |
| Beds | الأسرّة |
| Bedding | مفروشات النوم |
| Curtains | الستائر |
| Sofas & Living | الأرائك والمعيشة |
| Kids | الأطفال |

## 5. Shop by Need: "What are you looking for?" / «ماذا تبحث عن؟»

| EN card | AR card | Link to (confirm collections exist) |
|---------|---------|------------------------------------|
| Bring Hotel Sleep Home | أحضر نوم الفنادق إلى منزلك | Hotel Collection |
| I Sleep Hot | أشعر بالحرارة أثناء النوم | Cooling mattresses |
| Back & Body Support | دعم الظهر والجسم | Firm / supportive mattresses |
| Couples & Motion Isolation | للأزواج وعزل الحركة | Pocket-spring / motion isolation |
| Kids & Growing Sleepers | للأطفال والنائمين الصغار | Kids |
| New Home Essentials | أساسيات المنزل الجديد | First Home room set |
| Large Windows & Curtains | النوافذ الكبيرة والستائر | Large-window curtains |
| Upgrade My Entire Bedroom | جدّد غرفة نومي بالكامل | Shop the Room |

## 6. Mattress Finder section

- EN: **Not sure which mattress? Find your match in 60 seconds.** Four questions: sleep position, feel, body type, budget. Button: `Find My Mattress`
- AR: **لست متأكدًا أي مرتبة تناسبك؟ اعثر على مرتبتك المثالية في 60 ثانية.** أربعة أسئلة: وضعية النوم، الملمس، نوع الجسم، الميزانية. الزر: `اعثر على مرتبتي`
- Placement: immediately before or after Best Sellers. Link to existing `/pages/finder`.

## 7. Bundles (launch only when real)

Publish these four, then re-enable the homepage card. Each card shows regular combined price, bundle price, and AED saved.

| Bundle | Contents (map to real SKUs) | Regular | Bundle | You save |
|--------|----------------------------|---------|--------|----------|
| Hotel Sleep Bundle | mattress + pillows + duvet [SKUs] | [X] | [X] | [X] |
| Better Sleep Bundle | [SKUs] | [X] | [X] | [X] |
| Couple's Comfort Bundle | [SKUs] | [X] | [X] | [X] |
| New Home Bedroom Bundle | [SKUs] | [X] | [X] | [X] |

The "Save 15%" claim must match the real discount. Until bundles are live, hide the card.

Shop the Room: inside each room (The Hotel Bedroom, Couple's Bedroom, Minimalist Bedroom, First Home) list every product with its price and a `Buy the Complete Look: Save [X]%` / `اشترِ الإطلالة كاملة: وفّر [X]٪` button.

## 8. Essential / Signature / Luxe comparison

Show firmness, ideal sleeper, cooling level, motion isolation, trial, warranty, starting price. Fill from real product specs.

| | Essential | Signature | Luxe |
|--|-----------|-----------|------|
| Tagline EN | Hotel Collection | Cooling & Comfort | Natural Latex / Premium Hotel |
| Tagline AR | مجموعة الفنادق | تبريد وراحة | اللاتكس الطبيعي / فخامة الفنادق |
| Firmness / ideal sleeper / cooling / motion isolation | [X] | [X] | [X] |
| Trial / warranty | 100 nights / 10 years | 100 nights / 10 years | 100 nights / 10 years |
| From | AED [X] | AED [X] | AED [X] |

Column names AR: الأساسي / المميز / الفاخر.

## 9. Curtains lead-gen section

- EN: **Perfect Fit. Measured & Installed.** Buttons: `Get an Instant Estimate` · `Book Free Measurement` · `WhatsApp a Curtain Expert`
- AR: **قياس مثالي. نقيس ونركّب.** الأزرار: `احصل على تقدير فوري` · `احجز قياسًا مجانيًا` · `تواصل مع خبير الستائر عبر واتساب`
- Links: existing Online Price Estimator, Book a Free Visit, WhatsApp number.
- Large-window card price: "From AED 89" (verify against the collection before publishing).

## 10. Why MAYF Home (5 short points, before newsletter)

| EN | AR |
|----|----|
| Designed for UAE Homes | مصمّم للمنازل في الإمارات |
| Hotel-Inspired Comfort | راحة مستوحاة من الفنادق |
| Considered Prices | أسعار مدروسة |
| Expert Local Support | دعم محلي من الخبراء |
| Delivered & Installed | توصيل وتركيب |

## 11. Reviews and UAE Homes (data-dependent)

- Reviews: show real verified reviews and star ratings only. If a product has none, show nothing rather than "Be the first to write a review" on the homepage. Send a review request email 14 to 21 days after delivery.
- "Real MAYF Homes Across the UAE" / «منازل مايف الحقيقية في الإمارات»: add only once genuine customer photos or curtain-installation videos exist (Dubai, Abu Dhabi, Sharjah, Ajman). Get written permission before use.

## 12. FAQs (place directly before email capture)

Answers marked [policy] must be copied from the live shipping/returns/warranty pages, not paraphrased from memory.

| Question EN | Question AR | Answer source |
|-------------|-------------|---------------|
| How does the 100-night trial work? | كيف تعمل تجربة الـ100 ليلة؟ | [policy] |
| What happens if I return a mattress? | ماذا يحدث إذا أرجعت المرتبة؟ | [policy] |
| What does the 10-year warranty cover? | ماذا يغطي ضمان الـ10 سنوات؟ | [policy] |
| Is delivery free? | هل التوصيل مجاني؟ | Free on orders AED 500+; remote areas may incur a charge |
| Do you assemble beds? | هل تقومون بتركيب الأسرّة؟ | Yes: furniture assembly is part of delivery [confirm scope] |
| Do you remove old mattresses? | هل تقومون بإزالة المرتبة القديمة؟ | Optional old-mattress removal [confirm fee] |
| How quickly do you deliver? | ما مدة التوصيل؟ | [policy] |
| Can I pay with Tabby or Tamara? | هل يمكنني الدفع عبر تابي أو تمارا؟ | Yes [confirm eligibility rules] |
| How do curtain measurements work? | كيف يتم قياس الستائر؟ | Free visit booking or online estimator [confirm process] |

## 13. Arabic localization: strings to translate

| EN (currently showing on /ar) | AR draft |
|-------------------------------|----------|
| Shop Beds | تسوّق الأسرّة |
| Premium Quality | جودة فاخرة |
| Expert Support | دعم الخبراء |
| Secure Payments | مدفوعات آمنة |
| Sleep better, starting tonight | نم أفضل، ابتداءً من الليلة |

Also audit: buttons, form placeholders, cart/checkout notes, announcement bar, footer, alt text, and any text hard-coded in sections instead of `locales/ar.json`. Check RTL layout (arrows, icon order, carousels, price alignment).

## 14. Tracking (to measure the "choose" and "trust" jobs)

Events to add: finder start / finder complete, Shop-by-Need card clicks, bundle add-to-cart, curtain estimator start, curtain measurement booking, WhatsApp click (by section), FAQ expand.
