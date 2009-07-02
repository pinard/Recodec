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

declares = ['Bang-Bang']

class Bangbang(recode.GenericStep):
    internal_coding = 'Latin-1'
    external_coding = 'Bang-Bang'
    data = [
        (0, '!!@'),
        (1, ('!!A', '!!a')),
        (2, ('!!B', '!!b')),
        (3, ('!!C', '!!c')),
        (4, ('!!D', '!!d')),
        (5, ('!!E', '!!e')),
        (6, ('!!F', '!!f')),
        (7, ('!!G', '!!g')),
        (8, ('!!H', '!!h')),
        (9, ('!!I', '!!i')),
        (10, ('\n', '!!J', '!!j')),
        (11, ('!!K', '!!k')),
        (12, ('!!L', '!!l')),
        (13, ('!!M', '!!m')),
        (14, ('!!N', '!!n')),
        (15, ('!!O', '!!o')),
        (16, ('!!P', '!!p')),
        (17, ('!!Q', '!!q')),
        (18, ('!!R', '!!r')),
        (19, ('!!S', '!!s')),
        (20, ('!!T', '!!t')),
        (21, ('!!U', '!!u')),
        (22, ('!!V', '!!v')),
        (23, ('!!W', '!!w')),
        (24, ('!!X', '!!x')),
        (25, ('!!Y', '!!y')),
        (26, ('!!Z', '!!z')),
        (27, '!!['),
        (28, '!!\\'),
        (29, '!!]'),
        (30, '!!^'),
        (31, '!!_'),
        ((' ', 160), ' '),               # 160 = no break space
        ('!', '!\''),
        ('A', ('!A', '!a')),
        ('B', ('!B', '!b')),
        ('C', ('!C', '!c')),
        ('D', ('!D', '!d')),
        ('E', ('!E', '!e')),
        ('F', ('!F', '!f')),
        ('G', ('!G', '!g')),
        ('H', ('!H', '!h')),
        ('I', ('!I', '!i')),
        ('J', ('!J', '!j')),
        ('K', ('!K', '!k')),
        ('L', ('!L', '!l')),
        ('M', ('!M', '!m')),
        ('N', ('!N', '!n')),
        ('O', ('!O', '!o')),
        ('P', ('!P', '!p')),
        ('Q', ('!Q', '!q')),
        ('R', ('!R', '!r')),
        ('S', ('!S', '!s')),
        ('T', ('!T', '!t')),
        ('U', ('!U', '!u')),
        ('V', ('!V', '!v')),
        ('W', ('!W', '!w')),
        ('X', ('!X', '!x')),
        ('Y', ('!Y', '!y')),
        ('Z', ('!Z', '!z')),
        ('`', '!@'),
        ('{', '!['),
        ('|', '!\\'),
        ('}', '!]'),
        ('~', '!^'),
        (127, '!_'),
        (171, '!>'),                    # left angle quotation mark
        (187, '!?'),                    # right angle quotation mark
        (224, '!0'),                    # small a with grave accent
        (226, '!1'),                    # small a with circumflex accent
        (230, '!;'),                    # small diphthong a with e
        (231, '!='),                    # small c with cedilla
        (232, '!3'),                    # small e with grave accent
        (233, '!2'),                    # small e with acute accent
        (234, '!5'),                    # small e with circumflex accent
        (235, '!4'),                    # small e with diaeresis
        (238, '!7'),                    # small i with circumflex accent
        (239, '!6'),                    # small i with diaeresis
        (244, '!8'),                    # small o with circumflex accent
        (247, '!<'),                    # division sign (or French oe?)
        (249, '!9'),                    # small u with grave accent
        (251, '!:'),                    # small u with circumflex accent
        ]
