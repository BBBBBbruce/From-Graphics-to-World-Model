#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Check source links, labels, citation keys, and the figure allowlist offline."""
from pathlib import Path
import re
import json
import hashlib

root = Path(__file__).resolve().parents[1]
book = root / "book"
files = list(book.rglob("*.tex"))
text = "\n".join(p.read_text() for p in files)
bib = (book / "references.bib").read_text()
keys = set(re.findall(r"@\w+\{([^,]+),", bib))
labels = re.findall(r"\\label\{([^}]+)\}", text)
# Macro calls create figure and exercise labels during compilation.
labels += re.findall(r"\}\{(fig:[^}]+)\}", text)
labels += ["ex:" + x for x in re.findall(r"\\exercise\{([^}]+)\}", text)]
references = set(re.findall(r"\\(?:ref|eqref)\{([^}]+)\}", text))
citations = set()
for group in re.findall(r"\\cite\w*\s*(?:\[[^\]]*\]\s*)*\{([^}]+)\}", text):
    citations.update(x.strip() for x in group.split(","))
assert not (citations - keys), f"Missing bibliography keys: {citations - keys}"
assert not (references - set(labels)), f"Missing labels: {references - set(labels)}"
for match in re.finditer(r"\\input\{([^}]+)\}", text):
    name = match[1]
    if "#" not in name:
        assert (book / (name + ".tex")).is_file(), name
assert not re.search(r"\\(?:teaser|sourcefig)\b", text), "Unregistered legacy figure command found"
registry = json.loads((root / "docs/figure-attributions.json").read_text())
registered = {entry["file"] for entry in registry}
actual = {str(p.relative_to(root)) for p in (book / "figures/papers").iterdir() if p.is_file()}
assert actual == registered, "Paper figures must match the reviewed attribution register"
for entry in registry:
    assert entry["license"] == "CC-BY-4.0"
    assert hashlib.sha256((root / entry["file"]).read_bytes()).hexdigest() == entry["sha256"]
    assert entry["paper_key"] in keys
for filename in re.findall(r"\\paperfigure\{([^}]+)\}", text):
    assert "book/figures/papers/" + filename in registered, filename
assert "author={Qian, Cheng and Fan, Ruomeng and Ren, Yifei" in bib
assert all("http" in entry for entry in re.split(r"(?=@\w+\{)", bib) if entry.strip())
print(f"Source checks passed: {len(files)} TeX files, {len(citations)} cited keys, {len(references)} references")
