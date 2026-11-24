#!/usr/bin/env python3
"""Generates the static pages. Edit content here, then run: python3 build.py"""
import pathlib

OUT = pathlib.Path(__file__).parent
NAME = "All Sorted Fencing &amp; Landscaping"
PHONE = "+353 87 497 2416"
PHONE_TEL = "+353874972416"
EMAIL = "allsortedfencingandlandscaping@gmail.com"
WEB3FORMS_KEY = "14b0920f-0117-43f0-a08e-fb037efb93c7"  # public form key from web3forms.com, safe to publish


def svg(d):
    return ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" '
            f'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{d}</svg>')


I_FENCE = '<path d="M5 21V7l2-3 2 3v14M15 21V7l2-3 2 3v14M3 10h18M3 16h18"/>'
I_PLANT = '<path d="M12 21v-9M12 12c0-4 3-7 8-7 0 5-3 8-8 7zM12 15c0-3-2-5-7-5 0 4 3 6 7 5z"/>'
I_PAVE = '<rect x="3" y="3" width="8" height="8" rx="1"/><rect x="13" y="3" width="8" height="5" rx="1"/><rect x="13" y="10" width="8" height="11" rx="1"/><rect x="3" y="13" width="8" height="8" rx="1"/>'
I_PAINT = '<rect x="3" y="3" width="14" height="6" rx="1.5"/><path d="M17 6h3v6h-8v3M12 15v6"/>'
I_DROP = '<path d="M12 3s6 6.5 6 11a6 6 0 0 1-12 0c0-4.5 6-11 6-11z"/><path d="M9.5 14.5a2.5 2.5 0 0 0 2.5 2.5"/>'
I_SHEARS = '<circle cx="6" cy="18" r="3"/><circle cx="18" cy="18" r="3"/><path d="M8 16 20 4M16 16 4 4"/>'
I_GRASS = '<path d="M3 20h18M6 20v-5M10 20v-8M14 20v-6M18 20v-9"/>'
I_ROAD = '<path d="M4 21 9 3M20 21 15 3M12 5v3M12 11v3M12 17v3"/>'
I_HOME = '<path d="M3 11 12 4l9 7M5 10v10h14V10M10 20v-6h4v6"/>'
I_BRUSH = '<path d="M14 3l7 7-6 6-7-7zM8 9l-4 4 7 7 4-4M4 20h4"/>'
I_LAYERS = '<path d="M12 3 3 8l9 5 9-5zM3 13l9 5 9-5M3 18l9 5 9-5"/>'
I_SPARK = '<path d="M12 3v4M12 17v4M3 12h4M17 12h4M6 6l2.5 2.5M15.5 15.5 18 18M18 6l-2.5 2.5M8.5 15.5 6 18"/>'
I_BIN = '<path d="M4 7h16M9 7V4h6v3M6 7l1 13h10l1-13M10 11v6M14 11v6"/>'
I_CAL = '<rect x="3" y="5" width="18" height="16" rx="2"/><path d="M3 10h18M8 3v4M16 3v4"/>'

# slug, name, short blurb, icon, hero image, hero lead, intro h2, tiles, split (eyebrow, h2, ticks, image, alt)
SERVICES = [
    ("fencing", "Fencing", "Timber, composite and PVC fencing and gates on solid concrete or timber posts.", I_FENCE, "fence-3.jpg",
     "Timber, composite and PVC fencing and gates, supplied and fitted across Dublin.", None, None, None),
    ("landscaping", "Landscaping", "New lawns, planting, gravel and full garden makeovers from the ground up.", I_PLANT, "land-2.jpg",
     "New lawns, planting, gravel and full garden makeovers — designed around how you use the space.",
     "A garden you will<br>actually use.",
     [(I_GRASS, "Lawns &amp; turfing", "New roll-out lawns, levelling and reseeding to bring tired, patchy grass back to life."),
      (I_PLANT, "Planting &amp; borders", "Borders, hedging and planting schemes that suit your soil, your light and your schedule."),
      (I_ROAD, "Gravel &amp; decorative stone", "Low-maintenance gravel areas and paths, edged and laid over weed membrane."),
      (I_LAYERS, "Raised beds &amp; sleepers", "Timber sleeper beds, retaining edges and steps to give a flat garden some shape."),
      (I_HOME, "Full garden makeovers", "Overgrown or bare site? We clear it, level it and build the whole garden in one project."),
      (I_BIN, "Clearance &amp; levelling", "Old sheds, rubble and overgrowth removed, and the ground graded ready for what comes next.")],
     ("One project", "Fence and garden done together.",
      ["Ground levelled and drained before anything is laid", "One plan, one crew and one clean-up", "All waste taken away when we finish"],
      "land-1.jpg", "Gravel front garden with a curved path")),
    ("paving", "Paving", "Patios, driveways and paths laid on a proper base with clean edges.", I_PAVE, "pave-1.jpg",
     "Patios, driveways and paths laid on a proper base, with clean edges and good drainage.",
     "Paving that stays<br>flat and drains.",
     [(I_PAVE, "Patios", "Porcelain, sandstone, limestone and concrete slabs, laid to a fall so water runs away from the house."),
      (I_ROAD, "Driveways", "Block paving, gravel and paved driveways built on a compacted base that takes the weight of cars."),
      (I_LAYERS, "Paths &amp; steps", "Side passages, garden paths and steps that link the house, patio and lawn."),
      (I_HOME, "Kerbs &amp; edging", "Brick, block and kerb edging to hold paving and gravel in place and finish it neatly."),
      (I_DROP, "Drainage", "Channel drains and soakaways where needed, so you are not left with standing water."),
      (I_BRUSH, "Repairs &amp; relaying", "Sunken or rocking slabs lifted and relaid, and tired joints re-pointed.")],
     ("Done right", "It is all in the base.",
      ["Dug out and filled with compacted hardcore", "Laid to a fall, away from the house", "Finished level kept below the damp-proof course", "Joints pointed or sanded and the area washed down"],
      "pave-1.jpg", "Tarmac driveway with granite edging")),
    ("painting", "Painting", "Interior and exterior painting for homes, walls, fences, sheds and gates.", I_PAINT, "paint-1.jpg",
     "Interior and exterior painting — rooms, stairs, kitchens, house fronts, walls and fences — properly prepared so it lasts.",
     "A fresh coat,<br>properly prepared.",
     [(I_HOME, "House exteriors", "Render, dash and masonry washed, repaired and painted with weather-resistant masonry paint."),
      (I_LAYERS, "Interior rooms", "Walls, ceilings, woodwork, stairs and doors painted with clean lines and a smooth finish."),
      (I_FENCE, "Fences &amp; sheds", "Timber fences, sheds and decking stained or painted to protect them and tidy up the garden."),
      (I_PAINT, "Gates &amp; railings", "Metal and timber gates and railings rubbed down, primed and finished."),
      (I_BRUSH, "Preparation", "Scraping, filling, sanding and priming — the part that decides how long the paint lasts."),
      (I_SPARK, "Clean finish", "Windows, paths and plants covered while we work, and everything cleaned up after.")],
     ("How we paint", "Prep first, paint second.",
      ["Surfaces washed and left to dry fully", "Flaking paint removed, cracks filled", "Primer or stabiliser where it is needed", "Two full coats in dry weather"],
      "paint-5.jpg", "Kitchen painted in teal")),
    ("exterior-cleaning", "Exterior Cleaning", "Power washing for driveways, patios, roofs, walls and decking.", I_DROP, "clean-1.jpg",
     "Power washing for driveways, patios, walls, decking and paths, to lift years of moss and grime.",
     "Looks new again,<br>without replacing it.",
     [(I_ROAD, "Driveways", "Oil marks, tyre tracks, moss and weeds lifted from tarmac, concrete and block paving."),
      (I_PAVE, "Patios &amp; paths", "Green, slippery slabs brought back to their original colour and made safe to walk on."),
      (I_HOME, "Walls &amp; render", "House and garden walls cleaned at the right pressure so the surface is not damaged."),
      (I_FENCE, "Decking &amp; fences", "Timber cleaned gently and left ready for staining or treatment."),
      (I_LAYERS, "Re-sanding", "Block paving joints re-sanded after cleaning so the blocks stay locked in place."),
      (I_SPARK, "Roof cleaning", "Moss and dirt cleared from roof tiles and ridge lines.")],
     ("Careful work", "The right pressure for each surface.",
      ["Lower pressure on render, pointing and timber", "Drains and gullies kept clear of debris", "Doors, windows and cars rinsed down after", "Advice on sealing or treating once it is clean"],
      "clean-3.jpg", "Roof tiles after cleaning")),
    ("garden-care", "Garden Care", "Grass cutting, hedge trimming, weeding and seasonal tidy-ups.", I_SHEARS, "care-1.jpg",
     "Grass cutting, hedge trimming, weeding and seasonal tidy-ups — one-off or on a regular visit.",
     "Kept tidy,<br>all year round.",
     [(I_GRASS, "Grass cutting", "Lawns mown and edged, with cuttings taken away."),
      (I_SHEARS, "Hedge trimming", "Hedges and shrubs cut back and shaped, and kept clear of fences and paths."),
      (I_PLANT, "Weeding &amp; beds", "Beds and borders weeded, turned and mulched."),
      (I_CAL, "Regular visits", "Weekly, fortnightly or monthly visits through the growing season."),
      (I_SPARK, "Seasonal tidy-ups", "Spring and autumn clean-ups: leaves, pruning and getting the garden ready for the months ahead."),
      (I_BIN, "Green waste removal", "Everything we cut is bagged and taken away with us.")],
     ("No hassle", "You do not have to be home.",
      ["Same day and time agreed in advance", "Gates closed and the garden left tidy", "One-off clear-outs for overgrown gardens", "Happy to look after rental and commercial sites"],
      "care-1.jpg", "Boundary hedge trimmed")),
]
SVC = {s[0]: s for s in SERVICES}

