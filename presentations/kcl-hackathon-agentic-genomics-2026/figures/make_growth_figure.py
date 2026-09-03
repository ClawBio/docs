#!/usr/bin/env python3
"""ClawBio growth figure for the KCL agentic-genomics hackathon deck (18 Jun 2026).

Reads only the real, gathered CSVs (growth_monthly.csv, downloads_daily.csv,
clones_daily.csv) and renders a 2x3 panel styled to the ClawBio deck theme.
Top row: 4-month cumulative growth (commits, PRs, contributors).
Bottom row: recent adoption (clones + unique cloners, GitHub's 14-day window;
PyPI downloads since the 11 Jun launch). See README.md for provenance.

Regenerate:  python3 make_growth_figure.py
"""
import csv
import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))

BG = "#0d1117"
GRID = "#21262d"
TEXT = "#e6edf3"
MUTED = "#adbac7"
DIM = "#6e7681"
GREEN = "#56d364"
BLUE = "#58a6ff"
PURPLE = "#d2a8ff"
ORANGE = "#e3b341"
SALMON = "#ffa198"
TEAL = "#39c5cf"

MONTHS = {"2026-02": "Feb", "2026-03": "Mar", "2026-04": "Apr",
          "2026-05": "May", "2026-06": "Jun"}


def read(name):
    return list(csv.DictReader(open(os.path.join(HERE, name))))


def style_axes(ax):
    ax.set_facecolor(BG)
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    for s in ("bottom", "left"):
        ax.spines[s].set_color(GRID)
    ax.tick_params(colors=MUTED, labelsize=11, length=0)
    ax.grid(axis="y", color=GRID, linewidth=0.8, alpha=0.7)
    ax.set_axisbelow(True)


def panel(ax, x, xlabels, y, color, title, subtitle, headline):
    style_axes(ax)
    ax.plot(x, y, color=color, linewidth=2.6, marker="o", markersize=5,
            markerfacecolor=color, markeredgecolor=BG, zorder=3)
    ax.fill_between(x, y, color=color, alpha=0.12, zorder=1)
    ax.set_xticks(x)
    ax.set_xticklabels(xlabels)
    ax.set_ylim(0, max(y) * 1.30)
    ax.margins(x=0.04)
    ax.set_title(title, color=TEXT, fontsize=14, fontweight="bold", loc="left", pad=18)
    ax.annotate(subtitle, xy=(0, 1.02), xycoords="axes fraction", color=DIM,
                fontsize=10, ha="left", va="bottom")
    ax.annotate(headline, xy=(1, 1.04), xycoords="axes fraction", color=color,
                fontsize=19, fontweight="bold", ha="right", va="bottom")


def main():
    m = read("growth_monthly.csv")
    mx = list(range(len(m)))
    mlab = [MONTHS[r["month"]] for r in m]

    d = read("downloads_daily.csv")
    dx = list(range(len(d)))
    dlab = [r["date"][8:] for r in d]
    dcum = [int(r["downloads_cum"]) for r in d]

    c = read("clones_daily.csv")
    cx = list(range(len(c)))
    clab = [r["date"][8:] for r in c]
    clones_cum = [int(r["clones_cum"]) for r in c]
    uniq = [int(r["unique_cloners"]) for r in c]
    cticks = [0, 3, 6, 9, 13]

    fig, ax = plt.subplots(2, 3, figsize=(15, 8.2))
    fig.patch.set_facecolor(BG)
    fig.subplots_adjust(left=0.05, right=0.98, top=0.82, bottom=0.10,
                        hspace=0.52, wspace=0.22)

    panel(ax[0, 0], mx, mlab, [int(r["commits_cum"]) for r in m], GREEN,
          "Commits", "cumulative, since 25 Feb", "1,006")

    # Pull requests: opened + merged
    a = ax[0, 1]; style_axes(a)
    opened = [int(r["prs_opened_cum"]) for r in m]
    merged = [int(r["prs_merged_cum"]) for r in m]
    a.plot(mx, opened, color=BLUE, linewidth=2.6, marker="o", markersize=5,
           markerfacecolor=BLUE, markeredgecolor=BG, zorder=3, label="opened")
    a.fill_between(mx, opened, color=BLUE, alpha=0.12, zorder=1)
    a.plot(mx, merged, color=MUTED, linewidth=2.0, marker="o", markersize=4,
           markerfacecolor=MUTED, markeredgecolor=BG, linestyle="--", zorder=2, label="merged")
    a.set_xticks(mx); a.set_xticklabels(mlab); a.set_ylim(0, max(opened) * 1.30); a.margins(x=0.04)
    a.set_title("Pull requests", color=TEXT, fontsize=14, fontweight="bold", loc="left", pad=18)
    a.annotate("cumulative, since 25 Feb", xy=(0, 1.02), xycoords="axes fraction",
               color=DIM, fontsize=10, ha="left", va="bottom")
    a.annotate("188", xy=(1, 1.04), xycoords="axes fraction", color=BLUE,
               fontsize=19, fontweight="bold", ha="right", va="bottom")
    a.legend(loc="upper left", frameon=False, labelcolor=MUTED, fontsize=10)

    panel(ax[0, 2], mx, mlab, [int(r["contributors_cum"]) for r in m], PURPLE,
          "Contributors", "cumulative, since 25 Feb", "44")

    panel(ax[1, 0], cx, clab, clones_cum, ORANGE,
          "Clones", "cumulative, last 14 days", "8,617")
    ax[1, 0].set_xticks(cticks); ax[1, 0].set_xticklabels([clab[i] for i in cticks])
    ax[1, 0].set_xlabel("June 2026", color=MUTED, fontsize=10, labelpad=4)

    panel(ax[1, 1], cx, clab, uniq, SALMON,
          "Unique cloners", "per day; 611 unique over 14 days", "611")
    ax[1, 1].set_xticks(cticks); ax[1, 1].set_xticklabels([clab[i] for i in cticks])
    ax[1, 1].set_xlabel("June 2026", color=MUTED, fontsize=10, labelpad=4)

    panel(ax[1, 2], dx, dlab, dcum, TEAL,
          "PyPI downloads", "cumulative, since 11 Jun launch", "242")
    ax[1, 2].set_xlabel("June 2026", color=MUTED, fontsize=10, labelpad=4)

    fig.suptitle("ClawBio growth and adoption, 2026", color=TEXT, fontsize=22,
                 fontweight="bold", x=0.05, ha="left", y=0.95)
    fig.text(0.05, 0.90,
             "Open-source agentic-genomics skill library  ·  top row: growth since 25 Feb launch  ·  "
             "bottom row: recent adoption (GitHub retains clone traffic for 14 days only)",
             color=MUTED, fontsize=12, ha="left")
    fig.text(0.98, 0.015,
             "Sources: git history, GitHub API (stars, traffic), pypistats.org. As of 16 Jun 2026. "
             "Raw clones include CI/automation; unique cloners is the human signal.",
             color=DIM, fontsize=8.5, ha="right")

    fig.savefig(os.path.join(HERE, "growth.png"), dpi=200, facecolor=BG)
    fig.savefig(os.path.join(HERE, "growth.svg"), facecolor=BG)
    print("wrote growth.png and growth.svg")


if __name__ == "__main__":
    main()
