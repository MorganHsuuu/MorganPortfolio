#!/usr/bin/env python3
"""Export full portfolio slides for grad project detail pages."""

import fitz
from pathlib import Path

ASSETS = Path(__file__).resolve().parents[1] / "assets"
PDF = ASSETS / "2026 Morgan's Portfolio.pdf"
MAT = fitz.Matrix(2.5, 2.5)

PROJECTS = {
    "sleep-airline": list(range(6, 13)),
    "safedrive": list(range(14, 20)),
    "refly": [20] + list(range(21, 28)),
}


def main():
    doc = fitz.open(PDF)
    for slug, pages in PROJECTS.items():
        out = ASSETS / "grad-slides" / slug
        out.mkdir(parents=True, exist_ok=True)
        for pg in pages:
            pix = doc[pg - 1].get_pixmap(matrix=MAT, alpha=False)
            pix.save(str(out / f"slide-{pg:02d}.jpg"), jpg_quality=92)
        print(f"{slug}: {len(pages)} slides")


if __name__ == "__main__":
    main()
