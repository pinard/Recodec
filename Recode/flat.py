# Conversion of files between different charsets and surfaces.
# Copyright © 1990, 93, 94, 97, 98, 99, 00, 02 Free Software Foundation, Inc.
# Contributed by François Pinard <pinard@iro.umontreal.ca>, 1988.
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

declares = ['flat']

class Flat(recode.Step):
    internal_coding = recode.UNICODE_STRING
    external_coding = 'flat'
    composition_base = None

    def encode(self, input, errors='strict'):
        base = Flat.composition_base
        if base is None:
            import ucs
            base = Flat.composition_base = {}
            for character, composition in ucs.Combined.data:
                if isinstance(composition, tuple):
                    base[character] = composition[0][0]
                else:
                    base[character] = composition[0]
        output = []
        for character in input:
            if character < ' ' or character == unichr(127):
                if character in '\n\t':
                    output.append(character)
                else:
                    output.append('^' + chr(ord(character) ^ 1<<6))
            else:
                # FIXME: Recode's flat was also removing `_\b' and `\b_'.
                output.append(base.get(character, character))
        return ''.join(output), len(input)