NAV = [("about", "About Us"), ("services", "Our Services"), ("our-work", "Our Work"),
       ("process", "Process"), ("areas", "Areas"), ("blog", "Blog")]
FOOT = [(s[0], s[1]) for s in SERVICES] + [("about", "About Us"), ("our-work", "Our Work"), ("process", "Process"),
                                            ("areas", "Areas"), ("blog", "Blog"), ("faq", "FAQ"), ("contact", "Contact Us")]
SERVICE_SLUGS = {s[0] for s in SERVICES} | {"services"}


def page_hero(title, lead, img, crumb=None):
    crumb = crumb or title
    return f'''<section class="page-hero">
  <div class="hero-bg" style="background-image:url('img/{img}')"></div>
  <div class="wrap">
    <p class="crumbs"><a href="index.html">Home</a> / {crumb}</p>
    <h1>{title}</h1>
    <p>{lead}</p>
  </div>
</section>'''


CTA = f'''<section class="cta">
  <div class="wrap">
    <div><h2>Ready to get it sorted?</h2><p>Free site visit and a clear written quote, anywhere in Dublin.</p></div>
    <div class="cta-btns"><a href="tel:{PHONE_TEL}" class="btn btn-ghost">Call {PHONE}</a><a href="contact.html" class="btn btn-primary">Get my free quote</a></div>
  </div>
</section>'''


def nav_html(slug):
    def cur(s):
        on = s == slug or (s == "blog" and slug.startswith("blog-")) or (s == "services" and slug in SERVICE_SLUGS)
        return ' aria-current="page"' if on else ""
    out = []
    for s, t in NAV:
        if s == "services":
            subs = '<li><a href="services.html">All services</a></li>' + "".join(
                f'<li><a href="{x[0]}.html">{x[1]}</a></li>' for x in SERVICES)
            out.append(f'<li class="has-sub"><button type="button" class="sub-toggle" aria-expanded="false"{cur(s)}>{t}'
                       f'<svg viewBox="0 0 12 8" aria-hidden="true"><path d="M1 1.5 6 6.5l5-5" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>'
                       f'</button><div class="sub"><div class="sub-in"><ul>{subs}</ul></div></div></li>')
        else:
            out.append(f'<li><a href="{s}.html"{cur(s)}>{t}</a></li>')
    out.append('<li class="menu-cta"><a href="contact.html">Contact us</a></li>')
    return "".join(out)


