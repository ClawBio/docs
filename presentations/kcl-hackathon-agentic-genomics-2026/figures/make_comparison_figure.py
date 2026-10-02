#!/usr/bin/env python3
"""ClawBio vs peer open-source projects: per-month velocity comparisons.

Reads peers.csv (live GitHub data, gathered 16 Jun 2026) and renders two
horizontal bar charts styled to the ClawBio deck theme:
  comparison.png/svg  -> GitHub stars gained per month (lifetime average)
  forks.png/svg       -> forks gained per month (lifetime average)

Forks stands in for clones because GitHub clone traffic is private to each
repository's own maintainers (the traffic API returns 403 for repos you do not
own), so a cross-project clone comparison cannot be built from real data. Forks
are the public, comparable "took a copy" analog. ClawBio is highlighted; the one
faster peer is flagged dormant; project ages are shown so the lifetime-average
caveat is explicit.

Regenerate:  python3 make_comparison_figure.py
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
SALMON = "#ffa198"
COLOR = {"clawbio": GREEN, "established": BLUE, "agentic": DIM}


def age_str(mo):
    mo = float(mo)
    return f"{mo/12:.0f} yr" if mo >= 12 else f"{mo:.0f} mo"


def render(rows, metric, total_col, unit, title, subtitle, xlabel, outstem):
    rows = sorted(rows, key=lambda r: float(r[metric]))
    vals = [float(r[metric]) for r in rows]
    y = list(range(len(rows)))
    colors = [COLOR[r["category"]] for r in rows]

    fig, ax = plt.subplots(figsize=(12, 7))
    fig.patch.set_facecolor(BG)
    ax.set_facecolor(BG)
    fig.subplots_adjust(left=0.20, right=0.95, top=0.79, bottom=0.10)

    bars = ax.barh(y, vals, height=0.62, color=colors, zorder=3)
    for r, b in zip(rows, bars):
        if r["category"] == "agentic":
            b.set_hatch("///"); b.set_edgecolor(SALMON); b.set_alpha(0.55)
        if r["category"] == "clawbio":
            b.set_edgecolor(GREEN); b.set_linewidth(1.5)

    for r, yi, v in zip(rows, y, vals):
        tag = "  dormant 81 days" if r["category"] == "agentic" else ""
        c = SALMON if r["category"] == "agentic" else GREEN if r["category"] == "clawbio" else TEXT
        ax.text(v + max(vals) * 0.015, yi, f"{v:.0f}/mo", va="center", ha="left",
                color=c, fontsize=12, fontweight="bold")
        ax.text(v + max(vals) * 0.015, yi - 0.30,
                f"{int(r[total_col]):,} {unit} · {age_str(r['age_months'])}{tag}",
                va="center", ha="left", color=DIM, fontsize=9)

    ax.set_yticks(y); ax.set_yticklabels([r["label"] for r in rows], color=TEXT, fontsize=12)
    for t, r in zip(ax.get_yticklabels(), rows):
        if r["category"] == "clawbio":
            t.set_color(GREEN); t.set_fontweight("bold")
    ax.set_xlim(0, max(vals) * 1.40)
    ax.tick_params(colors=MUTED, labelsize=11, length=0)
    for s in ("top", "right", "left"):
        ax.spines[s].set_visible(False)
    ax.spines["bottom"].set_color(GRID)
    ax.grid(axis="x", color=GRID, linewidth=0.8, alpha=0.7); ax.set_axisbelow(True)
    ax.set_xlabel(xlabel, color=MUTED, fontsize=12, labelpad=8)

    fig.suptitle(title, color=TEXT, fontsize=20, fontweight="bold", x=0.20, ha="left", y=0.96)
    fig.text(0.20, 0.85, subtitle, color=MUTED, fontsize=11, ha="left", va="top", wrap=True)
    fig.text(0.95, 0.015, "Source: GitHub API, 16 Jun 2026.", color=DIM, fontsize=9, ha="right")

    fig.savefig(os.path.join(HERE, outstem + ".png"), dpi=200, facecolor=BG)
    fig.savefig(os.path.join(HERE, outstem + ".svg"), facecolor=BG)
    plt.close(fig)
    print("wrote", outstem + ".png /", outstem + ".svg")


def main():
    rows = list(csv.DictReader(open(os.path.join(HERE, "peers.csv"))))

    render(rows, "stars_per_month", "stars", "★",
           "ClawBio is growing an order of magnitude faster than\nthe tools genomics was built on",
           "Lifetime-average star velocity. ClawBio (green) is 4 months old; the established tools are 7 to 17 years "
           "old. The only faster peer, OpenClaw Medical Skills, has been dormant for 81 days.",
           "GitHub stars gained per month (average over project lifetime)", "comparison")

    render(rows, "forks_per_month", "forks", "forks",
           "ClawBio is forked an order of magnitude faster\nthan established genomics tools",
           "Lifetime-average fork velocity. GitHub clone traffic is private to each repo's maintainers, so forks "
           "(public copies of the repo) are the comparable proxy. ClawBio (green) is 4 months old; the established "
           "tools are 7 to 17 years old; the faster peer is dormant.",
           "Forks gained per month (average over project lifetime)", "forks")


if __name__ == "__main__":
    main()
