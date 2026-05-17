#!/usr/bin/env python3
"""
Optimize raw project screenshots into the web-ready set the site uses.

USAGE
-----
1. Drop the raw screenshots into:
       img/projects-raw/<slug>/...
   For example:
       img/projects-raw/mount-vernon-website/George-Washington-s-Mount-Vernon.png
       img/projects-raw/be-washington/Screenshot 2026-05-17 at 12.09.01 PM.png

2. Edit the JOBS dict below if you want to change which screenshots map to
   which output names, or swap crop strategies.

3. Run:
       python3 tools/optimize_screenshots.py

This writes a thumbnail (cropped where useful) AND a tall full-page variant
into img/projects/<slug>/ for each entry:

       hero.jpg            (cropped 3:2 thumbnail for the page)
       hero.webp
       hero-full.jpg       (full uncropped, scaled to 1400w — for lightbox)
       hero-full.webp

The lightbox JS auto-loads the -full variant if it exists.
"""
from __future__ import annotations
from pathlib import Path
from PIL import Image
import os, sys

ROOT = Path(__file__).resolve().parent.parent
RAW_BASE = ROOT / "img" / "projects-raw"
OUT_BASE = ROOT / "img" / "projects"

# Crop strategy: 'top'  -> use the top of a tall screenshot (for hero/page screenshots)
#                'center' -> center crop (for centered subjects)
#                None  -> no crop (for screenshots that are already a reasonable aspect)
# THUMB_RATIO is the width/height ratio used for the cropped thumbnail.
THUMB_RATIO = 1.5
THUMB_MAX_W = 1600         # cropped thumbnail max width
FULL_MAX_W  = 1400         # full-page (scrollable) max width
PHONE_MAX_W = 420          # iPhone screenshots

JOBS = {
    "be-washington": [
        ("Screenshot 2026-05-17 at 12.09.01 PM.png", "hero", "top"),
        ("Screenshot 2026-05-17 at 12.09.17 PM.png", "01",   None),
        ("Screenshot 2026-05-17 at 12.09.57 PM.png", "02",   None),
        ("Screenshot 2026-05-17 at 12.10.36 PM.png", "03",   None),
        ("Screenshot 2026-05-17 at 12.12.05 PM.png", "04",   None),
        ("Screenshot 2026-05-17 at 12.15.06 PM.png", "05",   None),
    ],
    "family-tree": [
        ("Briney-Family-Tree.png",   "hero", "top"),
        ("Briney-Family-Tree-2.png", "01",   "top"),
        ("Briney-Family-Tree-3.png", "02",   "top"),
        # Optional: include the very tall ones if you want them in the lightbox
        # ("Briney-Family-Tree-4.png", "03", "top"),
        # ("Briney-Family-Tree-5.png", "04", "top"),
        # ("Briney-Family-Tree-6.png", "05", "top"),
    ],
    "mount-vernon-website": [
        ("Add-Ons-Mount-Vernon.png",                                 "hero", "top"),
        ("George-Washington-s-Mount-Vernon.png",                     "01",   "top"),
        ("Plant-Finder-George-Washington-s-Mount-Vernon.png",        "02",   "top"),
        ("George-Washington-George-Washington-s-Mount-Vernon.png",   "03",   "top"),
    ],
    "multiplier": [
        ("IMG_0009.PNG", "hero", "center"),
        ("IMG_0010.PNG", "01",   None),
        ("IMG_0011.PNG", "02",   None),
        ("IMG_0013.PNG", "03",   None),
        ("IMG_0014.PNG", "04",   None),
        ("IMG_0016.PNG", "05",   None),
    ],
    "mv-explorer": [
        # iPhone screenshots — only thumb output (no scrollable "full")
        ("IMG_5632.PNG", "phone-01", "phone"),
        ("IMG_5673.PNG", "phone-02", "phone"),
        ("IMG_5674.PNG", "phone-03", "phone"),
        ("IMG_5759.PNG", "phone-04", "phone"),
        ("IMG_5774.PNG", "phone-05", "phone"),
        ("IMG_5790.PNG", "phone-06", "phone"),
        ("IMG_5800.PNG", "phone-07", "phone"),
        ("IMG_2055.PNG", "phone-08", "phone"),
    ],
    "mv-virtual-tour": [
        ("MOUNT-VERNON.png",   "hero", None),
        ("MOUNT-VERNON-2.png", "01",   None),
        ("MOUNT-VERNON-3.png", "02",   None),
        ("MOUNT-VERNON-4.png", "03",   None),
    ],
    "tr-llm": [
        ("Reading-Room-Theodore-Roosevelt-Presidential-Library-4.png", "hero", None),
    ],
    "travel-site": [
        ("Matt-Briney-—-Travel-Passport.png",   "hero", None),
        ("Matt-Briney-—-Travel-Passport-3.png", "01",   None),
        ("Screenshot 2026-05-17 at 12.01.07 PM.png", "02", None),
        ("Screenshot 2026-05-17 at 12.01.25 PM.png", "03", None),
        ("Matt-Briney-—-Travel-Passport-2.png", "04",   "top"),
        ("Matt-Briney-—-Travel-Passport-4.png", "05",   "top"),
    ],
}