def page(slug, title, desc, body, cta=True):
    foot = "".join(f'<a href="{s}.html">{t}</a>' for s, t in FOOT)
    slats = "".join(f'<i style="--i:{i}"></i>' for i in range(6))
    html = f'''<!DOCTYPE html>
<html lang="en-IE">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="#7B4321">
<link rel="icon" type="image/png" href="img/favicon.png">
<link rel="apple-touch-icon" href="img/icon-180.png">
<script>try{{document.documentElement.classList.add(sessionStorage.getItem('as-seen')?'quick':'first');sessionStorage.setItem('as-seen','1')}}catch(e){{}}</script>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="styles.css">
</head>
<body>
<div class="intro" aria-hidden="true">
  <div class="slats">{slats}</div>
  <div class="intro-logo"><div class="lock"><img class="mark" src="img/logo-mark.png" alt=""><img class="word" src="img/logo-word.png" alt=""></div><span class="line"></span></div>
</div>
<header class="nav" id="nav">
  <div class="wrap">
    <a href="index.html" class="brand" aria-label="{NAME} home"><img src="img/logo.png" alt="{NAME}" width="700" height="201"></a>
    <ul id="menu">{nav_html(slug)}</ul>
    <a href="contact.html" class="btn btn-primary">Contact us</a>
    <button class="burger" id="burger" aria-label="Open menu" aria-expanded="false" aria-controls="menu"><span></span><span></span><span></span></button>
  </div>
</header>
<main>
{body}
{CTA if cta else ""}
</main>
<footer>
  <div class="wrap">
    <a href="index.html" class="brand foot"><img src="img/logo.png" alt="{NAME}" width="700" height="201" loading="lazy"></a>
    <nav aria-label="Footer">{foot}</nav>
    <p class="foot-contact"><a href="tel:{PHONE_TEL}">{PHONE}</a><a href="mailto:{EMAIL}">{EMAIL}</a><span>Dublin, Ireland</span></p>
    <p class="copy">© <span id="yr"></span> {NAME}</p>
  </div>
<div class="almlab-credit-row" style="display:flex;justify-content:center;padding:12px 16px 4px"><a class="almlab-credit" href="https://almlabmarketing.com" target="_blank" rel="noopener" aria-label="Website by AlmLab" style="display:inline-flex;align-items:center;gap:3px;color:rgba(255,255,255,.55);font-size:11px;letter-spacing:.06em;line-height:1;text-decoration:none;white-space:nowrap"><span>Website by</span><img src="https://almlabmarketing.com/almlab-credit.png" alt="AlmLab" width="74" height="28" loading="lazy" style="height:28px;width:auto;display:block"></a></div>
</footer>
<div class="lightbox" id="lightbox" role="dialog" aria-modal="true" aria-label="Photo viewer" hidden>
  <button type="button" class="lb-close" aria-label="Close"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6 6l12 12M18 6 6 18"/></svg></button>
  <button type="button" class="lb-nav lb-prev" aria-label="Previous photo"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M15 5l-7 7 7 7"/></svg></button>
  <figure class="lb-stage"><img alt=""><figcaption><span class="lb-cap"></span><span class="lb-count"></span></figcaption></figure>
  <button type="button" class="lb-nav lb-next" aria-label="Next photo"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M9 5l7 7-7 7"/></svg></button>
</div>
<script src="site.js"></script>
</body>
</html>
'''
    (OUT / f"{slug}.html").write_text(html)


def card(img, alt, h, p):
    return (f'<article class="card reveal"><figure><img src="img/{img}" alt="{alt}" loading="lazy"></figure>'
            f'<div><h3>{h}</h3><p>{p}</p></div></article>')


def tiles(items):
    return '<div class="tiles">' + "".join(
        f'<div class="tile reveal">{svg(d)}<h3>{h}</h3><p>{p}</p></div>' for d, h, p in items) + '</div>'


COVER = {"fencing": "fence-10.jpg", "landscaping": "land-6.jpg", "paving": "pave-3.jpg",
         "painting": "paint-1.jpg", "exterior-cleaning": "clean-1.jpg", "garden-care": "care-1.jpg"}
# one photo per tile on each service page, in the same order as the tiles
TILE_IMG = {
    "landscaping": ["land-8.jpg", "land-11.jpg", "land-1.jpg", "land-10.jpg", "land-6.jpg", "land-3.jpg"],
    "paving": ["pave-3.jpg", "pave-8.jpg", "pave-5.jpg", "pave-1.jpg", "pave-6.jpg", "pave-4.jpg"],
    "painting": ["paint-1.jpg", "paint-2.jpg", "fence-11.jpg", "paint-7.jpg", "paint-9.jpg", "paint-5.jpg"],
    "exterior-cleaning": ["clean-1.jpg", "clean-9.jpg", "clean-5.jpg", "clean-6.jpg", "clean-8.jpg", "clean-3.jpg"],
    "garden-care": ["land-8.jpg", "care-1.jpg", "land-11.jpg", "land-9.jpg", "care-2.jpg", "care-3.jpg"],
}


def svc_grid(exclude=None):
    return '<div class="grid3">' + "".join(
        f'<a class="card post svc-card reveal" href="{s[0]}.html"><figure><img src="img/{COVER[s[0]]}" alt="{s[1]}" loading="lazy"></figure>'
        f'<div><h3>{s[1]}</h3><p>{s[2]}</p><span class="more">Learn more →</span></div></a>'
        for s in SERVICES if s[0] != exclude) + '</div>'


def photo_tiles(slug, items):
    return '<div class="grid3">' + "".join(
        card(img, h.replace("&amp;", "and"), h, p) for img, (d, h, p) in zip(TILE_IMG[slug], items)) + '</div>'


def split(eyebrow, h2, ticks, img, alt, lead="", flip=False):
    fig = f'<figure class="reveal"><img src="img/{img}" alt="{alt}" loading="lazy"></figure>'
    txt = (f'<div class="reveal"><span class="eyebrow">{eyebrow}</span><h2>{h2}</h2>'
           + (f'<p class="lead">{lead}</p>' if lead else "")
           + ('<ul class="ticks">' + "".join(f"<li>{t}</li>" for t in ticks) + "</ul>" if ticks else "") + "</div>")
    return f'<section class="areas"><div class="wrap">{txt + fig if flip else fig + txt}</div></section>'


def head(eyebrow, h2, lead="", link=None):
    right = f'<p class="lead">{lead}</p>' if lead else ""
    if link:
        right += f'<a class="btn btn-outline" href="{link[0]}">{link[1]}</a>'
    return f'<div class="head reveal"><div><span class="eyebrow">{eyebrow}</span><h2>{h2}</h2></div>{right}</div>'


FENCE_CARDS = '<div class="grid3">' + "".join([
    card("fence-3.jpg", "Horizontal timber panel fence on concrete posts", "Timber fencing",
         "Pressure-treated panels, hit-and-miss, wave-top and lattice designs on concrete posts and gravel boards."),
    card("fence-5.jpg", "Modern grey composite fence beside a patio", "Composite fencing",
         "Low-maintenance slatted boards in grey, green or wood-effect finishes. No painting, no rot."),
    card("fence-8.jpg", "White PVC fence with lattice top", "PVC fencing &amp; gates",
         "Clean, bright PVC privacy fencing with lattice tops and matching side gates that wipe clean."),
]) + '</div>'

