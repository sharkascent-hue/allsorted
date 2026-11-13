#!/usr/bin/env python3
"""Generates the static pages. Edit content here, then run: python3 build.py"""
import pathlib

OUT = pathlib.Path(__file__).parent
NAME = "All Sorted Fencing &amp; Landscaping"

NAV = [("fencing", "Fencing"), ("landscaping", "Landscaping"), ("our-work", "Our Work"),
       ("process", "Process"), ("areas", "Areas"), ("about", "About Us"), ("blog", "Blog")]
FOOT = NAV + [("faq", "FAQ"), ("contact", "Contact")]

LOGO = ('<svg viewBox="0 0 34 34" fill="none" aria-hidden="true"><path d="M7 28V11l4-4 4 4v17zM19 28V11l4-4 4 4v17z" fill="#F28C28"/>'
        '<path d="M3 15.5h28v3H3zM3 22.5h28v3H3z" fill="#fff"/></svg><span>All Sorted<small>Fencing &amp; Landscaping</small></span>')
ICON = ("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' height='32' rx='7' fill='%230F5C45'/%3E"
        "%3Cpath d='M8 24V11l3-3 3 3v13zm10 0V11l3-3 3 3v13z' fill='%23F28C28'/%3E%3Cpath d='M6 15h20v2.5H6z' fill='%23fff'/%3E%3C/svg%3E")


def svg(d):
    return ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" '
            f'stroke-linecap="round" stroke-linejoin="round">{d}</svg>')


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


CTA = '''<section class="cta">
  <div class="wrap">
    <div><h2>Ready to get it sorted?</h2><p>Free site visit and a clear written quote, anywhere in Dublin.</p></div>
    <a href="contact.html" class="btn btn-primary">Get my free quote</a>
  </div>
</section>'''


def page(slug, title, desc, body, cta=True):
    links = "".join(
        f'<li><a href="{s}.html"{" aria-current=\"page\"" if s == slug or (s == "blog" and slug.startswith("blog-")) else ""}>{t}</a></li>'
        for s, t in NAV)
    foot = "".join(f'<a href="{s}.html">{t}</a>' for s, t in FOOT)
    html = f'''<!DOCTYPE html>
<html lang="en-IE">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="#0F5C45">
<link rel="icon" href="{ICON}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="styles.css">
</head>
<body>
<header class="nav" id="nav">
  <div class="wrap">
    <a href="index.html" class="brand" aria-label="{NAME} home">{LOGO}</a>
    <ul id="menu">{links}</ul>
    <a href="contact.html" class="btn btn-white">Get a free quote</a>
    <button class="burger" id="burger" aria-label="Open menu" aria-expanded="false" aria-controls="menu"><span></span><span></span><span></span></button>
  </div>
</header>
<main>
{body}
{CTA if cta else ""}
</main>
<footer>
  <div class="wrap">
    <a href="index.html" class="brand">{LOGO}</a>
    <nav aria-label="Footer">{foot}</nav>
    <p class="copy">© <span id="yr"></span> {NAME} · Dublin, Ireland</p>
  </div>
</footer>
<div class="lightbox" id="lightbox" role="dialog" aria-modal="true" aria-label="Photo viewer"><img alt=""><p></p></div>
<script src="site.js"></script>
</body>
</html>
'''
    (OUT / f"{slug}.html").write_text(html)


def card(img, alt, h, p, href=None):
    more = f'<a class="more" href="{href}">Read more →</a>' if href else ""
    return (f'<article class="card reveal"><figure><img src="img/{img}" alt="{alt}" loading="lazy"></figure>'
            f'<div><h3>{h}</h3><p>{p}</p>{more}</div></article>')


FENCE_CARDS = '<div class="grid3">' + "".join([
    card("fence-3.jpg", "Horizontal timber panel fence on concrete posts", "Timber fencing",
         "Pressure-treated panels, hit-and-miss, wave-top and lattice designs on concrete posts and gravel boards."),
    card("fence-5.jpg", "Modern grey composite fence beside a patio", "Composite fencing",
         "Low-maintenance slatted boards in grey, green or wood-effect finishes. No painting, no rot."),
    card("fence-8.jpg", "White PVC fence with lattice top", "PVC fencing &amp; gates",
         "Clean, bright PVC privacy fencing with lattice tops and matching side gates that wipe clean."),
]) + '</div>'

