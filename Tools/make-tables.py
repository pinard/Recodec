#!/usr/bin/python
# -*- coding: latin-1 -*-
# Copyright � 1993, 94, 97, 98, 99, 00, 02 Free Software Foundation, Inc.
# Fran�ois Pinard <pinard@iro.umontreal.ca>, 1993.

# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2, or (at your option)
# any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software Foundation,
# Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.

"""\
`tables.py' derives `recode' table files from various sources.

Usage: python tables.py [OPTION]... DATA-FILE...

  -F  produce French versions for -n, -s or -t
  -P  produce Python sources instead of C sources (.py instead of .c or .h)

  -e  produce C source file for explode data (explode.c)
  -l  produce C source file for libiconv charsets (libiconv.h)
  -m  produce C inclusion file for short RFC 1345 mnemonics (rfc1345.h)
  -n  produce C inclusion file for character names (charname.h)
  -p  produce C source files for strip data (strip-pool.c and strip-data.c)
  -s  produce Texinfo inclusion file for libiconv (libiconv.texi)
  -t  produce Texinfo inclusion file for RFC 1345 (rfc1345.texi)

Options `-F' and `-P' should appear first.  When `-F' and `-n' are used,
process Alain's tables.  DATA-FILEs may be rfc1345.txt, mnemonic[.,]ds,
Unicode maps, or .def files from Keld's chset* packages.  The digesting
order for DATA-FILES is usually important.
"""

import re, sys

### Copied from `recode.py'.
#

# Unicode replacement character
REPLACEMENT_CHARACTER = u'\uFFFD'

# Not a Unicode character
NOT_A_CHARACTER = u'\uFFFF'

#
### End of copy.

class Main:
    def __init__(self):
        self.french_mode = False
        self.python_mode = False

    def main(self, *arguments):
        import getopt
        charnames = explodes = libiconv = mnemonics = rfc1345 = strips = None
        self.explodes = None            # Strips.charset_done() needs it
        options, arguments = getopt.getopt(arguments, 'FPelmnpst')
        for option, value in options:
            if option == '-F':
                self.french_mode = True
            elif option == '-P':
                self.python_mode = True
            elif option == '-e':
                if not explodes:
                    explodes = self.explodes = Explodes()
                explodes.do_sources = True
            elif option == '-l':
                if not libiconv:
                    libiconv = Libiconv()
                libiconv.do_sources = True
            elif option == '-m':
                if not mnemonics:
                    mnemonics = Mnemonics()
                mnemonics.do_sources = True
            elif option == '-n':
                if not charnames:
                    charnames = Charnames()
                charnames.do_sources = True
            elif option == '-p':
                if not strips:
                    strips = Strips()
                strips.do_sources = True
            elif option == '-s':
                if not libiconv:
                    libiconv = Libiconv()
                libiconv.do_texinfo = True
            elif option == '-t':
                if not strips:
                    strips = Strips()
                strips.do_texinfo = True
        if not arguments:
            sys.stderr.write(__doc__)
            sys.exit(1)

        # Read all data tables.
        for name in arguments:
            input = Input(name)
            for line in input:
                if line[0] == '\n':
                    continue
                if line[0:2] == '/*':
                    while line.find('*/') < 0:
                        line = input.next()
                    continue
                if line.startswith('DEFENCODING'):
                    if not libiconv:
                        libiconv = Libiconv()
                    libiconv.digest(input, line)
                    break
                if line.startswith('#    Name:'):
                    if not strips:
                        strips = Strips()
                    strips.digest_unimap(input, line)
                    break
                if line[0] == '#':
                    continue
                if line.startswith('escape_char'):
                    if not mnemonics:
                        mnemonics = Mnemonics()
                    mnemonics.digest_mnemonics_ds(input)
                    break
                if re.match('Network Working Group +K\. Simonsen$', line):
                    if charnames and charnames.do_sources:
                        if not self.french_mode:
                            while not line.startswith(
                                '   3rd field is the long descriptive'):
                                line = input.next()
                            if not mnemonics:
                                mnemonics = Mnemonics()
                            mnemonics.digest_rfc1345(input, charnames)
                    if explodes or strips:
                        while line != '5.  CHARSET TABLES\n':
                            line = input.next()
                        if not strips:
                            strips = Strips()
                        strips.digest_rfc1345(input, mnemonics)
                    break
                if line.startswith('@@\t'):
                    if charnames.do_sources and self.french_mode:
                        charnames.digest_french(input)
                    break
                if line == '&referenceset\n':
                    while line != '\n':
                        line = input.next()
                    if not strips:
                        strips = Strips()
                    if not mnemonics:
                        mnemonics = Mnemonics()
                    strips.digest_rfc1345(input, mnemonics)
                    break
                if line in (
                    '   Repertoire according to ISO/IEC 10646-1:1993\n',
                    '   Control characters\n',
                    '   Private use\n'
                    ):
                    while line not in ('   Plane 000\n',
                                       '   plane 000\n'):
                        line = input.next()
                    if not mnemonics:
                        mnemonics = Mnemonics()
                    mnemonics.digest_iso10646_def(input)
                    break
                input.die("Data file with unknown contents")
        for instance in explodes, strips, charnames, libiconv, mnemonics:
            if instance:
                instance.complete()

main = Main()

class Options:
    def __init__(self):
        self.do_sources = False
        self.do_texinfo = False

# Charnames.

