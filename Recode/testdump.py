# Conversion of files between different charsets and surfaces.
# Copyright © 1996, 97, 98, 99, 00, 02 Free Software Foundation, Inc.
# Contributed by François Pinard <pinard@iro.umontreal.ca>, 1997.
#
# The `recode' Library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Library General Public License
# as published by the Free Software Foundation; either version 2 of the
# License, or (at your option) any later version.
#
# The `recode' Library is distributed in the hope that it will be
# useful, but WITHOUT ANY WARRANTY; without even the implied warranty
# of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Library General Public License for more details.
#
# You should have received a copy of the GNU Library General Public
# License along with the `recode' Library; see the file `COPYING.LIB'.
# If not, write to the Free Software Foundation, Inc., 59 Temple Place -
# Suite 330, Boston, MA 02111-1307, USA.

import recode

# One should _remove_ pseudo-surfaces to _produce_ test patterns.
# This strange-looking decision comes from the fact that test patterns
# are usually requested from the `before' position in the request.

declares = ['test7', 'test8', 'test15', 'test16',
            'count-characters', 'dump-with-names']

class TestDumpStep(recode.Step):
    internal_coding = recode.UNICODE_STRING

## Test surfaces.

class Test7(TestDumpStep):
    external_coding = 'test7'
    def decode(self, input, errors='strict'):
        return ''.join(map(chr, range(1<<7))) + input, len(input)

class Test8(TestDumpStep):
    external_coding = 'test8'
    def decode(self, input, errors='strict'):
        return ''.join(map(chr, range(1<<8))) + input, len(input)

class Test15(TestDumpStep):
    external_coding = 'test15'
    def decode(self, input, errors='strict'):
        ignore = [ord(recode.BYTE_ORDER_MARK),
                  ord(recode.REPLACEMENT_CHARACTER),
                  ord(recode.BYTE_ORDER_MARK_SWAPPED),
                  ord(recode.NOT_A_CHARACTER)]
        before_surrogate = ''.join(map(unichr, xrange(0, 0xDC00)))
        after_surrogate = ''.join([
            unichr(code) for code in xrange(0xE000, 1<<16)
            if code not in ignore])
        return before_surrogate + after_surrogate + input, len(input)

class Test16(TestDumpStep):
    external_coding = 'test16'
    def decode(self, input, errors='strict'):
        return ''.join(map(unichr, range(1<<16))) + input, len(input)

## Analysis charsets.

class CountCharacters(TestDumpStep):
    external_coding = 'count-characters'
    def encode(self, input, errors='strict'):
        if not input:
            return '', 0
        # Count characters.
        table = {}
        for character in input:
            table[character] = table.get(character, 0) + 1
        # Sort results.
        items = table.items()
        items.sort()
        # Produce the report.  FIXME: Produce it column-wise (see transp.c).
        count_width = len(str(max(table.values())))
        entry_width = count_width + 12
        fragments = []
        column = 0
        line = []
        import rfc1345
        for character, count in items:
            if column + entry_width > 79:
                fragments.append(''.join(line).rstrip() + '\n')
                line = []
                column = 0
            line.append('%*d  %.4X %-3s  '
                        % (count_width, count, ord(character),
                           rfc1345.table.get(character, '')))
            column += entry_width
        if column > 0:
            fragments.append(''.join(line).rstrip() + '\n')
        return ''.join(fragments), len(input)

# Fully dump an UCS-2 file.
class DumpWithNames(TestDumpStep):
    external_coding = 'dump-with-names'
    def encode(self, input, errors='strict'):
        if not input:
            return '', 0
        import rfc1345
        fragments = []
        fragments.append("UCS2   Mne   Description\n\n")
        for character in input:
            description = recode.unicode_description(ord(character)) or ''
            fragments.append(
                (('%.4X   %-3s   %s' % (ord(character),
                                        rfc1345.table.get(ord(character), ''),
                                        description))
                 .rstrip()) + '\n')
        return ''.join(fragments), len(input)
