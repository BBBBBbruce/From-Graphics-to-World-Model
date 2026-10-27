# From Graphics to World Models

**A connected research textbook on seeing, predicting, and learning to act.**

A rendered scene tells us what the world looks like. A world model asks what an action will cause. This public learning book connects those questions through robot policies, demonstrations, controllable prediction, and evidence of improvement.

**[Read the book (PDF)](docs/from-graphics-to-world-model.pdf)** · **[Symbol reference](docs/symbols.pdf)** · [Editable LaTeX](book/main.tex)

The book assumes **at least third-year undergraduate foundations** in linear algebra, multivariable calculus, probability, basic machine learning, and Python. That is the prerequisite, not a limit on depth: the text develops research-paper mechanisms, derivations, assumptions, and comparisons. The opening refresher can be read selectively.

## The path

1. **From Images to Predictions** — rendering, state, observation, uncertainty, learning, and feedback.
2. **Policies, Demonstrations, and Context** — continuous action generation, flow matching, and adaptation from demonstrations.
3. **World Models, Rewards, and Policy Improvement** — prediction, returns, advantages, policy updates, and false imagined success.
4. **Controllable Prediction** — action conventions, information available at deployment, representations, and contact.
5. **Evidence of Improvement** — targets, gradient boundaries, reliability, and fair comparisons.
6. **Choosing Your First Research Direction** — a controlled warm-up, paper-level reproduction questions, research comparisons, and a two-week first pass.

Two appendices cover flow-loss likelihood bounds and solutions to twelve exercises. The book uses author–year references and one symbol system. Original flowcharts explain the connections. Seven actual paper figures illustrate architectures and results, with author–year attribution and verified CC BY 4.0 licenses. Ten further original figures are linked beside the relevant discussion; their public redistribution permission has not been established. See the [figure register](FIGURES.md).

![A book page pairing an original flowchart with the attributed WEAVER architecture](docs/paper-figure-preview.jpg)

*Example page: an original teaching flowchart alongside Jain et al. (2026)'s WEAVER Figure 2, reproduced under CC BY 4.0. [Figure credits](FIGURES.md).*

## Run the experiment

No GPU, datasets, or third-party Python packages are required. Use Python 3.9 or later:

```sh
python3 examples/one_dimensional_world.py --output results/toy
python3 -m unittest discover -s tests -v
```

The experiment fits persistence, linear, and deadband predictors to a one-dimensional response law. It evaluates next-position error, action-selection regret, and success on original and shifted conditions. It writes JSON and CSV with settings, parameters, counts, and units.

[Default results](docs/toy-results.json) use seed 2026, 400 training examples, and 200 cases per test condition. The correctly specified deadband predictor selects successful actions on 200/200 original-condition cases but only 14/200 shifted-condition cases. This is a deliberately favorable model-family example followed by a distribution shift, not evidence about robot performance. The program evaluates independent one-step choices; it does not train a neural policy or run a closed-loop robot trial.

## Build the book

Install a TeX distribution with `latexmk`, pdfLaTeX, BibTeX, Latin Modern, TikZ, and the packages imported in `book/main.tex`. Then run:

```sh
make book
make check
```

The main PDF is written to `docs/from-graphics-to-world-model.pdf`. To regenerate the extracted symbol reference, install `pypdf` and run `python3 scripts/extract_symbols.py`. Build files stay under the ignored `build/` directory. The checked-in PDF was built with TeX Live 2025.

## Evidence and corrections

This is an educational synthesis, not a peer-reviewed monograph. Teaching examples, published methods, and research proposals are identified separately. A prediction benchmark, an implementation check, and a policy-improvement result establish different things.

Primary sources and inspected versions are listed in [SOURCES.md](SOURCES.md) and the [bibliography](book/references.bib). Report corrections with a page or section, the disputed statement, and a primary source or reproducible counterexample. Numerical results from the small example are reproducible; they do not validate the broader proposed research systems.

## Reuse

This repository is shared for public, noncommercial learning.

- **Original book, text, and figures:** [CC BY-NC 4.0](LICENSE-book.txt). Share and adapt for noncommercial purposes with attribution and a change notice.
- **Example code, tests, and build/check scripts:** [MIT](LICENSE-code). MIT permits commercial reuse of the code; it does not change the book's noncommercial terms.
- **External papers, datasets, and software:** retain their own terms. Seven paper figures are included under their original CC BY 4.0 terms, separately from the book's noncommercial license. Other papers, datasets, and model weights are linked, not bundled.

See [NOTICE.md](NOTICE.md) for scope, attribution, and figure provenance. The choice of license does not grant rights in someone else's work.
