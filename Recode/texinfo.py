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
    internal_coding = 'ISO-8859-1'
    external_coding = 'Texinfo'
    data = [
        (160, '@ '),
        (161, '@exclamdown{}'),
        (171, '``'),
        (187, '\'\''),
        (191, '@questiondown{}'),
        (192, '@`A'),
        (194, '@^A'),
        (196, '@"A'),
        (197, '@AA{}'),
        (199, '@,{C}'),
        (200, '@`E'),
        (201, '@\'E'),
        (202, '@^E'),
        (203, '@"E'),
        (206, '@^I'),
        (207, '@"I'),
        (210, '@`O'),
        (212, '@^O'),
        (214, '@"O'),
        (216, '@O{}'),
        (217, '@`U'),
        (219, '@^U'),
        (220, '@"U'),
        (223, '@ss{}'),
        (224, '@`a'),
        (226, '@^a'),
        (228, '@"a'),
        (229, '@aa{}'),
        (231, '@,{c}'),
        (232, '@`e'),
        (233, '@\'e'),
        (234, '@^e'),
        (235, '@"e'),
        (236, '@`i'),
        (237, '@\'i'),
        (238, '@^{@dotless{i}}'),
        (239, '@"{@dotless{i}}'),
        (242, '@`o'),
        (244, '@^o'),
        (246, '@"o'),
        (249, '@`u'),
        (251, '@^u'),
        (252, '@"u'),
        ]
