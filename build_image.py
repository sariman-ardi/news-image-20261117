#!/usr/bin/env python3
"""Build entry.png v2 for the make.fun news-image-20261117 bounty.

Draws a one-page newspaper-style front page of Tuesday 17 November
2026 world news with Pillow: 36 stories across 6 sections, grouped by
region/field. Purely a build tool: it is NOT part of the entry
repository (the entry ships only main.py, entry.png, LICENSE and
README.md). Run: python3 build_image.py  -> writes entry.png next to it.
"""
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
OUT = "entry.png"

FONT_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FONT_REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
FONT_SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"

NAVY = (16, 35, 63)
GOLD = (201, 162, 39)
PAPER = (250, 248, 242)
INK = (24, 28, 36)
MUTED = (96, 102, 112)
RULE = (208, 203, 192)

# 36 stories: (headline, one-line fact). All reported on 17 Nov 2026.
SECTIONS = [
    ("EUROPE", (179, 38, 30), [
        ("Ukraine hits Crimea bridge again",
         "Part of the Kerch bridge collapses after a second strike in 24 hours"),
        ("France hit by second nationwide strike",
         "146,000 protest as unions strike over living costs"),
        ("Moldova closes airspace after drones",
         "Russian drones cross the border; flights suspended"),
        ("Russian military plane crashes, 19 dead",
         "An-12 goes down in Kemerovo region; fault suspected"),
        ("Depardieu admits sexual assault charge",
         "French star drops appeal before a Paris court"),
        ("Berlin raids Hezbollah-linked network",
         "Police raid 28 sites and ban the association"),
    ]),
    ("MIDDLE EAST", (194, 94, 0), [
        ("Iran fires drones at U.S. base in Bahrain",
         "Guards target a U.S. radar site; attack intercepted"),
        ("U.S. strikes IRGC site on Qeshm Island",
         "Strikes follow Iranian attacks on U.S. facilities"),
        ("Tanker hit near Strait of Hormuz",
         "Ships struck by suspected mines as strait stays shut"),
        ("Houthis advance in Yemen; army retreats",
         "Government forces pull back from the Red Sea coast"),
        ("West urges Israel to open Gaza crossings",
         "UK, Australia, Canada, Italy demand rapid aid access"),
        ("Settlers shoot dead Palestinian woman, 72",
         "Killed near Jericho, health ministry says"),
    ]),
    ("ASIA-PACIFIC", (14, 124, 123), [
        ("Xi, Trump and Putin to meet in Shenzhen",
         "First three-way summit set for Thursday at APEC"),
        ("APEC summit opens in Shenzhen",
         "Putin arrives as China hosts the 33rd leaders' meeting"),
        ("Japan scrambles jets over Russian planes",
         "Two suspected Russian aircraft violate airspace"),
        ("India and Japan hold 2+2 defence talks",
         "Foreign and defence ministers meet in Tokyo"),
        ("Quad unveils minerals pacts in Manila",
         "Trump announces critical-minerals and defence deals"),
        ("U.S. curbs China's remote AI chip access",
         "New export rule hits data centres; Beijing vows payback"),
    ]),
    ("AMERICAS", (31, 78, 121), [
        ("Pentagon fails its audit \u2014 9th year in a row",
         "Auditors cannot verify $4.8 trillion in assets"),
        ("U.S. loses measles-free status after 26 years",
         "5,400 cases and 10 deaths, a 40-year high"),
        ("Trump shrugs off U.S. outages as \u2018life\u2019",
         "Microsoft, FAA, United and JPMorgan hit in six days"),
        ("FEMA and FCC test emergency alert system",
         "One-minute nationwide TV and radio test at 2:20 p.m."),
        ("South Florida under flood watch",
         "Up to 10 inches of rain forecast through Friday"),
        ("U.S. soldier held in UK over spying claim",
         "Taken into U.S. military custody after arrest"),
    ]),
    ("AFRICA", (110, 80, 150), [
        ("South Africa warns of storms and heat",
         "Severe thunderstorms, winds and extreme heat forecast"),
        ("Zimbabwe beat Equatorial Guinea 3\u20130",
         "AFCON qualifiers: win in Harare boosts their hopes"),
        ("Senegal stay unbeaten with 4\u20132 win",
         "AFCON qualifiers: Senegal beat Sudan in Juba"),
        ("Angola central bank eases as prices cool",
         "Policy eased further with inflation still falling"),
        ("Rwanda genocide trial opens in Paris",
         "Ex-shopkeeper tried over 1994 checkpoint killings"),
        ("Togo stun Algeria 3\u20130 in Cup qualifying",
         "Three first-half goals cut Group I lead to one point"),
    ]),
    ("BUSINESS \u00b7 TECH \u00b7 SPORT", (46, 125, 50), [
        ("Nvidia beats forecasts after CEO exit",
         "Revenue $115.8bn tops estimates under interim chief"),
        ("AMD closes $8.2bn deal for World Labs",
         "All-stock buy of spatial-AI startup completed"),
        ("Isomorphic Labs raises $5bn for AI drugs",
         "Alphabet unit's Series C to scale drug design"),
        ("MBZUAI launches giant K2-Horizon AI model",
         "375-billion-parameter model tops tool-use tests"),
        ("Germany crush Netherlands 5\u20130",
         "Nations League: dominant win in European football"),
        ("Alcaraz beats Tiafoe at ATP Finals",
         "6\u20132, 6\u20132 win in Turin; Medvedev also through"),
    ]),
]