TILES = [
    ('<rect x="3" y="3" width="8" height="8" rx="1"/><rect x="13" y="3" width="8" height="5" rx="1"/><rect x="13" y="10" width="8" height="11" rx="1"/><rect x="3" y="13" width="8" height="8" rx="1"/>',
     "Patios &amp; paving", "Stone, porcelain and concrete paving laid on a proper base, with clean edges and good drainage."),
    ('<path d="M4 21 9 3M20 21 15 3M12 5v3M12 11v3M12 17v3"/>',
     "Gravel driveways", "Hard-wearing gravel and decorative stone driveways and paths, edged and weed-membraned."),
    ('<path d="M3 20h18M6 20v-5M10 20v-8M14 20v-6M18 20v-9"/>',
     "Lawns &amp; turfing", "New roll-out lawns, levelling and reseeding to bring tired, patchy grass back to life."),
    ('<path d="M12 21v-9M12 12c0-4 3-7 8-7 0 5-3 8-8 7zM12 15c0-3-2-5-7-5 0 4 3 6 7 5z"/>',
     "Planting &amp; beds", "Raised beds, borders, hedging and planting schemes that suit your soil and your schedule."),
    ('<circle cx="6" cy="18" r="3"/><circle cx="18" cy="18" r="3"/><path d="M8 16 20 4M16 16 4 4"/>',
     "Garden maintenance", "Hedge trimming, grass cutting, weeding and seasonal tidy-ups — one-off or on a regular visit."),
    ('<path d="M4 5h9v5H4zM13 7h4l3 3M8 10v4M5 18c1-2 5-2 6 0M14 16l1 3M18 15l2 3"/>',
     "Power washing", "Deep cleaning for patios, driveways, walls and decking to lift years of moss and grime."),
]
TILES_HTML = '<div class="tiles">' + "".join(
    f'<div class="tile reveal">{svg(d)}<h3>{h}</h3><p>{p}</p></div>' for d, h, p in TILES) + '</div>'

PHOTOS = [
    ("fence-2.jpg", "Wave-top timber fence along a new housing estate", "Wave-top timber fence"),
    ("fence-6.jpg", "Green slatted composite fence beside a lawn", "Green slatted composite"),
    ("fence-9.jpg", "Wood-effect composite fence in a corner garden", "Wood-effect composite"),
    ("fence-4.jpg", "Cream PVC fence with lattice top", "Cream PVC with lattice top"),
    ("fence-7.jpg", "Beige PVC privacy gate with lattice top", "Beige PVC privacy gate"),
    ("fence-1.jpg", "Arched lattice timber fence panels", "Arched lattice timber"),
    ("fence-5.jpg", "Grey composite fence beside a patio", "Grey composite &amp; patio"),
    ("fence-3.jpg", "Horizontal timber panel fence", "Horizontal timber panels"),
    ("fence-8.jpg", "White PVC fence with lattice top", "White PVC with lattice top"),
]


def gallery(items, cls=""):
    return f'<div class="gallery {cls} reveal" data-gallery>' + "".join(
        f'<button type="button"><img src="img/{f}" alt="{a}" loading="lazy"><span>{c}</span></button>'
        for f, a, c in items) + '</div>'


STEPS = '''<div class="steps">
  <div class="step reveal"><h3>Get in touch</h3><p>Tell us what you have in mind — a call, a message or the quote form.</p></div>
  <div class="step reveal"><h3>Free site visit</h3><p>We call out, measure up and talk through styles, materials and options.</p></div>
  <div class="step reveal"><h3>Clear written quote</h3><p>An itemised price with no hidden extras, and a start date that suits you.</p></div>
  <div class="step reveal"><h3>Built &amp; tidied</h3><p>We do the job properly, take the old fence and waste away, and leave it spotless.</p></div>
</div>'''

