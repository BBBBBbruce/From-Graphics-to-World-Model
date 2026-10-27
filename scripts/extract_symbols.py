#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Extract the symbol chapter from the built PDF. Requires pypdf."""
from pathlib import Path
from pypdf import PdfReader, PdfWriter

root = Path(__file__).resolve().parents[1]
reader = PdfReader(root / "docs/from-graphics-to-world-model.pdf")
start = None
stop = None
for index, page in enumerate(reader.pages):
    text = page.extract_text() or ""
    if "Symbols and Conventions" in text and "Interaction, context, and time" in text:
        start = index
    if start is not None and index > start and "Chapter 1" in text and "From Images to Predictions" in text:
        stop = index
        break
assert start is not None and stop is not None, "Could not locate symbol chapter boundaries"
writer = PdfWriter()
for page in reader.pages[start:stop]:
    writer.add_page(page)
writer.add_metadata({"/Title": "From Graphics to World Models — Symbols and Conventions",
                     "/Author": "From Graphics to World Models contributors"})
with (root / "docs/symbols.pdf").open("wb") as output:
    writer.write(output)
print(f"Extracted {stop-start} symbol pages")
