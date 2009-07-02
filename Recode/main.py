#!/usr/bin/env python
# Copyright © 2002 Free Software Foundation, Inc.
# Contributed by François Pinard <pinard@iro.umontreal.ca>, 2002.

# I postponed a bit the writing of the following `--help' block, not sure
# about when and how I will add internationalisation.  But pondering this
# a bit more, it's better having some help now than none at all.

"""\
Recodec converts between various character sets, surfaces and structures.

Usage: recodec [OPTION]... [ [CHARSET] | REQUEST [FILE]... ]

If a long option shows an argument as mandatory, then it is mandatory
for the equivalent short option as well.

WARNING: The `@' symbols, below, mark features which are not implemented
yet.  They will progressively melt as `0.X' releases progress, until `1.0'.
The `--sequence' setting is currently tied to `memory'.  Also missing
are charsets `applemac' and `ebcdic' (the old ones), the `mule' cleaner,
`rfc1345' and its options; and finally, message internationalisation.
Asian support will be reintroduced only after `1.0' is released, however.

Listings:
  -l, --list[=FORMAT]        list one or all known charsets and aliases
@ -k, --known=PAIRS          restrict charsets according to known PAIRS list
@ -h, --header[=[LN/]NAME]   write table NAME on stdout using LN, then exit
  -C, --copyright            display Copyright and copying conditions
      --help                 display this help and exit
      --version              output version information and exit

Operation modes:
  -v, --verbose           explain sequence of steps and report progress
  -q, --quiet, --silent   inhibit messages about irreversible recodings
  -f, --force             force recodings even when not reversible
  -t, --touch             touch the recoded files after replacement
@ -i, --sequence=files    use intermediate files for sequencing passes
@     --sequence=memory   use memory buffers for sequencing passes
@ -p, --sequence=pipe     use pipe machinery for sequencing passes
@ -p, --sequence=pipe     or, same as -i (on this system)

Fine tuning:
  -s, --strict           use strict mappings, even loose characters
@ -d, --diacritics       convert only diacritics or alike for HTML/LaTeX
@ -S, --source[=LN]      limit recoding to strings and comments as for LN
@ -c, --colons           use colons instead of double quotes for diaeresis
@ -g, --graphics         approximate IBMPC rulers by ASCII graphics
@ -x, --ignore=CHARSET   ignore CHARSET while choosing a recoding path

FORMAT is `codings', `decimal', `octal', `hexadecimal' or `full' (or one of
`cdohf').  If `codings', then list available charsets and surfaces.
@ Unless DEFAULT_CHARSET is set in environment, CHARSET defaults to the locale
@ dependent encoding, determined by LC_ALL, LC_CTYPE, LANG.
@ With -k, possible before charsets are listed for the given after CHARSET,
@ both being tabular charsets, with PAIRS of the form `BEF1:AFT1,BEF2:AFT2,...'
@ and BEFs and AFTs being codes are given as decimal numbers.
@ LN is some language, it may be `C', `Perl', `PO' or `Python'.

REQUEST is SUBREQUEST[,SUBREQUEST]...; SUBREQUEST is ENCODING[..ENCODING]...
ENCODING is [CHARSET][/[SURFACE]]...; REQUEST often looks like BEFORE..AFTER,
with BEFORE and AFTER being charsets.  An omitted CHARSET implies the usual
charset; an omitted [/SURFACE]... means the implied surfaces for CHARSET; a /
with an empty surface name means no surfaces at all.  @ See the manual.

@ If none of -i and -p are given, presume -p if no FILE, else -i.
Each FILE is recoded over itself, destroying the original.  If no
FILE is specified, then act as a filter and recode stdin to stdout.

Report bugs to mailto:recode-bugs@iro.umontreal.ca.
"""

import sys
import recode

