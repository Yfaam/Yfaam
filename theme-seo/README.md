# MAYF Home theme SEO / AIO / GEO additions

Untested drafts: I could not write to the live theme. Apply on a DUPLICATE theme, preview, then publish.

1. Copy `snippets/*.liquid` into the theme's `snippets/`.
2. In `layout/theme.liquid`, inside `<head>`: `{% render 'mayf-schema' %}`.
   First check the theme/apps do not already output Organization/WebSite/BreadcrumbList JSON-LD (view source) to avoid duplicates.
3. In the collection template (e.g. `sections/main-collection*.liquid`): `{% render 'mayf-collection-faq-schema' %}`.
4. Validate pages with Google's Rich Results Test and the Schema.org validator.
5. `llms.txt`: Shopify cannot serve a root text file. Create a page (Online Store > Pages) with this content and a plain-text template,
   then add a URL redirect `/llms.txt` -> that page. It is optional and has no confirmed ranking effect.
6. Confirm shipping wording first: the Shipping page says free delivery over AED 500, but several collections say "free delivery" unconditionally.
