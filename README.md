# SpotShield — website

Static site for the SpotShield family of Android apps. Plain HTML, CSS and JavaScript — no build tools, no frameworks, no external requests (fonts are self-hosted), so it can be served as-is by GitHub Pages.

```
index.html          English page
sl/index.html       Slovenian page
404.html            not-found page (GitHub Pages serves it automatically)
assets/css/site.css styles, both themes
assets/js/site.js   theme toggle, menu, hero deck, compare slider, scroll reveals, parallax
assets/fonts/       Manrope (SIL Open Font License — see LICENSE-OFL.txt)
assets/img/         scenes, icons, screens, OG images, favicons
tools/              generator for the two HTML pages (optional, see below)
sitemap.xml, robots.txt, .nojekyll
```

## Publish on GitHub Pages

This folder lives inside the `spotshield` monorepo, like `distributionMedia/privacy-site` does. The website itself is published from its own public repository, the same way the privacy policies are published from `spotshield-privacy`.

1. Commit this folder to the monorepo as usual.
2. Create an empty public repository called `Spotshield-Web` on GitHub (no README, no licence — it must be empty for the first push).
3. From the monorepo root, push just this folder to that repository:

   ```sh
   cd ~/Documents/Workspace/Spotshield
   git subtree push --prefix=Spotshield-Web https://github.com/deniskorinsek/Spotshield-Web.git main
   ```

   Run the same command again after every change you commit here. (If you prefer not to use subtree: clone `Spotshield-Web`, copy the contents of this folder into the clone, commit and push.)

4. On GitHub open the `Spotshield-Web` repository → **Settings → Pages**, choose **Deploy from a branch**, branch `main`, folder `/ (root)`, and save.
5. After a minute the site is live at `https://deniskorinsek.github.io/Spotshield-Web/`. The Slovenian page is at `…/Spotshield-Web/sl/`.

The pages use relative links, so they work from any folder or domain. Only the absolute URLs in the `<head>` (canonical, hreflang, Open Graph image) and in `sitemap.xml` / `robots.txt` assume the address above. If you host it somewhere else — a custom domain, a different repository name — change `SITE_URL` at the top of `tools/build.py` and run the generator (below), or search-and-replace the URL in those files.

### Custom domain (optional)

Add a file named `CNAME` containing the domain (for example `spotshield.si`), point the domain's DNS at GitHub Pages as described in GitHub's docs, and update `SITE_URL` as above.

## Editing

The copy for both languages lives in one place, `tools/content.py`. After changing it, regenerate the pages with:

```sh
python3 tools/build.py
```

This rewrites `index.html`, `sl/index.html`, `404.html`, `sitemap.xml` and `robots.txt`. It needs only Python 3 — nothing to install. (You can of course also edit the HTML files directly; just keep in mind that running the generator afterwards would overwrite those edits.)

Settings at the top of `tools/build.py`:

- `SITE_URL` — the public address of the site (see above).
- `DEFAULT_THEME` — `'dark'` (default), `'light'`, or `'system'` to follow the visitor's OS setting. Visitors can always switch with the sun/moon button; their choice is remembered in the browser.

Styles are in `assets/css/site.css`; the colour palette for both themes is defined in the `:root` blocks at the top.

## Images

- `scene-<app>-<lang>.webp` — the illustrated scene of each app (hero deck and app cards)
- `icon-<app>.webp` — app icons
- `hero-before-<lang>.webp` / `hero-after-<lang>.webp` — the before/after pair in the compare slider
- `step1…4-<lang>.webp` — phone screens in “How it works”
- `band.webp` — the pattern behind the closing call to action
- `contour-map.svg` — the contour-line drawing behind the hero (used as a CSS mask, so it takes the theme colour)
- `og-image-<lang>.jpg` — link previews (1200 × 630)
- `favicon.svg`, `favicon-32.png`, `apple-touch-icon.png`

## Links

- Google Play: `https://play.google.com/store/apps/details?id=si.spotshield.<app>` — all eight apps are live on Google Play (checked 15 October 2026).
- Privacy policies: `https://deniskorinsek.github.io/spotshield-privacy/<app>/`
- Contact: `korinsekdenis+play@gmail.com`

## Accessibility and motion

Every interactive element is keyboard-operable (the compare slider is a native range input; the app picker uses `aria-pressed`). When the visitor's system has “reduce motion” enabled, the intro, scroll reveals, parallax, hero tilt, ripples and the auto-rotating deck are switched off and everything is shown immediately.
