# Strip `_pos` / `_fid` / `_ss` from product links (mayfhome.com)

Search Console: "Page with redirect" (141 URLs, 133 of them `/products/<handle>?_pos=..&_fid=..&_ss=c`).
Shopify appends these tracking params to `product.url` on collection/search pages. Google crawls the
links and then gets redirected. Fix: emit the clean URL in the theme's product links.

## Steps (Online Store > Themes > ... > Edit code)

1. Find where product cards build their link. Search the theme for `product.url`
   (typically `snippets/product-card.liquid`, `snippets/card-product.liquid`, or similar).
2. Replace each `href="{{ product.url }}"` / `{{ product.url }}` with a clean version:

```liquid
{%- liquid
  assign clean_url = product.url | split: '?' | first
-%}
<a href="{{ clean_url }}">
```

   If the link relies on a selected variant, keep it: `{{ clean_url }}?variant={{ variant.id }}`.

3. Check also `snippets/*predictive-search*` and `sections/*search*` for the same `product.url` pattern.
4. Preview a collection page and confirm product links no longer contain `_pos`, `_fid`, `_ss`.

## After deploying

Search Console > Pages > "Page with redirect" > Validate fix. Old URLs drop off over a few weeks.
