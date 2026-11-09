"""Render the labeled age-group comparison from the supplied Power BI export."""
from html import escape
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main():
    data = json.loads((ROOT / 'data/nsduh-display-summary.json').read_text())
    rows = data['age_groups']
    peak = max(rows, key=lambda row: row['percent'])
    parts = [
        '<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="800" viewBox="0 0 1200 800" role="img" aria-labelledby="title desc">',
        '<title id="title">High-distress share by age group</title>',
        '<desc id="desc">Percentages labeled in the supplied NSDUH report: ages 15–20, 32.92%; 21–30, 48.41%; 31–45, 31.47%; 46–60, 18.81%.</desc>',
        '<rect width="1200" height="800" fill="#f4f0e6"/>',
        '<rect width="1200" height="160" fill="#171713"/>',
        '<g font-family="Arial, Helvetica, sans-serif">',
        '<text x="64" y="60" font-size="23" letter-spacing="2" fill="#d9f13a">NSDUH · 2021–2024 REPORT</text>',
        '<text x="64" y="116" font-size="43" font-weight="700" fill="#fffaf0">High-distress share by age group</text>',
        '<text x="64" y="218" font-size="25" fill="#4f4d47">Ages 21–30 have the highest share in the displayed comparison.</text>',
    ]
    left, top, width, maximum = 224, 294, 800, 50
    for tick in range(0, 51, 10):
        x = left + width * tick / maximum
        parts.extend([
            f'<line x1="{x}" y1="{top-30}" x2="{x}" y2="646" stroke="#d8d3c8" stroke-width="1"/>',
            f'<text x="{x}" y="683" text-anchor="middle" font-size="22" fill="#66645c">{tick}%</text>',
        ])
    for i, row in enumerate(rows):
        y = top + i * 94
        color = '#611f2a' if row == peak else '#8a8981'
        bar_width = width * row['percent'] / maximum
        parts.extend([
            f'<text x="176" y="{y+35}" text-anchor="end" font-size="32" fill="#171713">{escape(row["age_group"])}</text>',
            f'<rect x="{left}" y="{y}" width="{bar_width:.2f}" height="54" rx="3" fill="{color}"/>',
            f'<text x="{left+bar_width+16:.2f}" y="{y+35}" font-size="29" font-weight="700" fill="#171713">{row["percent"]:.2f}%</text>',
        ])
    parts.extend([
        '<text x="64" y="748" font-size="21" fill="#4f4d47">Source: percentages labeled in the supplied Power BI report.</text>',
        '<text x="64" y="778" font-size="18" fill="#66645c">Report-defined categories · age-group comparison · descriptive survey analysis</text>',
        '</g></svg>',
    ])
    (ROOT / 'images/projects/nsduh-overview.svg').write_text('\n'.join(parts) + '\n')


if __name__ == '__main__':
    main()
