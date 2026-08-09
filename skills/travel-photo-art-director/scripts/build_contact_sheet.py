#!/usr/bin/env python3
"""Build a labeled contact sheet from a travel photo folder."""

from __future__ import annotations

import argparse
import math
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont, ImageOps


DEFAULT_EXTENSIONS = {".jpg", ".jpeg", ".png", ".webp", ".tif", ".tiff"}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="Source image directory")
    parser.add_argument("output", type=Path, help="Output JPEG or PNG")
    parser.add_argument("--columns", type=int, default=5)
    parser.add_argument("--thumb-width", type=int, default=320)
    parser.add_argument("--thumb-height", type=int, default=220)
    parser.add_argument("--label-height", type=int, default=42)
    parser.add_argument("--gap", type=int, default=18)
    parser.add_argument("--margin", type=int, default=24)
    parser.add_argument("--recursive", action="store_true")
    parser.add_argument("--limit", type=int, default=0, help="0 means no limit")
    return parser.parse_args()


def find_images(folder: Path, recursive: bool) -> list[Path]:
    iterator = folder.rglob("*") if recursive else folder.glob("*")
    return sorted(
        path for path in iterator if path.is_file() and path.suffix.lower() in DEFAULT_EXTENSIONS
    )


def make_sheet(args: argparse.Namespace) -> None:
    if args.columns < 1:
        raise ValueError("--columns must be at least 1")
    paths = find_images(args.input, args.recursive)
    if args.limit > 0:
        paths = paths[: args.limit]
    if not paths:
        raise SystemExit(f"No supported images found in {args.input}")

    rows = math.ceil(len(paths) / args.columns)
    cell_width = args.thumb_width
    cell_height = args.thumb_height + args.label_height
    width = args.margin * 2 + args.columns * cell_width + (args.columns - 1) * args.gap
    height = args.margin * 2 + rows * cell_height + (rows - 1) * args.gap
    canvas = Image.new("RGB", (width, height), (232, 228, 217))
    draw = ImageDraw.Draw(canvas)
    font = ImageFont.load_default()

    for index, path in enumerate(paths):
        row, column = divmod(index, args.columns)
        x = args.margin + column * (cell_width + args.gap)
        y = args.margin + row * (cell_height + args.gap)
        try:
            with Image.open(path) as source:
                source = ImageOps.exif_transpose(source).convert("RGB")
                thumb = ImageOps.fit(
                    source,
                    (args.thumb_width, args.thumb_height),
                    method=Image.Resampling.LANCZOS,
                )
                canvas.paste(thumb, (x, y))
        except Exception as exc:  # keep broad-folder review moving
            draw.rectangle((x, y, x + args.thumb_width, y + args.thumb_height), fill=(190, 185, 176))
            draw.text((x + 8, y + 8), f"Unreadable: {exc}", fill=(80, 75, 70), font=font)

        label = path.name
        while draw.textlength(label, font=font) > args.thumb_width and len(label) > 8:
            label = label[:-5] + "..."
        draw.text((x, y + args.thumb_height + 8), label, fill=(48, 45, 42), font=font)

    args.output.parent.mkdir(parents=True, exist_ok=True)
    save_kwargs = {"quality": 91, "optimize": True} if args.output.suffix.lower() in {".jpg", ".jpeg"} else {}
    canvas.save(args.output, **save_kwargs)
    print(f"Wrote {len(paths)} images to {args.output} ({width}x{height})")


if __name__ == "__main__":
    make_sheet(parse_args())

