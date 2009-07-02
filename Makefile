# Conversion between charsets, surfaces and structures.
# Copyright © 2002 Progiciels Bourbeau-Pinard inc.
# François Pinard <pinard@iro.umontreal.ca>, 2002.

#ifdef MAKEFILE_COMMUN
# PROJET = recodec
# include $(MAKEFILE_COMMUN)
#else
# PYTHON = python
# PYSETUP = $(PYTHON) setup.py
#endif
PYTHON = python
PYSETUP = $(PYTHON) setup.py

RFC1345_TXT = data/rfc1345.txt
ENCODINGS_DEF = data/encodings.def $(wildcard data/encodings_*.def)
ISO10646_DEF = data/iso10646.def
CHARSETS_DEF = data/charsets.def
MNEMONICS_DS = data/iso10646.def data/other.def data/control.def
NOMS_CARACS = data/NomsSeulsfinal.lst

# Keep `builtin' last so, while computing `preset.py', Python built-in
# encodings automatically inherit better previous coding names, when known.
# As `NeXT' is already found in `strip.py', `next.py' is not included.
RECODING_MODULES = african afrtran ascii_bs atarist bangbang base64 cdcnos \
dump endline flat html ibmpc java juca latex permute qnx quoted strip \
testdump texinfo texte ucs utf16 utf7 utf8 varia vietnam builtin

EXTRA_BUILT = \
  $(addprefix doc/, \
    inc-iconv.txt inc-stamp.txt recodec.html) \
  $(addprefix Recode/, \
    charname.py fr_charname.py libiconv.py preset.py rfc1345.py)

all: $(EXTRA_BUILT)
	$(PYSETUP) build

install: $(EXTRA_BUILT)
	$(PYSETUP) install

check: $(EXTRA_BUILT)
	$(PYSETUP) build
	cd test && PYTHONPATH=.. $(PYTHON) -S suite.py -bv

profile:
	cd test && PYTHONPATH=.. $(PYTHON) -S suite.py -bp

clean::
	find -name '*.pyc' | xargs rm -f
#	rm -f $(EXTRA_BUILT)
	rm -f Recode/builtin.py Recode/preset.py

tags:
	find -name '*.py' | egrep -v '^./build|~$$' | etags -

DISTRIBUTION = $(shell $(PYTHON) Recode/version.py)

publish: distcheck
	mv $(DISTRIBUTION).tar.gz ../archives/
	ls -l ../archives/

distcheck: dist
	rm -rf =distcheck
	mkdir =distcheck
	cd =distcheck && tar xfz ../$(DISTRIBUTION).tar.gz
	cd =distcheck/$(DISTRIBUTION) \
	  && $(PYTHON) -S setup.py --quiet build \
	  && cd test && PYTHONPATH=.. $(PYTHON) -S suite.py -b
	rm -rf =distcheck

dist: $(DISTRIBUTION).tar.gz

$(DISTRIBUTION).tar.gz: $(EXTRA_BUILT)
	ajuster-web
	$(PYSETUP) sdist
	mv dist/$(DISTRIBUTION).tar.gz .
	rmdir dist
	ls -l *.gz

PYTHONTOOL = PYTHONPATH=.:tools $(PYTHON) -S

doc/inc-iconv.txt: tools/inc-iconv-txt.py Recode/libiconv.py
	$(PYTHONTOOL) tools/inc-iconv-txt.py
	mv $(notdir $@) $@

doc/inc-rfc1345.txt: tools/tables-py.py $(MNEMONICS_DS) $(RFC1345_TXT)
	$(PYTHONTOOL) tools/tables-py.py -t $(MNEMONICS_DS) $(RFC1345_TXT)
	mv $(notdir $@) $@

DOC_SOURCES = $(filter-out doc/inc-stamp.txt, $(wildcard doc/*.txt))
doc/inc-stamp.txt: tools/inc-stamp-txt.py Recode/version.py $(DOC_SOURCES)
	$(PYTHONTOOL) tools/inc-stamp-txt.py $(DOC_SOURCES)
	mv $(notdir $@) $@

doc/recodec.html: doc/inc-stamp.txt
	cd doc && rst2html.py recodec.txt > recodec.html

Recode/preset.py: tools/preset-py.py \
  $(addprefix Recode/, $(addsuffix .py, $(RECODING_MODULES)))
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
