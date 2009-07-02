#!/usr/bin/env python
# Copyright © 2002 Free Software Foundation, Inc.
# Contributed by François Pinard <pinard@iro.umontreal.ca>, 2002.

"""\
Conversion between different charsets, surfaces and structures.
"""

PACKAGE = 'recodec'
VERSION = '0.0'

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
            sys.stderr.write('Not implemented: %s.\n' % message)
            sys.exit(1)
        except recode.AmbiguousWordError, (name, found):
            sys.stderr.write("Ambiguous word `%s': `%s'...\n"
                             % (name, '\', `'.join(found[:4])))
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
            arguments, 'CFS:Tcdfgh:ik:l:pqstvx:',
            ['colons', 'copyright', 'diacritics', 'find-subsets', 'force',
             'freeze-tables', 'header', 'help', 'ignore', 'known', 'list',
             'listing', 'quiet', 'sequence', 'source', 'silent', 'strict',
             'touch', 'verbose', 'version'])
        for option, value in options:
            if option in ('-C', '--copyright'):
                self.write_copyright(sys.stdout.write)
                sys.exit(0)
            elif option in ('-F', '--freeze-tables'):
                pass                    # FIXME!
            elif option in ('-S', '--source'):
                self.source = recode.resolve(value.lower(),
                                             ['c', 'perl', 'po'])
            elif option in ('-T', '--find-subsets'):
                self.listing = 'subsets'
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
                sys.write_help(sys.stdout.write)
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
        pass                            # FIXME!

    def write_version(self, write):
        write('%s %s\n' % (PACKAGE, VERSION))

    def write_listing(self, write):
        import listings
        if self.listing == 'codings':
            assert not self.arguments, self.arguments
            listings.list_all_codings(write)
        elif self.listing == 'subsets':
            assert not self.arguments, self.arguments
            listings.list_all_subsets(write)
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
            import tempfile
            for name in arguments:
                # Choose a file name in same directory.
                saved_tempdir = tempfile.tempdir
                tempfile.tempdir = os.path.dirname(
                    os.path.abspath(name))
                tempname = tempfile.mktemp()
                tempfile.tempdir = saved_tempdir
                # Recode original file into the temporary one.
                text, length = codec.encode(file(name), self.errors)
                file(tempname, 'w').write(text)
                # Possibly adjust time stamp of copy.
                if not self.touch:
                    os.utime(tempname, (os.path.getatime(name),
                                        os.path.getmtime(name)))
                # Move copy over original, destroying it.
                os.remove(name)
                os.rename(tempname, name)
        else:
            text, length = codec.encode(sys.stdin.read(), self.errors)
            sys.stdout.write(text)

run = Main()
main = run.main

if __name__ == '__main__':
    main(*sys.argv[1:])
