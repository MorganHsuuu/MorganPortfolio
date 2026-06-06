#!/usr/bin/env python3
"""Generate undergraduate project detail pages from slide data."""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROJECTS = ROOT / "projects"
ASSETS = "../assets/ug-slides"

PROJECTS_DATA = [
    {
        "file": "sonar.html",
        "slug": "sonar",
        "num": "UG 01",
        "title": "SOÑAR",
        "subtitle": "Smart healthy-drink service — vending machine + personalized nutrition app.",
        "tags": ["Service Design", "EcoHealth", "Team of 3"],
        "meta": [
            ("Type", "Group project · EcoHealth"),
            ("Team", "3 designers"),
            ("Focus", "Vending + app ecosystem"),
            ("Theme", "Nutrition · Food waste"),
        ],
        "cover": "../assets/sonar.png",
        "slides": [
            (27, "Overview", "Make your drink come true.", [
                "Interactive healthy-drink service combining smart vending and a health app.",
                "Personalizes ingredient ratios to reduce food waste.",
                "Group project with Hsieh Chen-hsin & Chuang Peng-yeh.",
            ]),
            (28, "Research", "Taiwan eats out — veggies fall short.", [
                "Up to 90% of Taiwanese people lack sufficient fruit & vegetable intake.",
                "Eating-out culture drives convenient but unhealthy daily choices.",
            ]),
            (29, "People", "Three personas, three needs.", [
                "Busy office worker — quick, healthy options on the go.",
                "Middle-aged man with fatty liver — more vegetables in diet.",
                "Fitness enthusiast — personalized nutrition advice.",
            ]),
            (30, "Brand", "Sunshine in every ingredient.", [
                "Visual identity built around nutrition, vitality, and natural taste.",
                "Color system maps ingredient types to healthy associations.",
            ]),
            (31, "Service flow", "Six steps, zero guesswork.", [
                "Pay → scan QR → watch transparent prep → enjoy → recycle cup.",
                "App-integrated tracking for personalized re-ordering.",
            ]),
            (32, "Product", "Vending machine at human height.", [
                "Pickup height 84 cm — grab drinks without bending.",
                "Transparent ingredient display + cup QR triggers recycling.",
            ]),
            (33, "App", "Personalize, order, collect.", [
                "Ingredient analysis, loyalty points, and popular combos.",
                "QR code links mobile order to the nearest Soñar station.",
            ]),
        ],
        "prev": None,
        "next": ("CLEBELL", "clebell.html"),
    },
    {
        "file": "clebell.html",
        "slug": "clebell",
        "num": "UG 02",
        "title": "CLEBELL",
        "subtitle": "Interactive dumbbell that turns calories burned into renewable energy & music.",
        "tags": ["Product Design", "EcoHealth", "Solo"],
        "meta": [
            ("Type", "Individual · EcoHealth"),
            ("Role", "Research to model making"),
            ("Build", "Bluetooth · 3D modeling"),
            ("Theme", "Fitness · Clean energy"),
        ],
        "cover": "../assets/clebell.png",
        "slides": [
            (35, "Concept", "Work out. Generate power. Feel the beat.", [
                "Bluetooth dumbbell converts burned calories into stored energy.",
                "Powers an immersive music experience while you exercise.",
                "Solo project — research through physical prototyping.",
            ]),
            (36, "Research", "Why people quit working out.", [
                "Mapped motivation gaps in home fitness routines.",
                "Explored how feedback loops could make exercise stick.",
            ]),
            (37, "Design", "Form follows exertion.", [
                "Ergonomic grip and weight distribution for home use.",
                "Embedded tech module stays accessible yet protected.",
            ]),
            (38, "Interaction", "Calories become charge.", [
                "Visual + haptic feedback ties effort to energy gain.",
                "Music intensity responds to workout performance.",
            ]),
            (39, "App", "Track, play, stay motivated.", [
                "View calories converted, battery level, and playlists.",
                "Social sharing to keep routines accountable.",
            ]),
            (40, "Prototype", "From sketch to physical model.", [
                "Iterative model making to test grip, balance, and assembly.",
            ]),
            (41, "Outcome", "Fitness meets renewable play.", [
                "A product narrative where sustainability feels rewarding, not punishing.",
            ]),
        ],
        "prev": ("SOÑAR", "sonar.html"),
        "next": ("Balanced Planet", "balanced-planet.html"),
    },
    {
        "file": "balanced-planet.html",
        "slug": "balanced-planet",
        "num": "UG 03",
        "title": "Balanced Planet",
        "subtitle": "Children's board game visualizing carbon emissions. YODEX Finalist · NPS 75 / SUS 82.",
        "tags": ["Eco-Education", "Team of 4", "Board Game"],
        "meta": [
            ("Type", "Group of 4"),
            ("Outcome", "YODEX Finalist"),
            ("Metrics", "NPS 75 · SUS 82"),
            ("Theme", "Carbon · Education"),
        ],
        "cover": "../assets/balanced-planet.png",
        "slides": [
            (18, "Concept", "Learn carbon through play.", [
                "Educational board game helping children grasp carbon emissions.",
                "Turns abstract climate data into tangible, playable decisions.",
            ]),
            (19, "Problem", "Emissions keep rising.", [
                "Global carbon output grows yearly — early education is critical.",
                "Kids need intuitive tools, not lecture slides.",
            ]),
            (20, "Framework", "Teaching angle (TA).", [
                "Structured learning goals aligned with eco-education outcomes.",
            ]),
            (21, "Gameplay", "Actions have consequences.", [
                "Every player choice maps to environmental impact.",
                "Designed for classroom and family co-play.",
            ]),
            (22, "Content", "What players encounter.", [
                "Scenario cards tie daily habits to emission outcomes.",
            ]),
            (23, "Skill cards", "Build climate literacy.", [
                "Skill cards introduce terms and strategies step by step.",
            ]),
            (24, "System", "Balanced mechanics.", [
                "Winning requires trade-offs — mirroring real sustainability tension.",
            ]),
            (25, "Experience", "Playtesting insights.", [
                "Refined pacing so children stay engaged across full sessions.",
            ]),
            (26, "Product", "Board, pieces, visual language.", [
                "Physical components visualize emission flows at a glance.",
                "Tested with users — strong usability scores.",
            ]),
        ],
        "prev": ("CLEBELL", "clebell.html"),
        "next": ("EcoHarmony", "ecoharmony.html"),
    },
    {
        "file": "ecoharmony.html",
        "slug": "ecoharmony",
        "num": "UG 04",
        "title": "EcoHarmony",
        "subtitle": "Modular air-purifying soundproof wall — cuts noise ~90%, reduces scrap-iron waste.",
        "tags": ["Product Design", "SDG 11", "Modular"],
        "meta": [
            ("Type", "Product · Sustainability"),
            ("Impact", "~90% noise reduction"),
            ("Material", "Recycled scrap iron"),
            ("Theme", "Urban · SDG 11"),
        ],
        "cover": "../assets/ug-ecoharmony.jpg",
        "slides": [
            (10, "Concept", "Quiet cities, cleaner materials.", [
                "Modular soundproof wall that also purifies air.",
                "EcoHarmony — echo-friendly urban living.",
            ]),
            (11, "Performance", "80%+ noise cut.", [
                "Lab-tested acoustic performance for residential noise.",
                "Targets traffic, construction, and neighbor bleed-through.",
            ]),
            (12, "Market", "Who needs this?", [
                "Urban residents, studios, and co-living spaces.",
                "Growing demand for home wellness products post-pandemic.",
            ]),
            (13, "Brief", "Design challenge.", [
                "Innovative soundproof wall reducing pollution and reusing waste iron.",
                "Must modularize for small apartments.",
            ]),
            (14, "Product", "ECOHARMONY system.", [
                "Panel modules stack and connect for custom wall sizes.",
            ]),
            (15, "Mechanism", "Slide rail + magnetic suction.", [
                "Tool-free assembly and reconfiguration.",
                "Magnetic joints simplify install and maintenance.",
            ]),
            (16, "Detail", "Material & airflow.", [
                "Layer structure balances absorption, purification, and structure.",
            ]),
            (17, "Outcome", "Harmony at home.", [
                "Sustainable material story + measurable acoustic gain.",
            ]),
        ],
        "prev": ("Balanced Planet", "balanced-planet.html"),
        "next": ("2ND Chance", "2nd-chance.html"),
    },
    {
        "file": "2nd-chance.html",
        "slug": "2nd-chance",
        "num": "UG 05",
        "title": "2ND Chance",
        "subtitle": "Recycled-paper gift packaging that folds into a clothes hanger — design for circularity.",
        "tags": ["Product Design", "Circularity", "Packaging"],
        "meta": [
            ("Type", "Individual · Circularity"),
            ("Material", "Recycled kraft paper"),
            ("Transform", "Packaging → hanger"),
            ("Theme", "Zero-waste · Fashion"),
        ],
        "cover": "../assets/2nd-chance.png",
        "slides": [
            (4, "Concept", "Packaging gets a second life.", [
                "Textile accessory packaging that becomes a clothes hanger.",
                "Prevents single-use waste in the gift purchase journey.",
            ]),
            (5, "Research", "From gift to trash.", [
                "Mapped packaging journey: attract → surprise → discard.",
                "Plastic pollution spikes right after unboxing.",
            ]),
            (6, "Ideation", "Unfold, fold, regenerate.", [
                "Leveraged packaging structure to transform into a hanger.",
                "DIY steps keep the ritual playful.",
            ]),
            (7, "Material", "Strong, eco, elastic.", [
                "Compared plastic, corrugated paper, and recycled kraft.",
                "Recycled kraft balances durability with environmental protection.",
            ]),
            (8, "Usage", "Four steps to a hanger.", [
                "Unfold → fold simply → regenerate hanger → extend product life.",
                "1 kg packaging offset messaging for sustainability awareness.",
            ]),
            (9, "Circular loop", "Remanufacture mindset.", [
                "Closes the loop from packaging waste to everyday utility.",
                "Circularity as a tangible user action, not a slogan.",
            ]),
        ],
        "prev": ("EcoHarmony", "ecoharmony.html"),
        "next": None,
    },
]