def font(path, size):
    return ImageFont.truetype(path, size)


def fit_one_line(d, text, fnt, max_w):
    """Truncate to a single line with an ellipsis if it is too wide."""
    if d.textlength(text, font=fnt) <= max_w:
        return text
    ell = "\u2026"
    lo, hi = 0, len(text)
    while lo < hi:
        mid = (lo + hi + 1) // 2
        if d.textlength(text[:mid] + ell, font=fnt) <= max_w:
            lo = mid
        else:
            hi = mid - 1
    return text[:lo].rstrip() + ell


def draw_globe(d, cx, cy, r, color):
    d.ellipse([cx - r, cy - r, cx + r, cy + r], outline=color, width=3)
    d.ellipse([cx - r * 0.45, cy - r, cx + r * 0.45, cy + r],
              outline=color, width=2)
    d.line([cx - r, cy, cx + r, cy], fill=color, width=2)
    d.arc([cx - r, cy - r * 0.55, cx + r, cy + r * 0.55],
          start=200, end=340, fill=color, width=2)
    d.arc([cx - r, cy - r * 0.55, cx + r, cy + r * 0.55],
          start=20, end=160, fill=color, width=2)


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # ---- masthead ----
    d.rectangle([0, 0, W, 96], fill=NAVY)
    d.rectangle([0, 96, W, 99], fill=GOLD)
    draw_globe(d, 50, 48, 26, GOLD)
    d.text((88, 16), "THE WORLD IN ONE DAY",
           font=font(FONT_BOLD, 18), fill=GOLD)
    d.text((86, 40), "Tuesday, 17 November 2026",
           font=font(FONT_SERIF, 40), fill=(255, 255, 255))
    f_side = font(FONT_BOLD, 21)
    d.text((1000 - d.textlength("36 STORIES", font=f_side), 22),
           "36 STORIES", font=f_side, fill=GOLD)
    f_side2 = font(FONT_BOLD, 15)
    d.text((1000 - d.textlength("6 CONTINENTS", font=f_side2), 52),
           "6 CONTINENTS", font=f_side2, fill=(255, 255, 255))

    # ---- subhead: the day's three biggest stories ----
    d.text((24, 104),
           "Crimea bridge hit  \u00b7  Gulf strikes  \u00b7  Xi\u2013Trump\u2013Putin summit",
           font=font(FONT_BOLD, 16), fill=INK)

    # ---- sections ----
    f_sec = font(FONT_BOLD, 15)
    f_head = font(FONT_BOLD, 15)
    f_sub = font(FONT_REG, 12)
    margin, gutter = 24, 16
    col_w = (W - 2 * margin - gutter) // 2
    y = 128
    for name, color, stories in SECTIONS:
        # section header: colour chip + name + rule
        d.rectangle([margin, y + 6, margin + 12, y + 18], fill=color)
        d.text((margin + 20, y + 2), name, font=f_sec, fill=color)
        name_w = d.textlength(name, font=f_sec)
        rule_x = margin + 20 + name_w + 12
        d.line([rule_x, y + 12, W - margin, y + 12], fill=RULE, width=2)
        gy = y + 26
        for i, (head, sub) in enumerate(stories):
            col, row = i % 2, i // 2
            x = margin + col * (col_w + gutter)
            cy = gy + row * 40
            d.text((x, cy + 1),
                   fit_one_line(d, head, f_head, col_w),
                   font=f_head, fill=INK)
            d.text((x, cy + 21),
                   fit_one_line(d, sub, f_sub, col_w),
                   font=f_sub, fill=(74, 80, 92))
        y += 144

    # ---- footer ----
    d.line([24, 998, W - 24, 998], fill=RULE, width=2)
    d.text((24, 1005),
           "Events of Tuesday 17 November 2026, as reported. "
           "Sources: Reuters \u00b7 Al Jazeera \u00b7 AP \u00b7 BBC \u00b7 Sky Sports \u00b7 IANS \u00b7 Le Monde",
           font=font(FONT_REG, 12), fill=MUTED)

    img.save(OUT, "PNG")
    print("wrote", OUT, img.size)


if __name__ == "__main__":
    main()
