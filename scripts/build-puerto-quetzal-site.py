#!/usr/bin/env python3
"""Generate Puerto Quetzal Shore Excursion static site pages."""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOMAIN = "puertoquetzalshoreexcursion.com"
SITE = "Puerto Quetzal Shore Excursion"
BASE_URL = f"https://{DOMAIN}"

HERO_GRADIENT = (
    "linear-gradient(135deg, rgba(55, 48, 163, 0.68) 0%, "
    "rgba(234, 88, 12, 0.48) 50%, rgba(6, 78, 59, 0.52) 100%)"
)

TOUR_CHECKLIST = [
    "Cruise-friendly timing",
    "Strong cultural value",
    "Local expert guidance",
    "Return-to-ship confidence",
    "Unique Guatemalan experiences",
]

HEAD_COMMON = """  <script src="https://cdn.tailwindcss.com"></script>
  <script src="js/tailwind-config.js"></script>
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;600;700&family=Source+Sans+3:wght@400;500;600;700&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="css/site.css" />"""

RETURN_BADGE = (
    '<span class="return-to-ship-badge" role="status">'
    '<svg fill="none" viewBox="0 0 24 24" stroke="currentColor" aria-hidden="true">'
    '<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" '
    'd="M3 17h18M5 17l2-8h10l2 8M9 9l1-4h4l1 4"/></svg>'
    "Return To Ship On Time</span>"
)


def snapshot(items: dict[str, str]) -> str:
    rows = "".join(
        f'<div class="cruise-snapshot__item"><dt>{k}</dt><dd>{v}</dd></div>'
        for k, v in items.items()
    )
    return f'''<aside class="cruise-snapshot mb-10 px-4 sm:px-0" aria-label="Cruise passenger snapshot">
  <h3 class="font-display font-bold text-lg text-gray-900 mb-4">Cruise Passenger Snapshot</h3>
  <dl class="cruise-snapshot__grid">{rows}</dl>
</aside>'''


def related_links(links: list[tuple[str, str]]) -> str:
    parts = []
    for i, (href, label) in enumerate(links):
        if i:
            parts.append('<span class="text-gray-300">·</span>')
        parts.append(
            f'<a href="{href}" class="text-ocean-600 hover:text-ocean-800 font-medium">{label}</a>'
        )
    return f'''<nav class="mt-10 pt-8 border-t border-gray-100" aria-label="Related Puerto Quetzal guides">
  <p class="text-sm font-semibold text-gray-900 mb-3">Plan your port day</p>
  <div class="flex flex-wrap gap-3 text-sm">{"".join(parts)}</div>
</nav>'''


def cta_section() -> str:
    return '''<section class="py-16 cta-gradient"><div class="max-w-3xl mx-auto px-4 text-center">
  <h2 class="text-3xl font-display font-bold text-white mb-4">Plan Your Port Day</h2>
  <p class="text-white/85 text-sm mb-6">Compare Puerto Quetzal shore excursions, read the port guide and confirm departure times with your operator before you book.</p>
  <div class="flex flex-col sm:flex-row gap-4 justify-center flex-wrap">
    <a href="best-puerto-quetzal-shore-excursions.html" class="btn-primary inline-flex items-center justify-center text-white font-semibold px-8 py-4 rounded-full">View Puerto Quetzal Excursions</a>
    <a href="puerto-quetzal-cruise-port-guide.html" class="btn-outline inline-flex items-center justify-center text-white font-semibold px-8 py-4 rounded-full">Plan Your Port Day</a>
    <a href="antigua-guatemala-shore-excursion.html" class="btn-outline inline-flex items-center justify-center text-white font-semibold px-8 py-4 rounded-full">Explore Antigua Guatemala</a>
  </div>
</div></section>'''


def hero(
    path: str,
    *,
    breadcrumb: str | None = None,
    eyebrow: str,
    title_html: str,
    lead: str,
    image: str,
    aria: str,
    actions: str = "",
    tags: str = "",
) -> str:
    bc = ""
    if breadcrumb:
        bc = f'''<nav class="site-hero__breadcrumb flex items-center gap-2 mb-4 text-xs text-white/60" aria-label="Breadcrumb">
        <a href="index.html" class="hover:text-white transition-colors">Home</a>
        <svg class="w-3 h-3" fill="none" viewBox="0 0 24 24" stroke="currentColor" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/></svg>
        <span class="text-white/80">{breadcrumb}</span>
      </nav>'''
    tag_block = (
        f'<div class="site-hero__tags flex flex-wrap gap-2 mt-5 pt-4 border-t border-white/20">{tags}</div>'
        if tags
        else ""
    )
    act_block = (
        f'<div class="site-hero__actions flex flex-col sm:flex-row gap-3">{actions}</div>'
        if actions
        else '<div class="site-hero__actions flex flex-col sm:flex-row gap-3"></div>'
    )
    return f'''<section class="site-hero">
  <div class="absolute inset-0 hero-bg-custom" style="background-image: {HERO_GRADIENT}, url('images/{image}');" role="img" aria-label="{aria}"></div>
  <div class="site-hero__inner max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="max-w-3xl">{bc}
      <div class="site-hero__eyebrow inline-flex items-center gap-2 bg-white/15 backdrop-blur-sm border border-white/30 rounded-full px-4 py-1.5 mb-3">
        <span class="w-2 h-2 rounded-full bg-gt-400 animate-pulse"></span>
        <span class="text-white/90 text-xs font-semibold tracking-widest uppercase">{eyebrow}</span>
      </div>
      <h1 class="site-hero__title text-4xl sm:text-5xl lg:text-[3.25rem] font-display font-bold text-white leading-tight mb-3">{title_html}</h1>
      <p class="site-hero__lead text-base sm:text-lg text-white/85 font-light leading-relaxed mb-5 max-w-2xl">{lead}</p>
      {act_block}
      {tag_block}
    </div>
  </div>
  <div class="absolute bottom-0 left-0 right-0"><svg viewBox="0 0 1440 48" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="none" class="site-hero__wave" aria-hidden="true"><path d="M0 24 C360 48 1080 0 1440 24 L1440 48 L0 48 Z" fill="white"/></svg></div>
</section>'''


def shell(
    filename: str,
    *,
    title: str,
    description: str,
    keywords: str,
    canonical: str,
    preload: str,
    page: str,
    hero_file: str,
    content_file: str,
    ld_json: dict | list,
) -> None:
    ld = json.dumps(ld_json, indent=2)
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{title}</title>
  <meta name="description" content="{description}" />
  <meta name="keywords" content="{keywords}" />
  <link rel="canonical" href="{canonical}" />
  <link rel="preload" as="image" href="images/{preload}" fetchpriority="high" />
  <meta property="og:type" content="website" />
  <meta property="og:url" content="{canonical}" />
  <meta property="og:title" content="{title}" />
  <meta property="og:description" content="{description}" />
  <meta property="og:image" content="{BASE_URL}/images/{preload}" />
  <meta property="og:site_name" content="{SITE}" />
  <meta name="twitter:card" content="summary_large_image" />
  <script type="application/ld+json">
{ld}
  </script>
{HEAD_COMMON}
</head>
<body class="bg-white text-gray-800 antialiased" data-page="{page}" data-base="" data-hero="{hero_file}" data-content="{content_file}" data-trust-strip="partials/trust-strip.html">
  <div id="site-nav"></div>
  <div id="page-hero"></div>
  <div id="page-trust-strip"></div>
  <main id="page-content"></main>
  <div id="site-footer"></div>
  <script src="js/site.js"></script>
</body>
</html>'''
    (ROOT / filename).write_text(html)


def tour_content(
    name: str,
    badge: str,
    badge_class: str,
    intro: str,
    image: str,
    alt: str,
    highlights: list[tuple[str, str, str, str]],
    snap: dict[str, str],
    links: list[tuple[str, str]],
) -> str:
    checks = "".join(
        f'<li class="flex gap-2 text-sm text-gray-600"><span class="text-ocean-500">✓</span>{c}</li>'
        for c in TOUR_CHECKLIST
    )
    cards = ""
    for h_img, h_alt, h_title, h_desc in highlights:
        cards += f'''<div class="bg-white rounded-3xl overflow-hidden shadow-md border border-gt-100 flex flex-col">
      <div class="card-media h-40"><img src="images/{h_img}" alt="{h_alt}" width="400" height="240" loading="lazy" decoding="async" /></div>
      <div class="p-5"><h3 class="font-display font-semibold text-gray-900 mb-2">{h_title}</h3><p class="text-sm text-gray-600 leading-relaxed">{h_desc}</p></div>
    </div>'''
    return f'''<section class="pt-8 pb-4 bg-white"><div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8"><div class="grid lg:grid-cols-2 gap-12 items-start">
  <div>
    <div class="mb-3 flex flex-wrap gap-2"><span class="{badge_class}" role="status">{badge}</span> {RETURN_BADGE}</div>
    <h2 class="text-2xl font-display font-bold text-gray-900 mb-4">Why Cruise Passengers Choose This Excursion</h2>
    <p class="text-gray-600 leading-relaxed mb-6">{intro}</p>
    <ul class="space-y-3 mb-6">{checks}</ul>
    <p class="text-xs text-gray-500">Confirm excursion timings, inclusions and return policies with your operator before booking. Always verify your ship&apos;s all-aboard time. Volcano access and road conditions can change — do not rely on fixed schedules without operator confirmation.</p>
  </div>
  <div class="card-media rounded-3xl overflow-hidden aspect-[4/3] shadow-lg">
    <img src="images/{image}" alt="{alt}" width="600" height="450" loading="lazy" decoding="async" />
  </div>
</div></div></section>
<section class="py-14 bg-gt-50"><div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
  <div class="text-center mb-10"><h2 class="text-2xl sm:text-3xl font-display font-bold text-gray-900 mb-3">Tour Highlights</h2>
  <p class="text-gray-600 text-sm max-w-2xl mx-auto">What to expect on this Puerto Quetzal shore excursion.</p></div>
  <div class="grid sm:grid-cols-2 lg:grid-cols-3 gap-6">{cards}</div>
</div></section>
<section class="pb-8 bg-white"><div class="max-w-7xl mx-auto px-4">{snapshot(snap)}</div></section>
<section class="pb-16 bg-white"><div class="max-w-3xl mx-auto px-4">{related_links(links)}</div></section>
{cta_section()}'''


def faq_section(title: str, items: list[tuple[str, str]]) -> str:
    blocks = ""
    for q, a in items:
        blocks += f'''<details class="faq-item rounded-2xl border border-gt-100 p-5"><summary class="font-semibold text-gray-900 cursor-pointer">{q}</summary>
      <p class="mt-4 text-sm text-gray-500">{a}</p></details>'''
    return f'''<section class="py-16 bg-white"><div class="max-w-3xl mx-auto px-4">
  <h2 class="text-3xl font-display font-bold text-gray-900 text-center mb-8">{title}</h2>
  <div class="space-y-4">{blocks}</div>
</div></section>'''


def faq_schema(items: list[tuple[str, str]]) -> list[dict]:
    return [
        {
            "@type": "Question",
            "name": q,
            "acceptedAnswer": {"@type": "Answer", "text": a},
        }
        for q, a in items
    ]


# --- Partials ---
(ROOT / "partials").mkdir(exist_ok=True)
(ROOT / "content").mkdir(exist_ok=True)

(ROOT / "partials/nav.html").write_text('''<nav class="fixed top-0 left-0 right-0 z-50 bg-white/90 border-b border-gt-100 shadow-sm">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="flex items-center justify-between h-12">
      <a href="index.html" class="flex items-center gap-2">
        <div class="w-7 h-7 rounded-full btn-ocean flex items-center justify-center">
          <svg class="w-4 h-4 text-white" fill="currentColor" viewBox="0 0 24 24" aria-hidden="true">
            <path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-1 14H9V8h2v8zm4 0h-2V8h2v8z"/>
          </svg>
        </div>
        <span class="font-display font-semibold text-ocean-800 text-base leading-tight">Puerto Quetzal<br/><span class="text-[10px] font-body font-normal text-gt-600 tracking-widest uppercase">Shore Excursion</span></span>
      </a>
      <div class="hidden lg:flex items-center gap-5 text-sm font-medium">
        <a href="index.html" data-nav="home" class="text-gray-600 hover:text-ocean-600 transition-colors">Home</a>
        <a href="best-puerto-quetzal-shore-excursions.html" data-nav="excursions" class="text-gray-600 hover:text-ocean-600 transition-colors">Excursions</a>
        <a href="antigua-guatemala-shore-excursion.html" data-nav="antigua" class="text-gray-600 hover:text-ocean-600 transition-colors">Antigua</a>
        <a href="pacaya-volcano-shore-excursion.html" data-nav="volcano" class="text-gray-600 hover:text-ocean-600 transition-colors">Pacaya Volcano</a>
        <a href="guatemala-highlights-tour.html" data-nav="highlights" class="text-gray-600 hover:text-ocean-600 transition-colors">Highlights</a>
        <a href="puerto-quetzal-cruise-port-guide.html" data-nav="port" class="text-gray-600 hover:text-ocean-600 transition-colors">Port Guide</a>
      </div>
      <a href="best-puerto-quetzal-shore-excursions.html" class="hidden md:inline-flex items-center gap-2 btn-ocean text-white text-sm font-semibold px-4 py-2 rounded-full shadow-md">
        View Puerto Quetzal Excursions
      </a>
      <button type="button" class="lg:hidden p-2 rounded-lg text-gray-600 hover:bg-sand-50" aria-label="Open menu">
        <svg class="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"/></svg>
      </button>
    </div>
  </div>
