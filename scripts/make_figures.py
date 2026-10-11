#!/usr/bin/env python3
"""Figure generator for *Knowing the Constant*.

Every figure is computed from stated parameters. No figure is reproduced from any published
source. Each function writes one PNG into `figures/` and prints the parameters it used, so that
the manuscript caption can state the provenance.

Usage:
    python scripts/make_figures.py            # all figures
    python scripts/make_figures.py fig01      # one figure

Dependencies: numpy, Pillow. Deliberately not matplotlib, so that the figures can be regenerated
with the same minimal stack used to develop the manuscript.
"""
from __future__ import annotations

import math
import os
import sys

import numpy as np
from PIL import Image, ImageDraw, ImageFont

W = 1200
BG = (255, 255, 255)
INK = (34, 34, 34)
GRAY = (140, 140, 140)
GRID = (230, 234, 238)
AXIS = (200, 206, 212)
BLUE = (47, 93, 140)
RED = (168, 62, 52)
GREEN = (58, 122, 92)
ORANGE = (196, 124, 46)

OUTDIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "figures")

FONT_CANDIDATES = [
    r"C:\Windows\Fonts\segoeui.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    "/System/Library/Fonts/Helvetica.ttc",
]
FONT_BOLD_CANDIDATES = [
    r"C:\Windows\Fonts\segoeuib.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
    "/System/Library/Fonts/Helvetica.ttc",
]


def _load(candidates, size):
    for path in candidates:
        if os.path.exists(path):
            try:
                return ImageFont.truetype(path, size)
            except OSError:
                continue
    return ImageFont.load_default()


_F = {}


def font(size, bold=False):
    key = (size, bold)
    if key not in _F:
        _F[key] = _load(FONT_BOLD_CANDIDATES if bold else FONT_CANDIDATES, size)
    return _F[key]


def canvas(height):
    im = Image.new("RGB", (W, height), BG)
    return im, ImageDraw.Draw(im)


def text(d, xy, s, size=17, bold=False, fill=INK, anchor="la"):
    d.text(xy, s, font=font(size, bold), fill=fill, anchor=anchor)


def head(d, title, notes):
    text(d, (70, 30), title, 23, True)
    y = 64
    for n in notes:
        text(d, (70, y), n, 15.5, fill=GRAY)
        y += 24
    return y


def axes(im, d, l, t, r, b, xticks, yticks, xlab, ylab):
    d.rectangle([l, t, r, b], outline=AXIS, width=1)
    for gx, lab in xticks:
        d.line([gx, t, gx, b], fill=GRID, width=1)
        text(d, (gx, b + 9), lab, 15, fill=GRAY, anchor="ma")
    for gy, lab in yticks:
        d.line([l, gy, r, gy], fill=GRID, width=1)
        text(d, (l - 10, gy), lab, 15, fill=GRAY, anchor="rm")
    text(d, ((l + r) / 2, b + 40), xlab, 16, fill=(95, 95, 95), anchor="ma")
    tmp = Image.new("RGB", (340, 36), BG)
    ImageDraw.Draw(tmp).text((170, 18), ylab, font=font(16), fill=(95, 95, 95),
                             anchor="mm")
    tmp = tmp.rotate(90, expand=True)
    im.paste(tmp, (int(l - 118), int((t + b) / 2 - tmp.height / 2)))


def chip(d, x, y, col, label, size=15):
    d.rectangle([x, y + 4, x + 18, y + 18], fill=col)
    text(d, (x + 26, y), label, size)


def save(im, name):
    os.makedirs(OUTDIR, exist_ok=True)
    path = os.path.join(OUTDIR, name)
    im.save(path)
    print(f"  wrote {path}")


