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

declares = [('CDC-NOS', 'NOS')]

class Cdcnos(recode.GenericStep):
    internal_coding = 'ASCII-BS'
    external_coding = 'CDC-NOS'
    data = [
        (0, '^5'),
        (1, '^6'),
        (2, '^7'),
        (3, '^8'),
        (4, '^9'),
        (5, '^+'),
        (6, '^-'),
        (7, '^*'),
        (8, '^/'),
        (9, '^('),
        (10, ('\n', '^)')),
        (11, '^$'),
        (12, '^='),
        (13, '^ '),
        (14, '^,'),
        (15, '^.'),
        (16, '^#'),
        (17, '^['),
        (18, '^]'),
        (19, '^%'),
        (20, '^\"'),
        (21, '^_'),
        (22, '^!'),
        (23, '^&'),
        (24, '^\''),
        (25, '^?'),
        (26, '^<'),
        (27, '^>'),
        (28, '^@'),
        (29, '^\\'),
        (30, '^^'),
        (31, '^;'),
        (':', '@D'),
        ('@', '@A'),
        ('^', '@B'),
        ('`', '@G'),
        ('a', '^A'),
        ('b', '^B'),
        ('c', '^C'),
        ('d', '^D'),
        ('e', '^E'),
        ('f', '^F'),
        ('g', '^G'),
        ('h', '^H'),
        ('i', '^I'),
        ('j' '^J'),
        ('k', '^K'),
        ('l', '^L'),
        ('m', '^M'),
        ('n', '^N'),
        ('o', '^O'),
        ('p', '^P'),
        ('q', '^Q'),
        ('r', '^R'),
        ('s', '^S'),
        ('t', '^T'),
        ('u', '^U'),
        ('v', '^V'),
        ('w', '^W'),
        ('x', '^X'),
        ('y', '^Y'),
        ('z', '^Z'),
        ('{', '^0'),
        ('|', '^1'),
        ('}', '^2'),
        ('~', '^3'),
        (127, '^4'),
        ]
