"""Render the 1200×630 social image from a vector layout and the unchanged portrait."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle

ROOT = Path(__file__).resolve().parents[1]


def main():
    fig = plt.figure(figsize=(12, 6.3), dpi=100, facecolor='#f4f0e6')
    ax = fig.add_axes((0, 0, 1, 1))
    ax.set(xlim=(0, 1200), ylim=(630, 0))
    ax.axis('off')
    ax.add_patch(Rectangle((0, 616), 1200, 14, color='#171713'))
    portrait = mpimg.imread(ROOT / 'images/grace-ngo-headshot.jpg')
    image = ax.imshow(portrait, extent=(850, 1110, 440, 180))
    image.set_clip_path(Circle((980, 310), 130, transform=ax.transData))
    ax.add_patch(Circle((980, 310), 142, fill=False, edgecolor='#d7d0c2', linewidth=.8))
    def text(x, y, value, size, family='DejaVu Sans', color='#171713', weight='normal'):
        ax.text(x, y, value, fontsize=size * .72, fontfamily=family,
                color=color, fontweight=weight, va='baseline')
    text(72, 136, 'PORTFOLIO', 18, color='#66645c', weight='bold')
    text(72, 248, 'Grace Ngo', 96, family='DejaVu Serif')
    text(72, 324, 'Business & Data Analytics', 37, family='DejaVu Serif')
    text(72, 382, 'SQL · Python · Power BI · Excel', 20, color='#66645c')
    text(72, 414, 'Clear questions. Inspectable results.', 20, color='#66645c')
    text(72, 478, 'gracengg.github.io', 18, weight='bold')
    fig.savefig(ROOT / 'images/og-portfolio.png', dpi=100)
    plt.close(fig)


if __name__ == '__main__':
    main()
