PYTHON ?= python3
LATEXMK ?= latexmk

.PHONY: verify pdf checksums clean

verify:
	$(PYTHON) verification/verify_pii_obstruction.py
	$(PYTHON) verification/verify_prime_sieve.py
	$(PYTHON) verification/verify_checksums.py

pdf:
	cd paper && $(LATEXMK) -pdf -interaction=nonstopmode -halt-on-error main.tex

checksums:
	find . -type f ! -path './.git/*' ! -name 'SHA256SUMS' ! -name '*.aux' ! -name '*.bbl' ! -name '*.blg' ! -name '*.fdb_latexmk' ! -name '*.fls' ! -name '*.log' ! -name '*.out' ! -name '*.toc' ! -name '*.synctex.gz' -print0 | sort -z | xargs -0 sha256sum > SHA256SUMS

clean:
	cd paper && $(LATEXMK) -c
