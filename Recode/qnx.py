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

declares = [('Icon-QNX', 'QNX')]

ESCAPE = chr(25)		# QNX escape for diacritics
ENDLINE = chr(30)		# end-line code for QNX

class IconQnx(recode.GenericStep):
    internal_coding = 'IBM-PC'
    external_coding = 'Icon-QNX'
    data = [
        ('\n', ENDLINE),
        (133, ESCAPE + 'Aa'),
        (138, ESCAPE + 'Ae'),
        (151, ESCAPE + 'Au'),
        (130, ESCAPE + 'Be'),
        (144, ESCAPE + 'BE'),
        (131, ESCAPE + 'Ca'),
        (136, ESCAPE + 'Ce'),
        (140, ESCAPE + 'Ci'),
        (147, ESCAPE + 'Co'),
        (150, ESCAPE + 'Cu'),
        (137, ESCAPE + 'He'),
        (139, ESCAPE + 'Hi'),
        (129, ESCAPE + 'Hu'),
        (135, ESCAPE + 'Kc'),
        (128, ESCAPE + 'KC'),
        ]