</nav>''')

(ROOT / "partials/footer.html").write_text('''<footer class="bg-gray-900 text-gray-400 py-14">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="grid sm:grid-cols-2 lg:grid-cols-4 gap-10 mb-12">
      <div class="sm:col-span-2 lg:col-span-1">
        <a href="index.html" class="font-display font-semibold text-white text-lg">Puerto Quetzal Shore Excursion</a>
        <p class="mt-3 text-sm leading-relaxed">Planning guide for cruise visitors to Puerto Quetzal, Guatemala — gateway to Antigua, volcanoes and highland culture. Not affiliated with any cruise line.</p>
        <p class="mt-2 text-sm"><a href="https://puertoquetzalshoreexcursion.com" class="hover:text-white transition-colors">puertoquetzalshoreexcursion.com</a></p>
      </div>
      <div>
        <h3 class="text-white text-sm font-semibold uppercase tracking-wider mb-4">Excursions</h3>
        <ul class="space-y-2 text-sm">
          <li><a href="antigua-guatemala-shore-excursion.html" class="hover:text-white transition-colors">Antigua Guatemala</a></li>
          <li><a href="antigua-and-jade-factory-tour.html" class="hover:text-white transition-colors">Antigua &amp; Jade Factory</a></li>
          <li><a href="antigua-and-coffee-plantation-tour.html" class="hover:text-white transition-colors">Coffee Plantation Tour</a></li>
          <li><a href="pacaya-volcano-shore-excursion.html" class="hover:text-white transition-colors">Pacaya Volcano</a></li>
          <li><a href="guatemala-highlights-tour.html" class="hover:text-white transition-colors">Guatemala Highlights</a></li>
        </ul>
      </div>
      <div>
        <h3 class="text-white text-sm font-semibold uppercase tracking-wider mb-4">Guides</h3>
        <ul class="space-y-2 text-sm">
          <li><a href="best-puerto-quetzal-shore-excursions.html" class="hover:text-white transition-colors">Best Excursions</a></li>
          <li><a href="puerto-quetzal-cruise-port-guide.html" class="hover:text-white transition-colors">Port Guide</a></li>
          <li><a href="one-day-in-puerto-quetzal-from-a-cruise-ship.html" class="hover:text-white transition-colors">One Day in Puerto Quetzal</a></li>
          <li><a href="is-puerto-quetzal-worth-visiting.html" class="hover:text-white transition-colors">Is Puerto Quetzal Worth Visiting?</a></li>
          <li><a href="antigua-vs-pacaya-volcano-excursion.html" class="hover:text-white transition-colors">Antigua vs Pacaya Volcano</a></li>
        </ul>
      </div>
    </div>
    <div class="border-t border-gray-800 pt-8 text-xs text-center sm:text-left">
      <p>&copy; 2026 Puerto Quetzal Shore Excursion · puertoquetzalshoreexcursion.com. Verify times and availability with operators before booking.</p>
    </div>
  </div>
</footer>''')

(ROOT / "partials/trust-strip.html").write_text('''<section class="trust-strip" aria-label="Puerto Quetzal shore excursion highlights">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <ul class="trust-strip__list">
      <li class="trust-strip__item"><span class="trust-strip__check" aria-hidden="true">✔</span> Antigua Guatemala</li>
      <li class="trust-strip__item"><span class="trust-strip__check" aria-hidden="true">✔</span> Colonial Architecture</li>
      <li class="trust-strip__item"><span class="trust-strip__check" aria-hidden="true">✔</span> Volcanoes &amp; Coffee</li>
      <li class="trust-strip__item"><span class="trust-strip__check" aria-hidden="true">✔</span> Cruise-Friendly Returns</li>
    </ul>
  </div>
</section>''')

print("Partials written")

LINKS_DEFAULT = [
    ("puerto-quetzal-cruise-port-guide.html", "Port Guide"),
    ("best-puerto-quetzal-shore-excursions.html", "Best Excursions"),
    ("one-day-in-puerto-quetzal-from-a-cruise-ship.html", "One Day Itinerary"),
    ("antigua-guatemala-shore-excursion.html", "Antigua Guatemala"),
    ("pacaya-volcano-shore-excursion.html", "Pacaya Volcano"),
    ("antigua-vs-pacaya-volcano-excursion.html", "Antigua vs Volcano"),
]

HOME_FAQ = [
    ("How long do cruise ships stay in Puerto Quetzal?", "Most Puerto Quetzal port calls run 8 to 10 hours — enough for an Antigua day trip or volcano excursion with return buffer before all aboard, depending on your ship's schedule."),
    ("What is the best shore excursion from Puerto Quetzal?", "Antigua Guatemala tours are the most popular for colonial history and UNESCO heritage. Pacaya Volcano suits adventure seekers; coffee plantation and jade factory combos add cultural depth. Match the tour to your interests and confirm timings."),
    ("How far is Antigua from Puerto Quetzal cruise port?", "Antigua is inland in the highlands. Drive time is typically around 1.5 to 2 hours each way depending on traffic and route — confirm with your operator and ship schedule before booking."),
    ("Is Puerto Quetzal a beach port?", "No. Puerto Quetzal is primarily a gateway to Antigua Guatemala, volcanoes, coffee plantations and Guatemalan highland culture — not a typical Caribbean-style beach destination."),
    ("Ship excursion or book independently in Puerto Quetzal?", "Ship tours guarantee the vessel waits if the operator is late. Reputable local operators plan returns with buffer — always confirm policies and your all-aboard time before booking ashore."),
]

# --- Heroes ---
(ROOT / "partials/hero-home.html").write_text(hero(
    "partials/hero-home.html", eyebrow="Puerto Quetzal · Guatemala", image="hero-puerto-quetzal.png",
    aria="Colonial streets and Santa Catalina Arch in Antigua Guatemala with volcano backdrop — Puerto Quetzal shore excursion destination",
    title_html='Puerto Quetzal Shore<br/><span class="text-gt-300">Excursions</span><br/>from the Cruise Port',
    lead="Puerto Quetzal is the cruise gateway to Antigua Guatemala, volcanoes, coffee plantations, colonial architecture and Guatemalan culture — not a beach-only Caribbean stop.",
    actions='''<a href="best-puerto-quetzal-shore-excursions.html" class="btn-primary inline-flex items-center justify-center gap-2 text-white font-semibold px-7 py-3 rounded-full text-sm shadow-xl">View Puerto Quetzal Excursions</a>
          <a href="puerto-quetzal-cruise-port-guide.html" class="btn-outline inline-flex items-center justify-center gap-2 text-white font-semibold px-7 py-3 rounded-full text-sm">Plan Your Port Day</a>''',
    tags='''<span class="inline-flex items-center bg-white/10 border border-white/25 rounded-full px-3.5 py-1.5 text-xs font-semibold text-white">Antigua Guatemala</span>
          <span class="inline-flex items-center bg-white/10 border border-white/25 rounded-full px-3.5 py-1.5 text-xs font-semibold text-white">Colonial Architecture</span>
          <span class="inline-flex items-center bg-white/10 border border-white/25 rounded-full px-3.5 py-1.5 text-xs font-semibold text-white">Volcanoes &amp; Coffee</span>
          <span class="inline-flex items-center bg-white/10 border border-white/25 rounded-full px-3.5 py-1.5 text-xs font-semibold text-white">UNESCO Heritage</span>
          <span class="inline-flex items-center bg-white/10 border border-white/25 rounded-full px-3.5 py-1.5 text-xs font-semibold text-white">Cruise Passengers</span>'''
))

HERO_PAGES = [
    ("hero-best-excursions.html", "Best Excursions", "Guatemala Culture", "best-puerto-quetzal-excursions.png",
     "Comparison of top Puerto Quetzal cruise shore excursions including Antigua, Pacaya Volcano and coffee tours",
     "Best Puerto Quetzal<br/><span class=\"text-gt-300\">Shore Excursions</span>",
     "Compare Antigua Guatemala, Pacaya Volcano, coffee plantations, jade factory tours and Guatemala highlights timed for typical Puerto Quetzal port calls."),
    ("hero-port-guide.html", "Port Guide", "Puerto Quetzal Terminal", "puerto-quetzal-port.png",
     "Puerto Quetzal Guatemala cruise port terminal for passenger shore excursions to Antigua and highlands",
     "Puerto Quetzal Cruise<br/><span class=\"text-gt-300\">Port Guide</span>",
     "Where ships dock, distance to Antigua, excursion timing, currency, safety and return-to-ship advice for first-time visitors."),
    ("hero-one-day.html", "One Day Itinerary", "Cruise Port Day", "one-day-puerto-quetzal.png",
     "Antigua Guatemala colonial streets and cultural highlights for cruise passengers planning one day from Puerto Quetzal",
     "One Day in Puerto Quetzal<br/><span class=\"text-gt-300\">from a Cruise Ship</span>",
     "Sample itineraries for Antigua sightseeing, cultural lunch, colonial highlights and return-to-ship timing."),
    ("hero-antigua.html", "Antigua Guatemala", "UNESCO Heritage", "santa-catalina-arch.png",
     "Santa Catalina Arch and colonial streets in Antigua Guatemala UNESCO World Heritage city on Puerto Quetzal shore excursion",
     "Antigua Guatemala<br/><span class=\"text-gt-300\">Shore Excursion</span>",
     "Colonial streets, churches, markets and the iconic Santa Catalina Arch framed by volcano views — Puerto Quetzal's most popular excursion."),
    ("hero-jade.html", "Jade Factory", "Cultural Experience", "jade-factory.png",
     "Jade craftsmanship and Antigua Guatemala colonial highlights on shore excursion from Puerto Quetzal cruise port",
     "Antigua &amp; Jade Factory<br/><span class=\"text-gt-300\">Tour</span>",
     "Discover Mayan jade traditions, Guatemalan history and Antigua's colonial landmarks on a culture-focused port day."),
    ("hero-coffee.html", "Coffee Plantation", "Highland Culture", "coffee-plantation.png",
     "Coffee plantation and Antigua Guatemala colonial architecture on shore excursion from Puerto Quetzal cruise port",
     "Antigua &amp; Coffee<br/><span class=\"text-gt-300\">Plantation Tour</span>",
     "Visit working coffee farms, learn production from bean to cup and explore Antigua's UNESCO-listed streets."),
    ("hero-volcano.html", "Pacaya Volcano", "Adventure", "pacaya-volcano.png",
     "Pacaya Volcano hiking and volcanic landscape on adventure shore excursion from Puerto Quetzal Guatemala cruise port",
     "Pacaya Volcano<br/><span class=\"text-gt-300\">Shore Excursion</span>",
     "Active volcano views, hiking options and geological features — Guatemala's top adventure excursion from the cruise port."),
    ("hero-highlights.html", "Guatemala Highlights", "First-Time Visitors", "guatemala-highlights.png",
     "Guatemala highlights tour with Antigua colonial architecture and scenic viewpoints from Puerto Quetzal cruise port",
     "Guatemala Highlights<br/><span class=\"text-gt-300\">Tour</span>",
     "Overview of the region for first-time visitors — Antigua highlights, culture, history and scenic viewpoints in one port day."),
    ("hero-worth-visiting.html", "Worth Visiting?", "Cruise Planning", "puerto-quetzal-intro.png",
     "Antigua Guatemala colonial city and Guatemalan culture for cruise passengers evaluating Puerto Quetzal port calls",
     "Is Puerto Quetzal<br/><span class=\"text-gt-300\">Worth Visiting?</span>",
     "Honest guide for cruise passengers deciding whether Puerto Quetzal delivers enough culture and history for your port day."),
    ("hero-vs-volcano.html", "Antigua vs Pacaya", "Excursion Comparison", "volcano-backdrop.png",
     "Antigua Guatemala colonial history compared with Pacaya Volcano adventure excursions from Puerto Quetzal cruise port",
     "Antigua vs Pacaya Volcano<br/><span class=\"text-gt-300\">Excursion</span>",
     "Compare history versus adventure, walking requirements, photography and cruise suitability for your Puerto Quetzal port day."),
]

for hf, crumb, eyebrow, img, aria, title, lead in HERO_PAGES:
    (ROOT / f"partials/{hf}").write_text(hero(
        f"partials/{hf}", breadcrumb=crumb, eyebrow=eyebrow, image=img, aria=aria,
        title_html=title, lead=lead))

print("Heroes written")

# --- Home content ---
(ROOT / "content/home.html").write_text('''<section class="pt-8 pb-8 bg-white"><div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
  <div class="text-center mb-10">
    <div class="section-label mx-auto">Best Excursions</div>
    <h2 class="text-3xl sm:text-4xl font-display font-bold text-gray-900 mb-4">Best Puerto Quetzal Cruise Excursions</h2>
    <p class="text-gray-600 text-sm max-w-2xl mx-auto">Ranked for cruise schedules — Antigua Guatemala, Pacaya Volcano, coffee plantations, jade factory tours and Guatemala highlights from Guatemala&apos;s Pacific cruise gateway.</p>
  </div>
  <div class="grid sm:grid-cols-2 lg:grid-cols-4 gap-6">
    <div class="card-hover bg-white rounded-3xl overflow-hidden shadow-md border border-gt-50 flex flex-col">
      <div class="card-media h-44"><img src="images/santa-catalina-arch.png" alt="Santa Catalina Arch and colonial streets in Antigua Guatemala on shore excursion from Puerto Quetzal cruise port" width="600" height="352" loading="lazy" decoding="async" /></div>
      <div class="p-6 flex flex-col flex-1"><h3 class="text-lg font-display font-semibold text-gray-900 mb-2">Antigua Guatemala</h3><p class="text-sm text-gray-500 flex-1">UNESCO colonial city — Puerto Quetzal&apos;s signature cultural excursion.</p>
      <a href="antigua-guatemala-shore-excursion.html" class="mt-5 btn-ocean inline-flex items-center justify-center text-white text-xs font-semibold px-5 py-2.5 rounded-full">Antigua Tour</a></div>
    </div>
    <div class="card-hover bg-white rounded-3xl overflow-hidden shadow-md border border-gt-50 flex flex-col">
      <div class="card-media h-44"><img src="images/pacaya-volcano.png" alt="Pacaya Volcano volcanic landscape on adventure shore excursion from Puerto Quetzal Guatemala cruise port" width="600" height="352" loading="lazy" decoding="async" /></div>
      <div class="p-6 flex flex-col flex-1"><h3 class="text-lg font-display font-semibold text-gray-900 mb-2">Pacaya Volcano</h3><p class="text-sm text-gray-500 flex-1">Active volcano hiking and dramatic highland scenery.</p>
      <a href="pacaya-volcano-shore-excursion.html" class="mt-5 btn-ocean inline-flex items-center justify-center text-white text-xs font-semibold px-5 py-2.5 rounded-full">Volcano Tour</a></div>
    </div>
    <div class="card-hover bg-white rounded-3xl overflow-hidden shadow-md border border-gt-50 flex flex-col">
      <div class="card-media h-44"><img src="images/coffee-plantation.png" alt="Guatemalan coffee plantation visit on shore excursion from Puerto Quetzal cruise port" width="600" height="352" loading="lazy" decoding="async" /></div>
      <div class="p-6 flex flex-col flex-1"><h3 class="text-lg font-display font-semibold text-gray-900 mb-2">Coffee Plantation</h3><p class="text-sm text-gray-500 flex-1">Highland farms, bean-to-cup culture and Antigua sightseeing.</p>
      <a href="antigua-and-coffee-plantation-tour.html" class="mt-5 btn-ocean inline-flex items-center justify-center text-white text-xs font-semibold px-5 py-2.5 rounded-full">Coffee Tour</a></div>
    </div>
    <div class="card-hover bg-white rounded-3xl overflow-hidden shadow-md border border-gt-50 flex flex-col">
      <div class="card-media h-44"><img src="images/jade-factory.png" alt="Jade factory craftsmanship and Antigua highlights on cultural shore excursion from Puerto Quetzal" width="600" height="352" loading="lazy" decoding="async" /></div>
      <div class="p-6 flex flex-col flex-1"><h3 class="text-lg font-display font-semibold text-gray-900 mb-2">Antigua &amp; Jade Factory</h3><p class="text-sm text-gray-500 flex-1">Mayan jade traditions plus colonial Antigua landmarks.</p>
      <a href="antigua-and-jade-factory-tour.html" class="mt-5 btn-ocean inline-flex items-center justify-center text-white text-xs font-semibold px-5 py-2.5 rounded-full">Jade Tour</a></div>
    </div>
  </div>
  <p class="text-center mt-8"><a href="best-puerto-quetzal-shore-excursions.html" class="text-ocean-600 font-semibold text-sm">See full comparison →</a></p>