CATS = [("fencing", "Fencing"), ("painting", "Painting"), ("cleaning", "Exterior Cleaning"),
        ("paving", "Paving"), ("landscaping", "Landscaping"), ("care", "Garden Care")]
_P = {
    "fencing": [("fence-10.jpg", "Slatted cedar fencing with built-in seating"), ("fence-11.jpg", "Black horizontal slatted fence"), ("fence-12.jpg", "Dark fence panels with timber posts"), ("fence-13.jpg", "Closeboard timber fence"), ("fence-14.jpg", "Featheredge timber fence"),
                ("fence-2.jpg", "Wave-top timber fence"), ("fence-6.jpg", "Green slatted composite fence"), ("fence-9.jpg", "Wood-effect composite fence"),
                ("fence-4.jpg", "Cream PVC fence with lattice top"), ("fence-7.jpg", "Beige PVC privacy gate"), ("fence-1.jpg", "Arched lattice timber fence"),
                ("fence-5.jpg", "Grey composite fence and patio"), ("fence-3.jpg", "Horizontal timber panel fence"), ("fence-8.jpg", "White PVC fence with lattice top")],
    "painting": [("paint-1.jpg", "Exterior house painting"), ("paint-5.jpg", "Kitchen painted in teal"), ("paint-2.jpg", "Room painted in warm grey"),
                 ("paint-7.jpg", "Staircase in black satin"), ("paint-4.jpg", "Navy feature room"), ("paint-6.jpg", "Kitchen walls and ceiling"),
                 ("paint-3.jpg", "Painted room with new flooring"), ("paint-8.jpg", "Hall, stairs and landing"), ("paint-9.jpg", "Landing and doors"), ("paint-10.jpg", "Bathroom painting")],
    "cleaning": [("clean-1.jpg", "Block paving driveway cleaned"), ("clean-3.jpg", "Roof tiles cleaned"), ("clean-8.jpg", "Driveway and roof cleaned"),
                 ("clean-5.jpg", "House exterior wash"), ("clean-4.jpg", "Ridge and roof cleaned"), ("clean-7.jpg", "Roof after cleaning"),
                 ("clean-6.jpg", "Roof and walls cleaned"), ("clean-2.jpg", "Roof cleaning in progress"), ("clean-9.jpg", "Tarmac driveway washed")],
    "paving": [("pave-3.jpg", "Grey porcelain patio with slatted fence"), ("pave-4.jpg", "Porcelain patio and lawn"), ("pave-5.jpg", "Sandstone patio and steps"), ("pave-6.jpg", "Porcelain patio with drainage channel"), ("pave-7.jpg", "Patio and lawn with painted fence"), ("pave-8.jpg", "Charcoal block driveway"), ("pave-9.jpg", "Block-paved driveway and garage"), ("pave-10.jpg", "Gravel driveway with cobble border"), ("pave-11.jpg", "Gravel driveway with granite path"), ("pave-12.jpg", "Tarmac driveway with brick edging"),
                ("pave-1.jpg", "Tarmac driveway with granite edging"), ("pave-2.jpg", "Block-paved driveway")],
    "landscaping": [("land-3.jpg", "Porcelain patio, lawn and slatted fencing"), ("land-4.jpg", "Decking, lawn and feature wall"), ("land-5.jpg", "Patio, lawn and raised beds"), ("land-6.jpg", "Garden makeover with lighting"), ("land-7.jpg", "Sandstone patio and planting"), ("land-8.jpg", "Rear garden patio and lawn"), ("land-9.jpg", "Lawn and patio with new fencing"), ("land-10.jpg", "Artificial lawn with sleeper planters"), ("land-11.jpg", "Courtyard garden with planting"),
                ("land-2.jpg", "New lawn and paved patio"), ("land-1.jpg", "Gravel front garden with curved path")],
    "care": [("care-1.jpg", "Boundary hedge trimmed"), ("care-2.jpg", "Tree pruned and reduced"), ("care-3.jpg", "Tree cut back")],
}
# mixed order for the "All" view: one from each category in turn
PHOTOS = [(f, c, cat) for i in range(max(map(len, _P.values()))) for cat, _ in CATS for f, c in _P[cat][i:i + 1]]
HOME_PHOTOS = [(f, c, cat) for cat in ("fencing", "painting", "cleaning", "paving", "landscaping") for f, c in _P[cat][:1]]


def gallery(items, cls=""):
    return f'<div class="gallery {cls} reveal" data-gallery>' + "".join(
        f'<button type="button" data-cat="{cat}"><img src="img/{f}" alt="{c}" loading="lazy"><span>{c}</span></button>'
        for f, c, cat in items) + '</div>'


FILTERS = ('<div class="filters reveal" role="group" aria-label="Filter photos"><button type="button" class="on" data-filter="all">All</button>'
           + "".join(f'<button type="button" data-filter="{k}">{n}</button>' for k, n in CATS) + '</div>')


STEPS = '''<div class="steps">
  <div class="step reveal"><h3>Get in touch</h3><p>Tell us what you have in mind — a call, a message or the quote form.</p></div>
  <div class="step reveal"><h3>Free site visit</h3><p>We call out, measure up and talk through styles, materials and options.</p></div>
  <div class="step reveal"><h3>Clear written quote</h3><p>An itemised price with no hidden extras, and a start date that suits you.</p></div>
  <div class="step reveal"><h3>Built &amp; tidied</h3><p>We do the job properly, take the waste away, and leave it spotless.</p></div>
</div>'''

NOTE = '<p class="note">This is a general guide, not legal advice. If you are unsure about your own property, check with the planning section of your local council before going ahead.</p>'

