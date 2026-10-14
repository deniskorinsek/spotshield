#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Builds the SpotShield website: index.html (English), sl/index.html (Slovenian), 404.html, sitemap.xml.

Usage:  python3 tools/build.py          (run from the repository root, or from anywhere — paths are resolved from this file)

Everything you may want to change lives at the top of this file (SITE_URL, DEFAULT_THEME) and in tools/content.py (all copy).
No dependencies beyond the Python standard library.
"""
import os, sys, html, datetime

sys.dont_write_bytecode = True   # keep tools/ free of __pycache__
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import content as C  # noqa: E402

# ---- settings ------------------------------------------------------------------------------------
SITE_URL = 'https://deniskorinsek.github.io/Spotshield-Web/'   # public URL of the site (used for canonical/og/sitemap links)
DEFAULT_THEME = 'dark'                                          # 'dark' | 'light' | 'system'  (visitors can toggle; their choice is remembered)
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))   # repository root
OUT = ROOT

APP_COLORS = {'carp': '#D8C9A0', 'fly': '#E8875C', 'predator': '#F26A5C', 'sea': '#4FB0EA', 'hunter': '#D9A35E', 'mushroom': '#E39A3B', 'birder': '#F08A4B', 'treasure': '#D4AF5A'}

def esc(s):
    return html.escape(s, quote=True)

# ---- icons ----------------------------------------------------------------------------------------
def svg(body, size=18, extra='', stroke=True, vb='0 0 24 24'):
    attrs = 'fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"' if stroke else ''
    return '<svg aria-hidden="true" viewBox="%s" width="%d" height="%d" %s%s>%s</svg>' % (vb, size, size, attrs, extra, body)

ICON = {
    'pin': '<path d="M12 21s-6.5-5.9-6.5-11a6.5 6.5 0 0 1 13 0c0 5.1-6.5 11-6.5 11z"/><circle cx="12" cy="10" r="2.3"/>',
    'sign': '<path d="M12 13v8"/><path d="M4.5 4h12.5l2.5 4.5-2.5 4.5H4.5z"/><path d="M8 8.5h6"/>',
    'plate': '<rect x="2.5" y="7" width="19" height="10" rx="2.2"/><path d="M6.5 12h2.5M11.5 12h6"/>',
    'screen': '<rect x="3" y="4" width="18" height="12.5" rx="2.2"/><path d="M9 20.5h6M12 16.5v4"/><path d="M12 13s-2.6-2.3-2.6-4.2a2.6 2.6 0 0 1 5.2 0C14.6 10.7 12 13 12 13z"/>',
    'qr': '<rect x="3.5" y="3.5" width="6.5" height="6.5" rx="1.2"/><rect x="14" y="3.5" width="6.5" height="6.5" rx="1.2"/><rect x="3.5" y="14" width="6.5" height="6.5" rx="1.2"/><path d="M14 14h2.5v2.5H14zM18 18h2.5v2.5H18zM20.5 14v1M14 20.5h1"/>',
    'city': '<path d="M2.5 20.5h19"/><path d="M4.5 20.5V11h4v9.5"/><path d="M8.5 20.5V5.5h5.5v15"/><path d="M14 20.5l3.5-7 4 7"/>',
    'video': '<rect x="3" y="5.5" width="18" height="13" rx="2.5"/><path d="M10.5 9.5v5l4.2-2.5z"/>',
    'offline': '<path d="M2.5 8.8a14 14 0 0 1 4.3-2.6M10.4 5.1A14 14 0 0 1 21.5 8.8M5.8 12.4a9 9 0 0 1 3.4-1.9M14.6 10.6a9 9 0 0 1 3.6 1.8M9.2 16a4 4 0 0 1 5.6 0"/><circle cx="12" cy="19.3" r="1.1" fill="currentColor" stroke="none"/><path d="M3.5 3.5l17 17"/>',
    'noaccount': '<circle cx="12" cy="8.2" r="3.8"/><path d="M4.5 20.5c1.2-3.8 4.2-5.6 7.5-5.6s6.3 1.8 7.5 5.6"/><path d="M3.5 3.5l17 17"/>',
    'noanalytics': '<path d="M5 20V11M10 20V6M15 20v-6M20 20V9"/><path d="M3.5 3.5l17 17"/>',
    'scene': '<path d="M2.5 19.5l6-9 4 5.5 2.5-3.5 6.5 7z"/><circle cx="16.5" cy="6.5" r="1.8"/>',
    'plant': '<path d="M12 21V11"/><path d="M12 11c0-4 3-7 7-7 0 4-3 7-7 7z"/><path d="M12 15c0-3-2.5-5.5-6-5.5 0 3 2.5 5.5 6 5.5z"/><path d="M3 21h18"/>',
    'sun': '<circle cx="9" cy="9" r="3.4"/><path d="M9 2.5v1.4M9 14.1v1.4M2.5 9h1.4M14.1 9h1.4M4.4 4.4l1 1M12.6 12.6l1 1M4.4 13.6l1-1M12.6 5.4l1-1"/><path d="M12.5 20.5h9M15 17.5h6.5"/>',
    'glasses': '<circle cx="6.8" cy="14" r="3.6"/><circle cx="17.2" cy="14" r="3.6"/><path d="M10.4 14h3.2M3.2 14L5 7.5M20.8 14L19 7.5"/>',
    'people': '<circle cx="9" cy="8.5" r="3.2"/><path d="M3 19.5c.7-3.2 3-4.9 6-4.9s5.3 1.7 6 4.9"/><circle cx="17" cy="9.5" r="2.5"/><path d="M16 14.7c2.5-.3 4.4 1 5 4"/>',
    'clock': '<circle cx="12" cy="12" r="8.5"/><path d="M12 7.5V12l3 2"/>',
}
# finding icons in the demo list use the signal/warn colours
FOUND_ICON = {
    'pin': '<svg aria-hidden="true" viewBox="0 0 24 24" width="18" height="18"><path d="M12 22s7-6.4 7-12.2A7 7 0 0 0 5 9.8C5 15.6 12 22 12 22z" fill="var(--signal)"/><circle cx="12" cy="9.8" r="2.6" fill="#000" opacity=".4"/></svg>',
    'plate': svg(ICON['plate'], extra=' style="stroke:var(--signal);stroke-width:2"'),
    'screen': svg(ICON['screen'], extra=' style="stroke:var(--signal);stroke-width:2"'),
    'sign': svg(ICON['sign'], extra=' style="stroke:var(--warn);stroke-width:2"'),
    'qr': svg(ICON['qr'], extra=' style="stroke:var(--warn);stroke-width:2"'),
}
LOGO = ('<svg aria-hidden="true" viewBox="27 24.5 54 65" width="%d" height="%d" fill="none" stroke="currentColor" stroke-width="4.4" stroke-linecap="round" stroke-linejoin="round">'
        '<path d="M36,34 L44.2,34 Q46,34 46.9,32.4 L48.9,28.8 Q49.6,27.6 51,27.6 L57,27.6 Q58.4,27.6 59.1,28.8 L61.1,32.4 Q62,34 63.8,34 L72,34 Q78,34 78,40 L78,55 C78,70.5 68,80.5 54,87 C40,80.5 30,70.5 30,55 L30,40 Q30,34 36,34 Z"/>'
        '<path d="M41 58.5 q6.5 -5.6 13 0 t13 0" stroke="var(--accent)"/><rect class="dot" x="66.6" y="28.4" width="6.4" height="4.6" rx="2.3" fill="var(--signal)" stroke="none"/></svg>')
ARROW_DOWN = '<svg aria-hidden="true" viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 5v14"/><path d="M6 13l6 6 6-6"/></svg>'
ARROW_UP = '<svg aria-hidden="true" viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 19V5"/><path d="M6 11l6-6 6 6"/></svg>'
EXT = '<svg aria-hidden="true" viewBox="0 0 24 24" width="15" height="15" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M7 17L17 7"/><path d="M8 7h9v9"/></svg>'
DRAG = '<svg aria-hidden="true" viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="#10161A" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M9 7l-5 5 5 5"/><path d="M15 7l5 5-5 5"/></svg>'
DRAG_SM = '<svg aria-hidden="true" viewBox="0 0 24 24" width="15" height="15" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M9 7l-5 5 5 5"/><path d="M15 7l5 5-5 5"/></svg>'
SUN = '<svg class="sun" aria-hidden="true" viewBox="0 0 24 24" width="19" height="19" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><circle cx="12" cy="12" r="4.2"/><path d="M12 2.5v2M12 19.5v2M2.5 12h2M19.5 12h2M5.3 5.3l1.4 1.4M17.3 17.3l1.4 1.4M5.3 18.7l1.4-1.4M17.3 6.7l1.4-1.4"/></svg>'
MOON = '<svg class="moon" aria-hidden="true" viewBox="0 0 24 24" width="19" height="19" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M20 14.6A8.2 8.2 0 1 1 9.4 4a6.6 6.6 0 0 0 10.6 10.6z"/></svg>'
BARS = '<svg class="bars" aria-hidden="true" viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M4 7h16M4 12h16M4 17h16"/></svg>'
X = '<svg class="x" aria-hidden="true" viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M6 6l12 12M18 6L6 18"/></svg>'

DRAWING = '''<svg viewBox="0 0 1600 320" preserveAspectRatio="xMidYMax slice" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round">
<path d="M0 206 C140 176 250 150 400 160 C520 168 600 200 720 192 C840 184 900 140 1040 138 C1160 136 1230 176 1360 172 C1460 169 1530 150 1600 140" stroke-opacity=".55"/>
<path d="M860 252 C980 228 1080 206 1200 214 C1320 222 1400 248 1600 238" stroke-opacity=".75"/>
<circle cx="1370" cy="96" r="26" stroke-opacity=".7"/>
<path d="M980 92 c10 -12 22 -10 26 0 c4 -10 16 -12 26 0" stroke-opacity=".8"/>
<path d="M1046 116 c7 -8 15 -7 18 0 c3 -7 11 -8 18 0" stroke-opacity=".6"/>
<path d="M1186 214 L1200 168 L1214 214 M1189 200 L1200 184 L1211 200" stroke-opacity=".8"/>
<path d="M1218 212 L1234 158 L1250 212 M1221 196 L1234 178 L1247 196 M1225 184 L1234 170 L1243 184" stroke-opacity=".8"/>
<path d="M1256 216 L1268 176 L1280 216 M1259 204 L1268 190 L1277 204" stroke-opacity=".8"/>
<path d="M0 266 C120 262 260 268 420 262 S700 258 860 266 S1120 272 1300 264 S1500 262 1600 266" stroke-opacity=".9"/>
<path d="M660 266 L700 226 L740 266 M700 266 L700 240" stroke-opacity=".85"/>
<path d="M250 318 L330 128" stroke-opacity=".9"/>
<path d="M330 128 Q460 150 560 284" stroke-opacity=".55"/>
<ellipse cx="560" cy="284" rx="34" ry="5" stroke-opacity=".9"/>
<ellipse cx="560" cy="284" rx="68" ry="10" stroke-opacity=".55"/>
<ellipse cx="560" cy="284" rx="104" ry="15" stroke-opacity=".3"/>
<path d="M80 318 C78 280 90 250 86 210 M86 210 c-4 -6 -4 -14 0 -18 c4 4 4 12 0 18" stroke-opacity=".9"/>
<path d="M104 318 C100 276 112 240 110 196 M110 196 c-4 -6 -4 -14 0 -18 c4 4 4 12 0 18" stroke-opacity=".8"/>
<path d="M126 318 C130 282 118 254 124 222 M124 222 c-3 -5 -3 -12 0 -16 c3 4 3 11 0 16" stroke-opacity=".9"/>
<path d="M150 318 C146 284 158 260 154 232 M154 232 c-3 -5 -3 -12 0 -16 c3 4 3 11 0 16" stroke-opacity=".7"/>
<path d="M176 318 C180 290 170 268 174 244 M174 244 c-3 -5 -3 -12 0 -16 c3 4 3 11 0 16" stroke-opacity=".85"/>
<path d="M206 318 c0 -14 8 -22 18 -22 s18 8 18 22 Z M224 296 v22" stroke-opacity=".85"/>
<path d="M248 318 c0 -9 5 -14 11 -14 s11 5 11 14 Z M259 304 v14" stroke-opacity=".7"/>
<path d="M1392 318 l4 -14 M1400 318 l6 -18 M1408 318 l3 -12" stroke-opacity=".8"/>
<path d="M1480 318 l4 -12 M1488 318 l5 -16 M1496 318 l3 -10" stroke-opacity=".7"/>
<path d="M920 318 l3 -12 M928 318 l5 -16 M936 318 l3 -10" stroke-opacity=".7"/>
</svg>'''

def ripples():
    c = ''.join('<circle cx="1200" cy="1200" r="300"><animate attributeName="r" values="300;1200" dur="18s" begin="-%ds" repeatCount="indefinite"/><animate attributeName="stroke-opacity" values=".24;0" dur="18s" begin="-%ds" repeatCount="indefinite"/></circle>' % (b, b) for b in (0, 3, 6, 9, 12, 15))
    return '<svg class="ripples" aria-hidden="true" viewBox="0 0 2400 2400" fill="none" stroke="currentColor" stroke-width="1">%s</svg>' % c

def privacy_art(aria):
    rip = ''.join('<circle cx="260" cy="270" r="150"><animate attributeName="r" values="150;330" dur="9s" begin="-%ds" repeatCount="indefinite"/><animate attributeName="stroke-opacity" values=".35;0" dur="9s" begin="-%ds" repeatCount="indefinite"/></circle>' % (b, b) for b in (0, 3, 6))
    return ('<svg role="img" aria-label="%s" viewBox="0 0 520 520" fill="none" stroke-linecap="round" stroke-linejoin="round">'
            '<g class="rip" stroke="#D8C9A0" stroke-width="1">%s</g>'
            '<path d="M260 62 L372 104 V236 c0 76-48 134-112 164 C196 370 148 312 148 236 V104 Z" fill="rgba(216,201,160,.05)" stroke="#D8C9A0" stroke-width="3"/>'
            '<path d="M260 84 L352 118 V236 c0 62-40 112-92 138 C208 348 168 298 168 236 V118 Z" stroke="#D8C9A0" stroke-opacity=".3" stroke-width="1.5"/>'
            '<g><rect x="214" y="142" width="92" height="184" rx="16" fill="#111D30" stroke="#EEF0E8" stroke-width="2.5"/><rect x="226" y="160" width="68" height="104" rx="9" fill="#1B2A43"/><circle cx="276" cy="184" r="7" fill="#D8C9A0"/><path d="M226 250 L248 218 L262 236 L274 224 L294 250 Z" fill="#C8C28C"/><path d="M226 250 L244 232 L256 244 L268 236 L294 250" fill="#4F5A1E" opacity=".9"/><path d="M232 280 h40" stroke="#C8C28C" stroke-width="4"/><path d="M232 294 h56" stroke="#EEF0E8" stroke-opacity=".35" stroke-width="3"/><circle cx="260" cy="314" r="4" fill="#EEF0E8" fill-opacity=".5"/></g>'
            '<g class="float-a" stroke="#8A93A3" stroke-width="2.5"><path d="M372 118 a24 24 0 0 1 46 -8 a20 20 0 0 1 18 36 h-62 a18 18 0 0 1 -2 -28" fill="rgba(238,240,232,.04)"/><path d="M376 160 l64 -64" stroke="#FF8F7A" stroke-width="3"/></g>'
            '<g class="float-b" stroke="#8A93A3" stroke-width="2.5"><path d="M118 352 c0 -22 16 -38 36 -38 s36 16 36 38 c0 28 -36 60 -36 60 s-36 -32 -36 -60 z" fill="rgba(238,240,232,.04)"/><circle cx="154" cy="352" r="11"/><path d="M116 402 l76 -76" stroke="#FF8F7A" stroke-width="3"/></g>'
            '<g opacity=".9"><path d="M312 420 a52 52 0 0 1 -104 0" stroke="#7FE0B0" stroke-width="2.5"/><path d="M248 426 l9 9 16 -18" stroke="#7FE0B0" stroke-width="3.5"/></g>'
            '</svg>') % (esc(aria), rip)

THEME_SCRIPT = {
    'dark':   "(function(){var t='dark';try{var s=localStorage.getItem('spotshield-theme');if(s==='light'||s==='dark')t=s}catch(e){}document.documentElement.setAttribute('data-theme',t)})();",
    'light':  "(function(){var t='light';try{var s=localStorage.getItem('spotshield-theme');if(s==='light'||s==='dark')t=s}catch(e){}document.documentElement.setAttribute('data-theme',t)})();",
    'system': "(function(){var t=(window.matchMedia&&window.matchMedia('(prefers-color-scheme: light)').matches)?'light':'dark';try{var s=localStorage.getItem('spotshield-theme');if(s==='light'||s==='dark')t=s}catch(e){}document.documentElement.setAttribute('data-theme',t)})();",
}

# ---- page -----------------------------------------------------------------------------------------
def page(T, lang_dir):
    """T = content dict (EN or SL); lang_dir = 'en' for the root page, 'sl' for /sl/."""
    A = 'assets/' if lang_dir == 'en' else '../assets/'
    img = lambda name: A + 'img/' + name
    sfx = lang_dir                       # localized assets carry -en / -sl
    url_self = SITE_URL if lang_dir == 'en' else SITE_URL + 'sl/'
    url_en, url_sl = SITE_URL, SITE_URL + 'sl/'
    nav, hero, apps, demo, how, priv, lim, cta, foot = (T['nav'], T['hero'], T['apps'], T['demo'], T['how'], T['privacy'], T['limits'], T['cta'], T['footer'])
    out = []
    w = out.append

    # ---- head
    w('<!doctype html>\n<html lang="%s" data-theme="%s">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width, initial-scale=1">' % (T['lang'], 'light' if DEFAULT_THEME == 'light' else 'dark'))
    w('<title>%s</title>\n<meta name="description" content="%s">' % (esc(T['title']), esc(T['description'])))
    w('<meta name="theme-color" content="%s">' % ('#F1EFE6' if DEFAULT_THEME == 'light' else '#0B1424'))
    w('<link rel="canonical" href="%s">\n<link rel="alternate" hreflang="en" href="%s">\n<link rel="alternate" hreflang="sl" href="%s">\n<link rel="alternate" hreflang="x-default" href="%s">' % (url_self, url_en, url_sl, url_en))
    w('<meta property="og:type" content="website">\n<meta property="og:site_name" content="SpotShield">\n<meta property="og:locale" content="%s">\n<meta property="og:title" content="%s">\n<meta property="og:description" content="%s">\n<meta property="og:url" content="%s">\n<meta property="og:image" content="%simg/og-image-%s.jpg">\n<meta property="og:image:width" content="1200">\n<meta property="og:image:height" content="630">\n<meta name="twitter:card" content="summary_large_image">' % (T['locale'], esc(T['title']), esc(T['description']), url_self, SITE_URL + 'assets/', sfx))
    w('<link rel="icon" href="%sfavicon.svg" type="image/svg+xml">\n<link rel="icon" href="%sfavicon-32.png" sizes="32x32" type="image/png">\n<link rel="apple-touch-icon" href="%sapple-touch-icon.png">' % (A + 'img/', A + 'img/', A + 'img/'))
    for wgt in (800, 700, 500):
        w('<link rel="preload" href="%sfonts/manrope-latin-%d.woff2" as="font" type="font/woff2" crossorigin>' % (A, wgt))
    w('<script>%s</script>' % THEME_SCRIPT[DEFAULT_THEME])
    w('<link rel="stylesheet" href="%scss/site.css">' % A)
    w('<script src="%sjs/site.js" defer></script>' % A)
    w('</head>\n<body>\n<a class="skip" href="#main">%s</a>' % ('Skip to content' if lang_dir == 'en' else 'Preskoči na vsebino'))

    # ---- nav
    w('<header class="nav" id="top">\n<div class="wrap">')
    w('<a class="brand" href="#top" aria-label="%s">%s<span>SpotShield</span></a>' % (esc(nav['brand_aria']), LOGO % (26, 31)))
    w('<nav class="nav-links" id="menu" aria-label="%s"><a href="#apps">%s</a><a href="#how">%s</a><a href="#privacy">%s</a><a class="btn btn-primary btn-sm" href="#apps">%s</a></nav>' % (esc(nav['aria']), nav['apps'], nav['how'], nav['privacy'], nav['cta']))
    if lang_dir == 'en':
        w('<div class="lang" role="group" aria-label="%s"><span aria-current="page">EN</span><a href="%s" hreflang="sl" lang="sl" aria-label="Slovenščina">SL</a></div>' % (esc(nav['lang_aria']), T['other_href']))
    else:
        w('<div class="lang" role="group" aria-label="%s"><a href="%s" hreflang="en" lang="en" aria-label="English">EN</a><span aria-current="page">SL</span></div>' % (esc(nav['lang_aria']), T['other_href']))
    w('<button class="icon-btn theme" type="button" aria-label="%s" data-label-dark="%s" data-label-light="%s">%s%s</button>' % (esc(nav['theme_dark']), esc(nav['theme_dark']), esc(nav['theme_light']), SUN, MOON))
    w('<button class="icon-btn menu-btn" type="button" aria-expanded="false" aria-controls="menu" aria-label="%s">%s%s</button>' % (esc(nav['menu']), BARS, X))
    w('</div>\n</header>\n<main id="main">')

    # ---- hero
    w('<section class="hero" aria-labelledby="hero-title" data-parallax-root>')
    w('<div class="hero-bg" aria-hidden="true"><div class="contour" data-parallax="0.16"></div><div class="fade"></div><div class="drawing" data-parallax="-0.05">%s</div></div>' % DRAWING)
    w('<div class="wrap">\n<div class="hero-copy">')
    w('<p class="eyebrow intro d1">%s</p>' % hero['eyebrow'])
    w('<h1 id="hero-title"><span class="l1 intro d2">%s</span><span class="l2 intro d3">%s</span></h1>' % (hero['h1a'], hero['h1b']))
    w('<p class="lede intro d4">%s</p>' % hero['lede'])
    w('<div class="picker intro d5"><p class="label">%s</p><div class="icons" role="group" aria-label="%s">' % (hero['picker'], esc(hero['picker_aria'])))
    for i, a in enumerate(C.APP_IDS):
        w('<button type="button" data-pick="%d" aria-pressed="%s" aria-label="%s"><img src="%s" alt="" width="48" height="48"></button>' % (i, 'true' if i == 0 else 'false', esc(C.STORE_NAMES[a]), img('icon-%s.webp' % a)))
    w('</div></div>')
    w('<div class="hero-actions intro d6"><a class="btn btn-primary" href="#apps">%s%s</a><a class="btn btn-ghost" href="#demo">%s</a></div>' % (hero['primary'], ARROW_DOWN, hero['secondary']))
    w('<p class="trust intro d7">%s</p>\n</div>' % hero['trust'])
    w('<div class="hero-stage intro stage"><div class="glow" aria-hidden="true"></div>%s' % ripples())
    w('<div class="deck-wrap" data-parallax="-0.04"><div class="deck" id="deck" role="group" aria-label="%s">' % esc(hero['deck_aria']))
    for i, a in enumerate(C.APP_IDS):
        it = apps['items'][a]
        pos = 'pos-0' if i == 0 else 'pos-1' if i == 1 else 'pos-2' if i == 2 else 'pos-n'
        w('<div class="card app-%s %s" data-app="app-%s" aria-hidden="%s"><img class="scene" src="%s" alt="%s" width="690" height="920"%s><div class="shade" aria-hidden="true"></div><div class="ring" aria-hidden="true"></div>'
          '<div class="meta"><div class="row"><img src="%s" alt="" width="46" height="46"><div><p class="name">%s</p><p class="kicker">%s</p></div></div><p class="tag"><span class="l1">%s</span><span class="l2">%s</span></p></div></div>'
          % (a, pos, a, 'false' if i == 0 else 'true', img('scene-%s-%s.webp' % (a, sfx)), esc(it['alt']), '' if i < 3 else ' loading="lazy"', img('icon-%s.webp' % a), C.STORE_NAMES[a], it['kicker'], it['l1'], it['l2']))
    w('</div><div class="deck-foot"><div class="bars" aria-hidden="true">%s</div><p class="count"><span id="deck-n">01</span> / 08</p></div></div>' % ''.join('<span%s><i></i></span>' % (' class="on"' if i == 0 else '') for i in range(8)))
    w('</div>\n</div>\n</section>')

    # ---- apps
    w('<section class="section" id="apps" aria-labelledby="apps-title" data-reveal>\n<div class="wrap">')
    w('<div class="reveal"><p class="eyebrow">%s</p><div class="sec-head"><h2 class="h2" id="apps-title">%s</h2><p class="lede">%s</p></div></div>' % (apps['eyebrow'], apps['h2'], apps['lede']))
    w('<div class="apps-grid">')
    for i, a in enumerate(C.APP_IDS):
        it = apps['items'][a]; name = C.STORE_NAMES[a]
        w('<article class="app-card app-%s reveal s%d" id="app-%s" aria-labelledby="name-%s">'
          '<div class="pic"><img src="%s" alt="%s" width="690" height="920" loading="lazy"></div>'
          '<div class="body"><img class="icon" src="%s" alt="" width="60" height="60" loading="lazy"><p class="aud">%s</p><h3 id="name-%s">%s</h3><p class="tag">%s<br><span class="l2">%s</span></p>'
          '<div class="links"><a class="play" href="%s" aria-label="%s">%s%s</a><a class="priv" href="%s" aria-label="%s">%s</a></div></div></article>'
          % (a, i + 1, a, a, img('scene-%s-%s.webp' % (a, sfx)), esc(it['alt']), img('icon-%s.webp' % a), it['aud'], a, name, it['l1'], it['l2'],
             C.PLAY_URL.format(id=a), esc(apps['play_aria'].format(name=name)), apps['play'], EXT, C.PRIVACY_URL.format(id=a), esc(apps['priv_aria'].format(name=name)), apps['priv']))
    w('</div>\n</div>\n</section>')

    # ---- demo
    w('<section class="section demo" id="demo" aria-labelledby="demo-title" data-reveal>\n<div class="wrap">')
    w('<div class="demo-stage reveal"><div class="compare-wrap"><span class="corner tl" aria-hidden="true"></span><span class="corner tr" aria-hidden="true"></span><span class="corner bl" aria-hidden="true"></span><span class="corner br" aria-hidden="true"></span>')
    w('<div class="compare" style="--split:100%%"><img src="%s" alt="%s" width="1080" height="1440" loading="lazy">' % (img('hero-before-%s.webp' % sfx), esc(demo['alt_before'])))
    w('<span class="pill l">%s</span><span class="pill gps"><svg aria-hidden="true" viewBox="0 0 24 24" width="14" height="14"><path d="M12 22s7-6.4 7-12.2A7 7 0 0 0 5 9.8C5 15.6 12 22 12 22z" fill="#FF8F7A"/><circle cx="12" cy="9.8" r="2.6" fill="#000" opacity=".45"/></svg>%s</span>' % (demo['before'], demo['gps']))
    w('<div class="after"><img src="%s" alt="%s" width="1080" height="1440" loading="lazy"><span class="pill r">%s</span><span class="pill ok"><svg aria-hidden="true" viewBox="0 0 24 24" width="14" height="14"><circle cx="12" cy="12" r="10" fill="#7FE0B0" opacity=".22"/><path d="M7 12.4l3.3 3.3L17.2 8.8" fill="none" stroke="#7FE0B0" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/></svg>%s</span></div>' % (img('hero-after-%s.webp' % sfx), esc(demo['alt_after']), demo['after'], demo['ok']))
    w('<div class="edge" aria-hidden="true"></div><div class="bar" aria-hidden="true"></div><div class="knob" aria-hidden="true">%s</div>' % DRAG)
    w('<input type="range" min="0" max="100" step="1" value="44" aria-label="%s"></div>' % esc(demo['range_aria']))
    w('<p class="hint">%s%s</p></div></div>' % (DRAG_SM, demo['hint']))
    w('<div class="demo-copy reveal s2"><p class="eyebrow">%s</p><h2 class="h2" id="demo-title">%s</h2><p class="lede">%s</p><ul class="found">' % (demo['eyebrow'], demo['h2'], demo['lede']))
    for i, (ic, txt, verdict) in enumerate(demo['found']):
        w('<li class="reveal s%d">%s<span>%s</span><b>%s</b></li>' % (i + 3, FOUND_ICON[ic], txt, verdict))
    w('</ul><p class="note">%s</p></div>\n</div>\n</section>' % demo['note'])

    # ---- how
    w('<section class="section" id="how" aria-labelledby="how-title" data-reveal>\n<div class="wrap">')
    w('<div class="reveal"><p class="eyebrow">%s</p><div class="sec-head"><h2 class="h2" id="how-title">%s</h2><p class="lede">%s</p></div></div>' % (how['eyebrow'], how['h2'], how['lede']))
    w('<ol class="steps">')
    for i, (title, text, alt) in enumerate(how['steps']):
        w('<li class="step reveal s%d"><div class="shot"><div class="halo" aria-hidden="true"></div><div class="phone"><img src="%s" alt="%s" width="390" height="844" loading="lazy"></div></div>'
          '<div class="txt"><p class="num">0%d</p><h3>%s</h3><p>%s</p></div></li>' % (i + 1, img('step%d-%s.webp' % (i + 1, sfx)), esc(alt), i + 1, title, text))
    w('</ol>')
    w('<div class="checks reveal s5"><h3>%s</h3><ul>%s</ul></div>' % (how['checks_title'], ''.join('<li>%s%s</li>' % (svg(ICON[ic]), txt) for ic, txt in how['checks'])))
    w('</div>\n</section>')

    # ---- privacy
    w('<section class="privacy" id="privacy" aria-labelledby="privacy-title" data-reveal data-parallax-root>\n<div class="wrap">')
    w('<div class="privacy-copy reveal"><p class="eyebrow">%s</p><h2 class="h2" id="privacy-title">%s</h2><p class="lede">%s</p><ul class="pillars">' % (priv['eyebrow'], priv['h2'], priv['lede']))
    for i, (ic, title, text) in enumerate(priv['pillars']):
        w('<li class="reveal s%d"><span class="ic" aria-hidden="true">%s</span><div><b>%s</b><p>%s</p></div></li>' % (i + 2, svg(ICON[ic], 21), title, text))
    w('</ul></div>')
    w('<div class="privacy-art reveal s2" data-parallax="0.07">%s</div>' % privacy_art(priv['art_aria']))
    w('</div>\n</section>')

    # ---- limits
    w('<section class="section limits" id="limits" aria-labelledby="limits-title" data-reveal>\n<div class="wrap">')
    w('<div class="limits-copy reveal"><p class="eyebrow">%s</p><h2 class="h2" id="limits-title">%s</h2><p class="lede">%s</p></div>' % (lim['eyebrow'], lim['h2'], lim['lede']))
    w('<ul class="limits-grid">%s</ul>' % ''.join('<li class="reveal s%d"><span class="ic" aria-hidden="true">%s</span><p>%s</p></li>' % (i + 1, svg(ICON[ic], 20), txt) for i, (ic, txt) in enumerate(lim['items'])))
    w('</div>\n</section>')

    # ---- cta
    w('<section class="cta" aria-labelledby="cta-title" data-reveal>\n<div class="wrap">\n<div class="cta-box reveal" data-parallax-root>')
    w('<div class="pattern-wrap" data-parallax="0.08" aria-hidden="true"><img class="pattern" src="%s" alt="" width="2560" height="1040" loading="lazy"></div><div class="veil" aria-hidden="true"></div>' % img('band.webp'))
    w('<div class="icons" aria-hidden="true">%s</div>' % ''.join('<img src="%s" alt="" width="44" height="44" loading="lazy">' % img('icon-%s.webp' % a) for a in C.APP_IDS))
    w('<h2 id="cta-title">%s</h2><p>%s</p><a class="btn" href="#apps">%s%s</a>' % (cta['h2'], cta['p'], cta['btn'], ARROW_UP))
    w('</div>\n</div>\n</section>\n</main>')

    # ---- footer
    w('<footer class="footer">\n<div class="wrap">\n<div class="top">')
    w('<div class="about"><a class="brand" href="#top" aria-label="%s">%s<span>SpotShield</span></a><p>%s</p></div>' % (esc(nav['brand_aria']), LOGO % (24, 29), foot['about']))
    w('<div class="cols"><nav aria-labelledby="f-apps"><h4 id="f-apps">%s</h4><ul class="two">%s</ul></nav>' % (foot['apps'], ''.join('<li><a href="%s">%s</a></li>' % (C.PLAY_URL.format(id=a), C.SHORT_NAMES_EN[a]) for a in C.APP_IDS)))
    w('<nav aria-labelledby="f-more"><h4 id="f-more">%s</h4><ul><li><a href="%s">%s</a></li><li><a href="mailto:%s">%s</a></li><li><a href="%s" hreflang="%s" lang="%s">%s</a></li></ul></nav></div>' % (foot['more'], C.PRIVACY_INDEX, foot['policies'], C.CONTACT, foot['contact'], T['other_href'], T['other_lang'], T['other_lang'], T['other_label']))
    w('</div>\n<div class="bottom"><p>%s</p><p>%s</p></div>\n</div>\n</footer>\n</body>\n</html>\n' % (foot['copyright'], foot['trademark']))
    return '\n'.join(out)

def notfound(T):
    nf = T['notfound']
    return ('<!doctype html>\n<html lang="%s">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width, initial-scale=1">\n<title>%s</title>\n<meta name="robots" content="noindex">\n'
            '<style>html{background:#0B1424;color:#EEF0E8;font-family:Manrope,ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif;-webkit-font-smoothing:antialiased}body{margin:0;min-height:100vh;display:grid;place-items:center;padding:24px;box-sizing:border-box}'
            'main{max-width:520px;text-align:center}h1{margin:24px 0 0;font-size:clamp(32px,6vw,48px);line-height:1.05;letter-spacing:-.035em;font-weight:800}p{margin:16px 0 0;font-size:17px;line-height:1.6;color:#A9B1BF}'
            'a{display:inline-flex;align-items:center;height:54px;padding:0 26px;margin-top:32px;border-radius:999px;background:#C8C28C;color:#232108;font-weight:700;text-decoration:none}svg{display:block;margin:0 auto}</style>\n</head>\n<body>\n<main>%s<h1>%s</h1><p>%s</p><a href="%s">%s</a></main>\n</body>\n</html>\n'
            % (T['lang'], esc(nf['title']), (LOGO % (44, 53)).replace('var(--accent)', '#D8C9A0').replace('var(--signal)', '#FF8F7A'), nf['h1'], nf['p'], SITE_URL, nf['btn']))

def sitemap():
    today = datetime.date.today().isoformat()
    return ('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n'
            '<url><loc>%s</loc><lastmod>%s</lastmod><xhtml:link rel="alternate" hreflang="en" href="%s"/><xhtml:link rel="alternate" hreflang="sl" href="%ssl/"/></url>\n'
            '<url><loc>%ssl/</loc><lastmod>%s</lastmod><xhtml:link rel="alternate" hreflang="en" href="%s"/><xhtml:link rel="alternate" hreflang="sl" href="%ssl/"/></url>\n</urlset>\n'
            % (SITE_URL, today, SITE_URL, SITE_URL, SITE_URL, today, SITE_URL, SITE_URL))

def write(rel, text):
    path = os.path.join(OUT, rel)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(text)
    print('wrote', rel, '(%d bytes)' % len(text.encode('utf-8')))

if __name__ == '__main__':
    write('index.html', page(C.EN, 'en'))
    write('sl/index.html', page(C.SL, 'sl'))
    write('404.html', notfound(C.EN))
    write('sitemap.xml', sitemap())
    write('robots.txt', 'User-agent: *\nAllow: /\nSitemap: %ssitemap.xml\n' % SITE_URL)