</div></section>
<section class="pt-4 pb-8 bg-white"><div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8"><div class="grid lg:grid-cols-2 gap-12 items-center">
  <div>
    <div class="inline-flex items-center gap-2 text-ocean-600 text-xs font-semibold tracking-widest uppercase mb-3"><div class="w-8 h-px bg-ocean-400"></div>Puerto Quetzal Cruise Port</div>
    <h2 class="text-3xl sm:text-4xl font-display font-bold text-gray-900 mb-5">Why Cruise Passengers<br/><span class="text-ocean-600">Choose Antigua</span></h2>
    <p class="text-gray-600 leading-relaxed mb-5">Most cruise passengers who dock at Puerto Quetzal head inland to <strong>Antigua Guatemala</strong> — and for good reason. This UNESCO World Heritage city delivers <strong>colonial streets</strong>, <strong>ornate churches</strong>, <strong>colourful markets</strong> and the iconic <strong>Santa Catalina Arch</strong> framed by <strong>volcano views</strong>. It is a culture and history destination, not a beach day. Port calls typically run <strong>8–10 hours</strong>, enough for a full Antigua excursion with return buffer when you confirm timings with your operator.</p>
    <a href="antigua-guatemala-shore-excursion.html" class="btn-ocean inline-flex items-center justify-center gap-2 text-white font-semibold px-7 py-3.5 rounded-full text-sm shadow-lg">Explore Antigua Guatemala</a>
  </div>
  <div class="info-image rounded-3xl aspect-[4/3] shadow-2xl overflow-hidden">
    <img src="images/colonial-antigua.png" alt="Colonial architecture and cobblestone streets in Antigua Guatemala on Puerto Quetzal shore excursion" width="800" height="600" loading="lazy" decoding="async" />
  </div>
</div></div></section>
<section class="py-16 bg-gt-50"><div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
  <div class="text-center mb-12"><h2 class="text-3xl font-display font-bold text-gray-900">Featured Excursions</h2>
  <p class="text-gray-600 text-sm mt-3 max-w-xl mx-auto">Most-booked Puerto Quetzal shore excursions for cruise passengers.</p></div>
  <div class="grid sm:grid-cols-2 lg:grid-cols-4 gap-6">
    <div class="card-hover bg-white rounded-3xl overflow-hidden shadow-md border border-gt-50 flex flex-col">
      <div class="card-media h-44"><img src="images/guatemala-highlights.png" alt="Guatemala highlights tour with Antigua colonial architecture from Puerto Quetzal cruise port" width="600" height="352" loading="lazy" decoding="async" /></div>
      <div class="p-6 flex flex-col flex-1"><h3 class="text-lg font-display font-semibold text-gray-900 mb-2">Guatemala Highlights</h3><p class="text-sm text-gray-500 flex-1">Best overview for first-time visitors to the region.</p>
      <a href="guatemala-highlights-tour.html" class="mt-5 btn-ocean inline-flex items-center justify-center text-white text-xs font-semibold px-5 py-2.5 rounded-full">Highlights Tour</a></div>
    </div>
    <div class="card-hover bg-white rounded-3xl overflow-hidden shadow-md border border-gt-50 flex flex-col">
      <div class="card-media h-44"><img src="images/antigua-guatemala.png" alt="Antigua Guatemala UNESCO colonial city on most popular shore excursion from Puerto Quetzal" width="600" height="352" loading="lazy" decoding="async" /></div>
      <div class="p-6 flex flex-col flex-1"><h3 class="text-lg font-display font-semibold text-gray-900 mb-2">Colonial Antigua</h3><p class="text-sm text-gray-500 flex-1">Cobblestone plazas, church ruins and photography stops.</p>
      <a href="antigua-guatemala-shore-excursion.html" class="mt-5 btn-ocean inline-flex items-center justify-center text-white text-xs font-semibold px-5 py-2.5 rounded-full">Antigua</a></div>
    </div>
    <div class="card-hover bg-white rounded-3xl overflow-hidden shadow-md border border-gt-50 flex flex-col">
      <div class="card-media h-44"><img src="images/volcano-backdrop.png" alt="Volcano backdrop over Antigua Guatemala colonial city on Puerto Quetzal shore excursion" width="600" height="352" loading="lazy" decoding="async" /></div>
      <div class="p-6 flex flex-col flex-1"><h3 class="text-lg font-display font-semibold text-gray-900 mb-2">Volcano &amp; Highlands</h3><p class="text-sm text-gray-500 flex-1">Pacaya Volcano adventure or scenic highland viewpoints.</p>
      <a href="pacaya-volcano-shore-excursion.html" class="mt-5 btn-ocean inline-flex items-center justify-center text-white text-xs font-semibold px-5 py-2.5 rounded-full">Volcano</a></div>
    </div>
    <div class="card-hover bg-white rounded-3xl overflow-hidden shadow-md border border-gt-50 flex flex-col">
      <div class="card-media h-44"><img src="images/antigua-market.png" alt="Local market and Guatemalan culture in Antigua on shore excursion from Puerto Quetzal cruise port" width="600" height="352" loading="lazy" decoding="async" /></div>
      <div class="p-6 flex flex-col flex-1"><h3 class="text-lg font-display font-semibold text-gray-900 mb-2">Culture &amp; Markets</h3><p class="text-sm text-gray-500 flex-1">Jade, textiles, coffee and artisan traditions.</p>
      <a href="antigua-and-jade-factory-tour.html" class="mt-5 btn-ocean inline-flex items-center justify-center text-white text-xs font-semibold px-5 py-2.5 rounded-full">Cultural Tour</a></div>
    </div>
  </div>
</div></section>''' + f'''
<section class="pb-8 bg-white"><div class="max-w-7xl mx-auto px-4">{snapshot({
    "Typical Time In Port": "8–10 hours (typical)",
    "Best For": "Antigua, volcanoes, coffee &amp; Guatemalan culture",
    "Walking Required": "Varies — see comparison",
    "Cultural Interest Rating": "Very high on Antigua tours",
    "Return To Ship Friendly": "Operators usually allow 60–90 min buffer",
    "Popular Excursion Types": "Antigua, Pacaya, coffee, jade, highlights",
})}</div></section>''' + '''
<section class="py-16 bg-sand-50"><div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
  <h2 class="text-3xl font-display font-bold text-gray-900 text-center mb-10">Top Things To Do From Puerto Quetzal</h2>
  <div class="grid sm:grid-cols-2 lg:grid-cols-3 gap-6 text-sm">
    <div class="bg-white rounded-3xl p-6 border border-gt-100"><h3 class="font-display font-bold text-lg mb-2">Antigua Guatemala</h3><p class="text-gray-600">UNESCO colonial capital with cobblestone streets, church ruins and the Santa Catalina Arch against volcano backdrops.</p></div>
    <div class="bg-white rounded-3xl p-6 border border-gt-100"><h3 class="font-display font-bold text-lg mb-2">Pacaya Volcano</h3><p class="text-gray-600">Active volcano excursion with hiking options and geological features — confirm fitness level and access with your operator.</p></div>
    <div class="bg-white rounded-3xl p-6 border border-gt-100"><h3 class="font-display font-bold text-lg mb-2">Coffee Plantations</h3><p class="text-gray-600">Highland farm visits explaining Guatemalan coffee production from bean to cup, often paired with Antigua sightseeing.</p></div>
    <div class="bg-white rounded-3xl p-6 border border-gt-100"><h3 class="font-display font-bold text-lg mb-2">Jade Factory Tours</h3><p class="text-gray-600">Learn Mayan jade craftsmanship, Guatemalan history and shop for authentic pieces with local expert guidance.</p></div>
    <div class="bg-white rounded-3xl p-6 border border-gt-100"><h3 class="font-display font-bold text-lg mb-2">Colonial Churches</h3><p class="text-gray-600">Earthquake-scarred ruins and restored facades tell the story of Spanish colonial Guatemala across Antigua&apos;s plazas.</p></div>
    <div class="bg-white rounded-3xl p-6 border border-gt-100"><h3 class="font-display font-bold text-lg mb-2">Local Markets</h3><p class="text-gray-600">Textiles, handicrafts and regional flavours at Antigua&apos;s markets — strong cultural immersion for cruise passengers.</p></div>
  </div>
