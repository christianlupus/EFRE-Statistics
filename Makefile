
DATAIN=input.data

DATAOUT=tex/output.data
TEXOUT=tex/import.tex

.PHONY: all
all: build-pdf

.PHONY: build-pdf
build-pdf: create-datafiles
	cd tex; pdflatex -synctex=1 -interaction=nonstopmode statistik.tex
	cd tex; pdflatex -synctex=1 -interaction=nonstopmode stundenzettel.tex

.PHONY: create-datafiles
create-datafiles: $(DATAOUT) $(TEXOUT)

$(DATAOUT) $(TEXOUT): $(DATAIN)
	@-mkdir -p $(dir $(DATAOUT)) $(dir $(TEXOUT))
	python ./process.py $(DATAIN) $(DATAOUT) $(TEXOUT)