POSTS = [
    ("blog-timber-composite-pvc", "fence-9.jpg", "Buying guide",
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
<p>The quickest way to decide is to see the materials side by side. We bring samples on every site visit, so you can hold them up against your own house and garden before choosing.</p>'''),
    ("blog-fence-care-irish-weather", "fence-2.jpg", "Maintenance",
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
<p>After a big wind, walk the fence. Look for posts that have started to lean, loose panels and missing caps. A loose panel fixed this week is far cheaper than a run of fence that comes down in the next storm.</p>
<h2>When to replace</h2>
<p>If posts are rotten at ground level or several panels are soft to the touch, repair stops being worth it. At that point it is worth pricing a new fence on concrete posts.</p>'''),
    ("blog-fence-height-planning", "fence-4.jpg", "Planning",
     "How high can a garden fence be in Ireland?",
     "The general height limits for garden fences and walls before planning permission comes into it.",
     '''<p>It is one of the first questions we get asked. In most cases you can put up or replace a garden fence without planning permission, as long as you stay within the standard height limits.</p>
<h2>The general rule</h2>
<ul><li><strong>Back and side gardens:</strong> up to 2 metres high.</li><li><strong>Front gardens:</strong> up to 1.2 metres high in front of the house.</li></ul>
<p>These limits come from the exempted development rules for houses. Anything higher normally needs planning permission.</p>
<h2>When the rule may not apply</h2>
<ul><li>Protected structures and homes in architectural conservation areas.</li><li>Estates where the original planning permission has its own conditions on boundaries.</li><li>Corner sites, where a fence could block the view of drivers at a junction.</li></ul>
<h2>Talk to your neighbour</h2>
<p>If the fence sits on a shared boundary, have a chat with your neighbour before work starts. Agreeing the line, the height and which side faces where avoids nearly every dispute.</p>
<p class="note">This is a general guide, not legal advice. If you are unsure about your own property, check with the planning section of your local council before going ahead.</p>'''),
]
POST_CARDS = '<div class="grid3">' + "".join(
    f'<a class="card post reveal" href="{s}.html"><figure><img src="img/{i}" alt="" loading="lazy"></figure>'
    f'<div><span class="tag">{t}</span><h3>{h}</h3><p>{d}</p><span class="more">Read article →</span></div></a>'
    for s, i, t, h, d, _ in POSTS) + '</div>'

FORM = '''<form id="form" class="reveal">
  <h3>Request a quote</h3>
  <div class="row">
    <label>Name<input name="name" required autocomplete="name"></label>
    <label>Phone<input name="phone" type="tel" required autocomplete="tel"></label>
  </div>
  <div class="row">
    <label>Area / Eircode<input name="area" autocomplete="postal-code"></label>
    <label>Service
      <select name="service"><option>Fencing</option><option>Landscaping</option><option>Patio / paving</option><option>Gravel driveway</option><option>Garden maintenance</option><option>Something else</option></select>
    </label>
  </div>
  <label>Tell us about the job<textarea name="message" placeholder="Rough length of fence, style you like, anything we should know…"></textarea></label>
  <button class="btn btn-primary" type="submit">Send my request</button>
  <small>Opens your email app with the details filled in.</small>
</form>'''


def head(eyebrow, h2, lead="", link=None):
    right = f'<p class="lead">{lead}</p>' if lead else ""
    if link:
        right += f'<a class="btn btn-outline" href="{link[0]}">{link[1]}</a>'
    return f'<div class="head reveal"><div><span class="eyebrow">{eyebrow}</span><h2>{h2}</h2></div>{right}</div>'