</div></section>
<section class="py-16 bg-white"><div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8"><div class="grid lg:grid-cols-2 gap-12 items-center">
  <div class="card-media rounded-3xl overflow-hidden aspect-[4/3] shadow-lg">
    <img src="images/santa-catalina-arch.png" alt="Santa Catalina Arch with volcano backdrop in Antigua Guatemala on Puerto Quetzal shore excursion" width="600" height="450" loading="lazy" decoding="async" />
  </div>
  <div>
    <h2 class="text-3xl font-display font-bold text-gray-900 mb-4">Antigua From the Cruise Port</h2>
    <p class="text-gray-600 leading-relaxed mb-4">Puerto Quetzal&apos;s real advantage is straightforward access to <a href="antigua-guatemala-shore-excursion.html" class="text-ocean-600 font-medium">Antigua Guatemala</a> — one of Central America&apos;s finest colonial cities. Guided tours handle the inland drive, walking routes and return timing so you can focus on plazas, photography and UNESCO heritage rather than logistics.</p>
    <p class="text-gray-600 leading-relaxed mb-5">Drive times vary with traffic. Reputable operators plan returns with buffer before all aboard — always confirm your ship schedule and excursion end time the morning you dock.</p>
    <a href="puerto-quetzal-cruise-port-guide.html" class="text-ocean-600 font-semibold text-sm">Read the port guide →</a>
  </div>
</div></div></section>
<section class="py-16 bg-sand-50"><div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8"><div class="grid lg:grid-cols-2 gap-12 items-center">
  <div>
    <h2 class="text-3xl font-display font-bold text-gray-900 mb-4">Volcanoes, Coffee &amp; Highland Culture</h2>
    <p class="text-gray-600 leading-relaxed mb-4">Beyond Antigua&apos;s streets, <a href="pacaya-volcano-shore-excursion.html" class="text-ocean-600 font-medium">Pacaya Volcano</a> excursions suit travelers who want adventure and geological drama. <a href="antigua-and-coffee-plantation-tour.html" class="text-ocean-600 font-medium">Coffee plantation tours</a> pair farm visits with colonial sightseeing for a rounded Guatemalan port day.</p>
    <p class="text-gray-600 leading-relaxed mb-5">Volcano hiking requires reasonable fitness and appropriate footwear. Access and trail conditions change — confirm with your operator rather than assuming fixed routes or lava viewing.</p>
    <a href="antigua-vs-pacaya-volcano-excursion.html" class="text-ocean-600 font-semibold text-sm">Compare Antigua vs Pacaya →</a>
  </div>
  <div class="card-media rounded-3xl overflow-hidden aspect-[4/3] shadow-lg">
    <img src="images/pacaya-volcano.png" alt="Pacaya Volcano volcanic scenery on adventure shore excursion from Puerto Quetzal Guatemala cruise port" width="600" height="450" loading="lazy" decoding="async" />
  </div>
</div></div></section>
<section class="py-16 bg-sand-50"><div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
  <h2 class="text-3xl sm:text-4xl font-display font-bold text-gray-900 text-center mb-4">Which Puerto Quetzal Excursion Is Right for Me?</h2>
  <p class="text-center text-gray-600 text-sm max-w-2xl mx-auto mb-10">Match your port day to history, culture, adventure or coffee — timed for typical 8–10 hour Puerto Quetzal cruise calls in Guatemala.</p>
  <div class="overflow-x-auto rounded-3xl border border-gt-100 shadow-sm">
    <table class="w-full text-sm text-left min-w-[720px]">
      <thead class="bg-ocean-800 text-white"><tr>
        <th class="py-4 px-4 font-semibold rounded-tl-3xl">Excursion</th>
        <th class="py-4 px-3 font-semibold">Duration</th>
        <th class="py-4 px-3 font-semibold">Best For</th>
        <th class="py-4 px-3 font-semibold">Cultural Rating</th>
        <th class="py-4 px-4 font-semibold rounded-tr-3xl">Details</th>
      </tr></thead>
      <tbody class="bg-white">
        <tr class="border-b border-gt-50 hover:bg-sand-50/80"><td class="py-4 pr-4 font-semibold"><a href="antigua-guatemala-shore-excursion.html" class="text-ocean-600">Antigua Guatemala</a></td><td class="py-4 px-3 text-gray-600">6–7 hrs</td><td class="py-4 px-3 text-gray-600">History &amp; photography</td><td class="py-4 px-3 text-gray-600">Very high</td><td class="py-4 pl-3"><a href="antigua-guatemala-shore-excursion.html" class="text-gt-600 font-medium text-xs">Guide →</a></td></tr>
        <tr class="border-b border-gt-50 hover:bg-sand-50/80"><td class="py-4 pr-4 font-semibold"><a href="pacaya-volcano-shore-excursion.html" class="text-ocean-600">Pacaya Volcano</a></td><td class="py-4 px-3 text-gray-600">6–7 hrs</td><td class="py-4 px-3 text-gray-600">Adventure seekers</td><td class="py-4 px-3 text-gray-600">Moderate</td><td class="py-4 pl-3"><a href="pacaya-volcano-shore-excursion.html" class="text-gt-600 font-medium text-xs">Guide →</a></td></tr>
        <tr class="border-b border-gt-50 hover:bg-sand-50/80"><td class="py-4 pr-4 font-semibold"><a href="antigua-and-coffee-plantation-tour.html" class="text-ocean-600">Coffee Plantation</a></td><td class="py-4 px-3 text-gray-600">6–7 hrs</td><td class="py-4 px-3 text-gray-600">Coffee lovers</td><td class="py-4 px-3 text-gray-600">High</td><td class="py-4 pl-3"><a href="antigua-and-coffee-plantation-tour.html" class="text-gt-600 font-medium text-xs">Guide →</a></td></tr>
        <tr class="border-b border-gt-50 hover:bg-sand-50/80"><td class="py-4 pr-4 font-semibold"><a href="antigua-and-jade-factory-tour.html" class="text-ocean-600">Antigua &amp; Jade</a></td><td class="py-4 px-3 text-gray-600">6–7 hrs</td><td class="py-4 px-3 text-gray-600">Culture &amp; shopping</td><td class="py-4 px-3 text-gray-600">Very high</td><td class="py-4 pl-3"><a href="antigua-and-jade-factory-tour.html" class="text-gt-600 font-medium text-xs">Guide →</a></td></tr>
        <tr class="border-b border-gt-50 hover:bg-sand-50/80"><td class="py-4 pr-4 font-semibold"><a href="guatemala-highlights-tour.html" class="text-ocean-600">Guatemala Highlights</a></td><td class="py-4 px-3 text-gray-600">6–7 hrs</td><td class="py-4 px-3 text-gray-600">First-time visitors</td><td class="py-4 px-3 text-gray-600">High</td><td class="py-4 pl-3"><a href="guatemala-highlights-tour.html" class="text-gt-600 font-medium text-xs">Guide →</a></td></tr>
      </tbody>
    </table>
  </div>