# slug, image, tag, title, description, body
POSTS = [
    ("blog-timber-composite-pvc", "fence-9.jpg", "Fencing",
     "Timber, composite or PVC: which fence is right for your garden?",
     "The three main fence materials compared on looks, upkeep, lifespan and cost.",
     '''<p>Most Dublin gardens end up with one of three fence types. None is "the best" — they suit different budgets and different levels of patience for upkeep. Here is how they compare.</p>
<h2>Timber</h2>
<p>Timber is the classic choice and usually the lowest cost up front. Pressure-treated panels on concrete posts with a concrete gravel board underneath will give you the longest life, because the timber never sits in wet soil.</p>
<ul><li><strong>Good for:</strong> a natural look, tighter budgets, matching existing fences.</li><li><strong>Watch out for:</strong> it needs a coat of treatment or stain every couple of years to stay looking well.</li></ul>
<h2>Composite</h2>
<p>Composite boards are made from a mix of wood fibre and recycled plastic. They slot between posts as horizontal slats and come in greys, greens and wood-effect tones. They do not rot, warp or need painting.</p>
<ul><li><strong>Good for:</strong> a modern look and almost no maintenance.</li><li><strong>Watch out for:</strong> higher cost up front than timber.</li></ul>
<h2>PVC</h2>
<p>PVC fencing gives a clean, bright finish in white, cream or beige, often with a lattice top. It will not rot and washes down with a hose.</p>
<ul><li><strong>Good for:</strong> a tidy, uniform look and easy cleaning.</li><li><strong>Watch out for:</strong> fewer colour choices, and lighter colours show dirt sooner.</li></ul>
<h2>Still not sure?</h2>
<p>The quickest way to decide is to see the materials side by side. We bring samples on every site visit, so you can hold them up against your own house and garden before choosing.</p>''', "fencing"),
    ("blog-choosing-patio-paving", "pave-1.jpg", "Paving",
     "Porcelain, sandstone or concrete: choosing patio paving",
     "What each type of patio slab is like to live with, and why the base matters more than the slab.",
     '''<p>The slab you pick decides how a patio looks. The base underneath decides how long it stays looking that way. Here is a plain guide to both.</p>
<h2>Porcelain</h2>
<p>Porcelain is hard, even in colour and does not soak up water, so it resists staining and green growth better than anything else. It suits modern gardens and needs very little upkeep.</p>
<ul><li><strong>Watch out for:</strong> it costs more and must be laid on a full mortar bed with a bonding primer.</li></ul>
<h2>Natural stone</h2>
<p>Sandstone and limestone have natural variation that suits most houses. Every slab is slightly different, which gives a softer, more traditional look.</p>
<ul><li><strong>Watch out for:</strong> stone is porous, so it will weather and pick up algae sooner. A yearly wash keeps it right.</li></ul>
<h2>Concrete slabs</h2>
<p>Concrete paving is the budget option and comes in a wide range of finishes. Good-quality concrete slabs laid well will last for many years.</p>
<ul><li><strong>Watch out for:</strong> colour can fade over time in strong sun and weather.</li></ul>
<h2>The part you do not see</h2>
<p>Whatever slab you choose, it needs a dug-out, compacted hardcore base, a slight fall so rain runs away from the house, and a finished level that sits below the damp-proof course. Skipping any of these is how patios end up sinking, rocking or holding puddles.</p>''', "paving"),
    ("blog-painting-house-exterior", "paint-1.jpg", "Painting",
     "When is the best time to paint the outside of a house in Ireland?",
     "Picking the right weather window, and the preparation that makes exterior paint last.",
     '''<p>Exterior paint fails early for two reasons: it went on in the wrong weather, or it went on over a surface that was not ready. Both are avoidable.</p>
<h2>Pick the right window</h2>
<p>Late spring to early autumn is the usual season. You are looking for a dry spell with mild temperatures, and walls that have had time to dry out after rain. Paint applied to damp masonry or just before a shower will not bond properly.</p>
<h2>Avoid the extremes</h2>
<ul><li><strong>Too cold or damp:</strong> paint cures slowly and can wash off or bloom.</li><li><strong>Hot, direct sun:</strong> paint dries too fast and can blister or show lap marks.</li><li><strong>Late evening:</strong> dew can settle on paint before it has dried.</li></ul>
<h2>Preparation is most of the job</h2>
<p>Walls should be washed down to remove dirt, moss and algae, then left to dry. Flaking paint is scraped back, cracks are filled, and chalky or bare patches get a stabilising primer. Only then do two full coats of masonry paint go on.</p>
<h2>How long should it last?</h2>
<p>That depends on the paint, the wall and how exposed the house is, but good preparation and a quality masonry paint will always outlast a quick coat over a dirty wall.</p>''', "painting"),
    ("blog-power-washing-guide", "clean-1.jpg", "Exterior Cleaning",
     "Power washing: what it can and cannot fix",
     "Where power washing works well, where it can do damage, and how to keep surfaces clean for longer.",
     '''<p>Power washing is one of the quickest ways to make a property look cared for again. Used on the wrong surface or at the wrong pressure, it can also cause damage. Here is what to know.</p>
<h2>Where it works well</h2>
<ul><li>Concrete and block paving driveways</li><li>Patios and garden paths that have turned green and slippery</li><li>Garden walls and hard standing</li></ul>
<h2>Where care is needed</h2>
<ul><li><strong>Render and pointing:</strong> too much pressure can blow out mortar and mark render.</li><li><strong>Timber decking and fences:</strong> high pressure raises the grain and leaves stripes.</li><li><strong>Old tarmac:</strong> loose stone can be lifted out.</li></ul>
<p>On these surfaces a wider fan, more distance and lower pressure do the job without harm.</p>
<h2>After the clean</h2>
<p>Block paving should have its joints re-sanded once dry, as washing removes the sand that locks the blocks together. Timber is best treated or stained soon after cleaning, while it is bare and clean.</p>
<h2>Keeping it clean</h2>
<p>Moss and algae come back fastest in shade and where water sits. A light clean once a year is easier on the surface than a heavy clean every five.</p>''', "exterior-cleaning"),
    ("blog-garden-care-calendar", "care-1.jpg", "Garden Care",
     "A simple garden care calendar for Irish gardens",
     "What to do in each season to keep a garden tidy without it taking over your weekends.",
     '''<p>Most gardens only need a handful of jobs done at the right time. This is the rough calendar we work to.</p>
<h2>Spring</h2>
<ul><li>First cuts of the lawn, with the blades set high</li><li>Edge the lawn and weed the beds before weeds seed</li><li>Mulch borders to hold moisture and keep weeds down</li></ul>
<h2>Summer</h2>
<ul><li>Regular mowing — little and often is better than a hard cut</li><li>Trim fast-growing hedges, checking first for nesting birds</li><li>Keep on top of weeds in paving and gravel</li></ul>
<h2>Autumn</h2>
<ul><li>Clear fallen leaves from lawns, paths and drains</li><li>Main hedge cut once the nesting season is over</li><li>A good time to lay new turf and plant hedging</li></ul>
<h2>Winter</h2>
<ul><li>Prune dormant shrubs and trees where needed</li><li>Check fences, gates and posts after storms</li><li>Plan any bigger landscaping work for the year ahead</li></ul>
<p>If you would rather not think about any of it, a regular visit through the growing season covers the lot.</p>''', "garden-care"),
    ("blog-low-maintenance-garden", "land-2.jpg", "Landscaping",
     "Five ways to make a garden lower maintenance",
     "Design choices that cut down the weekly work without turning the garden into a car park.",
     '''<p>A low-maintenance garden is not one with nothing in it. It is one where the jobs that eat your time have been designed out.</p>
<h2>1. Shrink the awkward bits of lawn</h2>
<p>Narrow strips and tight corners are slow to mow. Turning them into gravel or planting leaves a simpler lawn shape that takes minutes to cut.</p>
<h2>2. Edge everything</h2>
<p>A firm edge between lawn, beds and gravel stops grass creeping and keeps stone where it belongs. It is the single biggest saver on tidying time.</p>
<h2>3. Use membrane and mulch</h2>
<p>Weed membrane under gravel and a thick mulch on beds stop most weeds before they start.</p>
<h2>4. Plant in groups</h2>
<p>A few hardy shrubs and grasses planted in blocks cover the ground, look deliberate and need far less attention than lots of small, different plants.</p>
<h2>5. Choose the boundary wisely</h2>
<p>A composite or PVC fence needs a wash now and then. A timber fence needs treating, and a hedge needs cutting. Pick the one that matches the time you actually have.</p>''', "landscaping"),
    ("blog-fence-care-irish-weather", "fence-1.jpg", "Fencing",
     "How to look after a timber fence in Irish weather",
     "A few small jobs each year that add years to the life of a timber fence.",
     '''<p>Rain and wind are what wear a timber fence out. A little attention once or twice a year makes a real difference to how long it lasts.</p>
<h2>Keep timber off the soil</h2>
<p>Timber that sits in damp earth rots first. If soil, bark or leaves have built up against the bottom of your panels, rake them back. Concrete gravel boards under the panels solve this for good.</p>
<h2>Treat it in dry weather</h2>
<p>Give the fence a coat of a good fence treatment or stain every two to three years. Pick a dry spell, brush off any green growth first, and pay extra attention to the tops and end grain where water soaks in.</p>
<h2>Cut back plants</h2>
<p>Ivy and heavy climbers hold moisture against the timber and add weight in the wind. Keep hedges and shrubs trimmed a little away from the panels so air can move.</p>
<h2>Check after storms</h2>
<p>After a big wind, walk the fence. Look for posts that have started to lean, loose panels and missing caps. A loose panel fixed this week is far cheaper than a run of fence that comes down in the next storm.</p>''', "fencing"),
    ("blog-fence-height-planning", "fence-7.jpg", "Fencing",
     "How high can a garden fence be in Ireland?",
     "The general height limits for garden fences and walls before planning permission comes into it.",
     f'''<p>It is one of the first questions we get asked. In most cases you can put up or replace a garden fence without planning permission, as long as you stay within the standard height limits.</p>
<h2>The general rule</h2>
<ul><li><strong>Back and side gardens:</strong> up to 2 metres high.</li><li><strong>Front gardens:</strong> up to 1.2 metres high in front of the house.</li></ul>
<p>These limits come from the exempted development rules for houses. Anything higher normally needs planning permission.</p>
<h2>When the rule may not apply</h2>
<ul><li>Protected structures and homes in architectural conservation areas.</li><li>Estates where the original planning permission has its own conditions on boundaries.</li><li>Corner sites, where a fence could block the view of drivers at a junction.</li></ul>
<h2>Talk to your neighbour</h2>
<p>If the fence sits on a shared boundary, have a chat with your neighbour before work starts. Agreeing the line, the height and which side faces where avoids nearly every dispute.</p>
{NOTE}''', "fencing"),
]


