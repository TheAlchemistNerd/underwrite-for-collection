"""Generate the Part 1 dated, separately scoped population chart panel.

The values reproduce data cited in Part 1. The panels intentionally retain their
populations and dates rather than presenting unlike observations as one series.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


DEEP_BLUE = "#2E4A62"
LINK_BLUE = "#0078D4"
TEAL = "#16857B"
GOLD = "#D8A028"
RED = "#B5524A"
PALE_GOLD = "#FFF4D6"
SLATE = "#526D82"
GRID = "#D5DEE5"
TEXT = "#17324D"


def style_axis(axis, title: str, subtitle: str) -> None:
    axis.set_facecolor("white")
    axis.set_title(title, loc="left", fontsize=16, fontweight="bold", color=DEEP_BLUE, pad=22)
    axis.text(
        0,
        1.025,
        subtitle,
        transform=axis.transAxes,
        ha="left",
        va="bottom",
        fontsize=10.5,
        color=SLATE,
    )
    for spine in axis.spines.values():
        spine.set_color(GRID)
        spine.set_linewidth(1.0)


def add_horizontal_labels(axis, containers) -> None:
    for container in containers:
        axis.bar_label(
            container,
            labels=[f"{bar.get_width():.1f}%" for bar in container],
            padding=5,
            fontsize=10.5,
            color=TEXT,
        )


def main() -> None:
    plt.rcParams.update(
        {
            "font.family": "Arial",
            "font.size": 11,
            "axes.labelcolor": TEXT,
            "xtick.color": TEXT,
            "ytick.color": TEXT,
            "text.color": TEXT,
        }
    )

    figure = plt.figure(figsize=(10, 14), dpi=240, facecolor="white", constrained_layout=True)
    grid = figure.add_gridspec(3, 1, height_ratios=[1.0, 1.2, 1.15], hspace=0.22)

    # Panel A: grouped bars within one fixed CBK MSME population.
    axis_a = figure.add_subplot(grid[0, 0])
    style_axis(
        axis_a,
        "A. Account and value lenses within one MSME population",
        "CBK surveyed banking industry, December 2024",
    )
    categories = ["Account count", "Outstanding value"]
    npl_share = np.array([28.4, 19.1])
    non_npl_share = 100.0 - npl_share
    positions = np.arange(len(categories))
    bar_height = 0.30
    npl_bars = axis_a.barh(
        positions - bar_height / 2,
        npl_share,
        height=bar_height,
        label="NPL share",
        color=RED,
    )
    other_bars = axis_a.barh(
        positions + bar_height / 2,
        non_npl_share,
        height=bar_height,
        label="Non-NPL share",
        color=TEAL,
    )
    axis_a.set_yticks(positions, categories)
    axis_a.invert_yaxis()
    axis_a.set_xlim(0, 100)
    axis_a.set_xlabel("Share of the stated population (%)")
    axis_a.xaxis.grid(True, color=GRID, linewidth=0.8)
    axis_a.set_axisbelow(True)
    axis_a.legend(
        loc="upper right",
        bbox_to_anchor=(1.0, 1.12),
        frameon=False,
        ncol=2,
    )
    add_horizontal_labels(axis_a, [npl_bars, other_bars])

    # Panel B: horizontal bars with separate scopes and reporting dates.
    axis_b = figure.add_subplot(grid[1, 0])
    style_axis(
        axis_b,
        "B. Value-based NPL ratios across separately scoped populations",
        "The values are a scope comparison, not a time series",
    )
    population_labels = [
        "CBK surveyed MSMEs\nDec 2024",
        "CBK all commercial banks\nDec 2025",
        "KBA selected MSMEs\nJun 2026",
        "CBK all commercial banks\nJun 2026",
    ]
    population_values = [19.1, 16.0, 24.5, 14.8]
    population_colours = [LINK_BLUE, DEEP_BLUE, GOLD, SLATE]
    bars = axis_b.barh(
        np.arange(len(population_labels)),
        population_values,
        height=0.62,
        color=population_colours,
    )
    axis_b.set_yticks(np.arange(len(population_labels)), population_labels)
    axis_b.invert_yaxis()
    axis_b.set_xlim(0, 30)
    axis_b.set_xlabel("Reported value-based NPL ratio (%)")
    axis_b.xaxis.grid(True, color=GRID, linewidth=0.8)
    axis_b.set_axisbelow(True)
    axis_b.bar_label(
        bars,
        labels=[f"{value:.1f}%" for value in population_values],
        padding=5,
        fontsize=10.5,
        fontweight="bold",
        color=TEXT,
    )

    # Panel C: pie chart for the approximate active-account composition.
    axis_c = figure.add_subplot(grid[2, 0])
    style_axis(
        axis_c,
        "C. Approximate active-account composition",
        "CBK surveyed banking industry, December 2024",
    )
    pie_values = [80, 20]
    pie_labels = ["Micro enterprises", "Small and medium\nenterprises combined"]
    _, _, percentages = axis_c.pie(
        pie_values,
        labels=pie_labels,
        colors=[LINK_BLUE, PALE_GOLD],
        startangle=90,
        counterclock=False,
        autopct="%1.0f%%",
        pctdistance=0.68,
        labeldistance=1.08,
        wedgeprops={"linewidth": 1.5, "edgecolor": "white"},
        textprops={"fontsize": 11, "color": TEXT},
    )
    percentages[0].set_color("white")
    percentages[0].set_fontweight("bold")
    percentages[1].set_color(DEEP_BLUE)
    percentages[1].set_fontweight("bold")
    figure.suptitle(
        "Matched populations reveal different credit-risk questions",
        fontsize=21,
        fontweight="bold",
        color=DEEP_BLUE,
        x=0.02,
        ha="left",
    )
    output = Path(__file__).resolve().parents[1] / "assets" / "figures" / "part1_matched_population_views.png"
    output.parent.mkdir(parents=True, exist_ok=True)
    figure.savefig(output, dpi=240, facecolor="white", bbox_inches="tight")
    plt.close(figure)
    print(output)


if __name__ == "__main__":
    main()
