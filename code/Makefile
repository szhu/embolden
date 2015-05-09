INS := $(wildcard *.in.tex)
OUTS := $(patsubst %.in.tex,%.out.tex,$(INS))

all: $(OUTS)

%.out.tex: %.in.tex embolden.py
	python embolden.py < $< > $@