def post_cards(posts):
    return '<div class="grid3">' + "".join(
        f'<a class="card post reveal" href="{p[0]}.html"><figure><img src="img/{p[1]}" alt="" loading="lazy"></figure>'
        f'<div><span class="tag">{p[2]}</span><h3>{p[3]}</h3><p>{p[4]}</p><span class="more">Read article →</span></div></a>'
        for p in posts) + '</div>'


FORM = f'''<form id="form" class="reveal" action="https://api.web3forms.com/submit" method="POST">
  <h3>Request a quote</h3>
  <input type="hidden" name="access_key" value="{WEB3FORMS_KEY}">
  <input type="hidden" name="subject" value="New quote request – All Sorted website">
  <input type="hidden" name="from_name" value="All Sorted website">
  <input type="checkbox" name="botcheck" class="hp" tabindex="-1" autocomplete="off" aria-hidden="true">
  <label>Name<input name="name" required autocomplete="name"></label>
  <div class="row">
    <label>Phone<input name="phone" type="tel" required autocomplete="tel"></label>
    <label>Email<input name="email" type="email" required autocomplete="email"></label>
  </div>
  <div class="row">
    <label>Area / Eircode<input name="area" autocomplete="postal-code"></label>
    <label>Service
      <select name="service">{"".join(f"<option>{x[1]}</option>" for x in SERVICES)}<option>Something else</option></select>
    </label>
  </div>
  <label>Tell us about the job<textarea name="message" required placeholder="What you need done, rough sizes, anything we should know…"></textarea></label>
  <button class="btn btn-primary" type="submit">Send my request</button>
  <p class="form-status" role="status" aria-live="polite"></p>
  <small>We usually reply within one working day.</small>
</form>'''

CONTACT = f'''<section class="contact"><div class="wrap">
  <div class="reveal">
    <span class="eyebrow">Free quote</span>
    <h2>Let's get it sorted.</h2>
    <dl>
      <div><dt>Phone</dt><dd><a href="tel:{PHONE_TEL}">{PHONE}</a></dd></div>
      <div><dt>Email</dt><dd><a class="email" href="mailto:{EMAIL}">{EMAIL}</a></dd></div>
      <div><dt>Based in</dt><dd>Dublin, Ireland</dd></div>
    </dl>
  </div>
  {FORM}
</div></section>'''