class Charnames(Options):
    C_SOURCES = 'charname.h'
    PY_SOURCES = 'charname.py'

    # Name of character, given its numerical value.
    charname_map = {}

    # Maximum printable length of a character name.
    max_length = 0

    # Frequency of each word, then its crypt code.
    code_map = {}

    def digest_french(self, input):
        self.preset_french()
        import string
        folding = string.maketrans('ABCDEFGHIJKLMNOPQRSTUVWXYZ������������',
                                   'abcdefghijklmnopqrstuvwxyz������������')
        for line in input:
            if line.startswith('@@\t'):
                continue
            # Pour �liminer la fin de ligne.
            line = line.rstrip()
            match = re.match('([0-9A-F]{4})\t([^(]+)( \\(.*\\))?( \\*)?$',
                             line)
            if match:
                ucs = int(match.group(1), 16)
                text = match.group(2).translate(folding)
                if text in ('<commande>', '<r�serv�>', '<pas un caract�re>'):
                    continue
                self.declare(ucs, re.sub(r' +\*$', '', text, 1))
            else:
                input.warn("Unrecognised line")

    def preset_french(self):
        self.max_length = 0
        ucs = 0x0000
        for text in (
            "nul (nul)",                                        # 0000
            "d�but d'en-t�te (soh)",                            # 0001
            "d�but de texte (stx)",                             # 0002
            "fin de texte (etx)",                               # 0003
            "fin de transmission (eot)",                        # 0004
            "demande (enq)",                                    # 0005
            "accus� de r�ception positif (ack)",                # 0006
            "sonnerie (bel)",                                   # 0007
            "espace arri�re (bs)",                              # 0008
            "tabulation horizontale (ht)",                      # 0009
            "interligne (lf)",                                  # 000A
            "tabulation verticale (vt)",                        # 000B
            "page suivante (ff)",                               # 000C
            "retour de chariot (cr)",                           # 000D
            "hors code (so)",                                   # 000E
            "en code (si)",                                     # 000F
            "�chappement transmission (dle)",                   # 0010
            "commande d'appareil un (dc1)",                     # 0011
            "commande d'appareil deux (dc2)",                   # 0012
            "commande d'appareil trois (dc3)",                  # 0013
            "commande d'appareil quatre (dc4)",                 # 0014
            "accus� de r�ception n�gatif (nak)",                # 0015
            "synchronisation (syn)",                            # 0016
            "fin de transmission de bloc (etb)",                # 0017
            "annulation (can)",                                 # 0018
            "fin de support (em)",                              # 0019
            "caract�re de substitution (sub)",                  # 001A
            "�chappement (esc)",                                # 001B
            "s�parateur de fichier (fs)",                       # 001C
            "s�parateur de groupe (gs)",                        # 001D
            "s�parateur d'article (rs)",                        # 001E
            "s�parateur de sous-article (us)",                  # 001F
            ):
            self.declare(ucs, text)
            ucs += 1
        ucs = 0x007F
        for text in (
            "suppression (del)",                                # 007F
            "caract�re de bourre (pad)",                        # 0080
            "octet sup�rieur pr�d�fini (hop)",                  # 0081
            "arr�t permis ici (bph)",                           # 0082
            "aucun arr�t ici (nbh)",                            # 0083
            "index (ind)",                                      # 0084
            "� la ligne (nel)",                                 # 0085
            "d�but de zone s�lectionn�e (ssa)",                 # 0086
            "fin de zone s�lectionn�e (esa)",                   # 0087
            "arr�t de tabulateur horizontal (hts)",             # 0088
            "tabulateur horizontal avec justification (htj)",   # 0089
            "arr�t de tabulateur vertical (vts)",               # 008A
            "interligne partiel vers <= bas (pld)",             # 008B
            "interligne partiel vers <= haut (plu)",            # 008C
            "index invers� (ri)",                               # 008D
            "remplacement unique deux (ss2)",                   # 008E
            "remplacement unique trois (ss3)",                  # 008F
            "cha�ne de commande d'appareil (dcs)",              # 0090
            "usage priv� un (pu1)",                             # 0091
            "usage priv� deux (pu2)",                           # 0092
            "mise en mode transmission (sts)",                  # 0093
            "annulation du caract�re pr�c�dent (cch)",          # 0094
            "message en attente (mw)",                          # 0095
            "d�but de zone prot�g�e (sga)",                     # 0096
            "fin de zone prot�g�e (ega)",                       # 0097
            "d�but de cha�ne (sos)",                            # 0098
            "introducteur de caract�re graphique unique (sgci)",# 0099
            "introducteur de caract�re unique (sci)",           # 009A
            "introducteur de s�quence de commande (csi)",       # 009B
            "fin de cha�ne (st)",                               # 009C
            "commande de syst�me d'exploitation (osc)",         # 009D
            "message priv� (pm)",                               # 009E
            "commande de progiciel (apc)",                      # 009F
            ):
            self.declare(ucs, text)
            ucs += 1

    def declare(self, ucs, text):
        self.charname_map[ucs] = text
        if len(text) > self.max_length:
            self.max_length = len(text)
        for word in text.split():
            if word in self.code_map:
                self.code_map[word] += 1
            else:
                self.code_map[word] = 1

    # Write a compressed list of character names.
    def complete(self):
        if not self.do_sources:
            return
        if main.french_mode:
            if main.python_mode:
                write = Output('fr_%s' % self.PY_SOURCES).write
            else:
                write = Output('fr-%s' % self.C_SOURCES).write
        else:
            if main.python_mode:
                write = Output(self.PY_SOURCES).write
            else:
                write = Output(self.C_SOURCES).write
        # Establish a mild compression scheme.  Words word[0:singles]
        # will be represented by a single byte running from 1 to
        # singles.  All remaining words will be represented by two
        # bytes, the first one running slowly from singles+1 to 255,
        # the second cycling faster from 1 to 255.
        sys.stderr.write('  sorting words...')
        pairs = [(-self.code_map[word], word) for word in self.code_map]
        pairs.sort()
        words = [pair[1] for pair in pairs]
        pairs = None
        sys.stderr.write(' %d of them\n' % len(words))
        count = len(words)
        singles = (255 * 255 - count) // 254
        # Transmit a few values for further usage by the code.
        sys.stderr.write('  sorting names...')
        unicode_table = self.charname_map.keys()
        unicode_table.sort()
        sys.stderr.write(' %d of them\n' % len(unicode_table))
        if main.python_mode:
            write('\n'
                  'number_of_singles = %d\n'
                  'max_charname_length = %d\n'
                  'number_of_charnames = %d\n'
                  % (singles, self.max_length, len(unicode_table)))
        else:
            write('\n'
                  '#define NUMBER_OF_SINGLES %d\n'
                  '#define MAX_CHARNAME_LENGTH %d\n'
                  '#define NUMBER_OF_CHARNAMES %d\n'
                  % (singles, self.max_length, len(unicode_table)))
        # Establish a mild compression scheme (one or two bytes per word).
        sys.stderr.write("  writing words\n")
        if main.python_mode:
            write('\n'
                  'word = [\n')
        else:
            write('\n'
                  'static const char *const word[%d] =\n'
                  '  {\n'
                  % count)
        char1 = 1
        char2 = 1
        for counter in range(singles):
            word = words[counter]
            if main.python_mode:
                write('    %-28s# \\%0.3o\n' % ('%r,' % word, char1))
            else:
                write('    %-28s/* \\%0.3o */\n'
                      % ('"%s",' % word.replace('"', r'\"'), char1))
            self.code_map[words[counter]] = char1
            char1 += 1
        for counter in range(singles, count):
            word = words[counter]
            if main.python_mode:
                write('    %-28s# \\%0.3o\\%0.3o\n'
                      % ('%r,' % word, char1, char2))
            else:
                write('    %-28s/* \\%0.3o\\%0.3o */\n'
                      % ('"%s",' % word.replace('"', r'\"', 1), char1, char2))
            self.code_map[words[counter]] = 256 * char1 + char2
            if char2 == 255:
                char1 += 1
                char2 = 1
            else:
                char2 += 1
        if main.python_mode:
            write('    ]\n')
        else:
            write('  };\n')
        sys.stderr.write("  writing names\n")
        if main.python_mode:
            write('\n'
                  'charname = {\n')
        else:
            write('\n'
                  'struct charname\n'
                  '  {\n'
                  '    recode_ucs2 code;\n'
                  '    const char *crypted;\n'
                  '  };\n'
                  '\n'
                  'static const struct charname charname[NUMBER_OF_CHARNAMES]'
                  ' =\n'
                  '  {\n')
        for unicode in unicode_table:
            if main.python_mode:
                write('    0x%04X: "' % unicode)
            else:
                write('    {0x%04X, "' % unicode)
            for word in self.charname_map[unicode].split():
                if word in self.code_map:
                    code = self.code_map[word]
                    if code < 256:
                        write('\\%0.3o' % code)
                    else:
                        write('\\%0.3o\\%0.3o' % divmod(code, 256))
                else:
                    sys.stderr.write('??? %s\n' % word)
            if main.python_mode:
                write('",\n')
            else:
                write('"},\n')
        if main.python_mode:
            write('    }\n')
        else:
            write('  };\n')