# -----------------------------------------------------------------------------

def flatten(im):
    if im.mode == "RGBA":
        bg = Image.new("RGB", im.size, (255, 255, 255))
        bg.paste(im, mask=im.split()[3])
        return bg
    return im.convert("RGB") if im.mode != "RGB" else im

def crop_top(im, target_ratio):
    w, h = im.size
    desired_h = int(w / target_ratio)
    if h > desired_h:
        return im.crop((0, 0, w, desired_h))
    return im

def crop_center(im, target_ratio):
    w, h = im.size
    desired_h = int(w / target_ratio)
    if h > desired_h:
        top = (h - desired_h) // 2
        return im.crop((0, top, w, top + desired_h))
    return im

def resize_to_width(im, w):
    if im.size[0] > w:
        h = round(im.size[1] * w / im.size[0])
        return im.resize((w, h), Image.LANCZOS)
    return im

def save_pair(im, base_path, jpg_q=82, webp_q=78):
    im = flatten(im)
    im.save(f"{base_path}.jpg",  "JPEG", quality=jpg_q, optimize=True, progressive=True)
    im.save(f"{base_path}.webp", "WEBP", quality=webp_q, method=6)
    sz_jpg  = os.path.getsize(f"{base_path}.jpg")
    sz_webp = os.path.getsize(f"{base_path}.webp")
    return sz_jpg, sz_webp

def is_tall(im, ratio=THUMB_RATIO * 1.05):
    """True if this image is meaningfully taller than the thumbnail crop."""
    w, h = im.size
    return (h / w) > (1 / ratio) * 1.05  # slightly more than 1.05x the cropped aspect

def process(slug: str, items):
    raw_dir = RAW_BASE / slug
    out_dir = OUT_BASE / slug
    out_dir.mkdir(parents=True, exist_ok=True)
    print(f"\n=== {slug} ===")
    if not raw_dir.exists():
        print(f"  (skipped — no raw dir at {raw_dir})")
        return

    for fname, name, strat in items:
        src = raw_dir / fname
        if not src.exists():
            print(f"  MISSING: {fname}")
            continue

        im = Image.open(src)
        src_w, src_h = im.size

        # --- THUMBNAIL ---
        thumb = im
        if strat == "top":
            thumb = crop_top(thumb, THUMB_RATIO)
        elif strat == "center":
            thumb = crop_center(thumb, THUMB_RATIO)
        elif strat == "phone":
            thumb = resize_to_width(thumb, PHONE_MAX_W)
        else:
            thumb = resize_to_width(thumb, THUMB_MAX_W)
        if strat in ("top", "center"):
            thumb = resize_to_width(thumb, THUMB_MAX_W)

        sj, sw = save_pair(thumb, str(out_dir / name))
        print(f"  {name}.{{jpg,webp}}  thumb {thumb.size}  jpg={sj//1024}KB")

        # --- FULL (only for tall screenshots that benefit from it) ---
        if strat == "phone":
            continue
        if strat in ("top",) and is_tall(im):
            full = resize_to_width(im, FULL_MAX_W)
            sj2, sw2 = save_pair(full, str(out_dir / f"{name}-full"))
            print(f"  {name}-full.{{jpg,webp}}  full {full.size}  jpg={sj2//1024}KB")

def main():
    if not RAW_BASE.exists():
        print(f"No raw directory at {RAW_BASE}.")
        print("Drop raw screenshots into img/projects-raw/<slug>/ and rerun.")
        sys.exit(1)

    for slug, items in JOBS.items():
        process(slug, items)

    # Summary
    total = 0
    for root, dirs, files in os.walk(OUT_BASE):
        for f in files:
            total += os.path.getsize(os.path.join(root, f))
    print(f"\nTotal optimized size: {total / 1024 / 1024:.1f} MB")
    print("Done.")

if __name__ == "__main__":
    main()
