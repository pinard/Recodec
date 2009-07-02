# Conversion of files between different charsets and surfaces.
# Copyright © 1990, 93, 97, 98, 99, 00, 02 Free Software Foundation, Inc.
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

declares = [('Texinfo', 'texi', 'ti')]

class Texinfo(recode.GenericStep):
    internal_coding = recode.UNICODE_STRING
    external_coding = 'Texinfo'
    data = [
        (u'\xa0', '@ '),
        (u'\xa1', '@exclamdown{}'),
        (u'\xab', '``'),
        (u'\xbb', "''"),
        (u'\xbf', '@questiondown{}'),
        (u'\xc0', '@`A'),
        (u'\xc2', '@^A'),
        (u'\xc4', '@"A'),
        (u'\xc5', '@AA{}'),
        (u'\xc7', '@,{C}'),
        (u'\xc8', '@`E'),
        (u'\xc9', "@'E"),
        (u'\xca', '@^E'),
        (u'\xcb', '@"E'),
        (u'\xce', '@^I'),
        (u'\xcf', '@"I'),
        (u'\xd2', '@`O'),
        (u'\xd4', '@^O'),
        (u'\xd6', '@"O'),
        (u'\xd8', '@O{}'),
        (u'\xd9', '@`U'),
        (u'\xdb', '@^U'),
        (u'\xdc', '@"U'),
        (u'\xdf', '@ss{}'),
        (u'\xe0', '@`a'),
        (u'\xe2', '@^a'),
        (u'\xe4', '@"a'),
        (u'\xe5', '@aa{}'),
        (u'\xe7', '@,{c}'),
        (u'\xe8', '@`e'),
        (u'\xe9', "@'e"),
        (u'\xea', '@^e'),
        (u'\xeb', '@"e'),
        (u'\xec', '@`i'),
        (u'\xed', "@'i"),
        (u'\xee', '@^{@dotless{i}}'),
        (u'\xef', '@"{@dotless{i}}'),
        (u'\xf2', '@`o'),
        (u'\xf4', '@^o'),
        (u'\xf6', '@"o'),
        (u'\xf9', '@`u'),
        (u'\xfb', '@^u'),
        (u'\xfc', '@"u'),
        ]