# ----------------------------------------------------------------------------
def fig01():
    """Tail comparison: Gaussian vs power-law tail, on log-log axes.

    Parameters used (stated in the caption):
      Gaussian   : density exp(-x^2/2)/sqrt(2*pi)
      fat tailed : survival P(X > x) = x^-1.7 for x >= 1
    Both are expressed as survival probabilities, so the vertical axis is comparable.
    """
    x = np.logspace(0, 1.8, 400)
    gauss_surv = np.array([0.5 * math.erfc(v / math.sqrt(2)) for v in x])
    power_surv = x ** -1.7

    im, d = canvas(680)
    l, t, r, b = 180, 150, 1110, 560
    head(d, "The diagnostic plot: how fast the tail decays",
         ["Vertical axis: probability of a change larger than x. Horizontal axis: x, in units of",
          "the typical change. Both logarithmic. Computed for this book from the stated families."])
    X = lambda v: l + (np.log10(v) - 0) / 1.8 * (r - l)
    lo, hi = 1e-6, 1.2
    Y = lambda v: b - (np.log10(max(v, lo)) - np.log10(lo)) / \
        (np.log10(hi) - np.log10(lo)) * (b - t)
    xt = [(X(v), f"{v:g}") for v in (1, 2, 5, 10, 20, 60)]
    yt = [(Y(v), f"{v:g}") for v in (1e-5, 1e-4, 1e-3, 1e-2, 1e-1, 1)]
    axes(im, d, l, t, r, b, xt, yt,
         "size of the change (multiples of the typical change)",
         "probability of exceeding it")
    d.line([(X(v), Y(w)) for v, w in zip(x, gauss_surv)], fill=BLUE, width=3)
    d.line([(X(v), Y(w)) for v, w in zip(x, power_surv)], fill=RED, width=3)
    chip(d, X(2.2), Y(3e-4), BLUE, "Gaussian: the line dives")
    chip(d, X(2.2), Y(4e-3), RED, "power-law tail: the line stays straight")
    text(d, (X(1.02), Y(3e-6)),
         "At 20 typical changes out, the Gaussian is below one in a million; "
         "the power-law tail is still near one in a thousand.", 16, fill=(110, 110, 110))
    save(im, "fig01-tail-comparison.png")




def fig02():
    """Koch curve refinement at three resolutions.

    Construction: each segment is replaced by four segments of one third the length,
    so N = 4 and r = 1/3, giving D = log 4 / log 3 = 1.2619 exactly.
    """
    def koch_points(order, size=1.0):
        pts = [(0.0, 0.0), (size, 0.0)]
        for _ in range(order):
            new = []
            for i in range(len(pts) - 1):
                ax, ay = pts[i]
                bx, by = pts[i + 1]
                dx, dy = bx - ax, by - ay
                length = (dx * dx + dy * dy) ** 0.5
                ux, uy = dx / length, dy / length
                ang = math.atan2(dy, dx)
                def pol(t, ll):
                    return (ax + math.cos(ang + t) * ll, ay + math.sin(ang + t) * ll)
                new += [pts[i], pol(0, length / 3), pol(-math.pi / 3, length / 3),
                        pol(0, 2 * length / 3)]
            new.append(pts[-1])
            pts = new
        return pts

    im, d = canvas(760)
    head(d, "Same construction, three resolutions",
         ["Each refinement replaces one segment with four of one third the length:",
          "N = 4, r = 1/3, so D = log 4 / log 3 = 1.2619 exactly. Drawn for this book."])
    for row, order in enumerate((1, 3, 5)):
        pts = koch_points(order, size=760.0)
        y0 = 190 + row * 175
        xs = [p[0] for p in pts]
        ys = [p[1] for p in pts]
        sx = 900.0 / max(xs)
        sy = 90.0 / (max(ys) + 1e-9) if max(ys) > 0 else 1.0
        xy = [(120 + x * sx, y0 - y * sy) for x, y in zip(xs, ys)]
        d.line(xy, fill=(47, 93, 140) if row == 0 else (168, 62, 52) if row == 1 else (58, 122, 92), width=2)
        text(d, (120, y0 + 14), f"order {order}: 4^{order} = {4 ** order} segments",
             16, fill=(120, 120, 120))
    text(d, (120, 700), "Length grows by 4/3 at every step. The curve never leaves the box.",
         16, fill=(110, 110, 110))
    save(im, "fig02-koch-refinement.png")


if __name__ == "__main__":
    wanted = sys.argv[1:]
    figs = {"fig01": fig01, "fig02": fig02}
    for name, fn in figs.items():
        if wanted and name not in wanted:
            continue
        print(f"{name}:")
        fn()
