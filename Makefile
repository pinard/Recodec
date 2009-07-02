# Conversion between charsets, surfaces and structures.
# Copyright © 2002 Progiciels Bourbeau-Pinard inc.
# François Pinard <pinard@iro.umontreal.ca>, 2002.

PROJET = recodec
DISTRIBUTION = Recodec-0.0

ifdef MAKEFILE_COMMUN
 include $(MAKEFILE_COMMUN)
else
 PYTHON = python
 PYSETUP = $(PYTHON) setup.py
endif

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
dump endline html ibmpc juca latex permute qnx quoted strip testdump texinfo \
texte ucs utf16 utf7 utf8 vietnam builtin

EXTRA_BUILT = $(addprefix Recode/, \
  charname.py fr_charname.py libiconv.py preset.py rfc1345.py)

all: $(EXTRA_BUILT)
	$(PYSETUP) build

install: $(EXTRA_BUILT)
	$(PYSETUP) install

check: $(EXTRA_BUILT)
	$(PYSETUP) build
	cd test && PYTHONPATH=.. $(PYTHON) suite.py
	@find Recode -name '*.pyc' | xargs rm -f

clean::
	find Recode -name '*.pyc' | xargs rm -f
#	rm -f $(EXTRA_BUILT)
	rm -f Recode/builtin.py Recode/preset.py

tags:
	find -name '*.py' | egrep -v '^./build|~$$' | etags -

dist: $(DISTRIBUTION).tar.gz

publish: $(DISTRIBUTION).tar.gz
	python $(HOME)/webert-0.0/Webert/htmlpage.py README index.html
	chmod 644 index.html $(DISTRIBUTION).tar.gz
	scp -p index.html $(DISTRIBUTION).tar.gz bor:w/recodec/
#	rm index.html $(DISTRIBUTION).tar.gz
	ssh bor rm -vf w/recodec/Recodec.tar.gz
	ssh bor ln -vs $(DISTRIBUTION).tar.gz w/recodec/Recodec.tar.gz
	ssh bor ls -Llt w/recodec

$(DISTRIBUTION).tar.gz: $(EXTRA_BUILT)
	$(PYSETUP) sdist
	mv dist/$(DISTRIBUTION).tar.gz .
	rmdir dist
	ls -l *.gz

MAKE_BUILTIN_PY = PYTHONPATH=`pwd` $(PYTHON) Tools/make-builtin.py
MAKE_PRESET_PY = PYTHONPATH=`pwd` $(PYTHON) Tools/make-preset.py
MAKE_TABLES_PY = $(PYTHON) Tools/make-tables.py

Recode/preset.py: Tools/make-preset.py \
  $(addprefix Recode/, $(addsuffix .py, $(RECODING_MODULES)))
	rm -f $@
	$(MAKE_PRESET_PY) $(RECODING_MODULES)
	mv $(notdir $@) $@

Recode/builtin.py: Tools/make-builtin.py
	$(MAKE_BUILTIN_PY)
	mv $(notdir $@) $@

Recode/charname.py: Tools/make-tables.py $(MNEMONICS_DS) $(RFC1345_TXT)
	$(MAKE_TABLES_PY) -Pn $(MNEMONICS_DS) $(RFC1345_TXT)
	mv $(notdir $@) $@

Recode/fr_charname.py: Tools/make-tables.py $(NOMS_CARACS)
	$(MAKE_TABLES_PY) -PFn $(NOMS_CARACS)
	mv $(notdir $@) $@

Recode/libiconv.py: Tools/make-tables.py $(ENCODINGS_DEF)
	$(MAKE_TABLES_PY) -Pl $(ENCODINGS_DEF)
	mv $(notdir $@) $@

Recode/rfc1345.py: Tools/make-tables.py $(MNEMONICS_DS)
	$(MAKE_TABLES_PY) -Pm $(MNEMONICS_DS)
	mv $(notdir $@) $@

Recode/strip.py: Tools/make-tables.py $(MNEMONICS_DS) $(CHARSETS_DEF)
	$(MAKE_TABLES_PY) -Pp $(MNEMONICS_DS) $(CHARSETS_DEF)
	mv $(notdir $@) $@