</div></section>''' + faq_section("Puerto Quetzal Shore Excursions FAQ", HOME_FAQ) + cta_section())

print("Home content written")

# --- Tour pages ---
(ROOT / "content/antigua-guatemala-shore-excursion.html").write_text(tour_content(
    "Antigua Guatemala", "Most Popular", "popular-badge",
    "Antigua Guatemala shore excursions are the headline Puerto Quetzal experience — a UNESCO World Heritage city of cobblestone streets, colonial churches, vibrant markets and the iconic Santa Catalina Arch with Agua Volcano rising behind. Local guides walk you through plazas and ruins while operators coordinate inland transport and return times with your ship's all-aboard schedule.",
    "santa-catalina-arch.png",
    "Santa Catalina Arch with volcano backdrop in Antigua Guatemala UNESCO city on shore excursion from Puerto Quetzal cruise port",
    [("santa-catalina-arch.png", "Santa Catalina Arch framed by volcanoes in Antigua Guatemala on Puerto Quetzal shore excursion", "Santa Catalina Arch", "Antigua's most photographed landmark — colonial passageway with dramatic volcano views."),
     ("colonial-antigua.png", "Colonial cobblestone streets and colourful facades in Antigua Guatemala on shore excursion from Puerto Quetzal", "Colonial Streets", "Walk centuries-old cobblestone lanes lined with pastel facades and courtyard gardens."),
     ("colonial-church.png", "Colonial church ruins and heritage architecture in Antigua Guatemala on Puerto Quetzal cruise excursion", "Churches &amp; Ruins", "Earthquake-scarred church ruins and restored sanctuaries tell Guatemala's colonial story."),
     ("antigua-market.png", "Local market and artisan crafts in Antigua Guatemala on cultural shore excursion from Puerto Quetzal", "Markets &amp; Crafts", "Textiles, handicrafts and regional flavours at Antigua's markets."),
     ("volcano-backdrop.png", "Volcano backdrop over Antigua Guatemala colonial city for photography on Puerto Quetzal shore excursion", "Photography Stops", "Volcano-framed plazas and archways offer standout photo opportunities throughout the city.")],
    {"Best For": "History, culture &amp; photography", "Duration": "6–7 hours typical", "Walking Required": "Moderate — cobblestone streets", "Cultural Interest Rating": "Very high", "Adventure Level": "Low to moderate", "Return To Ship Confidence": "High with reputable operators", "Family Friendly": "Good — manageable walking pace"},
    LINKS_DEFAULT))

(ROOT / "content/antigua-and-jade-factory-tour.html").write_text(tour_content(
    "Antigua & Jade Factory", "Best Cultural Experience", "culture-badge",
    "The Antigua and jade factory tour pairs UNESCO colonial sightseeing with Guatemala's ancient jade tradition. Learn how Mayan craftsmen shaped jade for centuries, explore a working factory or showroom, and walk Antigua's historic streets with a local guide. Shopping opportunities are part of the experience — confirm inclusions and timing with your operator before booking.",
    "jade-factory.png",
    "Jade craftsmanship demonstration and Antigua colonial highlights on cultural shore excursion from Puerto Quetzal Guatemala",
    [("jade-factory.png", "Jade carving and Mayan craftsmanship at factory visit on Puerto Quetzal shore excursion", "Jade Craftsmanship", "See how raw jade becomes jewellery and art with expert demonstrations."),
     ("colonial-antigua.png", "Colonial Antigua streets visited on jade factory and cultural tour from Puerto Quetzal cruise port", "Antigua Highlights", "Colonial plazas and landmarks woven into the factory visit itinerary."),
     ("antigua-guatemala.png", "Guatemalan history and cultural heritage on jade factory shore excursion from Puerto Quetzal", "Guatemalan History", "Guides connect jade traditions to Mayan and colonial-era heritage."),
     ("antigua-market.png", "Shopping for jade and artisan crafts in Antigua on shore excursion from Puerto Quetzal", "Shopping Opportunities", "Authentic jade pieces and local crafts — buy from reputable sources.")],
    {"Best For": "Culture, history &amp; artisan shopping", "Duration": "6–7 hours typical", "Walking Required": "Moderate — city streets and factory visit", "Cultural Interest Rating": "Very high", "Adventure Level": "Low", "Return To Ship Confidence": "High with cruise-timed departures", "Family Friendly": "Good for curious learners"},
    LINKS_DEFAULT))

(ROOT / "content/antigua-and-coffee-plantation-tour.html").write_text(tour_content(
    "Coffee Plantation", "Best for Coffee Lovers", "coffee-badge",
    "Coffee plantation tours from Puerto Quetzal combine highland farm visits with Antigua sightseeing. Walk through working plantations, learn how Guatemalan arabica is grown and processed, taste fresh brews, and explore Antigua's colonial streets — a port day built around Guatemala's most famous export and its UNESCO heritage city.",
    "coffee-plantation.png",
    "Guatemalan coffee plantation with Antigua colonial architecture on shore excursion from Puerto Quetzal cruise port",
    [("coffee-plantation.png", "Coffee cherries and plantation rows on highland farm tour from Puerto Quetzal shore excursion", "Coffee Production", "From cherry picking to roasting — see the full bean-to-cup process."),
     ("coffee-plantation.png", "Plantation visit with local culture on coffee and Antigua tour from Puerto Quetzal Guatemala", "Plantation Visits", "Working farms in the highlands surrounding Antigua — conditions vary by season."),
     ("colonial-antigua.png", "Antigua colonial sightseeing paired with coffee plantation on Puerto Quetzal shore excursion", "Antigua Sightseeing", "Colonial plazas and landmarks included on most combined itineraries."),
     ("antigua-market.png", "Local culture and regional flavours on coffee plantation shore excursion from Puerto Quetzal", "Local Culture", "Meet farmers and learn how coffee shapes highland communities.")],
    {"Best For": "Coffee enthusiasts &amp; culture seekers", "Duration": "6–7 hours typical", "Walking Required": "Easy to moderate — farm paths and city streets", "Cultural Interest Rating": "High", "Adventure Level": "Low", "Return To Ship Confidence": "High with planned buffer", "Family Friendly": "Good — educational for all ages"},
    LINKS_DEFAULT))

(ROOT / "content/pacaya-volcano-shore-excursion.html").write_text(tour_content(
    "Pacaya Volcano", "Best Adventure", "adventure-badge",
    "Pacaya Volcano shore excursions deliver Guatemala's most adventurous port day from Puerto Quetzal. Hike volcanic slopes for dramatic views, observe geological features and experience an active volcano environment with local guides. Fitness requirements vary by route — confirm hiking distance, elevation and current access restrictions with your operator. Do not assume lava flows or specific viewpoints without verification.",
    "pacaya-volcano.png",
    "Pacaya Volcano hiking trail and volcanic landscape on adventure shore excursion from Puerto Quetzal Guatemala cruise port",
    [("pacaya-volcano.png", "Pacaya Volcano summit views on hiking shore excursion from Puerto Quetzal cruise port", "Volcano Views", "Panoramic highland and volcanic scenery — visibility depends on weather."),
     ("pacaya-volcano.png", "Hiking options on Pacaya Volcano adventure excursion from Puerto Quetzal Guatemala", "Hiking Options", "Routes range from moderate walks to steeper climbs — match fitness to itinerary."),
     ("volcano-backdrop.png", "Geological features and volcanic terrain on Pacaya shore excursion from Puerto Quetzal", "Geological Features", "Guides explain Pacaya's active geology and recent eruption history."),
     ("pacaya-volcano.png", "Cruise timing and return planning for Pacaya Volcano shore excursion from Puerto Quetzal", "Cruise Timing", "Operators plan inland drives and hiking windows around your ship schedule — confirm end times.")],
    {"Best For": "Adventure seekers &amp; active travelers", "Duration": "6–7 hours typical", "Walking Required": "Moderate to strenuous — volcanic terrain", "Cultural Interest Rating": "Moderate", "Adventure Level": "High", "Return To Ship Confidence": "Good with reputable operators — confirm buffer", "Family Friendly": "Best for fit teens and adults"},
    LINKS_DEFAULT))

(ROOT / "content/guatemala-highlights-tour.html").write_text(tour_content(
    "Guatemala Highlights", "Best for First-Time Visitors", "best-for-badge",
    "The Guatemala Highlights tour is designed for cruise passengers visiting the country for the first time. It samples Antigua's colonial landmarks, introduces Guatemalan culture and history, and includes scenic viewpoints without overloading a single theme. A practical overview when you want breadth rather than a deep dive into one specialty.",
    "guatemala-highlights.png",
    "Guatemala highlights tour with Antigua colonial architecture and scenic viewpoints from Puerto Quetzal cruise port",
    [("guatemala-highlights.png", "Regional overview and Antigua highlights on first-time visitor tour from Puerto Quetzal", "Region Overview", "Introduction to Guatemala's highlands, history and culture in one port day."),
     ("santa-catalina-arch.png", "Antigua landmarks including Santa Catalina Arch on Guatemala highlights shore excursion", "Antigua Highlights", "Key colonial sites and photo stops across the UNESCO city."),
     ("colonial-antigua.png", "Guatemalan culture and heritage on highlights tour from Puerto Quetzal cruise port", "Culture &amp; History", "Guided context on Mayan heritage, colonial era and modern Guatemala."),
     ("volcano-backdrop.png", "Scenic viewpoints over Antigua and highlands on Guatemala highlights Puerto Quetzal excursion", "Scenic Viewpoints", "Volcano-framed vistas and highland panoramas when weather allows.")],
    {"Best For": "First-time visitors to Guatemala", "Duration": "6–7 hours typical", "Walking Required": "Moderate — mixed city walking", "Cultural Interest Rating": "High", "Adventure Level": "Low to moderate", "Return To Ship Confidence": "High with cruise-timed tours", "Family Friendly": "Good — balanced pacing"},
    LINKS_DEFAULT))

print("Tour content written")

BEST_FAQ = [
    ("Which Puerto Quetzal excursion is best for history?", "Antigua Guatemala tours deliver the strongest colonial history and UNESCO heritage. The jade factory tour adds artisan culture; Guatemala Highlights samples multiple themes for first-timers."),
    ("Best excursion for photography?", "Antigua Guatemala — especially the Santa Catalina Arch, colonial streets and volcano backdrops. Pacaya Volcano offers dramatic landscape shots for fit hikers."),
    ("Best excursion for first-time visitors?", "Guatemala Highlights tour or a classic Antigua Guatemala day trip. Both introduce the region without extreme activity requirements."),
    ("Do I need a full port day for Antigua?", "Most Antigua and volcano tours run 6–7 hours plus transport — comfortable on typical 8–10 hour port calls. Confirm end times against your all-aboard before booking."),
]

(ROOT / "content/best-puerto-quetzal-shore-excursions.html").write_text(f'''<section class="pt-8 pb-4 bg-white"><div class="max-w-3xl mx-auto px-4 text-center">
  <h2 class="text-3xl font-display font-bold text-gray-900 mb-4">Best Puerto Quetzal Shore Excursions</h2>
  <p class="text-gray-600 leading-relaxed text-sm">Operators meet at the <strong>Puerto Quetzal cruise terminal</strong> and plan returns with buffer before all aboard. Compare Antigua, volcano, coffee and cultural options below — confirm timings and ship schedules before booking.</p>
</div></section>
<section class="pb-8 bg-white"><div class="max-w-7xl mx-auto px-4">{snapshot({
    "Typical Time In Port": "8–10 hours (typical)",
    "Best For": "Comparing all excursion types",
    "Walking Required": "Varies — see comparison",
    "Cultural Interest Rating": "Very high on Antigua tours",
    "Return To Ship Friendly": "Operators usually allow 60–90 min buffer",
    "Popular Excursion Types": "See comparison table below",
})}</div></section>
<section class="py-16 bg-sand-50"><div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
  <h2 class="text-3xl sm:text-4xl font-display font-bold text-gray-900 text-center mb-4">Which Puerto Quetzal Excursion Is Right for Me?</h2>
  <p class="text-center text-gray-600 text-sm max-w-2xl mx-auto mb-10">Match your Puerto Quetzal port day to history, culture, adventure or coffee.</p>
  <div class="overflow-x-auto rounded-3xl border border-gt-100 shadow-sm">
    <table class="w-full text-sm text-left min-w-[720px]">
      <thead class="bg-ocean-800 text-white"><tr>
        <th class="py-4 px-4 font-semibold rounded-tl-3xl">Excursion</th>
        <th class="py-4 px-3 font-semibold">Duration</th>
        <th class="py-4 px-3 font-semibold">Best For</th>
        <th class="py-4 px-3 font-semibold">Badge</th>
        <th class="py-4 px-4 font-semibold rounded-tr-3xl">Details</th>
      </tr></thead>
      <tbody class="bg-white">
        <tr class="border-b border-gt-50 hover:bg-sand-50/80"><td class="py-4 pr-4 font-semibold"><a href="antigua-guatemala-shore-excursion.html" class="text-ocean-600">Antigua Guatemala</a></td><td class="py-4 px-3 text-gray-600">6–7 hrs</td><td class="py-4 px-3 text-gray-600">History &amp; photography</td><td class="py-4 px-3"><span class="popular-badge text-[10px] py-0.5 px-2">Most Popular</span></td><td class="py-4 pl-3"><a href="antigua-guatemala-shore-excursion.html" class="text-gt-600 font-medium text-xs">Guide →</a></td></tr>
        <tr class="border-b border-gt-50 hover:bg-sand-50/80"><td class="py-4 pr-4 font-semibold"><a href="antigua-and-jade-factory-tour.html" class="text-ocean-600">Antigua &amp; Jade Factory</a></td><td class="py-4 px-3 text-gray-600">6–7 hrs</td><td class="py-4 px-3 text-gray-600">Culture &amp; shopping</td><td class="py-4 px-3"><span class="culture-badge text-[10px] py-0.5 px-2">Best for Culture</span></td><td class="py-4 pl-3"><a href="antigua-and-jade-factory-tour.html" class="text-gt-600 font-medium text-xs">Guide →</a></td></tr>
        <tr class="border-b border-gt-50 hover:bg-sand-50/80"><td class="py-4 pr-4 font-semibold"><a href="antigua-and-coffee-plantation-tour.html" class="text-ocean-600">Coffee Plantation</a></td><td class="py-4 px-3 text-gray-600">6–7 hrs</td><td class="py-4 px-3 text-gray-600">Coffee lovers</td><td class="py-4 px-3"><span class="coffee-badge text-[10px] py-0.5 px-2">Best for Coffee</span></td><td class="py-4 pl-3"><a href="antigua-and-coffee-plantation-tour.html" class="text-gt-600 font-medium text-xs">Guide →</a></td></tr>
        <tr class="border-b border-gt-50 hover:bg-sand-50/80"><td class="py-4 pr-4 font-semibold"><a href="pacaya-volcano-shore-excursion.html" class="text-ocean-600">Pacaya Volcano</a></td><td class="py-4 px-3 text-gray-600">6–7 hrs</td><td class="py-4 px-3 text-gray-600">Adventure</td><td class="py-4 px-3"><span class="adventure-badge text-[10px] py-0.5 px-2">Best Adventure</span></td><td class="py-4 pl-3"><a href="pacaya-volcano-shore-excursion.html" class="text-gt-600 font-medium text-xs">Guide →</a></td></tr>
        <tr class="border-b border-gt-50 hover:bg-sand-50/80"><td class="py-4 pr-4 font-semibold"><a href="guatemala-highlights-tour.html" class="text-ocean-600">Guatemala Highlights</a></td><td class="py-4 px-3 text-gray-600">6–7 hrs</td><td class="py-4 px-3 text-gray-600">First-time visitors</td><td class="py-4 px-3"><span class="best-for-badge text-[10px] py-0.5 px-2">First-Timers</span></td><td class="py-4 pl-3"><a href="guatemala-highlights-tour.html" class="text-gt-600 font-medium text-xs">Guide →</a></td></tr>
      </tbody>
    </table>
  </div>