# ── Home ────────────────────────────────────────────────────────
page("index", "All Sorted Fencing &amp; Landscaping | Dublin",
     "Dublin-based fencing and garden landscaping. Timber, composite and PVC fencing, patios, gravel driveways and garden care. Free quotes across Dublin.",
     f'''<section class="hero">
  <div class="hero-bg" role="img" aria-label="Timber fence being installed in a garden"></div>
  <div class="chip l"><b>Dublin</b><span>based &amp; local</span></div>
  <div class="chip r"><b>Free</b><span>no-obligation quotes</span></div>
  <div class="wrap">
    <h1>Your garden,<br><em>all sorted.</em></h1>
    <p>Quality fencing and landscaping across Dublin — built properly, finished cleanly and made to last through every Irish season.</p>
    <div class="hero-cta">
      <a href="contact.html" class="btn btn-primary">Get my free quote</a>
      <a href="our-work.html" class="btn btn-ghost">See our work</a>
    </div>
  </div>
  <nav class="tabs" aria-label="Services">
    <a href="fencing.html">Fencing</a>
    <a href="landscaping.html" style="text-align:center">Landscaping</a>
    <a href="landscaping.html">Garden care</a>
  </nav>
</section>
<div class="strip"><div class="wrap">
  <span>Dublin-based team</span><span>Free on-site quotes</span><span>Timber, composite &amp; PVC</span><span>Tidy site, every time</span>
</div></div>
<section><div class="wrap">
  {head("Fencing", "Fences built to stand<br>up to Dublin weather.", "", ("fencing.html", "All fencing"))}
  {FENCE_CARDS}
</div></section>
<section class="land"><div class="wrap">
  {head("Landscaping &amp; garden care", "The whole garden,<br>not just the boundary.", "", ("landscaping.html", "All landscaping"))}
  {TILES_HTML}
</div></section>
<section><div class="wrap">
  {head("Our work", "Recent fences &amp; gardens.", "", ("our-work.html", "View the gallery"))}
  {gallery(PHOTOS[:5], "four")}
</div></section>
<section class="process"><div class="wrap">
  {head("From the blog", "Advice before you buy.", "", ("blog.html", "All articles"))}
  {POST_CARDS}
</div></section>''')

# ── Fencing ─────────────────────────────────────────────────────
page("fencing", "Fencing in Dublin | All Sorted Fencing &amp; Landscaping",
     "Timber, composite and PVC fencing and gates supplied and fitted across Dublin. Free quotes.",
     page_hero("Fencing", "Timber, composite and PVC fencing and gates, supplied and fitted across Dublin.", "fence-3.jpg") + f'''
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
<section class="areas"><div class="wrap">
  <figure class="reveal"><img src="img/fence-7.jpg" alt="Beige PVC gate with lattice top" loading="lazy"></figure>
  <div class="reveal">
    <span class="eyebrow">Also included</span>
    <h2>Gates, posts and the old fence gone.</h2>
    <ul class="ticks">
      <li>Side gates and garden gates to match your fence</li>
      <li>Concrete posts and gravel boards for a longer life</li>
      <li>Removal and disposal of your old fence</li>
      <li>Repairs and storm-damage replacement panels</li>
    </ul>
  </div>
</div></section>''')

# ── Landscaping ─────────────────────────────────────────────────
page("landscaping", "Landscaping &amp; Garden Care in Dublin | All Sorted",
     "Patios, paving, gravel driveways, lawns, planting, garden maintenance and power washing across Dublin.",
     page_hero("Landscaping", "Patios, driveways, lawns, planting and regular garden care — one team for the whole garden.", "fence-5.jpg") + f'''
<section class="land"><div class="wrap">
  {head("Landscaping &amp; garden care", "The whole garden,<br>not just the boundary.", "From the ground works to the finishing touches, so you only have to make one call.")}
  {TILES_HTML}
</div></section>
<section class="areas"><div class="wrap">
  <div class="reveal">
    <span class="eyebrow">One project</span>
    <h2>Fence and garden done together.</h2>
    <p class="lead">Doing the boundary, the paving and the planting as one job means one plan, one crew and one clean-up. It usually saves time and avoids digging up finished work later.</p>
    <ul class="ticks">
      <li>Ground levelled and drained before anything is laid</li>
      <li>Paving and gravel on a proper compacted base</li>
      <li>All waste taken away when we finish</li>
    </ul>
  </div>
  <figure class="reveal"><img src="img/fence-6.jpg" alt="Green composite fence beside a new lawn" loading="lazy"></figure>
</div></section>''')

