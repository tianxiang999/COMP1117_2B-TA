# Commands
latex = pdflatex
bibtex = bibtex
latexmk = latexmk
htlatex = htlatex
chktex = chktex

# Variables
title = description
papers = $(title).tex

# Environment variables
export TEXINPUTS:=.:./style:${TEXINPUTS}

#########################################
all:
	$(latexmk) -bibtex -pdf $(papers)

complete: pdf bib
	$(latex) $(papers)

pdf:
	$(latex) $(papers)

bib:
	$(bibtex) $(title)

lint:
	$(chktex) *.tex sections/*.tex

html:
	$(htlatex) $(papers)

clean:
	$(RM) *.synctex.gz *.aux *.dvi *.log *.bbl *.blg *.build.log *~ *.out *.fls *.fdb_latexxmk *.fdb_latexmk
	$(RM) $(SRC).pdfsync $(SRC).synctex.gz
	$(RM) -rf _minted-paper*


latexclean:
	$(latexmk) -c

serve:
	python -m SimpleHTTPServer