# ── Home ────────────────────────────────────────────────────────
page("index", "All Sorted Fencing &amp; Landscaping | Dublin",
     "Dublin-based fencing, landscaping, paving, painting, exterior cleaning and garden care. Free quotes across Dublin.",
     f'''<section class="hero with-form">
  <video class="hero-bg" id="heroVideo" autoplay muted loop playsinline preload="none" aria-label="Fencing and paving by All Sorted"></video>
  <script>(function(){{var v=document.getElementById('heroVideo'),t=matchMedia('(max-width:760px) and (orientation:portrait)').matches?'tall':'wide';v.poster='img/hero-'+t+'.jpg';v.src='img/hero-'+t+'.mp4';}})();</script>
  <div class="wrap hero-grid">
    <div class="hero-copy">
      <h1>Your home &amp; garden,<br><em>all sorted.</em></h1>
      <p>Fencing, landscaping, paving, painting, exterior cleaning and garden care across Dublin — done properly and finished cleanly.</p>
      <ul class="hero-pills"><li><b>Dublin</b> based &amp; local</li><li><b>Free</b> no-obligation quotes</li></ul>
      <div class="hero-cta">
        <a href="tel:{PHONE_TEL}" class="btn btn-primary">Call {PHONE}</a>
        <a href="our-work.html" class="btn btn-ghost">See our work</a>
      </div>
    </div>
    <div class="hero-form" id="quote">{FORM.replace('class="reveal" ', '').replace('<h3>Request a quote</h3>', '<h3>Get your free quote</h3>')}</div>
  </div>
</section>
<div class="strip"><div class="wrap">
  <span>Dublin-based team</span><span>Free on-site quotes</span><span>Six services, one call</span><span>Tidy site, every time</span>
</div></div>
<section><div class="wrap">
  {head("What we do", "Everything outside<br>your front door.", "One team for the boundary, the garden and the outside of the house.", ("services.html", "All services"))}
  {svc_grid()}
</div></section>
<section class="process"><div class="wrap">
  {head("Fencing", "Fences built to stand<br>up to Dublin weather.", "", ("fencing.html", "More on fencing"))}
  {FENCE_CARDS}
</div></section>
<section><div class="wrap">
  {head("Our work", "Recent jobs.", "", ("our-work.html", "View the gallery"))}
  {gallery(HOME_PHOTOS, "four")}
</div></section>
<section class="process"><div class="wrap">
  {head("From the blog", "Advice before you buy.", "", ("blog.html", "All articles"))}
  {post_cards(POSTS[:3])}
</div></section>''', cta=False)

# ── Services overview ───────────────────────────────────────────
page("services", "Our Services | All Sorted Fencing &amp; Landscaping",
     "Fencing, landscaping, paving, painting, exterior cleaning and garden care across Dublin.",
     page_hero("Our Services", "Six services, one team. Pick one, or have us look after the lot.", "fence-9.jpg") + f'''
<section><div class="wrap">{svc_grid()}</div></section>
<section class="process"><div class="wrap">{head("How it works", "Four steps to sorted.", "", ("process.html", "Our process"))}{STEPS}</div></section>''')

# ── Fencing (custom layout) ─────────────────────────────────────
f = SVC["fencing"]
page("fencing", "Fencing in Dublin | All Sorted Fencing &amp; Landscaping",
     "Timber, composite and PVC fencing and gates supplied and fitted across Dublin. Free quotes.",
     page_hero("Fencing", f[5], f[4], crumb='<a href="services.html">Services</a> / Fencing') + f'''
<section><div class="wrap">
  {head("What we fit", "Fences built to stand<br>up to Dublin weather.", "Privacy, security and a boundary that looks the part. We supply and fit every style on solid concrete or timber posts.")}
  {FENCE_CARDS}
</div></section>
<section class="process"><div class="wrap">
  {head("Compare", "Which material suits you?", "A quick side-by-side. We bring samples to every site visit.")}
  <div class="tablewrap reveal"><table>
    <thead><tr><th></th><th>Timber</th><th>Composite</th><th>PVC</th></tr></thead>
    <tbody>
      <tr><th>Look</th><td>Natural, traditional</td><td>Modern, slatted</td><td>Clean, bright</td></tr>
      <tr><th>Upkeep</th><td>Treat every 2–3 years</td><td>Occasional wash</td><td>Occasional wash</td></tr>
      <tr><th>Up-front cost</th><td>Lowest</td><td>Higher</td><td>Higher</td></tr>
      <tr><th>Colours</th><td>Any stain or paint</td><td>Grey, green, wood-effect</td><td>White, cream, beige</td></tr>
    </tbody>
  </table></div>
  <p class="lead reveal" style="margin-top:22px">More detail in our guide: <a class="inline" href="blog-timber-composite-pvc.html">Timber, composite or PVC?</a></p>
</div></section>
{split("Also included", "Gates, posts and the old fence gone.", ["Side gates and garden gates to match your fence", "Concrete posts and gravel boards for a longer life", "Removal and disposal of your old fence", "Repairs and storm-damage replacement panels"], "fence-7.jpg", "Beige PVC gate with lattice top")}
<section class="process"><div class="wrap">{head("More from us", "Our other services.")}{svc_grid("fencing")}</div></section>''')

# ── Other service pages ─────────────────────────────────────────
for slug, name, short, icon, img, lead, h2, items, sp in SERVICES:
    if slug == "fencing":
        continue
    related = [p for p in POSTS if p[6] == slug]
    blog = (f'<p class="lead reveal" style="margin-top:26px">Read our guide: <a class="inline" href="{related[0][0]}.html">{related[0][3]}</a></p>'
            if related else "")
    page(slug, f"{name} in Dublin | All Sorted Fencing &amp; Landscaping", f"{short} Free quotes across Dublin.",
         page_hero(name, lead, img, crumb=f'<a href="services.html">Services</a> / {name}') + f'''
<section><div class="wrap">
  {head(name, h2, short)}
  {photo_tiles(slug, items)}
  {blog}
</div></section>
{split(sp[0], sp[1], sp[2], sp[3], sp[4])}
<section class="process"><div class="wrap">{head("More from us", "Our other services.")}{svc_grid(slug)}</div></section>''')

# ── Our work ────────────────────────────────────────────────────
page("our-work", "Our Work | All Sorted Fencing &amp; Landscaping",
     "Photos of recent fencing, painting, cleaning, paving and garden jobs.",
     page_hero("Our Work", "A look at some recent jobs. Tap any photo to see it full size.", "fence-2.jpg") + f'''
<section><div class="wrap">{FILTERS}{gallery(PHOTOS, "even")}</div></section>''')

# ── Process ─────────────────────────────────────────────────────
page("process", "How It Works | All Sorted Fencing &amp; Landscaping",
     "Our four-step process: get in touch, free site visit, clear written quote, built and tidied.",
     page_hero("Our Process", "Simple and transparent from the first call to the final tidy-up.", "fence-4.jpg") + f'''
<section class="process"><div class="wrap">
  {head("How it works", "Four steps to sorted.")}
  {STEPS}
</div></section>
{split("What to expect", "No surprises on the day.", ["We agree the details with you before starting", "You get the price in writing, itemised", "We keep the site safe and tidy while we work", "We walk the finished job with you before we leave"], "fence-9.jpg", "Finished wood-effect composite fence")}''')