# ── Our work ────────────────────────────────────────────────────
page("our-work", "Our Work | All Sorted Fencing &amp; Landscaping",
     "Photos of timber, composite and PVC fences and gardens.",
     page_hero("Our Work", "A look at the fence styles we fit. Tap any photo to see it full size.", "fence-2.jpg") + f'''
<section><div class="wrap">{gallery(PHOTOS)}</div></section>''')

# ── Process ─────────────────────────────────────────────────────
page("process", "How It Works | All Sorted Fencing &amp; Landscaping",
     "Our four-step process: get in touch, free site visit, clear written quote, built and tidied.",
     page_hero("Our Process", "Simple and transparent from the first call to the final tidy-up.", "fence-4.jpg") + f'''
<section class="process"><div class="wrap">
  {head("How it works", "Four steps to sorted.")}
  {STEPS}
</div></section>
<section class="areas"><div class="wrap">
  <figure class="reveal"><img src="img/fence-9.jpg" alt="Finished wood-effect composite fence" loading="lazy"></figure>
  <div class="reveal">
    <span class="eyebrow">What to expect</span>
    <h2>No surprises on the day.</h2>
    <ul class="ticks">
      <li>We agree the fence line, height and style with you before starting</li>
      <li>You get the price in writing, itemised</li>
      <li>We keep the site safe and tidy while we work</li>
      <li>We walk the finished job with you before we leave</li>
    </ul>
  </div>
</div></section>''')

# ── Areas ───────────────────────────────────────────────────────
page("areas", "Areas We Cover in Dublin | All Sorted Fencing &amp; Landscaping",
     "Fencing and landscaping across Dublin city and county — north side, south side and west Dublin.",
     page_hero("Areas We Cover", "Based in Dublin and working right across the city and county.", "fence-6.jpg") + '''
<section class="areas"><div class="wrap">
  <figure class="reveal"><img src="img/fence-2.jpg" alt="Timber fence along a housing estate" loading="lazy"></figure>
  <div class="reveal">
    <span class="eyebrow">Where we work</span>
    <h2>Covering all of Dublin.</h2>
    <p class="lead">North side, south side and everywhere in between. If you are a little outside the county, ask — we will tell you straight if we can get to you.</p>
  </div>
</div></section>
<section class="process"><div class="wrap">
  <div class="grid3">
    <div class="box reveal"><h3>North Dublin</h3><ul class="pills"><li>Swords</li><li>Malahide</li><li>Howth</li><li>Clontarf</li><li>Finglas</li><li>Santry</li><li>Balbriggan</li><li>Skerries</li></ul></div>
    <div class="box reveal"><h3>South Dublin</h3><ul class="pills"><li>Rathfarnham</li><li>Dundrum</li><li>Dún Laoghaire</li><li>Blackrock</li><li>Stillorgan</li><li>Terenure</li><li>Sandyford</li><li>Dalkey</li></ul></div>
    <div class="box reveal"><h3>West Dublin &amp; City</h3><ul class="pills"><li>Dublin City</li><li>Blanchardstown</li><li>Castleknock</li><li>Lucan</li><li>Clondalkin</li><li>Tallaght</li><li>Ballyfermot</li><li>Palmerstown</li></ul></div>
  </div>
</div></section>''')

