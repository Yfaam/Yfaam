# MAYF HOME · Hotel Collection email

Built from *MAYF-Home-Hotel-Collection-Email.docx*.

## Setting it up in Shopify Email
1. **Email colours:** set Content background to `#F5F0E8` and Border to `#F5F0E8`. Leave the black footer as it is.
2. **Email details**
   - Subject: `Sleep like you're checked in, every night`
   - Preview text: `Hotel-grade mattresses, linens and pillows, curated for UAE homes.`
   - To: Customers who haven't purchased (18,733)
3. **Sections:** delete the "Mayf home" header text. Click **+ → Custom Liquid** and paste all of `email.html`.
   If your editor has no Custom Liquid section, use native sections and copy the text and colours from `email.html`.
4. Check that each social icon in the footer links to the right account.

## Product choices (from The Hotel Bedroom, sorted by best-selling)
| Slot | Product | Price |
|---|---|---|
| Mattress | MAYF Signature Hotel Collection Mattress | from AED 2,799 |
| Duvet | MAYF Home 300TC Duvet – White | from AED 130 |
| Sheet/cover | MAYF Home 300TC Duvet Cover – White | from AED 90 |
| Pillow | MAYF Home VIROSA Micro Fiber Pillow 1200g | from AED 45 |

- The two bundles sell best, but they are **not published to the Online Store**, so their links would 404. Publish them if you want them in the email.
- The collection has **no topper**. Flat sheet, pillow case, protector and Luxury Hybrid mattress are still **Draft**.

## Still to do
- **Logo:** there is no logo file in Shopify Files. The header uses a gold "MAYF / HOME" wordmark in text. Upload the M monogram, then replace the `<span>`s with `<img src="…" width="120">`.
- **Hero image:** for now it uses the Signature mattress photo. When the 1200×800 hotel-bedroom photo is ready, swap the `src` and also set it as The Hotel Bedroom collection image.
- Send a test and check it on mobile. Send Sunday–Wednesday, 8–10pm UAE time. Don't use a discount code. Consider "free pillow pair with any mattress" instead.