# ── Areas ───────────────────────────────────────────────────────
page("areas", "Areas We Cover in Dublin | All Sorted Fencing &amp; Landscaping",
     "Fencing, landscaping, paving, painting and garden care across Dublin city and county.",
     page_hero("Areas We Cover", "Based in Dublin and working right across the city and county.", "fence-6.jpg") +
     split("Where we work", "Covering all of Dublin.", [], "fence-2.jpg", "Timber fence along a housing estate",
           lead="North side, south side and everywhere in between. If you are a little outside the county, ask — we will tell you straight if we can get to you.") + '''
<section class="process"><div class="wrap">
  <div class="grid3">
    <div class="box reveal"><h3>North Dublin</h3><ul class="pills"><li>Swords</li><li>Malahide</li><li>Howth</li><li>Clontarf</li><li>Finglas</li><li>Santry</li><li>Balbriggan</li><li>Skerries</li></ul></div>
    <div class="box reveal"><h3>South Dublin</h3><ul class="pills"><li>Rathfarnham</li><li>Dundrum</li><li>Dún Laoghaire</li><li>Blackrock</li><li>Stillorgan</li><li>Terenure</li><li>Sandyford</li><li>Dalkey</li></ul></div>
    <div class="box reveal"><h3>West Dublin &amp; City</h3><ul class="pills"><li>Dublin City</li><li>Blanchardstown</li><li>Castleknock</li><li>Lucan</li><li>Clondalkin</li><li>Tallaght</li><li>Ballyfermot</li><li>Palmerstown</li></ul></div>
  </div>
</div></section>''')

# ── About ───────────────────────────────────────────────────────
page("about", "About Us | All Sorted Fencing &amp; Landscaping",
     "All Sorted Fencing &amp; Landscaping is a Dublin-based team looking after fences, gardens and the outside of homes across the city and county.",
     page_hero("About Us", "A Dublin team that looks after fences, gardens and the outside of your home the way we would want our own done.", "fence-3.jpg") +
     split("Who we are", "Local, hands-on and easy to deal with.", [], "fence-9.jpg", "Wood-effect composite fence in a garden", flip=True,
           lead="All Sorted Fencing &amp; Landscaping is a Dublin-based company. We fit fencing, build and look after gardens, lay paving, paint inside and out and power wash — so one call covers everything outside your front door.</p><p class=\"lead\">The name says how we like to leave a job: finished, tidy and with nothing left for you to chase up.") + f'''
<section class="process"><div class="wrap">
  <div class="head reveal"><div><span class="eyebrow">How we work</span><h2>What you can count on.</h2></div></div>
  <div class="grid3">
    <div class="box reveal"><h3>Straight answers</h3><p>A clear written price, and honest advice on what is worth spending on and what is not.</p></div>
    <div class="box reveal"><h3>Proper materials</h3><p>Good timber, concrete posts, a solid base under paving and quality paint. The parts you cannot see matter most.</p></div>
    <div class="box reveal"><h3>Tidy finish</h3><p>Waste removed, the place swept, and a walk-round with you before we go.</p></div>
  </div>
</div></section>
<section><div class="wrap">{head("What we do", "Our services.", "", ("services.html", "All services"))}{svc_grid()}</div></section>''')

# ── Blog ────────────────────────────────────────────────────────
page("blog", "Blog | All Sorted Fencing &amp; Landscaping",
     "Fencing, paving, painting, cleaning and garden advice for Dublin homeowners.",
     page_hero("Blog", "Practical advice on fencing, paving, painting, cleaning and gardens for Dublin homeowners.", "fence-1.jpg") + f'''
<section><div class="wrap">{post_cards(POSTS)}</div></section>''')

for slug, img, tag, title, desc, body, svc in POSTS:
    page(slug, f"{title} | All Sorted", desc,
         page_hero(title, desc, img, crumb='<a href="blog.html">Blog</a>') + f'''
<section><article class="wrap prose"><span class="tag">{tag}</span>
{body}
<p>Need a hand with this? See our <a class="inline" href="{svc}.html">{SVC[svc][1].lower()} service</a> or <a class="inline" href="contact.html">ask for a free quote</a>.</p>
<p><a class="inline" href="blog.html">← Back to all articles</a></p></article></section>''')

# ── FAQ ─────────────────────────────────────────────────────────
FAQS = [
    ("Are quotes free?", "Yes. We call out, measure up and give you a written quote with no obligation."),
    ("What services do you offer?", 'Fencing, landscaping, paving, painting, exterior cleaning and garden care. See <a class="inline" href="services.html">all services</a>.'),
    ("Can you do several jobs together?", "Yes — that is what we are here for. Doing the fence, paving and planting as one project usually saves time and mess."),
    ("Do you take away the old fence and waste?", "We can remove and dispose of your existing fence, old paving and garden waste as part of the job — just mention it when you get in touch."),
    ("Which fence type is best for me?", "Timber is the most affordable and natural looking; composite and PVC cost more up front but need almost no upkeep. We bring samples and talk you through it on the site visit."),
    ("How long does a fence take to fit?", "Most garden fences are finished in one to three days, depending on length, ground conditions and the style chosen."),
    ("Do I need planning permission for a fence?", 'Usually not for fences up to 2 metres at the back and side or 1.2 metres at the front. See <a class="inline" href="blog-fence-height-planning.html">our guide to fence heights</a>.'),
    ("Do you do regular garden maintenance?", "Yes. We do weekly, fortnightly or monthly visits as well as one-off tidy-ups."),
]
page("faq", "FAQ | All Sorted Fencing &amp; Landscaping", "Answers to common questions about our fencing, landscaping and outdoor services in Dublin.",
     page_hero("Questions", "The things people ask us most.", "fence-8.jpg", crumb="FAQ") +
     '<section class="faq"><div class="wrap">' +
     "".join(f'<details class="reveal"><summary>{q}</summary><p>{a}</p></details>' for q, a in FAQS) +
     '</div></section>')

# ── Contact ─────────────────────────────────────────────────────
page("contact", "Contact Us | All Sorted Fencing &amp; Landscaping",
     "Get a free quote for fencing, landscaping, paving, painting, exterior cleaning or garden care anywhere in Dublin.",
     page_hero("Contact Us", "Send us a few details and we will come back to you to arrange a free site visit.", "fence-5.jpg") + f'''
{CONTACT}''', cta=False)

print("built", len(list(OUT.glob("*.html"))), "pages")