# ── About ───────────────────────────────────────────────────────
page("about", "About Us | All Sorted Fencing &amp; Landscaping",
     "All Sorted Fencing &amp; Landscaping is a Dublin-based team fitting fences and building gardens across the city and county.",
     page_hero("About Us", "A Dublin team that fits fences and builds gardens the way we would want our own done.", "hero.jpg") + '''
<section class="areas"><div class="wrap">
  <div class="reveal">
    <span class="eyebrow">Who we are</span>
    <h2>Local, hands-on and easy to deal with.</h2>
    <p class="lead">All Sorted Fencing &amp; Landscaping is a Dublin-based company. We fit timber, composite and PVC fencing and take care of the garden around it — patios, driveways, lawns and planting.</p>
    <p class="lead">The name says how we like to leave a job: finished, tidy and with nothing left for you to chase up.</p>
  </div>
  <figure class="reveal"><img src="img/fence-3.jpg" alt="Newly fitted timber panel fence" loading="lazy"></figure>
</div></section>
<section class="process"><div class="wrap">
  <div class="head reveal"><div><span class="eyebrow">How we work</span><h2>What you can count on.</h2></div></div>
  <div class="grid3">
    <div class="box reveal"><h3>Straight answers</h3><p>A clear written price, and honest advice on what is worth spending on and what is not.</p></div>
    <div class="box reveal"><h3>Proper materials</h3><p>Pressure-treated timber, concrete posts and gravel boards, and quality composite and PVC systems.</p></div>
    <div class="box reveal"><h3>Tidy finish</h3><p>Old fencing and waste removed, the garden swept, and a walk-round with you before we go.</p></div>
  </div>
</div></section>''')

# ── Blog ────────────────────────────────────────────────────────
page("blog", "Blog | All Sorted Fencing &amp; Landscaping",
     "Fencing and garden advice for Dublin homeowners.",
     page_hero("Blog", "Practical fencing and garden advice for Dublin homeowners.", "fence-1.jpg") + f'''
<section><div class="wrap">{POST_CARDS}</div></section>''')

for slug, img, tag, title, desc, body in POSTS:
    page(slug, f"{title} | All Sorted", desc,
         page_hero(title, desc, img, crumb='<a href="blog.html">Blog</a>') + f'''
<section><article class="wrap prose"><span class="tag">{tag}</span>
{body}
<p><a class="inline" href="blog.html">← Back to all articles</a></p></article></section>''')

# ── FAQ ─────────────────────────────────────────────────────────
FAQS = [
    ("Are quotes free?", "Yes. We call out, measure up and give you a written quote with no obligation."),
    ("Do you take away the old fence?", "We can remove and dispose of your existing fence, posts and any garden waste as part of the job — just mention it when you get in touch."),
    ("Which fence type is best for me?", "Timber is the most affordable and natural looking; composite and PVC cost more up front but need almost no upkeep. We bring samples and talk you through it on the site visit."),
    ("How long does a fence take to fit?", "Most garden fences are finished in one to three days, depending on length, ground conditions and the style chosen."),
    ("Can you do the fence and the garden together?", "Absolutely — that is what we are here for. Doing fencing, paving and planting as one project usually saves time and mess."),
    ("Do I need planning permission?", 'Usually not for fences up to 2 metres at the back and side or 1.2 metres at the front. See <a class="inline" href="blog-fence-height-planning.html">our guide to fence heights</a>.'),
]
page("faq", "FAQ | All Sorted Fencing &amp; Landscaping", "Answers to common questions about fencing and landscaping in Dublin.",
     page_hero("Questions", "The things people ask us most.", "fence-8.jpg", crumb="FAQ") +
     '<section class="faq"><div class="wrap">' +
     "".join(f'<details class="reveal"><summary>{q}</summary><p>{a}</p></details>' for q, a in FAQS) +
     '</div></section>')

# ── Contact ─────────────────────────────────────────────────────
page("contact", "Contact &amp; Free Quote | All Sorted Fencing &amp; Landscaping",
     "Get a free fencing or landscaping quote anywhere in Dublin.",
     page_hero("Get a Free Quote", "Send us a few details and we will come back to you to arrange a free site visit.", "fence-5.jpg", crumb="Contact") + f'''
<section class="contact"><div class="wrap">
  <div class="reveal">
    <span class="eyebrow">Contact</span>
    <h2>Let's get your garden sorted.</h2>
    <dl>
      <div><dt>Phone</dt><dd><a data-phone href="contact.html">Add phone number</a></dd></div>
      <div><dt>Email</dt><dd><a data-email href="contact.html">Add email address</a></dd></div>
      <div><dt>Based in</dt><dd>Dublin, Ireland</dd></div>
    </dl>
  </div>
  {FORM}
</div></section>''', cta=False)

print("built", len(list(OUT.glob("*.html"))), "pages")