def render_section(page, eyebrow, title, bullets, slug, flip):
    flip_class = " flip" if flip else ""
    items = "".join(f"<li>{b}</li>" for b in bullets)
    return f"""
<section class="p-sec">
  <div class="wrap p-grid{flip_class}">
    <div class="p-text reveal">
      <span class="eyebrow">{eyebrow}</span>
      <h2>{title}</h2>
      <ul>{items}</ul>
    </div>
    <figure class="figure slide reveal d1"><img src="{ASSETS}/{slug}/slide-{page:02d}.jpg" alt="{title}"></figure>
  </div>
</section>"""


def render_page(data):
    tags = "".join(f'<span class="tag">{t}</span>' for t in data["tags"])
    meta = "".join(
        f'<div><div class="k">{k}</div><div class="v">{v}</div></div>'
        for k, v in data["meta"]
    )
    sections = ""
    for i, (page, eyebrow, title, bullets) in enumerate(data["slides"]):
        sections += render_section(page, eyebrow, title, bullets, data["slug"], flip=i % 2 == 1)

    if data["prev"]:
        prev = f'<a class="back" href="{data["prev"][1]}">← {data["prev"][0]}</a>'
    else:
        prev = '<a class="back" href="../index.html#earlier">← All work</a>'

    if data["next"]:
        nxt = f'<a class="next" href="{data["next"][1]}"><span><span class="lbl">Next project</span>{data["next"][0]}</span> →</a>'
    else:
        nxt = '<a class="next" href="../index.html#earlier"><span><span class="lbl">Back to</span>All work</span> →</a>'

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{data['title']} — Morgan Hsu</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,400;0,9..144,500;0,9..144,600;1,9..144,400&family=Sora:wght@300;400;500;600;700&family=Noto+Sans+TC:wght@400;500;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="../style.css">
</head>
<body>

