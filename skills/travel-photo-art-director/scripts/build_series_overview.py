#!/usr/bin/env python3
"""Build a clean overview grid for series-level visual QA."""

from __future__ import annotations

import argparse
import math
from pathlib import Path

from PIL import Image, ImageOps


EXTENSIONS = {".jpg", ".jpeg", ".png", ".webp", ".tif", ".tiff"}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="Directory containing final images")
    parser.add_argument("output", type=Path, help="Output overview JPEG or PNG")
    parser.add_argument("--columns", type=int, default=3)
    parser.add_argument("--count", type=int, default=9)
    parser.add_argument("--thumb-width", type=int, default=360)
    parser.add_argument("--thumb-height", type=int, default=600)
    parser.add_argument("--gap", type=int, default=20)
    parser.add_argument("--margin", type=int, default=28)
    return parser.parse_args()


def build(args: argparse.Namespace) -> None:
    paths = sorted(
        path
        for path in args.input.iterdir()
        if path.is_file()
        and path.suffix.lower() in EXTENSIONS
        and not path.name.startswith("00-")
    )[: args.count]
    if len(paths) != args.count:
        raise SystemExit(f"Expected {args.count} images, found {len(paths)} in {args.input}")
    if args.columns < 1:
        raise ValueError("--columns must be at least 1")

    rows = math.ceil(args.count / args.columns)
    width = args.margin * 2 + args.columns * args.thumb_width + (args.columns - 1) * args.gap
    height = args.margin * 2 + rows * args.thumb_height + (rows - 1) * args.gap
    canvas = Image.new("RGB", (width, height), (225, 221, 211))

    for index, path in enumerate(paths):
        row, column = divmod(index, args.columns)
        x = args.margin + column * (args.thumb_width + args.gap)
        y = args.margin + row * (args.thumb_height + args.gap)
        with Image.open(path) as source:
            source = ImageOps.exif_transpose(source).convert("RGB")
            thumb = ImageOps.fit(
                source,
                (args.thumb_width, args.thumb_height),
                method=Image.Resampling.LANCZOS,
            )
            canvas.paste(thumb, (x, y))

    args.output.parent.mkdir(parents=True, exist_ok=True)
    save_kwargs = {"quality": 92, "optimize": True} if args.output.suffix.lower() in {".jpg", ".jpeg"} else {}
    canvas.save(args.output, **save_kwargs)
    print(f"Wrote overview to {args.output} ({width}x{height})")


if __name__ == "__main__":
    build(parse_args())

