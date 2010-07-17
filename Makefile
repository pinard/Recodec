# Conversion between charsets, surfaces and structures.
# Copyright © 2002, 2005 Progiciels Bourbeau-Pinard inc.
# François Pinard <pinard@iro.umontreal.ca>, 2002.

DISTRIBUTION = $(shell python Recode/version.py)

PYTHON = python
PYSETUP = $(PYTHON) setup.py
PYTHONTOOL = PYTHONPATH=.:tools $(PYTHON) -S
RST2HTML = rst2html

RFC1345_TXT = data/rfc1345.txt
ENCODINGS_DEF = data/encodings.def $(wildcard data/encodings_*.def)
ISO10646_DEF = data/iso10646.def
CHARSETS_DEF = data/charsets.def
MNEMONICS_DS = data/iso10646.def data/other.def data/control.def
NOMS_CARACS = data/NomsSeulsfinal.lst

# Keep `builtin' last so, while computing `preset.py', Python built-in
# encodings automatically inherit better previous coding names, when known.
# As `NeXT' is already found in `strip.py', `next.py' is not included.

RECODING_MODULES = \
    african afrtran ascii_bs atarist bangbang base64 cdcnos dump endline \
    flat html ibmpc java juca latex permute qnx quoted strip testdump \
    texinfo texte ucs utf16 utf7 utf8 varia vietnam builtin

EXTRA_BUILT = \
    doc/inc-iconv.txt doc/inc-stamp.txt doc/recodec.html \
    Recode/charname.py Recode/fr_charname.py Recode/libiconv.py \
    Recode/preset.py Recode/rfc1345.py

DOC_SOURCES = $(filter-out doc/inc-stamp.txt, $(wildcard doc/*.txt))

PY_SOURCES = $(addprefix Recode/, $(addsuffix .py, $(RECODING_MODULES)))

all: $(EXTRA_BUILT)
	$(PYSETUP) build

install: $(EXTRA_BUILT)
	$(PYSETUP) install

check: all
	cd test && PYTHONPATH=.. $(PYTHON) -S suite.py -bv

profile: all
	cd test && PYTHONPATH=.. $(PYTHON) -S suite.py -bp

clean:
	rm -f Recode/*.pyc test/*.pyc tools/*.pyc
	rm -f $(EXTRA_BUILT)
	rm -f Recode/builtin.py Recode/preset.py

tags:
#	Should be Exuberant ctags.
	ctags -R Recode test tools

publish: distcheck
	mv $(DISTRIBUTION).tar.gz ../archives/
	ls -l ../archives/

distcheck: dist
	rm -rf =distcheck
	mkdir =distcheck
	cd =distcheck && tar xfz ../$(DISTRIBUTION).tar.gz
	cd =distcheck && $(PYTHON) -S setup.py --quiet build
	cd =distcheck/test && PYTHONPATH=.. $(PYTHON) -S suite.py -b
	rm -rf =distcheck

dist: $(DISTRIBUTION).tar.gz

$(DISTRIBUTION).tar.gz: $(EXTRA_BUILT)
	$(PYSETUP) sdist
	mv dist/$(DISTRIBUTION).tar.gz .
	rmdir dist
	ls -l *.gz

doc/inc-iconv.txt: tools/inc-iconv-txt.py Recode/libiconv.py
	$(PYTHONTOOL) tools/inc-iconv-txt.py
	mv $(notdir $@) $@

doc/inc-rfc1345.txt: tools/tables-py.py $(MNEMONICS_DS) $(RFC1345_TXT)
	$(PYTHONTOOL) tools/tables-py.py -t $(MNEMONICS_DS) $(RFC1345_TXT)
	mv $(notdir $@) $@

doc/inc-stamp.txt: tools/inc-stamp-txt.py Recode/version.py $(DOC_SOURCES)
	$(PYTHONTOOL) tools/inc-stamp-txt.py $(DOC_SOURCES)
	mv $(notdir $@) $@

doc/recodec.html: doc/inc-stamp.txt doc/inc-iconv.txt doc/inc-rfc1345.txt
	cd doc && $(RST2HTML) recodec.txt > recodec-tmp.html
	mv doc/recodec-tmp.html $@


Recode/preset.py: tools/preset-py.py $(PY_SOURCES)
	rm -f $@
	$(PYTHONTOOL) tools/preset-py.py $(RECODING_MODULES)
	mv $(notdir $@) $@

Recode/builtin.py: tools/builtin-py.py
	$(PYTHONTOOL) tools/builtin-py.py
	mv $(notdir $@) $@

Recode/charname.h: tools/charname-h.py Recode/charname.py
	$(PYTHONTOOL) tools/charname-h.py
	mv $(notdir $@) $@

Recode/charname.py: tools/tables-py.py $(MNEMONICS_DS) $(RFC1345_TXT)
	$(PYTHONTOOL) tools/tables-py.py -n $(MNEMONICS_DS) $(RFC1345_TXT)
	mv $(notdir $@) $@

Recode/fr-charname.h: tools/charname-h.py Recode/fr_charname.py
	$(PYTHONTOOL) tools/charname-h.py -F
	mv $(notdir $@) $@

Recode/fr_charname.py: tools/tables-py.py $(NOMS_CARACS)
	$(PYTHONTOOL) tools/tables-py.py -Fn $(NOMS_CARACS)
	mv $(notdir $@) $@

Recode/libiconv.h: tools/libiconv-h.py Recode/libiconv.py
	$(PYTHONTOOL) tools/libiconv-h.py
	mv $(notdir $@) $@

Recode/libiconv.py: tools/tables-py.py $(ENCODINGS_DEF)
	$(PYTHONTOOL) tools/tables-py.py -l $(ENCODINGS_DEF)
	mv $(notdir $@) $@

Recode/rfc1345.h: tools/rfc1345-h.py Recode/rfc1345.py
	$(PYTHONTOOL) tools/rfc1345-h.py
	mv $(notdir $@) $@

Recode/rfc1345.py: tools/tables-py.py $(MNEMONICS_DS)
	$(PYTHONTOOL) tools/tables-py.py -m $(MNEMONICS_DS)
	mv $(notdir $@) $@

Recode/strip.c: tools/strip-c.py Recode/strip.py
	$(PYTHONTOOL) tools/strip-c.py
	mv $(notdir $@) $@

Recode/strip.py: tools/tables-py.py $(MNEMONICS_DS) $(CHARSETS_DEF)
	$(PYTHONTOOL) tools/tables-py.py -p $(MNEMONICS_DS) $(CHARSETS_DEF)
	mv $(notdir $@) $@

# JUCA_DCL = $HOME/fontes/bpi/develop/dcl/afrbpi/AFR-ucs2.dcl
# Recode/juca.py: tools/juca-py.py $(JUCA_DCL)
# 	$(PYTHONTOOL) tools/juca-py.py $(JUCA_DCL) > $(notdir $@)
# 	mv $(notdir $@) $@

# vim: sw=4 :
