# Editing and building

The book source is in `book/`; the reader-facing PDF is in `docs/`.

## Build

Use a TeX distribution with `latexmk`, pdfLaTeX, BibTeX, Latin Modern, TikZ, and the packages imported in `book/main.tex`. The current build uses TeX Live 2025.

```sh
make book
make check
```

Build files stay under `build/`. The main PDF is copied to `docs/from-graphics-to-world-model.pdf`. To regenerate the symbol extract, install `pypdf` and run:

```sh
python3 scripts/extract_symbols.py
```

Render changed PDF pages and inspect them before committing. If pagination or the previewed content changes, regenerate `docs/paper-figure-preview.jpg` from the page containing the WEAVER architecture.

## Sources and figures

Maintain inspected source versions in `book/references.bib` and `SOURCES.md`. For paper figures, record attribution and license evidence in `FIGURES.md` and `docs/figure-attributions.json`. The source checker verifies registered files and their hashes. Keep required source credits and license notices when editing captions.

Keep original teaching examples distinguishable from reported experiments. Preserve the assumptions of mathematical derivations and the scope of empirical results; avoid adding generic disclaimers where a precise explanation will do.

## Corrections

For a technical correction, give the page or section, the disputed statement, and supporting reasoning or a primary source. For a code issue, include a small reproducible example.
