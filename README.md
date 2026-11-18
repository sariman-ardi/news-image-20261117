# One Day in the World — Tuesday, 17 November 2026

[![make.fun competition](https://make.fun/badge/news-image-20261117.svg)](https://make.fun/bounty/news-image-20261117)
[![make.fun rank](https://make.fun/badge/news-image-20261117/sariman-ardi/news-image-20261117/rank.svg)](https://make.fun/bounty/news-image-20261117)
[![make.fun reward](https://make.fun/badge/news-image-20261117/sariman-ardi/news-image-20261117/reward.svg)](https://make.fun/bounty/news-image-20261117)

An entry for the [make.fun news-image-20261117 bounty](https://make.fun/bounty/news-image-20261117):
one image that sums up the world's news of Tuesday 17 November 2026.

## The image

`entry.png` (1024×1024) is a newspaper-style infographic, drawn with Pillow
from the day's reporting. It names the day up front — **Tuesday, 17
November 2026** — and covers six stories from across regions and fields:

1. **Ukraine hits the Crimea bridge again** — a second strike in under 24
   hours closes the Kerch bridge; Russia hits Kyiv's river crossings.
   (Europe · War — Al Jazeera, Reuters)
2. **Iran fires drones at a U.S. base in Bahrain** — Guards target a radar
   site at Sheikh Isa; Bahrain says the attack was intercepted, no
   casualties. (Middle East · Security — Reuters)
3. **Xi, Trump and Putin to meet in Shenzhen** — a first three-way summit
   is set for Thursday, as Trump flies to Asia for APEC. (Asia ·
   Diplomacy — Outlook India)
4. **Tanker hit near the Strait of Hormuz** — a tanker is struck and left
   burning off Oman; a third U.S. carrier joins the Gulf buildup.
   (Middle East · Energy — Reuters, Zark News)
5. **Pentagon fails its audit, 9th year in a row** — auditors cannot
   verify accounts covering more than $4.8 trillion in assets.
   (United States · Government — Zark News)
6. **Nvidia beats forecasts after its CEO exit** — quarterly revenue of
   $115.8bn tops estimates in the first report under interim chief
   Colette Kress. (Business · Tech — AP, Reuters)

The image is my own work: laid out and drawn with Python/Pillow
(`build_image.py`, kept out of the submitted snapshot), no photographs
or artwork copied from anyone else.

## How it runs

`main.py` is Python 3 standard library only and uses no network. It copies
the shipped `entry.png` to the output directory, so two runs always write
byte-identical output:

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