</div></section>
<section class="py-12 bg-white"><div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
  <h2 class="text-2xl font-display font-bold text-center mb-8">Excursions by Traveler Type</h2>
  <div class="grid sm:grid-cols-2 lg:grid-cols-3 gap-6 text-sm">
    <div class="bg-sand-50 rounded-3xl p-6 border border-gt-100"><h3 class="font-display font-bold text-lg mb-2">Best for History</h3><p class="text-gray-600 mb-3">Antigua&apos;s colonial churches, ruins and UNESCO plazas.</p><a href="antigua-guatemala-shore-excursion.html" class="text-ocean-600 font-semibold">Antigua Guatemala →</a></div>
    <div class="bg-sand-50 rounded-3xl p-6 border border-gt-100"><h3 class="font-display font-bold text-lg mb-2">Best for Culture</h3><p class="text-gray-600 mb-3">Jade craftsmanship, Mayan heritage and artisan shopping.</p><a href="antigua-and-jade-factory-tour.html" class="text-ocean-600 font-semibold">Jade Factory Tour →</a></div>
    <div class="bg-sand-50 rounded-3xl p-6 border border-gt-100"><h3 class="font-display font-bold text-lg mb-2">Best for Photography</h3><p class="text-gray-600 mb-3">Santa Catalina Arch, colonial streets and volcano frames.</p><a href="antigua-guatemala-shore-excursion.html" class="text-ocean-600 font-semibold">Antigua Tour →</a></div>
    <div class="bg-ocean-50 rounded-3xl p-6 border border-ocean-100"><h3 class="font-display font-bold text-lg mb-2">Best for First-Time Visitors</h3><p class="text-gray-600 mb-3">Guatemala Highlights — balanced overview of the region.</p><a href="guatemala-highlights-tour.html" class="text-ocean-600 font-semibold">Highlights Tour →</a></div>
    <div class="bg-ocean-50 rounded-3xl p-6 border border-ocean-100"><h3 class="font-display font-bold text-lg mb-2">Best Adventure</h3><p class="text-gray-600 mb-3">Pacaya Volcano hiking — confirm fitness and access.</p><a href="pacaya-volcano-shore-excursion.html" class="text-ocean-600 font-semibold">Pacaya Volcano →</a></div>
    <div class="bg-ocean-50 rounded-3xl p-6 border border-ocean-100"><h3 class="font-display font-bold text-lg mb-2">Hidden Gem</h3><p class="text-gray-600 mb-3">Coffee plantation combo — farm culture beyond the city centre.</p><a href="antigua-and-coffee-plantation-tour.html" class="text-ocean-600 font-semibold">Coffee Tour →</a></div>
  </div>
</div></section>
<section class="pb-16 bg-white"><div class="max-w-3xl mx-auto px-4">{related_links(LINKS_DEFAULT)}</div></section>
{faq_section("Best Puerto Quetzal Excursions FAQ", BEST_FAQ)}
{cta_section()}''')

PORT_FAQ = [
    ("How far is Antigua from Puerto Quetzal?", "Antigua is typically around 1.5 to 2 hours inland by road depending on traffic and route. Confirm drive times with your operator and ship schedule."),
    ("What currency is used in Puerto Quetzal?", "Guatemalan quetzal (GTQ) is official. USD is widely accepted on tours and in tourist areas — small bills are helpful."),
    ("Is Puerto Quetzal safe for cruise passengers?", "Organized shore excursions and tourist routes in Antigua are generally safe with reputable operators. Stay with your group, follow guide advice and avoid wandering alone in unfamiliar areas."),
]

(ROOT / "content/puerto-quetzal-cruise-port-guide.html").write_text(f'''<section class="pt-8 pb-4 bg-white"><div class="max-w-3xl mx-auto px-4">
  <h2 class="text-3xl font-display font-bold text-gray-900 mb-4 text-center">Puerto Quetzal Cruise Port Guide</h2>
  <p class="text-gray-600 leading-relaxed text-sm text-center">Practical advice for first-time cruise passengers docking in Puerto Quetzal, Guatemala — terminal layout, distance to Antigua, currency, customs, excursion timing, safety and return-to-ship confidence.</p>
</div></section>
<section class="pb-8 bg-white"><div class="max-w-7xl mx-auto px-4">{snapshot({
    "Typical Time In Port": "8–10 hours (typical)",
    "Best For": "Gateway to Antigua &amp; highlands",
    "Walking Required": "Minimal at terminal — more in Antigua",
    "Cultural Interest Rating": "Very high inland",
    "Return To Ship Friendly": "Allow 60–90 min buffer on independent tours",
    "Popular Excursion Types": "Antigua, Pacaya, coffee, jade",
})}</div></section>
<section class="py-12 bg-white"><div class="max-w-3xl mx-auto px-4 sm:px-6 space-y-8 text-sm text-gray-600 leading-relaxed">
  <div><h3 class="text-xl font-display font-bold text-gray-900 mb-3">Cruise terminal information</h3>
  <p>Puerto Quetzal is Guatemala&apos;s main <strong>Pacific cruise port</strong>, serving ships on Panama Canal and Central America itineraries. The terminal area has basic facilities — excursion meeting points, taxis and vendor stalls. It is a working port, not a resort pier. Most passengers book inland tours to Antigua rather than staying at the dock.</p></div>
  <div><h3 class="text-xl font-display font-bold text-gray-900 mb-3">Distance to Antigua &amp; journey times</h3>
  <p><strong>Antigua Guatemala</strong> sits in the central highlands, roughly <strong>90–100 km</strong> from Puerto Quetzal. Drive time is typically <strong>1.5 to 2 hours each way</strong> depending on traffic, road conditions and time of day. Pacaya Volcano excursions use similar inland routes. Always confirm total tour duration including transport before booking.</p></div>
  <div><h3 class="text-xl font-display font-bold text-gray-900 mb-3">Currency</h3>
  <p>Official currency is the <strong>Guatemalan quetzal (GTQ)</strong>. USD is commonly accepted on shore excursions and in Antigua tourist areas. ATMs may be limited at the pier — carry small bills if shopping or tipping. Credit cards work at many Antigua restaurants and shops but not everywhere.</p></div>
  <div><h3 class="text-xl font-display font-bold text-gray-900 mb-3">Local customs</h3>
  <p>Guatemala is culturally warm and formal in churches — dress modestly when visiting religious sites. Bargaining is common in markets but not in fixed-price shops. A basic Spanish greeting goes a long way. Tipping guides and drivers is appreciated when not included in your tour price.</p></div>
  <div><h3 class="text-xl font-display font-bold text-gray-900 mb-3">Excursion timing tips</h3>
  <ul class="list-disc pl-5 space-y-2"><li>Antigua and volcano tours often depart within 30–60 minutes of docking — be ready when you disembark.</li><li>Most excursions run 6–7 hours plus transport — fits 8–10 hour port calls when timed correctly.</li><li>Highland weather can shift quickly — pack a light layer and sun protection.</li><li>Confirm your operator&apos;s stated return time against your ship&apos;s all-aboard the morning you dock.</li></ul></div>
  <div><h3 class="text-xl font-display font-bold text-gray-900 mb-3">Return-to-ship advice</h3>
  <p>Ship excursions guarantee the vessel waits if the tour is late. Independent operators should state a return policy — look for tours that build in <strong>60–90 minutes</strong> before all aboard. Keep your cruise line&apos;s port contact number. Inland drives are the main variable — allow margin for traffic on return legs.</p></div>
  <div><h3 class="text-xl font-display font-bold text-gray-900 mb-3">Safety information</h3>
  <p>Stay with organized excursions or reputable guides. Avoid displaying valuables in crowded areas. Drink bottled water if unsure. Volcano hikes require appropriate footwear and fitness — follow guide instructions on Pacaya routes. Puerto Quetzal itself is a port town; the cultural highlights are inland in Antigua and the highlands.</p></div>
  <div><h3 class="text-xl font-display font-bold text-gray-900 mb-3">First-time visitor tips</h3>
  <p>Book an Antigua or highlights tour rather than expecting a beach day. Wear comfortable shoes for cobblestones. Bring a camera for colonial architecture and volcano views. Confirm excursion inclusions — lunch, entries and shopping stops vary by operator. Read our <a href="one-day-in-puerto-quetzal-from-a-cruise-ship.html" class="text-ocean-600 font-medium">one-day itinerary</a> and <a href="best-puerto-quetzal-shore-excursions.html" class="text-ocean-600 font-medium">excursion comparison</a> before you choose.</p></div>
</div></section>
<section class="pb-16 bg-white"><div class="max-w-3xl mx-auto px-4">{related_links(LINKS_DEFAULT)}</div></section>
{faq_section("Puerto Quetzal Port Guide FAQ", PORT_FAQ)}
{cta_section()}''')

(ROOT / "content/one-day-in-puerto-quetzal-from-a-cruise-ship.html").write_text(f'''<section class="pt-8 pb-4 bg-white"><div class="max-w-3xl mx-auto px-4 text-center">
  <h2 class="text-3xl font-display font-bold text-gray-900 mb-4">One Day in Puerto Quetzal from a Cruise Ship</h2>
  <p class="text-gray-600 text-sm">A complete cruise day itinerary focused on Antigua Guatemala. Adjust based on your ship&apos;s actual schedule and confirm tour availability before booking.</p>
</div></section>
<section class="pb-8 bg-white"><div class="max-w-7xl mx-auto px-4">{snapshot({
    "Typical Time In Port": "8–10 hours (typical)",
    "Best For": "Planning your full port day",
    "Walking Required": "Moderate in Antigua",
    "Cultural Interest Rating": "Very high",
    "Return To Ship Friendly": "Always keep 60–90 min buffer",
    "Popular Excursion Types": "Antigua-focused day below",
})}</div></section>
<section class="py-12 bg-sand-50"><div class="max-w-3xl mx-auto px-4 space-y-10">
  <div class="bg-white rounded-3xl p-6 border border-gt-100 shadow-sm">
    <span class="popular-badge mb-3 inline-block">Classic Antigua Day</span>
    <h3 class="text-xl font-display font-bold text-gray-900 mb-3">Morning: Departure &amp; Inland Transfer</h3>
    <ol class="text-sm text-gray-600 space-y-2 list-decimal pl-5">
      <li>Disembark promptly and meet your operator at the Puerto Quetzal terminal assembly point.</li>
      <li>Coach transfer inland toward Antigua Guatemala — typically 1.5 to 2 hours depending on traffic.</li>
      <li>Use the drive for guide introductions and context on Guatemalan history and highland geography.</li>
    </ol>
    <h3 class="text-xl font-display font-bold text-gray-900 mb-3 mt-6">Mid-Morning: Antigua Sightseeing</h3>
    <ol class="text-sm text-gray-600 space-y-2 list-decimal pl-5">
      <li>Walk colonial streets toward the <strong>Santa Catalina Arch</strong> — Antigua&apos;s iconic photo stop.</li>
      <li>Visit church ruins, plazas and colourful facades across the UNESCO World Heritage centre.</li>
      <li>Stop at a local market for textiles, crafts and regional flavours when your tour includes it.</li>
    </ol>
    <h3 class="text-xl font-display font-bold text-gray-900 mb-3 mt-6">Lunch Suggestions</h3>
    <p class="text-sm text-gray-600">Many tours include lunch at an Antigua restaurant — pepián, tamales, grilled meats and fresh tortillas are regional staples. If lunch is not included, ask your guide for a central restaurant with reliable timing. Allow enough sit-down time without rushing your afternoon.</p>
    <h3 class="text-xl font-display font-bold text-gray-900 mb-3 mt-6">Afternoon: Cultural Highlights</h3>
    <p class="text-sm text-gray-600">Depending on your booked tour: jade factory visit, coffee tasting, additional church ruins or a scenic viewpoint over the city and volcanoes. Photography opportunities are strongest in afternoon light on clear days — weather varies.</p>
    <h3 class="text-xl font-display font-bold text-gray-900 mb-3 mt-6">Return-to-Ship Timing</h3>
    <p class="text-sm text-gray-600">Depart Antigua with your operator&apos;s scheduled buffer. Inland return drives take 1.5 to 2 hours — confirm your tour&apos;s stated pier arrival time leaves at least <strong>60–90 minutes</strong> before all aboard. Verify with your guide throughout the day.</p>
    <a href="antigua-guatemala-shore-excursion.html" class="inline-block mt-4 text-ocean-600 font-semibold text-sm">Antigua Guatemala guide →</a>
  </div>
  <div class="bg-white rounded-3xl p-6 border border-gt-100 shadow-sm">
    <span class="adventure-badge mb-3 inline-block">Adventure Alternative</span>
    <h3 class="text-xl font-display font-bold text-gray-900 mb-3">Pacaya Volcano Day</h3>
    <ol class="text-sm text-gray-600 space-y-2 list-decimal pl-5">
      <li>Early departure for Pacaya Volcano hiking — confirm fitness requirements and current trail access.</li>
      <li>Guided hike on volcanic terrain with geological interpretation from local experts.</li>
      <li>Return inland drive to Puerto Quetzal with operator buffer — verify end time against ship schedule.</li>
    </ol>
    <p class="text-sm text-gray-600 mt-3">Volcano conditions and access change. Do not book assuming lava viewing or specific summit routes without operator confirmation.</p>
    <a href="pacaya-volcano-shore-excursion.html" class="inline-block mt-4 text-ocean-600 font-semibold text-sm">Pacaya Volcano guide →</a>
  </div>
