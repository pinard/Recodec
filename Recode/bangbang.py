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
        (1, '!!a'),
        (2, '!!b'),
        (3, '!!c'),
        (4, '!!d'),
        (5, '!!e'),
        (6, '!!f'),
        (7, '!!g'),
        (8, '!!h'),
        (9, '!!i'),
        (10, ('\n', '!!j')),
        (11, '!!k'),
        (12, '!!l'),
        (13, '!!m'),
        (14, '!!n'),
        (15, '!!o'),
        (16, '!!p'),
        (17, '!!q'),
        (18, '!!r'),
        (19, '!!s'),
        (20, '!!t'),
        (21, '!!u'),
        (22, '!!v'),
        (23, '!!w'),
        (24, '!!x'),
        (25, '!!y'),
        (26, '!!z'),
        (27, '!!['),
        (28, '!!\\'),
        (29, '!!]'),
        (30, '!!^'),
        (31, '!!_'),
        ((' ', 160), ' '),               # 160 = no break space
        ('!', '!\''),
        ('A', '!a'),
        ('B', '!b'),
        ('C', '!c'),
        ('D', '!d'),
        ('E', '!e'),
        ('F', '!f'),
        ('G', '!g'),
        ('H', '!h'),
        ('I', '!i'),
        ('J', '!j'),
        ('K', '!k'),
        ('L', '!l'),
        ('M', '!m'),
        ('N', '!n'),
        ('O', '!o'),
        ('P', '!p'),
        ('Q', '!q'),
        ('R', '!r'),
        ('S', '!s'),
        ('T', '!t'),
        ('U', '!u'),
        ('V', '!v'),
        ('W', '!w'),
        ('X', '!x'),
        ('Y', '!y'),
        ('Z', '!z'),
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