# Explodes.

class Explodes(Options):
    C_SOURCES = 'explode.c'
    PY_SOURCES = 'explode.py'

    def __init__(self):
        Options.__init__(self)
        # Table fragments will be produced while reading data tables.
        if main.python_mode:
            write = self.write = Output(self.PY_SOURCES).write
        else:
            write = self.write = Output(self.C_SOURCES).write
            write('\n'
                  '#include "common.h"\n')

    def complete(self):
        if not self.do_sources:
            return
        # Print the collectable initialization function.
        if main.python_mode:
            sys.stderr.write("Completing %s\n" % self.PY_SOURCES)
        else:
            sys.stderr.write("Completing %s\n" % self.C_SOURCES)
        write = self.write
        if main.python_mode:
            pass
        else:
            write('\n'
                  'bool\n'
                  'module_explodes (struct recode_outer *outer)\n'
                  '{\n')
            count = 0
            while self.declare_charset:
                write('  if (!declare_explode_data (outer, &data_%d, "%s"))\n'
                      '    return false;\n'
                      % (count, self.declare_charset[0]))
                del self.declare_charset[0]
                count += 1
            write('\n')
            while declare_alias:
                write('  if (!declare_alias (outer, "%s", "%s"))\n'
                      '    return false;\n'
                      % declare_alias[0])
                del declare_alias[0]
            write('\n'
                  '  return true;\n'
                  '}\n'
                  '\n'
                  'void\n'
                  'delmodule_explodes (struct recode_outer *outer)\n'
                  '{\n'
                  '}\n')

# Libiconv.