<nav>
  <div class="wrap nav-in">
    <a href="../index.html" class="brand">Morgan Hsu <span class="cjk">徐梓晏</span></a>
    <div class="nav-links">
      <a href="../index.html#earlier">Earlier Work</a>
      <a href="../index.html#background">Background</a>
      <a href="../index.html#contact" class="nav-cta">Let's connect</a>
    </div>
  </div>
</nav>

<header class="p-hero">
  <div class="wrap">
    <a href="../index.html#earlier" class="back reveal">← All work</a>
    <div class="num reveal" style="margin-top:18px">{data['num']} — {data['title']}</div>
    <h1 class="reveal d1">{data['title']}</h1>
    <p class="p-sub reveal d1">{data['subtitle']}</p>
    <div class="tags p-tags reveal d2">{tags}</div>
    <div class="p-meta reveal d2">{meta}</div>
    <div class="p-cover reveal d3"><img src="{data['cover']}" alt="{data['title']}"></div>
  </div>
</header>
{sections}
<div class="wrap">
  <div class="p-nav">
    {prev}
    {nxt}
  </div>
</div>

<footer>
  <div class="wrap foot-in">
    <span>© 2026 Morgan Hsu · 徐梓晏</span>
    <span>Observe life, create better experiences.</span>
  </div>
</footer>

<script>
  const io=new IntersectionObserver((es)=>{{es.forEach(e=>{{if(e.isIntersecting){{e.target.classList.add('in');io.unobserve(e.target)}}}})}},{{threshold:.12}});
  document.querySelectorAll('.reveal').forEach(el=>io.observe(el));
</script>
</body>
</html>
"""


def main():
    PROJECTS.mkdir(parents=True, exist_ok=True)
    for data in PROJECTS_DATA:
        path = PROJECTS / data["file"]
        path.write_text(render_page(data), encoding="utf-8")
        print("wrote", path.name)


if __name__ == "__main__":
    main()
