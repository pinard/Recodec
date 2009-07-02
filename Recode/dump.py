# Conversion of files between different charsets and surfaces.
# Copyright © 1997, 98, 99, 00, 02 Free Software Foundation, Inc.
# Contributed by François Pinard <pinard@iro.umontreal.ca>, 1997.
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

import recode

declares = [
    ('Decimal-1', 'd', 'd1'),
    ('Decimal-2', 'd2'),
    ('Decimal-3', 'd3'),
    ('Decimal-4', 'd4'),
    ('Hexadecimal-1', 'x', 'x1'),
    ('Hexadecimal-2', 'x2'),
    ('Hexadecimal-3', 'x3'),
    ('Hexadecimal-4', 'x4'),
    ('Octal-1', 'o', 'o1'),
    ('Octal-2', 'o2'),
    ('Octal-3', 'o3'),
    ('Octal-4', 'o4'),
    ]

# Constants for the possible bases.  If these are reordered, so should be
# the MATRIX array near the end of this module.
DECIMAL, HEXADECIMAL, OCTAL = range(3)

class DumpStep(recode.Step):
    # Sub-classes define FORMAT for the printing format to use and PER_LINE
    # for the number of printed values per output line; these are used by
    # `encode'.  Sub-classes also define WIDTH as the number of active
    # digits to expect, including and counting a possible `0' or `0x'
    # for the base prefix; this is used by `decode'.

    internal_coding = recode.TRIVIAL_SURFACE

    def encode(self, input, errors='strict'):
        size = self.size
        format = self.format
        index = 0
        column = 0
        output = []
        while index < len(input):
            # Adjust for shorter output at end.
            if index + size > len(input):
                size = len(input) - index
                format = matrix[size][self.base].format
            # Get combined value.
            value = 0
            for counter in range(size):
                value = (value << 8) + ord(input[index])
                index += 1
            # Write delimiters.
            if column == self.per_line:
                output.append(',\n')
                column = 1
            elif column == 0:
                column = 1
            else:
                output.append(', ')
                column += 1
            # Write formatted value.
            output.append(format % value)
        output.append('\n')
        return ''.join(output), len(input)

    def decode(self, input, errors='strict'):
        output = []
        for line in input.splitlines():
            for field in line.replace(', ', ',').split(','):
                token = field.strip()
                # Ignore comma at end of line, or two consecutive commas.
                if not token:
                    continue
                # Let the number announce its base, ignore user prediction.
                # Silently ignore rest of line on first error.
                try:
                    if token == '0':
                        base = DECIMAL
                        value = 0
                    elif token.startswith('0x'):
                        base = HEXADECIMAL
                        value = long(token[2:], 16)
                    elif token.startswith('0'):
                        base = OCTAL
                        value = long(token[1:], 8)
                    elif token:
                        base = DECIMAL
                        value = long(token)
                except ValueError:
                    break
                # Deduce number of bytes from field width, but in case the
                # width has no exact match, use whatever the user predicted.
                for size in range(1, 5):
                    if matrix[size][base].width == len(field):
                        break
                else:
                    size = self.size
                # Produce characters from value.
                for shift in range(8*size-8, -8, -8):
                    output.append(chr(value >> shift & 255))
        return ''.join(output), len(input)

class DecimalStep(DumpStep):
    base = DECIMAL

class Decimal_1(DecimalStep):
    external_coding = 'Decimal-1'
    size = 1
    format = '%3d'
    width = 3
    per_line = 15

class Decimal_2(DecimalStep):
    external_coding = 'Decimal-2'
    size = 2
    format = '%5d'
    width = 5
    per_line = 10

class Decimal_3(DecimalStep):
    external_coding = 'Decimal-3'
    size = 3
    format = '%8d'
    width = 8
    per_line = 7

class Decimal_4(DecimalStep):
    external_coding = 'Decimal-4'
    size = 4
    format = '%10d'
    width = 10
    per_line = 5

class HexadecimalStep(DumpStep):
    base = HEXADECIMAL

class Hexadecimal_1(HexadecimalStep):
    external_coding = 'Hexadecimal-1'
    size = 1
    format = '0x%02X'
    width = 4
    per_line = 12

class Hexadecimal_2(HexadecimalStep):
    external_coding = 'Hexadecimal-2'
    size = 2
    format = '0x%04X'
    width = 6
    per_line = 8

class Hexadecimal_3(HexadecimalStep):
    external_coding = 'Hexadecimal-3'
    size = 3
    format = '0x%06X'
    width = 8
    per_line = 7

class Hexadecimal_4(HexadecimalStep):
    external_coding = 'Hexadecimal-4'
    size = 4
    format = '0x%08X'
    width = 10
    per_line = 6

class OctalStep(DumpStep):
    base = OCTAL

class Octal_1(OctalStep):
    external_coding = 'Octal-1'
    size = 1
    format = '0%03o'
    width = 4
    per_line = 12

class Octal_2(OctalStep):
    external_coding = 'Octal-2'
    size = 2
    format = '0%06o'
    width = 7
    per_line = 8

class Octal_3(OctalStep):
    external_coding = 'Octal-3'
    size = 3
    format = '0%08o'
    width = 9
    per_line = 6

class Octal_4(OctalStep):
    external_coding = 'Octal-4'
    size = 4
    format = '0%011o'
    width = 12
    per_line = 4

# The notation `matrix[SIZE][BASE].PARAMETER' is sometimes useful.
matrix = ((None,      None,          None   ),
          (Decimal_1, Hexadecimal_1, Octal_1),
          (Decimal_2, Hexadecimal_2, Octal_2),
          (Decimal_3, Hexadecimal_3, Octal_3),
          (Decimal_4, Hexadecimal_4, Octal_4))