class Libiconv(Options):
    C_SOURCES = 'libiconv.h'
    PY_SOURCES = 'libiconv.py'
    TEXINFO = 'libiconv.texi'

    data = []

    def digest(self, input, line):
        canonical = {}
        for charset in ('Georgian-Academy', 'Georgian-PS', 'MuleLao-1',
                        'Macintosh', 'MacArabic', 'MacCentralEurope',
                        'MacCroatian', 'MacCyrillic', 'MacGreek', 'MacHebrew',
                        'MacIceland', 'MacRoman', 'MacRomania', 'MacThai',
                        'MacTurkish', 'MacUkraine'):
            canonical[charset.upper()] = charset

        comment = None
        # Read in the encodings.def file.
        while line:
            if line.startswith('DEFENCODING(('):
                aliases = []
                match = re.search('"(.*)"', line)
                if match:
                    alias = match.group(1)
                    if alias in canonical:
                        alias = canonical[alias]
                    aliases.append(alias)
                line = input.readline().lstrip()
                while line != '),\n':
                    match = re.search('"(.*)"', line)
                    if match:
                        alias = match.group(1)
                        if alias in canonical:
                            alias = canonical[alias]
                        aliases.append(alias)
                    line = input.readline().lstrip()
                while line and line != '\n':
                    line = input.readline()
                self.data.append((comment, aliases[0], aliases[1:]))
                comment = None
            else:
                if line.startswith('/*'):
                    comment = line[3:-4]
                elif line != '\n':
                    input.warn("Unrecognised line")
                line = input.readline()

    def complete(self):
        if self.do_sources:
            self.complete_sources()
        if self.do_texinfo:
            self.complete_texinfo()

    def complete_sources(self):
        if not self.do_sources:
            return
        if main.python_mode:
            write = Output(self.PY_SOURCES).write
        else:
            write = Output(self.C_SOURCES).write
        count = 1
        for comment, charset, aliases in self.data:
            count += 2 + len(aliases)
        if main.python_mode:
            write('\n'
                  "# This is derived from Bruno Haible's `libiconv' package.\n"
                  'iconv_name_list = [\n')
        else:
            write('\n'
                  "/* This is derived from Bruno Haible's `libiconv'"
                  " package.  */\n"
                  'static const char *iconv_name_list[%d] =\n'
                  '  {\n'
                  % count)
        for comment, charset, aliases in self.data:
            if comment:
                if main.python_mode:
                    write('\n'
                          '    # %s.\n'
                          '\n'
                          % comment)
                else:
                    write('\n'
                          '    /* %s.  */\n'
                          '\n'
                          % comment)
            if aliases:
                if main.python_mode:
                    write('    (%r' % charset)
                    for alias in aliases:
                        write(',\n        %r' % alias)
                    write('),\n')
                else:
                    write('    "%s",\n' % charset)
                    for alias in aliases[:-1]:
                        write('\t"%s",\n' % alias)
                    write('\t"%s", NULL,\n' % aliases[-1])
            else:
                if main.python_mode:
                    write('    (%r,),\n' % charset)
                else:
                    write('    "%s", NULL,\n' % charset)
        if main.python_mode:
            write('    ]\n')
        else:
            write('    NULL\n'
                  '  };\n')

    def complete_texinfo(self):
        if not self.do_texinfo:
            return
        if main.french_mode:
            write = Output('fr-%s' % self.TEXINFO, noheader=True).write
        else:
            write = Output(self.TEXINFO, noheader=True).write
        write('\n'
              '@itemize @bullet\n')
        block = None
        for comment, charset, aliases in self.data:
            if not block and not comment:
                comment = 'General character sets'
            if comment:
                if block:
                    write('@end table\n'
                          '\n')
                write('@item %s\n'
                      '@table @code\n'
                      % comment)
                block = comment
            else:
                write('\n')
            write('@item %s\n' % charset)
            if aliases:
                write('@tindex %s@r{, aliases}\n'
                      % re.sub(':([0-9]+)', r'(\1)', charset))
                for alias in aliases:
                    write('@tindex %s\n' % re.sub(':([0-9]+)', r'(\1)', alias))
                if len(aliases) == 1:
                    write('@code{%s} is an alias for this charset.\n'
                          % aliases[0])
                else:
                    write('@code{%s} and @code{%s} are aliases'
                          ' for this charset.\n'
                          % ('}, @code{'.join(aliases[:-1]), aliases[-1]))
            else:
                write('@tindex %s\n' % re.sub(':([0-9]+)', r'(\1)', charset))
        write('@end table\n'
              '@end itemize\n')

# Mnemonics.