</div></section>
<section class="pb-16 bg-white"><div class="max-w-3xl mx-auto px-4">{related_links(LINKS_DEFAULT)}</div></section>
{cta_section()}''')

WORTH_FAQ = [
    ("Is Puerto Quetzal worth visiting on a cruise?", "Yes — if you want Guatemalan culture, colonial Antigua and highland scenery rather than a beach-only port day. It is one of the strongest Central America ports for history and UNESCO heritage."),
    ("What is Puerto Quetzal known for?", "Being Guatemala's Pacific cruise gateway to Antigua Guatemala, volcanoes, coffee plantations, jade craftsmanship and Guatemalan highland culture."),
    ("Is Antigua worth visiting from a cruise ship?", "Yes. Antigua is among the finest colonial cities in the Americas — cobblestone streets, churches, markets and volcano views make it a standout shore excursion destination."),
    ("What should cruise passengers do in Puerto Quetzal?", "Book an inland excursion to Antigua, Pacaya Volcano, a coffee plantation or jade factory tour. Staying at the terminal misses the port's main value."),
    ("Is Puerto Quetzal safe?", "Organized shore excursions to Antigua and reputable volcano tours are generally safe when you stay with your group and follow guide advice. Confirm operators and avoid wandering alone in unfamiliar areas."),
]

(ROOT / "content/is-puerto-quetzal-worth-visiting.html").write_text(f'''<section class="pt-8 pb-4 bg-white"><div class="max-w-3xl mx-auto px-4">
  <h2 class="text-3xl font-display font-bold text-gray-900 mb-4 text-center">Is Puerto Quetzal Worth Visiting on a Cruise?</h2>
  <p class="text-gray-600 text-sm text-center leading-relaxed">An honest look at what Puerto Quetzal delivers for cruise passengers — culture, history and highland scenery, not Caribbean beaches.</p>
</div></section>
<section class="pb-8 bg-white"><div class="max-w-7xl mx-auto px-4">{snapshot({
    "Typical Time In Port": "8–10 hours (typical)",
    "Best For": "Culture, history &amp; volcanoes",
    "Walking Required": "Moderate on Antigua tours",
    "Cultural Interest Rating": "Very high inland",
    "Return To Ship Friendly": "Plan buffer on all excursions",
    "Popular Excursion Types": "Antigua, Pacaya, coffee, jade",
})}</div></section>
<section class="py-12 bg-white"><div class="max-w-3xl mx-auto px-4 space-y-6 text-sm text-gray-600 leading-relaxed">
  <p><strong>Is Puerto Quetzal worth visiting?</strong> Yes — for cruise passengers who want Guatemala&apos;s colonial heritage, volcano scenery and coffee culture. Puerto Quetzal is not a beach destination; its value is as the gateway to <a href="antigua-guatemala-shore-excursion.html" class="text-ocean-600 font-medium">Antigua Guatemala</a> and the highlands.</p>
  <p><strong>What is Puerto Quetzal known for?</strong> Serving as Guatemala&apos;s Pacific cruise port with access to Antigua&apos;s UNESCO streets, Pacaya Volcano, coffee plantations, jade workshops and Guatemalan artisan traditions. Most passengers never linger at the pier — they head inland.</p>
  <p><strong>Is Antigua worth visiting from a cruise ship?</strong> Absolutely. Antigua delivers cobblestone plazas, the Santa Catalina Arch, church ruins, markets and volcano backdrops in a compact, walkable city. It is the reason most travelers rate Puerto Quetzal highly.</p>
  <p><strong>What should cruise passengers do in Puerto Quetzal?</strong> Book a shore excursion — Antigua tour, Guatemala Highlights, coffee plantation, jade factory or Pacaya Volcano depending on your interests. Compare options on our <a href="best-puerto-quetzal-shore-excursions.html" class="text-ocean-600 font-medium">best excursions page</a>.</p>
  <p><strong>Is Puerto Quetzal safe?</strong> Tourist excursions with reputable operators are generally safe. Stay with your group, follow guide advice, use bottled water when unsure and confirm return policies before booking independently.</p>
  <p><strong>Bottom line:</strong> Puerto Quetzal is worth visiting when you plan an inland cultural or adventure day. It may disappoint if you expect a tropical beach stop — read our <a href="puerto-quetzal-cruise-port-guide.html" class="text-ocean-600 font-medium">port guide</a> and <a href="antigua-vs-pacaya-volcano-excursion.html" class="text-ocean-600 font-medium">Antigua vs Pacaya comparison</a> to choose the right excursion.</p>
</div></section>
<section class="py-12 bg-sand-50"><div class="max-w-3xl mx-auto px-4">
  <h3 class="text-xl font-display font-bold text-gray-900 mb-4 text-center">Quick Verdict</h3>
  <div class="grid sm:grid-cols-2 gap-4 text-sm">
    <div class="bg-white rounded-2xl p-5 border border-green-200"><p class="font-semibold text-green-800 mb-2">Worth it for</p><ul class="text-gray-600 space-y-1"><li>• Colonial Antigua &amp; UNESCO sites</li><li>• Guatemalan culture &amp; coffee</li><li>• Volcano adventure (Pacaya)</li><li>• First-time Central America visitors</li></ul></div>
    <div class="bg-white rounded-2xl p-5 border border-gt-200"><p class="font-semibold text-gt-800 mb-2">Less ideal for</p><ul class="text-gray-600 space-y-1"><li>• Beach lounging only</li><li>• Very short port calls</li><li>• Guaranteed volcano lava viewing</li></ul></div>
  </div>
</div></section>
<section class="pb-16 bg-white"><div class="max-w-3xl mx-auto px-4">{related_links(LINKS_DEFAULT)}</div></section>
{faq_section("Is Puerto Quetzal Worth Visiting? FAQ", WORTH_FAQ)}
{cta_section()}''')

(ROOT / "content/antigua-vs-pacaya-volcano-excursion.html").write_text(f'''<section class="pt-8 pb-4 bg-white"><div class="max-w-3xl mx-auto px-4 text-center">
  <h2 class="text-3xl font-display font-bold text-gray-900 mb-4">Antigua vs Pacaya Volcano Excursion</h2>
  <p class="text-gray-600 text-sm">Two defining Puerto Quetzal port days — colonial history in Antigua versus volcanic adventure at Pacaya. Use this comparison to match your interests, fitness and ship schedule.</p>
</div></section>
<section class="pb-8 bg-white"><div class="max-w-7xl mx-auto px-4">{snapshot({
    "Typical Time In Port": "8–10 hours (typical)",
    "Best For": "Choosing between culture &amp; adventure",
    "Walking Required": "Antigua moderate · Pacaya moderate-strenuous",
    "Cultural Interest Rating": "Antigua very high · Pacaya moderate",
    "Return To Ship Friendly": "Confirm buffer on both",
    "Popular Excursion Types": "See comparison below",
})}</div></section>
<section class="py-12 bg-white"><div class="max-w-4xl mx-auto px-4">
  <div class="overflow-x-auto rounded-3xl border border-gt-100 shadow-sm">
    <table class="w-full text-sm text-left min-w-[600px]">
      <thead class="bg-ocean-800 text-white"><tr>
        <th class="py-4 px-4 font-semibold">Factor</th>
        <th class="py-4 px-4 font-semibold"><a href="antigua-guatemala-shore-excursion.html" class="text-white hover:text-gt-200">Antigua Guatemala</a></th>
        <th class="py-4 px-4 font-semibold"><a href="pacaya-volcano-shore-excursion.html" class="text-white hover:text-gt-200">Pacaya Volcano</a></th>
      </tr></thead>
      <tbody class="bg-white">
        <tr class="border-b border-gt-50"><td class="py-4 px-4 font-semibold text-gray-900">Main appeal</td><td class="py-4 px-4 text-gray-600">Colonial history, UNESCO heritage, markets</td><td class="py-4 px-4 text-gray-600">Active volcano, hiking, geological drama</td></tr>
        <tr class="border-b border-gt-50"><td class="py-4 px-4 font-semibold text-gray-900">History vs adventure</td><td class="py-4 px-4 text-gray-600">Strong history &amp; culture focus</td><td class="py-4 px-4 text-gray-600">Adventure &amp; nature focus</td></tr>
        <tr class="border-b border-gt-50"><td class="py-4 px-4 font-semibold text-gray-900">Walking requirements</td><td class="py-4 px-4 text-gray-600">Moderate — cobblestone city streets</td><td class="py-4 px-4 text-gray-600">Moderate to strenuous — volcanic terrain</td></tr>
        <tr class="border-b border-gt-50"><td class="py-4 px-4 font-semibold text-gray-900">Photography</td><td class="py-4 px-4 text-gray-600">Arch, plazas, colonial facades, volcano frames</td><td class="py-4 px-4 text-gray-600">Volcanic landscapes, lava fields (when accessible)</td></tr>
        <tr class="border-b border-gt-50"><td class="py-4 px-4 font-semibold text-gray-900">Families</td><td class="py-4 px-4 text-gray-600">Excellent — walkable, educational, varied stops</td><td class="py-4 px-4 text-gray-600">Best for fit teens and adults — assess hiking distance</td></tr>
        <tr class="border-b border-gt-50"><td class="py-4 px-4 font-semibold text-gray-900">First-time visitors</td><td class="py-4 px-4 text-gray-600">Top pick — iconic Guatemala experience</td><td class="py-4 px-4 text-gray-600">Memorable if you want adventure over architecture</td></tr>
        <tr class="border-b border-gt-50"><td class="py-4 px-4 font-semibold text-gray-900">Cruise suitability</td><td class="py-4 px-4 text-gray-600">Fits 8–10 hr port calls comfortably</td><td class="py-4 px-4 text-gray-600">Fits most port calls — confirm hiking duration &amp; access</td></tr>
        <tr><td class="py-4 px-4 font-semibold text-gray-900">Duration typical</td><td class="py-4 px-4 text-gray-600">6–7 hours</td><td class="py-4 px-4 text-gray-600">6–7 hours</td></tr>
      </tbody>
    </table>
  </div>
  <p class="mt-8 text-sm text-gray-600 leading-relaxed">Most first-time visitors choose <a href="antigua-guatemala-shore-excursion.html" class="text-ocean-600 font-medium">Antigua</a> for culture and photography. Choose <a href="pacaya-volcano-shore-excursion.html" class="text-ocean-600 font-medium">Pacaya</a> if you prefer hiking and volcanic scenery and can handle uneven terrain. Volcano access and conditions change — confirm with your operator. Cannot decide? See our <a href="best-puerto-quetzal-shore-excursions.html" class="text-ocean-600 font-medium">full excursion comparison</a> or <a href="guatemala-highlights-tour.html" class="text-ocean-600 font-medium">Guatemala Highlights</a> for a balanced sample.</p>
