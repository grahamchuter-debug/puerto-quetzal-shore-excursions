#!/usr/bin/env python3
"""Download hero and content images from Unsplash (Unsplash License)."""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
IMAGES = ROOT / "images"

DOWNLOADS: list[tuple[str, str]] = [
    ("hero-puerto-quetzal.png", "https://images.unsplash.com/photo-1578662996442-48f60103fc96?w=1920&q=80&fm=jpg"),
    ("antigua-guatemala.png", "https://images.unsplash.com/photo-1578662996442-48f60103fc96?w=1920&q=80&fm=jpg"),
    ("santa-catalina-arch.png", "https://images.unsplash.com/photo-1559827260-dc66d52bef19?w=1920&q=80&fm=jpg"),
    ("colonial-antigua.png", "https://images.unsplash.com/photo-1559827260-dc66d52bef19?w=1920&q=80&fm=jpg"),
    ("pacaya-volcano.png", "https://images.unsplash.com/photo-1506905925346-21bda4d32df4?w=1920&q=80&fm=jpg"),
    ("coffee-plantation.png", "https://images.unsplash.com/photo-1447933601403-0c6688de566e?w=1920&q=80&fm=jpg"),
    ("jade-factory.png", "https://images.unsplash.com/photo-1515562141207-7a88fb7ce338?w=1920&q=80&fm=jpg"),
    ("guatemala-highlights.png", "https://images.unsplash.com/photo-1548013146-72479768bada?w=1920&q=80&fm=jpg"),
    ("puerto-quetzal-port.png", "https://images.unsplash.com/photo-1544551763-46a013bb70d5?w=1920&q=80&fm=jpg"),
    ("puerto-quetzal-intro.png", "https://images.unsplash.com/photo-1578662996442-48f60103fc96?w=1920&q=80&fm=jpg"),
    ("best-puerto-quetzal-excursions.png", "https://images.unsplash.com/photo-1559827260-dc66d52bef19?w=1920&q=80&fm=jpg"),
    ("one-day-puerto-quetzal.png", "https://images.unsplash.com/photo-1559827260-dc66d52bef19?w=1920&q=80&fm=jpg"),
    ("antigua-market.png", "https://images.unsplash.com/photo-1548013146-72479768bada?w=1920&q=80&fm=jpg"),
    ("volcano-backdrop.png", "https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?w=1920&q=80&fm=jpg"),
    ("colonial-church.png", "https://images.unsplash.com/photo-1548013146-72479768bada?w=1920&q=80&fm=jpg"),
]


def download(filename: str, url: str) -> bool:
    dest = IMAGES / filename
    print(f"  {filename}")
    result = subprocess.run(
        ["curl", "-fsSL", "-o", str(dest), url],
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        print(f"    FAILED: {result.stderr.strip()}", file=sys.stderr)
        return False
    size = dest.stat().st_size
    if size < 10_000:
        print(f"    WARNING: small file ({size} bytes)", file=sys.stderr)
    print(f"    OK ({size // 1024} KB)")
    return True


def main() -> None:
    IMAGES.mkdir(parents=True, exist_ok=True)
    print("Downloading Puerto Quetzal images from Unsplash…")
    failed = 0
    for filename, url in DOWNLOADS:
        if not download(filename, url):
            failed += 1
    if failed:
        raise SystemExit(f"{failed} download(s) failed.")
    print("Done.")


if __name__ == "__main__":
    main()
