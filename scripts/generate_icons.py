from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ICONS_DIR = Path(__file__).resolve().parent.parent / "desktop" / "src-tauri" / "icons"

WIDTH = 512
HEIGHT = 512
BG = (18, 18, 26)
ACCENT = (0, 180, 255)
ACCENT2 = (120, 80, 255)

def draw_kaos_logo(draw):
    cx, cy = WIDTH // 2, HEIGHT // 2
    r = 170

    draw.ellipse([cx - r, cy - r, cx + r, cy + r], outline=ACCENT, width=6)

    for i in range(3):
        angle = i * 120 - 90
        import math
        rad = math.radians(angle)
        x1 = cx + int(70 * math.cos(rad))
        y1 = cy + int(70 * math.sin(rad))
        x2 = cx + int(r * 0.85 * math.cos(rad))
        y2 = cy + int(r * 0.85 * math.sin(rad))
        draw.line([(x1, y1), (x2, y2)], fill=ACCENT, width=5)

    for i in range(3):
        angle = i * 120 + 90
        rad = math.radians(angle)
        x = cx + int(r * 0.65 * math.cos(rad))
        y = cy + int(r * 0.65 * math.sin(rad))
        sr = 12
        draw.ellipse([x - sr, y - sr, x + sr, y + sr], fill=ACCENT2)

    try:
        font = ImageFont.truetype("arialbd.ttf", 100)
    except Exception:
        font = ImageFont.load_default()
    bbox = draw.textbbox((0, 0), "K", font=font)
    tw = bbox[2] - bbox[0]
    th = bbox[3] - bbox[1]
    tx = cx - tw // 2
    ty = cy - th // 2 - 10
    draw.text((tx, ty), "K", fill=ACCENT, font=font)


def generate():
    ICONS_DIR.mkdir(parents=True, exist_ok=True)

    img = Image.new("RGBA", (WIDTH, HEIGHT), BG)
    draw = ImageDraw.Draw(img)
    draw_kaos_logo(draw)

    sizes = {
        "32x32.png": 32,
        "128x128.png": 128,
        "128x128@2x.png": 256,
    }

    for name, size in sizes.items():
        resized = img.resize((size, size), Image.LANCZOS)
        path = ICONS_DIR / name
        resized.save(path, "PNG")
        print(f"  {path} ({size}x{size})")

    icns_path = ICONS_DIR / "icon.icns"
    img_resized = img.resize((256, 256), Image.LANCZOS)
    img_resized.save(icns_path, "ICNS")
    print(f"  {icns_path}")

    ico_path = ICONS_DIR / "icon.ico"
    img_256 = img.resize((256, 256), Image.LANCZOS)
    img_256.save(ico_path, "ICO", sizes=[(256, 256), (128, 128), (64, 64), (48, 48), (32, 32), (16, 16)])
    print(f"  {ico_path}")


if __name__ == "__main__":
    generate()
