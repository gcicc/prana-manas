#!/usr/bin/env python3
"""
Generate PWA icons for Prana Manas with lotus/om visual.
Requires Pillow: pip install Pillow
"""

from PIL import Image, ImageDraw, ImageFont
import os

def create_icon(size, maskable=False):
    """Create a PWA icon with lotus/om design."""

    # Colors from Prana theme
    bg_color = (13, 17, 23)  # #0d1117
    accent_color = (196, 168, 130)  # #c4a882 (sand/gold)

    # Create image
    img = Image.new('RGBA', (size, size), bg_color + (255,))
    draw = ImageDraw.Draw(img)

    # Maskable icons need safe area
    if maskable:
        safe_margin = size // 10
    else:
        safe_margin = size // 8

    center_x, center_y = size // 2, size // 2

    # Draw lotus petals (simplified)
    petal_radius = (size // 2) - safe_margin
    num_petals = 8

    for i in range(num_petals):
        angle = (360 / num_petals) * i
        rad = angle * 3.14159 / 180

        # Petal positions
        x1 = center_x + int(petal_radius * 0.5 * math.cos(rad))
        y1 = center_y + int(petal_radius * 0.5 * math.sin(rad))

        # Draw petal as small circle
        petal_size = size // 8
        draw.ellipse(
            [x1 - petal_size//2, y1 - petal_size//2,
             x1 + petal_size//2, y1 + petal_size//2],
            fill=accent_color
        )

    # Draw center circle (om symbol area)
    center_size = size // 4
    draw.ellipse(
        [center_x - center_size//2, center_y - center_size//2,
         center_x + center_size//2, center_y + center_size//2],
        fill=accent_color
    )

    # Draw inner circle
    inner_size = size // 6
    draw.ellipse(
        [center_x - inner_size//2, center_y - inner_size//2,
         center_x + inner_size//2, center_y + inner_size//2],
        fill=bg_color
    )

    return img

import math

# Create icons
sizes = [192, 512]

for size in sizes:
    # Standard icon
    img = create_icon(size, maskable=False)
    img.save(f'icon-{size}.png')
    print(f'Created icon-{size}.png')

    # Maskable icon
    img = create_icon(size, maskable=True)
    img.save(f'icon-{size}-maskable.png')
    print(f'Created icon-{size}-maskable.png')

print('All icons generated successfully!')
