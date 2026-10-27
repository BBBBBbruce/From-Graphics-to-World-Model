.PHONY: book check example
book:
	mkdir -p build docs
	cd book && latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=../build main.tex
	cp build/main.pdf docs/from-graphics-to-world-model.pdf
check:
	python3 scripts/check_sources.py
	python3 -m unittest discover -s tests -v
example:
	python3 examples/one_dimensional_world.py --output results/toy
