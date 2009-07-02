# Conversion of files between different charsets and surfaces.
# Copyright © 1997, 98, 99, 00, 02 Free Software Foundation, Inc.
# This file is part of the GNU C Library.
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
    ('21-Permutation', 'swabytes'),
    '4321-Permutation',
    ]

class PermuteStep(recode.Step):
    internal_coding = recode.TRIVIAL_SURFACE

class Permute21(PermuteStep):
    external_coding = '21-Permutation'

    def encode(self, input, errors='strict'):
        output = []
        index = 0
        while index+2 <= len(input):
            output.append(input[index+1] + input[index])
            index += 2
        if index+1 == len(input):
            output.append(input[index])
        return ''.join(output), len(input)

    decode = encode

class Permute4321(PermuteStep):
    external_coding = '4321-Permutation'

    def encode(self, input, errors='strict'):
        output = []
        index = 0
        while index+4 <= len(input):
            output.append(input[index+3] + input[index+2]
                          + input[index+1] + input[index])
            index += 4
        if index+3 == len(input):
            output.append(input[index+2] + input[index+1] + input[index])
        elif index+2 == len(input):
            output.append(input[index+1] + input[index])
        elif index+1 == len(input):
            output.append(input[index])
        return ''.join(output), len(input)

    decode = encode