class Mnemonics(Options):
    C_SOURCES = 'rfc1345.h'
    PY_SOURCES = 'rfc1345.py'

    # Ignore any mnemonic whose length is greater than MAX_MNEMONIC_LENGTH.
    MAX_MNEMONIC_LENGTH = 3

    # Numeric value of a character, given its mnemonic.
    unicode_map = {}

    table_length = 0
    mnemonic_map = {}

    # Read in a mnemonics file.
    def digest_mnemonics_ds(self, input):
        for line in input:
            match = re.match('<([^ \t\n]+)>\t<U(....)>', line)
            if match:
                mnemonic = re.sub('/(.)', r'\1', match.group(1))
                unicode = int(match.group(2), 16)
                self.declare(mnemonic, unicode, input.warn)

    # Read in Keld's list of 10646 characters.
    def digest_iso10646_def(self, input):
        for line in input:
            if line == '\n':
                continue
            if len(line) == 3:
                continue
            if line.startswith('   \.\.\.'):
                continue
            if line == '   Presentation forms\n':
                continue
            if line.startswith('   naming: first vertical '):
                continue
            match = re.match('   row ([0-9][0-9][0-9])$', line)
            if match and int(match.group(1)) < 256:
                row = int(match.group(1))
                cell = 0
                continue
            if line == '   cell 00\n':
                cell = 0
                continue
            match = re.match('   cell ([0-9][0-9][0-9])$', line)
            if match and int(match.group(1)) < 256:
                cell = int(match.group(1))
                continue
            if re.match('   [^ ]+', line):
                if not re.match('   [A-Z][A-Z][A-Z]', line):
                    continue
            if re.match('   [^ ].*', line):
                if cell == 256:
                    input.warn("Over 256 cells in row %d", row)
                cell += 1
                continue
            match = (re.match('([^ ])  [^ ].*', line)
                     or re.match('([^ ][^ ]+) [^ ].*', line))
            if match:
                if cell == 256:
                    input.warn("Over 256 cells in row %d", row)
                self.declare(match.group(1), 256*row + cell, input.warn)
                cell += 1
                continue
            input.warn("Unrecognised line")

    # Read the text of RFC 1345, saving all character names it declares.
    def digest_rfc1345(self, input, charnames):
        def read_line():
            skip = False
            while True:
                line = input.next()
                if not line:
                    break
                if line.startswith('Simonsen'):
                    skip = True
                    continue
                if skip:
                    if line.startswith('RFC 1345'):
                        skip = False
                    continue
                if line.startswith('4.  CHARSETS'):
                    break
                if line == '\n':
                    continue
                if line[0] == ' ':
                    return line[:-1].lstrip()
            return None
        self.max_length = 0
        # Read the character descriptions.  Count words in charnames.
        line = read_line()
        while line:
            # Look ahead one line and merge it if it should.
            next = read_line()
            while next:
                match = re.match('             *( .*)', next)
                if not match:
                    break
                line += match.group(1)
                next = read_line()
            # Separate fields and save needed information.
            match = re.search('([^ ]+) +[0-9a-f]+ +(.*)', line)
            if match:
                mnemo = match.group(1)
                text = match.group(2).lower()
                if mnemo in self.unicode_map:
                    charnames.declare(self.unicode_map[mnemo], text)
                elif len(mnemo) <= self.MAX_MNEMONIC_LENGTH:
                    input.warn("No known UCS-2 code for `%s'", mnemo)
            elif not re.search(' +e000', line):
                input.warn("Unrecognised line")
            line = next

    # Declare a correspondence between a mnemonic and an UCS-2 value.
    def declare(self, mnemonic, unicode, warn):
        if len(mnemonic) > self.MAX_MNEMONIC_LENGTH:
            return
        if self.do_sources:
            if unicode in self.mnemonic_map:
                if self.mnemonic_map[unicode] != mnemonic:
                    warn("U+%04X `%s' known as `%s'",
                               unicode, mnemonic, self.mnemonic_map[unicode])
                    if len(mnemonic) < len(self.mnemonic_map[unicode]):
                        self.mnemonic_map[unicode] = mnemonic
            else:
                self.mnemonic_map[unicode] = mnemonic
                self.table_length += 1
        if mnemonic in self.unicode_map:
            if self.unicode_map[mnemonic] != unicode:
                warn("`%s' U+%04X known as U+%04X",
                     mnemonic, unicode, self.unicode_map[mnemonic])
                #FIXME: ??? cell = self.unicode_map[mnemonic] - 256*row
        else:
            self.unicode_map[mnemonic] = unicode

    def complete(self):
        if self.do_sources:
            self.complete_sources()

    # Write an UCS-2 to RFC 1345 mnemonic table.
    def complete_sources(self):
        if main.python_mode:
            write = Output(self.PY_SOURCES).write
            write('\n'
                  'max_mnemonic_length = %d\n'
                  % self.MAX_MNEMONIC_LENGTH)
            write('\n'
                  'table = {\n')
            pairs = self.mnemonic_map.items()
            pairs.sort()
            for unicode, mnemonic in pairs:
                write('    0x%04X: %r,\n' % (unicode, mnemonic))
            write('    }\n')

            write('\n'
                  'inverse = {\n')
            pairs = [(mnemonic, unicode)
                     for unicode, mnemonic in self.mnemonic_map.items()]
            pairs.sort()
            for mnemonic, unicode in pairs:
                write('    %r: 0x%04X,\n' % (mnemonic, unicode))
            write('    }\n')
        else:
            inverse_map = {}
            write = Output(self.C_SOURCES).write
            write('\n'
                  '#define TABLE_LENGTH %d\n'
                  '#define MAX_MNEMONIC_LENGTH %d\n'
                  % (self.table_length, self.MAX_MNEMONIC_LENGTH))
            write('\n'
                  'struct entry\n'
                  '  {\n'
                  '    recode_ucs2 code;\n'
                  '    const char *rfc1345;\n'
                  '  };\n'
                  '\n'
                  'static const struct entry table[TABLE_LENGTH] =\n'
                  '  {\n')
            count = 0
            indices = self.mnemonic_map.keys()
            indices.sort()
            for unicode in indices:
                text = self.mnemonic_map[unicode]
                inverse_map[text] = count
                write('    /* %4d */ {0x%04X, "%s"},\n'
                      % (count, unicode, re.sub(r'([\"])', r'\\\1', text)))
                count += 1
            write('  };\n')

            write('\n'
                  'static const unsigned short inverse[TABLE_LENGTH] =\n'
                  '  {')
            count = 0
            keys = inverse_map.keys()
            keys.sort()
            for text in keys:
                if count % 10 == 0:
                    if count != 0:
                        write(',')
                    write('\n    /* %4d */ ' % count)
                else:
                    write(', ')
                write('%4d' % inverse_map[text])
                count += 1
            write('\n'
                  '  };\n')


# Global table of strips.

