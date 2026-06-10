#!/usr/bin/env python3
"""Build a seamless sliding marquee GIF of tech stack icons for GitHub README.

Downloads SVG icons from skillicons.dev, rasterises with cairosvg, then builds
a smooth right-to-left marquee GIF composited onto GitHub dark background.
No transparency or special disposal needed — the background matches the page.
"""

import io
import os
import ssl
import urllib.request
from PIL import Image
import cairosvg


# ── Work around skillicons.dev blocking default urllib user-agent ─────────────
ssl_ctx = ssl.create_default_context()
OPENER = urllib.request.build_opener(urllib.request.HTTPSHandler(context=ssl_ctx))
OPENER.addheaders = [("User-Agent", "Mozilla/5.0 (compatible; tech-marquee-builder/1.0)")]
urllib.request.install_opener(OPENER)


# ── Config ────────────────────────────────────────────────────────────────────
ICONS = [
    "react", "nextjs", "ts", "tailwind", "python", "java",
    "ruby", "nodejs", "docker", "linux", "bash", "git",
    "githubactions", "postgres", "vagrant", "convex", "netlify",
    "spring", "ansible", "redhat",
]

ICON_SIZE = 48             # pixel dimension per icon
GAP = 12                   # pixels between icons
VIEWPORT_W = 680           # viewport width (matches header SVG max-width)
VIEWPORT_H = ICON_SIZE     # viewport height
FRAME_STEP = 3             # pixels to shift per frame
FRAME_DELAY_MS = 50        # delay per frame (5 cs)
BG_COLOR = (13, 17, 23)   # GitHub dark background (#0d1117)

CACHE_DIR = "/tmp/tech_icons"
OUTPUT = "/home/ntoampi/Documents/Projects/Lintshiwe/assets/tech-slideshow.gif"


# ── Helpers ───────────────────────────────────────────────────────────────────
def download_svg_as_png(name: str) -> Image.Image:
    """Fetch SVG from skillicons.dev and rasterise to 48×48 RGBA PIL image."""
    png_path = os.path.join(CACHE_DIR, f"{name}.png")
    if os.path.exists(png_path):
        img = Image.open(png_path)
        img.load()
        return img.convert("RGBA")

    print(f"  Downloading + rasterising {name}...")
    url = f"https://skillicons.dev/icons?i={name}"
    req = urllib.request.Request(url, headers={
        "User-Agent": "Mozilla/5.0 (compatible; tech-marquee-builder/1.0)",
    })
    with urllib.request.urlopen(req) as resp:
        svg_data = resp.read()

    png_bytes = cairosvg.svg2png(
        bytestring=svg_data,
        output_width=ICON_SIZE,
        output_height=ICON_SIZE,
        background_color="transparent",
    )
    img = Image.open(io.BytesIO(png_bytes)).convert("RGBA")
    img.save(png_path, "PNG")
    return img


# ── Download / rasterise all icons ────────────────────────────────────────────
os.makedirs(CACHE_DIR, exist_ok=True)

icon_imgs: list[Image.Image] = []
for name in ICONS:
    img = download_svg_as_png(name)
    if img.size != (ICON_SIZE, ICON_SIZE):
        img = img.resize((ICON_SIZE, ICON_SIZE), Image.LANCZOS)
    icon_imgs.append(img)
    print(f"    {name}: {img.size} {img.mode}")

print(f"\n{len(icon_imgs)} icons ready.")


# ── Build the full icon strip (N icons × 2 for seamless loop) ────────────────
UNIT = ICON_SIZE + GAP                            # 60 px per icon slot
STRIP_W = len(ICONS) * UNIT                       # pixels for one full set
TOTAL_W = STRIP_W * 2                             # two full sets for seamless loop

# Create strip composited onto GitHub dark background
strip_img = Image.new("RGBA", (TOTAL_W, VIEWPORT_H), BG_COLOR + (255,))
for i in range(len(ICONS) * 2):
    x = i * UNIT
    strip_img.paste(icon_imgs[i % len(ICONS)], (x, 0), icon_imgs[i % len(ICONS)])

print(f"Strip built: {strip_img.size}")

# Convert to RGB (flatten alpha against the dark background)
# Since we pasted icons with their alpha masks onto BG_COLOR, there's
# no real transparency left — just convert directly.
strip_rgb = strip_img.convert("RGB")


# ── Quantize to shared palette ────────────────────────────────────────────────
print(f"Quantizing strip to 64-colour palette...")
palette_strip = strip_rgb.quantize(
    colors=64,
    method=Image.Quantize.FASTOCTREE,
    dither=Image.Dither.NONE,
)

print(f"Strip quantized: {palette_strip.mode}")


# ── Generate frames from the palette strip ────────────────────────────────────
# Each frame is simply cropped from the pre-processed P-mode strip.
# Since the strip was composited onto the background colour, no disposal
# or transparency handling is needed.
num_frames = STRIP_W // FRAME_STEP
frames: list[Image.Image] = []

print(f"Generating {num_frames} frames (step={FRAME_STEP}px, "
      f"delay={FRAME_DELAY_MS}ms)...")

for fi in range(num_frames):
    x = fi * FRAME_STEP
    frames.append(palette_strip.crop((x, 0, x + VIEWPORT_W, VIEWPORT_H)))

    if (fi + 1) % 100 == 0:
        print(f"    ... {fi + 1}/{num_frames} frames done")


# ── Save as optimised GIF ─────────────────────────────────────────────────────
total_sec = num_frames * FRAME_DELAY_MS / 1000
print(f"\nSaving GIF: {num_frames} frames × {FRAME_DELAY_MS}ms = "
      f"{total_sec:.1f}s loop")

frames[0].save(
    OUTPUT,
    save_all=True,
    append_images=frames[1:],
    duration=FRAME_DELAY_MS,
    loop=0,            # infinite loop
    optimize=True,     # LZW + remove duplicates
    disposal=1,        # do not dispose (solid frames, no transparency needed)
)

size_kb = os.path.getsize(OUTPUT) / 1024
print(f"Saved to: {OUTPUT}")
print(f"File size: {size_kb:.1f} KB ({os.path.getsize(OUTPUT):,} bytes)")
print("Done")
