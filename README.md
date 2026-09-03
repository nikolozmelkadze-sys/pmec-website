# PMEC website

Static site for Project Management Excellence Centre (PMEC), a PMP training and mentoring practice in Georgia. Bilingual Georgian and English, served by GitHub Pages at https://nikolozmelkadze-sys.github.io/pmec-website/.

## Deployment

GitHub Pages builds from `main`, root directory. Push to `main` and the site rebuilds. There is no build step and no framework.

## Files

| File | Purpose |
| --- | --- |
| `index.html` | The whole site. Markup, CSS and JS live in this one file, including the language switcher and the Web3Forms contact and mentoring forms. |
| `blog-pmp-eligibility-georgia.html` | Standalone article on PMP eligibility in Georgia, linked from the homepage. |
| `sitemap.xml` | Submitted to Google Search Console. Add every new page here. |
| `robots.txt` | Allows all crawlers, points at the sitemap. |
| `logo.svg`, `logo.png`, `logo-monogram.svg`, `logo-wordmark.svg`, `logo-icon-wordmark.svg` | Brand marks. `logo.svg` is the one the site uses; the rest are variants kept for print and social. |
| `og-image.png` | 1200x630 social sharing card. |
| `trainer.jpg` | Trainer photograph. |

## Editing the language toggle

Bilingual copy is handled with paired spans: Georgian text carries `class="ka-text"`, English carries `class="en"`, and the switcher sets `data-lang` on the root element. Any new copy needs both spans, or it will appear in only one language.

## Analytics

Google Analytics 4, property `G-B6LCX2QG3T`, loaded inline in `index.html`. The Search Console verification meta tag sits in the same head block.

## Before adding a page

1. Add both language variants of the copy.
2. Add a `<loc>` entry to `sitemap.xml`.
3. Link it from `index.html`, otherwise it is unreachable and Google treats it as an orphan.