class Strips(Options):
    C_STRIP = 'strip.c'
    PY_STRIP = 'strip.py'
    TEXINFO = 'rfc1345.texi'

    # Change STRIP_SIZE in `src/recode.h' if you change the value here.
    # See the accompanying documentation there, as needed.
    STRIP_SIZE = 8

    # Prepare the production of tables.
    pool_size = 0
    pool_refs = 0
    strip_map = {}
    strips = []

    # While digesting files.
    used_map = {}
    table = []
    declare_alias = []
    implied_surface = {}

    def __init__(self):
        Options.__init__(self)
        self.write = None
        self.aliases_map = {}
        self.remark_map = {}
        self.declare_charset = []
        self.strip_codecs = []
        # Prepare to read various tables.
        self.charset_ordinal = 0
        self.discard_charset = 0
        self.alias_count = 0
        self.comments = []

    # Read the text of RFC 1345, saving all charsets it declares.
    # UCS-2 mnemonics files should have been read in already.
    def digest_rfc1345(self, input, mnemonics):
        self.init_write()
        # Informal canonical order of presentation.
        CHARSET, REM, ALIAS, ESC, BITS, CODE = range(6)
        charset = None
        skip = False
        for line in input:
            if line.startswith('Simonsen'):
                skip = True
                continue
            if skip:
                if line.startswith('RFC 1345'):
                    skip = False
                continue
            if line == '\n':
                continue
            if line == 'ACKNOWLEDGEMENTS\n':
                break
            line, count = re.subn('^  ?', '', line)
            if not count:
                continue
            # Recognize `&charset'.
            match = re.match('&charset (.*)', line)
            if match:
                # Before beginning a new charset, process the previous one.
                if charset:
                    self.charset_done(charset, remark, aliases)
                charset = match.group(1)
                # Prepare for processing a new charset: save the charset
                # name for further declaration; announce this charset in
                # the array initialization section; and initialize its
                # processing.
                sys.stderr.write('  %d) %s\n'
                                 % (self.charset_ordinal + 1, charset))
                status = CHARSET
                self.comments.append(charset)
                hashname = re.sub('[^a-z0-9]', '', charset.lower())
                if hashname in self.used_map:
                    input.warn("Duplicate of %s (discarded)",
                               self.used_map[hashname])
                    self.discard_charset = True
                    continue
                self.used_map[hashname] = charset
                self.alias_count = 0
                self.table = [ord(NOT_A_CHARACTER)] * 256
                codedim = 0
                code = 0
                aliases = []
                remark = []
                match = re.match('(CP|IBM)([0-9]+)$', charset)
                if match:
                    self.implied_surface[match.group(2)] = 'CR-LF'
                    self.implied_surface['CP' + match.group(2)] = 'CR-LF'
                    self.implied_surface['IBM' + match.group(2)] = 'CR-LF'
                    self.declare_alias.append((charset, charset))
                    self.alias_count += 1
                    continue
                #FIXME!
                #match = re.match('windows-([0-9]+)$', charset)
                #if match:
                #      self.implied_surface[match.group(1)] = 'CR-LF'
                #      self.implied_surface['CP' + match.group(1)] = 'CR-LF'
                #      self.implied_surface['IBM' + match.group(1)] = 'CR-LF'
                #      self.declare_alias.append((charset, charset))
                #      self.alias_count += 1
                #      continue
                if charset in ('macintosh', 'macintosh_ce'):
                    self.implied_surface[charset] = 'CR'
                    self.declare_alias.append((charset, charset))
                    self.alias_count += 1
                    continue
                continue
            # Recognize other `&' directives.
            match = re.match('&rem (.*)', line)
            if match and not line.startswith('&rem &alias'):
                # Keld now prefers `&rem' to be allowed everywhere.
                #if status > REM:
                #    input.warn("`&rem' out of sequence")
                #status = REM;
                if self.do_texinfo:
                    # Save remarks for Texinfo.
                    text = match.group(1)
                    remark.append(text)
                continue
            match = re.match('(&rem )?&alias (.*)', line)
            if match:
                if status > ALIAS:
                    input.warn("`&alias' out of sequence")
                status = ALIAS
                # Save synonymous charset names for later declarations.
                alias = match.group(2)
                if alias[-1] == ' ':
                    input.warn("Spurious trailing whitespace")
                    alias = alias.rstrip()
                self.comments.append(alias)
                hashname = re.sub('[^a-z0-9]', '', alias.lower())
                if hashname in self.used_map:
                    if self.used_map[hashname] != charset:
                        input.warn("Duplicate of %s", self.used_map[hashname])
                        continue
                else:
                    self.used_map[hashname] = charset
                aliases.append(alias)
                match = re.match('(CP|IBM)([0-9]+)$', alias)
                if match:
                    self.implied_surface[match.group(2)] = 'CR-LF'
                    self.implied_surface['CP' + match.group(2)] = 'CR-LF'
                    self.implied_surface['IBM' + match.group(2)] = 'CR-LF'
                elif alias in ('mac', 'macce'):
                    self.implied_surface[alias] = 'CR'
                self.declare_alias.append((alias, charset))
                self.alias_count += 1
                continue
            if re.match('&g[0-4]esc', line):
                if status > ESC:
                    input.warn("`&esc' out of sequence")
                status = ESC
                continue
            match = re.match('&bits ([0-9]+)$', line)
            if match:
                if status > BITS:
                    input.warn("`&bits' out of sequence")
                status = BITS
                if int(match.group(1)) > 8:
                    input.warn("`&bits %s' not accepted (charset discarded)",
                               match.group(1))
                    self.discard_charset = True
                continue
            match = re.match('&code (.*)', line)
            if match:
                if status > CODE:
                    input.warn("`&code' out of sequence")
                status = CODE
                # Save the code position.
                code = int(match.group(1))
                continue
            # Other lines cause the charset to be discarded.
            match = re.match('&([^ ]+)', line)
            if match:
                if not self.discard_charset:
                    input.warn("`&%s' not accepted (charset discarded)",
                               match.group(1))
                    self.discard_charset = True
            if self.discard_charset:
                continue
            # Save all other tokens into the double table.
            for token in line.split():
                if token == '??':
                    self.table[code] = ord(NOT_A_CHARACTER)
                elif token == '__':
                    self.table[code] = ord(REPLACEMENT_CHARACTER)
                elif token in mnemonics.unicode_map:
                    self.table[code] = mnemonics.unicode_map[token]
                    if len(token) > codedim:
                        codedim = len(token)
                else:
                    input.warn("Unknown mnemonic for code: %s", token)
                    self.table[code] = ord(REPLACEMENT_CHARACTER)
                code += 1
        # Push the last charset out.
        self.charset_done(charset, remark, aliases)

    # Read a Unicode map, as found in ftp://ftp.unicode.com/MAPPINGS.
    def digest_unimap(self, input, line):
        self.init_write()
        match = re.match('# +Name: +([^ ]+) to Unicode table$', line)
        if match:
            # Set comment.
            name = match.group(1).split()
            charset = name[0]
            del name[0]
            self.comments.append(charset)
            # Set charset.
            hashname = re.sub('[^a-z0-9]', '', charset.lower())
            if self.used_map[hashname]:
                input.warn("`%s' duplicates `%s' (charset discarded)",
                           hashname, self.used_map[hashname])
                self.discard_charset = True
                return
            self.used_map[hashname] = charset
            # Prepare for read.
            self.alias_count = 0
            self.table = [ord(NOT_A_CHARACTER)] * 256
            codedim = 0
            code = 0
            aliases = []
            remark = []
        if self.discard_charset:
            return
        # Process aliases.
        for alias in name:
            self.comments.append(alias)

            hashname = re.sub('[^a-z0-9]', '', alias.lower())
            if self.used_map[hashname] and self.used_map[hashname] != charset:
                input.warn("`%s' duplicates `%s'", hashname,
                           self.used_map[hashname])
                continue
            self.used_map[hashname] = charset

            aliases.append(alias)
            self.declare_alias.append((alias, charset))
            self.alias_count += 1
        # Read table contents.
        for line in input:
            if line == '\n':
                continue
            if line[0] == '#':
                continue
            if re.match('0x([0-9A-F]+)\t\t#UNDEFINED$', line):
                continue
            if re.search('\032', line):
                # Old MS-DOS C-z !!
                break
            match = re.match('0x([0-9A-F]+)\t0x([0-9A-F]+)\t\#', line)
            if match:
                self.table[int(match.group(1), 16)] = int(match.group(2), 16)
            else:
                input.warn("Unrecognised input line")
        # Complete processing.
        self.charset_done(charset, remark, aliases)

    def init_write(self):
        if self.do_sources and not self.write:
            # Table fragments will be produced while reading data tables.
            if main.python_mode:
                write = self.write = Output(self.PY_STRIP).write
                write('\n'
                      'import recode\n'
                      '\n'
                      'declares = [\n')
            else:
                write = self.write = Output(self.C_STRIP).write
                write('\n'
                      '#include \"common.h\"\n')

    # Print all accumulated information for the charset.  If the
    # charset should be discarded, adjust tables.
    def charset_done(self, charset, remark, aliases):
        if self.discard_charset:
            while self.alias_count > 0:
                del self.declare_alias[-1]
                self.alias_count -= 1
            self.discard_charset = False
            self.comments = []
        if not self.comments:
            return
        if self.do_texinfo:
            # Save the documentation.
            aliases.sort()
            self.aliases_map[charset] = aliases
            self.remark_map[charset] = remark
        if main.explodes:
            write = main.explodes.write
            # Make introductory comments.
            if main.python_mode:
                write('\n# %s\n' % '\n# '.join(self.comments))
            else:
                write('\n/* %s */\n' % '\n   '.join(self.comments))
            # Make the table for this charset.  (FIXME: Python!)
            if main.python_mode:
                write('\n'
                      'data_%d = {\n'
                      % self.charset_ordinal)
                for code in range(256):
                    if code != self.table[code]:
                        write('    %3d: (0x%.4X,),\n'
                              % (code, self.table[code]))
                write('    }\n')
            else:
                write('\n'
                      'static const unsigned short data_%d[] =\n'
                      '  {\n'
                      % self.charset_ordinal)
                for code in range(256):
                    if code != self.table[code]:
                        write('    %3d, 0x%.4X, DONE,\n'
                              % (code, self.table[code]))
                write('    DONE\n'
                      '  };\n')
            # Register the table.
            self.declare_charset.append(charset)
        if self.do_sources:
            write = self.write
            # Make introductory comments.
            if main.python_mode:
                if len(self.comments) == 1:
                    write('    %r,\n' % self.comments[0])
                else:
                    write('    (%s),\n' % ', '.join(
                        [repr(comment) for comment in self.comments]))
            # Make the table for this charset.
            self.strip_codecs.append((
                self.charset_ordinal,
                self.comments[0],
                [self.pool_index(self.table[code:code+self.STRIP_SIZE])
                 for code in range(0, 256, self.STRIP_SIZE)]))
            # Register the table.
            self.declare_charset.append(charset)
        self.charset_ordinal += 1
        self.comments = []

    # Return the pool index for strip.  Add to the pool as required.
    def pool_index(self, strip):
        self.pool_refs += 1
        text = ''.join(['%04X' % item for item in strip])
        if text not in self.strip_map:
            self.strip_map[text] = self.pool_size
            self.pool_size += self.STRIP_SIZE
            self.strips.append(text)
        return self.strip_map[text]

    def complete(self):
        if self.do_sources:
            self.complete_sources()
        if self.do_texinfo:
            self.complete_texinfo()

    def complete_sources(self):
        if main.python_mode:
            sys.stderr.write("Completing %s\n" % self.PY_STRIP)
        else:
            sys.stderr.write("Completing %s\n" % self.C_STRIP)
        write = self.write
        # Write out the UCS2 character pool.
        sys.stderr.write('  (table memory = %d bytes: pool %d, refs %d)\n'
                         % (self.pool_size * 2 + self.pool_refs * 2,
                            self.pool_size * 2,
                            self.pool_refs * 2))
        if main.python_mode:
            write('    ]\n'
                  '\n'
                  'unicode_data_pool = (\n'
                  '    u\'')
        else:
            write('\n'
                  'const recode_ucs2 ucs2_data_pool[%d] =\n'
                  '  {'
                  % self.pool_size)
        count = 0
        for strip in self.strips:
            for pos in range(0, self.STRIP_SIZE * 4, 4):
                if main.python_mode:
                    if count % 10 == 0:
                        if count != 0:
                            write('\'  # %d\n'
                                  '    u\''
                                  % (count-10))
                    write('\\u' + strip[pos:pos+4])
                else:
                    if count % 8 == 0:
                        if count != 0:
                            write(',')
                        write('\n    /* %4d */ ' % count)
                    else:
                        write(', ')
                    write('0x' + strip[pos:pos+4])
                count += 1
        if main.python_mode:
            if count > 0:
                if count % 10 == 0:
                    fill = ''
                else:
                    fill = '      ' * (10 - count % 10)
            write('\'%s  # %d\n'
                  '    )\n'
                  % (fill, count // 10 * 10))
        else:
            write('\n'
                  '  };\n')
        # Write charset description data.
        for ordinal, charset, indices in self.strip_codecs:
            if main.python_mode:
                write('\n'
                      'class StripCodec_%d(recode.StripStep):\n'
                      '    external_coding = %r\n'
                      '    strip_pool = unicode_data_pool\n'
                      % (ordinal, charset))
            else:
                write('\n'
                      '/* %s */\n'
                      '\n'
                      'static struct strip_data data_%d =\n'
                      '  {\n'
                      '    ucs2_data_pool,\n'
                      '    {\n'
                      % (charset, ordinal))
            count = 0
            for indice in indices:
                if main.python_mode:
                    if count % 11 == 0:
                        if count == 0:
                            write('    data = (')
                        else:
                            write(',\n'
                                  '            ')
                    else:
                        write(', ')
                    write('%d' % indice)
                else:
                    if count % 12 == 0:
                        if count != 0:
                            write(',\n')
                        write('      ')
                    else:
                        write(', ')
                    write('%4d' % indice)
                count += 1
            if main.python_mode:
                write(')\n')
            else:
                write('\n'
                      '    }\n'
                      '  };\n')
        # Print the collectable initialization function.
        if main.python_mode:
            del self.declare_charset[:]
            write('\n'
                  'implied_surfaces = [\n')
            for alias, charset in self.declare_alias:
                surface = self.implied_surface.get(alias)
                if surface is not None:
                    write('    (%r, %r),\n' % (alias, surface))
            write('    ]\n')
            del self.declare_alias[:]
        else:
            write('\n'
                  'bool\n'
                  'module_strips (struct recode_outer *outer)\n'
                  '{\n'
                  '  RECODE_ALIAS alias;\n'
                  '\n')
            count = 0
            for charset in self.declare_charset:
                write('  if (!declare_strip_data (outer, &data_%d, "%s"))\n'
                      '    return false;\n'
                      % (count, charset))
                count += 1
            write('\n')
            del self.declare_charset[:]
            for alias, charset in  self.declare_alias:
                if alias in self.implied_surface:
                    write('  if (alias = declare_alias (outer, "%s", "%s"),'
                          ' !alias)\n'
                          '    return false;\n'
                          % (alias, charset))
                    write('  if (!declare_implied_surface (outer, alias,'
                          ' outer->%s_surface))\n'
                          '    return false;\n'
                          % self.implied_surface[alias])
                else:
                    write('  if (!declare_alias (outer, "%s", "%s"))\n'
                          '    return false;\n'
                          % (alias, charset))
            write('\n'
                  '  return true;\n'
                  '}\n'
                  '\n'
                  'void\n'
                  'delmodule_strips (struct recode_outer *outer)\n'
                  '{\n'
                  '}\n')
            del self.declare_alias[:]

    def complete_texinfo(self):
        if main.french_mode:
            write = Output('fr-%s' % self.TEXINFO, noheader=True).write
        else:
            write = Output(self.TEXINFO, noheader=True).write
        charsets = self.remark_map.keys()
        charsets.sort()
        for charset in charsets:
            write('\n'
                  '@item %s\n'
                  '@tindex %s@r{, aliases and source}\n'
                  % (charset, re.sub(':([0-9]+)', r'(\1)', charset)))
            aliases = self.aliases_map[charset]
            if aliases:
                if len(aliases) == 1:
                    if aliases[0]:      # FIXME: pourquoi parfois vide ??
                        write('@tindex %s\n'
                              '@code{%s} is an alias for this charset.\n'
                              % (re.sub(':([0-9]+)', r'(\1)', aliases[0]),
                                 aliases[0]))
                else:
                    for alias in aliases:
                        write('@tindex %s\n'
                              % re.sub(':([0-9]+)', r'(\1)', alias))
                    write('@code{%s} and @code{%s} are aliases'
                          ' for this charset.\n'
                          % ('}, @code{'.join(aliases[:-1]), aliases[-1]))
            for line in self.remark_map[charset]:
                if line[0].islower():
                    line = line[0].upper() + line[1:]
                write(line.replace('@', '@@'))
                if line[-1] != '.':
                    write('.')
                write('\n')

# Handling basic input and output.

class Input:
    def __init__(self, name):
        self.name = name
        self.input = file(name)
        self.line_count = 0
        sys.stderr.write("Reading %s\n" % name)

    def __iter__(self):
        return self

    def next(self):
        line = self.input.readline()
        if line:
            self.line_count += 1
            return line
        raise StopIteration

    def readline(self):
        line = self.input.readline()
        if line:
            self.line_count += 1
        return line

    def warn(self, format, *args):
        sys.stderr.write('%s:%s: %s\n'
                         % (self.name, self.line_count, format % args))

    def die(self, format, *args):
        sys.stderr.write('%s:%s: %s\n'
                         % (self.name, self.line_count, format % args))
        raise 'Fatal'

class Output:
    def __init__(self, name, noheader=False):
        self.name = name
        self.write = file(name, 'w').write
        sys.stderr.write("Writing %s\n" % name)
        if not noheader:
            if main.python_mode:
                self.write("""\
# DO NOT MODIFY THIS FILE!  It was generated by `recode/doc/tables.py'.

# Conversion between different charsets, surfaces and structures.
# Copyright � 1993, 1997, 1999, 2002 Free Software Foundation, Inc.
# Contributed by Fran�ois Pinard <pinard@iro.umontreal.ca>, 1993.
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public License
# as published by the Free Software Foundation; either version 2 of the
# License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be
# useful, but WITHOUT ANY WARRANTY; without even the implied warranty
# of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with the `recode' Library; see the file `COPYING.LIB'.
# If not, write to the Free Software Foundation, Inc., 59 Temple Place -
# Suite 330, Boston, MA 02111-1307, USA.
""")
            else:
                self.write("""\
/* DO NOT MODIFY THIS FILE!  It was generated by `recode/doc/tables.py'.  */

/* Conversion between different charsets, surfaces and structures.
   Copyright � 1993, 1997, 1999, 2002 Free Software Foundation, Inc.
   Contributed by Fran�ois Pinard <pinard@iro.umontreal.ca>, 1993.

   This library is free software; you can redistribute it and/or
   modify it under the terms of the GNU Lesser General Public License
   as published by the Free Software Foundation; either version 2 of the
   License, or (at your option) any later version.

   This library is distributed in the hope that it will be
   useful, but WITHOUT ANY WARRANTY; without even the implied warranty
   of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
   Lesser General Public License for more details.

   You should have received a copy of the GNU Lesser General Public
   License along with the `recode' Library; see the file `COPYING.LIB'.
   If not, write to the Free Software Foundation, Inc., 59 Temple Place -
   Suite 330, Boston, MA 02111-1307, USA.  */
""")

if __name__ == '__main__':
    main.main(*sys.argv[1:])