class Main:
    def __init__(self):
        self.errors = None
        self.headers = None
        self.listing = None
        self.sequence = None
        self.source = None
        self.touch = False
        self.verbose = False

    def main(self, *arguments):
        if not arguments:
            sys.stdout.write(__doc__)
            sys.exit(0)
        try:
            self.decode_program_options(arguments)
            if self.listing is not None:
                self.write_listing(sys.stdout.write)
                sys.exit(0)
            self.recode_all_files()
        except recode.NotImplementedError, message:
            sys.stderr.write("Not implemented: %s.\n" % message)
            sys.exit(1)
        except recode.AmbiguousWordError, name:
            sys.stderr.write("Word `%s' is ambiguous.\n" % name)
            sys.exit(1)
        except recode.UnknownWordError, name:
            sys.stderr.write("Word `%s' is unknown.\n" % name)
            sys.exit(1)
        except recode.UnresolvedRecodecError, (before, after):
            sys.stderr.write("Cannot recode from `%s' to `%s'.\n"
                             % (before, after))
            sys.exit(1)
        except recode.ComplexRecodecError, (before, after):
            sys.stderr.write("Going from `%s' to `%s' is not simple enough.\n"
                             % (before, after))
            sys.exit(1)

    def decode_program_options(self, arguments):
        import getopt
        options, self.arguments = getopt.getopt(
            arguments, 'CFS:cdfgh:ik:l:pqstvx:',
            ['colons', 'copyright', 'diacritics', 'force', 'freeze-tables',
            'header', 'help', 'ignore', 'known', 'list', 'listing', 'quiet',
            'sequence', 'source', 'silent', 'strict', 'touch', 'verbose',
            'version'])
        for option, value in options:
            if option in ('-C', '--copyright'):
                self.write_copyright(sys.stdout.write)
                sys.exit(0)
            elif option in ('-F', '--freeze-tables'):
                pass                    # FIXME!
            elif option in ('-S', '--source'):
                self.source = recode.resolve(value.lower(),
                                             ['c', 'perl', 'po'])
            elif option in ('-c', '--colons'):
                pass                    # FIXME!
            elif option in ('-d', '--diacritics'):
                pass                    # FIXME!
            elif option in ('-f', '--force'):
                assert self.errors is None, self.errors
                self.errors = 'ignore'
            elif option in ('-g', '--graphics'):
                pass                    # FIXME!
            elif option in ('-h', '--headers'):
                self.headers = recode.resolve(value.lower(), ['c', 'perl'])
            elif option in ('-k', '--known'):
                pass                    # FIXME!
            elif option in ('-l', '--list', '--listing'):
                self.listing = recode.resolve(
                    value.lower(),
                    ['codings', 'decimal', 'octal', 'hexadecimal', 'full'])
            elif option in ('-q', '--quiet', '--silent'):
                pass
            elif option in ('-s', '--strict'):
                assert self.errors is None, self.errors
                self.errors = 'strict'
            elif option in ('-t', '--touch'):
                self.touch = True
            elif option in ('-v', '--verbose'):
                self.verbose = True
            elif option in ('-x', '--ignore'):
                pass                    # FIXME!
            elif option == '--help':
                self.write_help(sys.stdout.write)
                sys.exit(0)
            elif option == '--version':
                sys.write_version(sys.stdout.write)
                sys.exit(0)
            elif option == '--sequence':
                self.sequence = recode.resolve(
                    value.lower(), ['memory', 'files', 'pipe'])
        if self.errors is None:
            self.errors = 'replace'

    def write_copyright(self, write):
        write("""\
This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2, or (at your option)
any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software Foundation,
Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.
""")

    def write_help(self, write):
        write(__doc__)

    def write_version(self, write):
        import version
        write('%s %s\n' % (version.package, version.version))

    def write_listing(self, write):
        import listings
        if self.listing == 'codings':
            assert not self.arguments, self.arguments
            listings.list_all_codings(write)
        else:
            assert len(self.arguments) == 1, self.arguments
            charset = self.arguments[0]
            if self.listing == 'full':
                listings.list_full_charset(charset, write)
            else:
                listings.list_concise_charset(
                    charset,
                    ({'decimal': 10, 'octal': 8, 'hexadecimal': 16}
                     [self.listing]),
                    write)

    def recode_all_files(self):
        assert len(self.arguments) > 0
        request = self.arguments[0]
        arguments = self.arguments[1:]
        codec = recode.Recodec(request)
        if self.verbose:
            counter = 0
            for before, after in codec.encoding_arcs():
                counter += 1
                sys.stderr.write('  %d: %s..%s\n' % (counter, before, after))
        if arguments:
            import os, tempfile
            counter = 0
            for name in arguments:
                counter += 1
                if self.verbose:
                    sys.stderr.write('%d/%d. %s...' %
                                     (counter, len(arguments), name))
                # Choose a file name in same directory.
                saved_tempdir = tempfile.tempdir
                tempfile.tempdir = os.path.dirname(
                    os.path.abspath(name))
                tempname = tempfile.mktemp()
                tempfile.tempdir = saved_tempdir
                # Recode original file into the temporary one.
                text, length = codec.encode(file(name).read(), self.errors)
                file(tempname, 'w').write(text)
                # Possibly adjust time stamp of copy.
                if not self.touch:
                    os.utime(tempname, (os.path.getatime(name),
                                        os.path.getmtime(name)))
                # Move copy over original, destroying it.
                os.remove(name)
                os.rename(tempname, name)
                if self.verbose:
                    sys.stderr.write(' done\n')
        else:
            text, length = codec.encode(sys.stdin.read(), self.errors)
            sys.stdout.write(text)

run = Main()
main = run.main

if __name__ == '__main__':
    main(*sys.argv[1:])