</div></section>
<section class="pb-16 bg-white"><div class="max-w-3xl mx-auto px-4">{related_links(LINKS_DEFAULT)}</div></section>
{cta_section()}''')

print("All content written")

PAGES = [
    ("index.html", "home", "partials/hero-home.html", "content/home.html", "hero-puerto-quetzal.png",
     "Puerto Quetzal Shore Excursion | Antigua, Volcanoes &amp; Tours from Puerto Quetzal Cruise Port",
     "Plan Puerto Quetzal shore excursions for cruise passengers — Antigua Guatemala, Pacaya Volcano, coffee plantations and cultural tours from Guatemala's Pacific cruise gateway.",
     "Puerto Quetzal shore excursions, Puerto Quetzal cruise excursions, Puerto Quetzal cruise port excursions, Antigua Guatemala shore excursion",
     BASE_URL + "/",
     {"@context": "https://schema.org", "@graph": [
         {"@type": "WebSite", "name": SITE, "url": BASE_URL + "/", "description": "Planning guide for Puerto Quetzal cruise shore excursions in Guatemala"},
         {"@type": "LocalBusiness", "name": SITE, "url": BASE_URL + "/", "description": "Cruise passenger planning guide for Puerto Quetzal, Guatemala shore excursions",
          "address": {"@type": "PostalAddress", "addressLocality": "Puerto Quetzal", "addressRegion": "Escuintla", "addressCountry": "GT"},
          "areaServed": {"@type": "City", "name": "Puerto Quetzal", "containedInPlace": {"@type": "AdministrativeArea", "name": "Escuintla"}}},
         {"@type": "TouristInformationCenter", "name": SITE, "url": BASE_URL + "/", "description": "Puerto Quetzal cruise port excursion planning information"},
         {"@type": "FAQPage", "mainEntity": faq_schema(HOME_FAQ)},
     ]}),
    ("best-puerto-quetzal-shore-excursions.html", "excursions", "partials/hero-best-excursions.html", "content/best-puerto-quetzal-shore-excursions.html", "best-puerto-quetzal-excursions.png",
     "Best Puerto Quetzal Shore Excursions | Compare Top Cruise Tours",
     "Compare the best Puerto Quetzal shore excursions for cruise passengers — Antigua Guatemala, Pacaya Volcano, coffee plantations, jade factory and highlights tours with return-to-ship timing.",
     "best Puerto Quetzal shore excursions, Puerto Quetzal cruise excursions, Antigua from Puerto Quetzal cruise port",
     BASE_URL + "/best-puerto-quetzal-shore-excursions.html",
     {"@context": "https://schema.org", "@graph": [
         {"@type": "TouristInformationCenter", "name": "Best Puerto Quetzal Shore Excursions", "url": BASE_URL + "/best-puerto-quetzal-shore-excursions.html", "description": "Comparison guide for Puerto Quetzal cruise shore excursions"},
         {"@type": "FAQPage", "mainEntity": faq_schema(BEST_FAQ)},
     ]}),
    ("puerto-quetzal-cruise-port-guide.html", "port", "partials/hero-port-guide.html", "content/puerto-quetzal-cruise-port-guide.html", "puerto-quetzal-port.png",
     "Puerto Quetzal Cruise Port Guide | Terminal, Timing &amp; Tips",
     "Puerto Quetzal cruise port guide — terminal info, distance to Antigua, journey times, currency, safety, excursion timing and return-to-ship advice.",
     "Puerto Quetzal cruise port guide, Puerto Quetzal cruise port excursions, Antigua from Puerto Quetzal",
     BASE_URL + "/puerto-quetzal-cruise-port-guide.html",
     {"@context": "https://schema.org", "@graph": [
         {"@type": "TouristInformationCenter", "name": "Puerto Quetzal Cruise Port Guide", "url": BASE_URL + "/puerto-quetzal-cruise-port-guide.html"},
         {"@type": "FAQPage", "mainEntity": faq_schema(PORT_FAQ)},
     ]}),
    ("one-day-in-puerto-quetzal-from-a-cruise-ship.html", "oneday", "partials/hero-one-day.html", "content/one-day-in-puerto-quetzal-from-a-cruise-ship.html", "one-day-puerto-quetzal.png",
     "One Day in Puerto Quetzal from a Cruise Ship | Itinerary Guide",
     "Sample one-day Puerto Quetzal itineraries for cruise passengers — Antigua sightseeing, lunch suggestions, cultural highlights and return-to-ship timing.",
     "one day Puerto Quetzal cruise ship, Puerto Quetzal itinerary cruise, Antigua from cruise ship",
     BASE_URL + "/one-day-in-puerto-quetzal-from-a-cruise-ship.html",
     {"@context": "https://schema.org", "@type": "TouristInformationCenter", "name": "One Day in Puerto Quetzal", "url": BASE_URL + "/one-day-in-puerto-quetzal-from-a-cruise-ship.html"}),
    ("antigua-guatemala-shore-excursion.html", "antigua", "partials/hero-antigua.html", "content/antigua-guatemala-shore-excursion.html", "santa-catalina-arch.png",
     "Antigua Guatemala Shore Excursion from Puerto Quetzal | Colonial UNESCO Tour",
     "Antigua Guatemala shore excursion from Puerto Quetzal cruise port — Santa Catalina Arch, colonial streets, churches, markets and UNESCO heritage with ship-timed returns.",
     "Antigua Guatemala shore excursion, Antigua from Puerto Quetzal cruise port, Puerto Quetzal Antigua tour",
     BASE_URL + "/antigua-guatemala-shore-excursion.html",
     {"@context": "https://schema.org", "@type": "TouristTrip", "name": "Antigua Guatemala Shore Excursion from Puerto Quetzal", "description": "Colonial UNESCO city tour from Puerto Quetzal cruise port.", "touristType": "Cruise passengers", "provider": {"@type": "Organization", "name": SITE, "url": BASE_URL}}),
    ("antigua-and-jade-factory-tour.html", "jade", "partials/hero-jade.html", "content/antigua-and-jade-factory-tour.html", "jade-factory.png",
     "Antigua &amp; Jade Factory Tour from Puerto Quetzal | Cultural Shore Excursion",
     "Antigua and jade factory shore excursion from Puerto Quetzal — Mayan jade craftsmanship, Guatemalan history, shopping and colonial Antigua highlights.",
     "Antigua jade factory tour Puerto Quetzal, jade shore excursion Guatemala cruise",
     BASE_URL + "/antigua-and-jade-factory-tour.html",
     {"@context": "https://schema.org", "@type": "TouristTrip", "name": "Antigua and Jade Factory Tour from Puerto Quetzal", "description": "Cultural jade factory and Antigua tour from Puerto Quetzal cruise port.", "touristType": "Cruise passengers", "provider": {"@type": "Organization", "name": SITE, "url": BASE_URL}}),
    ("antigua-and-coffee-plantation-tour.html", "coffee", "partials/hero-coffee.html", "content/antigua-and-coffee-plantation-tour.html", "coffee-plantation.png",
     "Antigua &amp; Coffee Plantation Tour from Puerto Quetzal | Shore Excursion",
     "Coffee plantation and Antigua shore excursion from Puerto Quetzal — highland farm visits, coffee production, local culture and colonial sightseeing.",
     "coffee plantation tour Puerto Quetzal, Antigua coffee shore excursion Guatemala",
     BASE_URL + "/antigua-and-coffee-plantation-tour.html",
     {"@context": "https://schema.org", "@type": "TouristTrip", "name": "Antigua and Coffee Plantation Tour from Puerto Quetzal", "description": "Coffee plantation and Antigua tour from Puerto Quetzal cruise port.", "touristType": "Cruise passengers", "provider": {"@type": "Organization", "name": SITE, "url": BASE_URL}}),
    ("pacaya-volcano-shore-excursion.html", "volcano", "partials/hero-volcano.html", "content/pacaya-volcano-shore-excursion.html", "pacaya-volcano.png",
     "Pacaya Volcano Shore Excursion from Puerto Quetzal | Adventure Tour",
     "Pacaya Volcano shore excursion from Puerto Quetzal cruise port — volcano hiking, geological features and adventure with cruise-timed returns. Confirm access and fitness requirements.",
     "Pacaya Volcano excursion, Pacaya Volcano Puerto Quetzal cruise port, Guatemala volcano shore excursion",
     BASE_URL + "/pacaya-volcano-shore-excursion.html",
     {"@context": "https://schema.org", "@type": "TouristTrip", "name": "Pacaya Volcano Shore Excursion from Puerto Quetzal", "description": "Volcano hiking adventure from Puerto Quetzal cruise port.", "touristType": "Cruise passengers", "provider": {"@type": "Organization", "name": SITE, "url": BASE_URL}}),
    ("guatemala-highlights-tour.html", "highlights", "partials/hero-highlights.html", "content/guatemala-highlights-tour.html", "guatemala-highlights.png",
     "Guatemala Highlights Tour from Puerto Quetzal | First-Time Visitor Excursion",
     "Guatemala Highlights shore excursion from Puerto Quetzal — Antigua overview, culture, history and scenic viewpoints for first-time cruise visitors.",
     "Guatemala cruise excursions, Guatemala highlights tour Puerto Quetzal, first time Guatemala cruise",
     BASE_URL + "/guatemala-highlights-tour.html",
     {"@context": "https://schema.org", "@type": "TouristTrip", "name": "Guatemala Highlights Tour from Puerto Quetzal", "description": "Regional highlights tour for first-time visitors from Puerto Quetzal cruise port.", "touristType": "Cruise passengers", "provider": {"@type": "Organization", "name": SITE, "url": BASE_URL}}),
    ("is-puerto-quetzal-worth-visiting.html", "worth", "partials/hero-worth-visiting.html", "content/is-puerto-quetzal-worth-visiting.html", "puerto-quetzal-intro.png",
     "Is Puerto Quetzal Worth Visiting on a Cruise? | Honest Guide",
     "Is Puerto Quetzal worth visiting on a cruise? Honest guide — Antigua Guatemala, volcanoes, coffee culture and what cruise passengers should expect.",
     "is Puerto Quetzal worth visiting cruise, Puerto Quetzal cruise port worth it, Antigua worth visiting cruise ship",
     BASE_URL + "/is-puerto-quetzal-worth-visiting.html",
     {"@context": "https://schema.org", "@graph": [
         {"@type": "TouristInformationCenter", "name": "Is Puerto Quetzal Worth Visiting", "url": BASE_URL + "/is-puerto-quetzal-worth-visiting.html"},
         {"@type": "FAQPage", "mainEntity": faq_schema(WORTH_FAQ)},
     ]}),
    ("antigua-vs-pacaya-volcano-excursion.html", "vs", "partials/hero-vs-volcano.html", "content/antigua-vs-pacaya-volcano-excursion.html", "volcano-backdrop.png",
     "Antigua vs Pacaya Volcano Excursion from Puerto Quetzal | Comparison",
     "Compare Antigua Guatemala vs Pacaya Volcano shore excursions from Puerto Quetzal — history vs adventure, walking, photography, families and cruise suitability.",
     "Antigua vs Pacaya Volcano excursion, Puerto Quetzal shore excursion comparison",
     BASE_URL + "/antigua-vs-pacaya-volcano-excursion.html",
     {"@context": "https://schema.org", "@type": "TouristInformationCenter", "name": "Antigua vs Pacaya Volcano Excursion", "url": BASE_URL + "/antigua-vs-pacaya-volcano-excursion.html"}),
]

for fname, page, hero_f, content_f, preload, title, desc, kw, canon, ld in PAGES:
    shell(fname, title=title, description=desc, keywords=kw, canonical=canon,
          preload=preload, page=page, hero_file=hero_f, content_file=content_f, ld_json=ld)

urls = [
    (BASE_URL + "/", "1.0", "weekly"),
    (BASE_URL + "/best-puerto-quetzal-shore-excursions.html", "0.9", "monthly"),
    (BASE_URL + "/puerto-quetzal-cruise-port-guide.html", "0.8", "monthly"),
    (BASE_URL + "/one-day-in-puerto-quetzal-from-a-cruise-ship.html", "0.8", "monthly"),
    (BASE_URL + "/antigua-guatemala-shore-excursion.html", "0.9", "monthly"),
    (BASE_URL + "/antigua-and-jade-factory-tour.html", "0.9", "monthly"),
    (BASE_URL + "/antigua-and-coffee-plantation-tour.html", "0.9", "monthly"),
    (BASE_URL + "/pacaya-volcano-shore-excursion.html", "0.9", "monthly"),
    (BASE_URL + "/guatemala-highlights-tour.html", "0.9", "monthly"),
    (BASE_URL + "/is-puerto-quetzal-worth-visiting.html", "0.8", "monthly"),
    (BASE_URL + "/antigua-vs-pacaya-volcano-excursion.html", "0.8", "monthly"),
]
sitemap = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
for loc, pri, freq in urls:
    sitemap += f"  <url><loc>{loc}</loc><lastmod>2026-06-10</lastmod><changefreq>{freq}</changefreq><priority>{pri}</priority></url>\n"
sitemap += "</urlset>\n"
(ROOT / "sitemap.xml").write_text(sitemap)

(ROOT / "robots.txt").write_text(f"User-agent: *\nAllow: /\n\nSitemap: {BASE_URL}/sitemap.xml\n")

(ROOT / "wrangler.jsonc").write_text('''{
  "$schema": "node_modules/wrangler/config-schema.json",
  "name": "puerto-quetzal-shore-excursions",
  "compatibility_date": "2026-06-10",
  "observability": { "enabled": true },
  "assets": { "directory": "." },
  "routes": [{ "pattern": "puertoquetzalshoreexcursion.com", "custom_domain": true }]
}
''')

(ROOT / "images").mkdir(exist_ok=True)
(ROOT / "images/ATTRIBUTION.md").write_text("""# Image Attribution

Images sourced from [Unsplash](https://unsplash.com) under the Unsplash License.

Themes: Antigua Guatemala colonial architecture, Santa Catalina Arch, volcanoes, coffee plantations, jade craftsmanship, and Guatemalan highland culture.

Run `python3 scripts/fetch-puerto-quetzal-images.py` to download assets.
""")

print("Shells, sitemap, robots, wrangler written — DONE")
