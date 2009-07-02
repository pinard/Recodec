#!/usr/bin/env python
# Copyright © 2002 Free Software Foundation, Inc.
# Contributed by François Pinard <pinard@iro.umontreal.ca>, 2002.

"""\
Conversion between different charsets, surfaces and structures.

Pre-computation of recoding preset data.
"""

import sys
from Recode import recode
import common

class Main:

    def main(self, *arguments):
        assert not arguments, arguments
        self.study_python_modules()
        write = common.Output('builtin.py', 'Python').write
        write('\n'
              'import recode\n')
        self.write_aliases(write)
        self.write_methods(write)

    def study_python_modules(self):
        import encodings, glob, os
        # Saving Python aliases.
        self.aliases = {}
        self.codings = []
        for name in glob.glob('%s/*.py' % os.path.dirname(encodings.__file__)):
            # Study module BASE within the `encodings' package.
            base = os.path.split(name)[1][:-3]
            if base in ('charmap', 'undefined'):
                # These are not meant for users.
                continue
            if base == 'iso8859_1':
                # This duplicates `latin_1' module.  Uselessly?
                continue
            try:
                module = getattr(__import__('encodings.' + base), base)
            except AttributeError:
                if base == 'mbcs':
                    # Precisely ignore this Python 2.2.1 bug.
                    continue
                raise
            # Any module which registers itself is a coding name.  There is
            # still no way to get the real canonical coding name, however.
            try:
                encode, decode, reader, writer = module.getregentry()
            except AttributeError:
                pass
            else:
                self.save_alias(base, base)
                self.codings.append(base)
            # A module may define its own aliases.  Not so useful for finding
            # that module, unless it has already been found and imported!
            try:
                aliases = getattr(module, 'getaliases')()
            except AttributeError:
                pass
            else:
                for alias in aliases:
                    self.save_alias(base, alias)
            # The `aliases' module defines ALIASES as a dictionary, study it.
            # But let's skip the `aliases' module imported within `__init__'.
            try:
                aliases = getattr(module, 'aliases')
            except AttributeError:
                pass
            else:
                if isinstance(aliases, dict):
                    for alias, base in aliases.iteritems():
                        self.save_alias(base, alias)

    def save_alias(self, base, alias):
        if base not in self.aliases:
            self.aliases[base] = []
        if recode.cleaned_alias(alias) != recode.cleaned_alias(base):
            self.aliases[base].append(alias)

    def write_aliases(self, write):
        # Write out aliases.
        write('\n'
              'declares = [\n')
        items = self.aliases.items()
        items.sort()
        for coding, aliases in items:
            aliases.sort()
            if len(aliases) == 0:
                write('    %r,\n' % coding)
            else:
                write('    (%r, %s),\n'
                      % (coding,
                         ', '.join([repr(alias) for alias in aliases])))
        write('    ]\n')

    def write_methods(self, write):
        self.codings.sort()
        for coding in self.codings:
            # Find out the internal and external coding names.
            external = coding
            for prefix in 'cp', 'iso8859_', 'mac_', 'utf_':
                if coding.startswith(prefix):
                    internal = recode.UNICODE_STRING
                    break
            else:
                if coding in ('ascii', 'euc_kr', 'koi8_r', 'latin_1',
                              'raw_unicode_escape', 'uhc',
                              'unicode_escape', 'unicode_internal'):
                    internal = recode.UNICODE_STRING
                elif coding in ('base64_codec', 'hex_codec',
                                'quopri_codec', 'rot_13', 'uu_codec',
                                'zlib_codec'):
                    internal = recode.TRIVIAL_SURFACE
                else:
                    sys.stderr.write("Unknown methods for Python `%s'.\n"
                                     % coding)
                    continue
            # Produce a trampoline class.
            write('\n'
                  'class Codec_%s(recode.BuiltinStep):\n'
                  '    internal_coding = %r\n'
                  '    external_coding = %r\n'
                  % (coding, internal, external))
            if internal == recode.TRIVIAL_SURFACE:
                write('    always_strict = True\n')

if __name__ == '__main__':
    Main().main(*sys.argv[1:])
