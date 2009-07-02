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
        (':', ('@D', '@d')),
        ('@', ('@A', '@a')),
        ('^', ('@B', '@b')),
        ('`', ('@G', '@g')),
        ('a', ('^A', '^a')),
        ('b', ('^B', '^b')),
        ('c', ('^C', '^c')),
        ('d', ('^D', '^d')),
        ('e', ('^E', '^e')),
        ('f', ('^F', '^f')),
        ('g', ('^G', '^g')),
        ('h', ('^H', '^h')),
        ('i', ('^I', '^i')),
        ('j', ('^J', '^j')),
        ('k', ('^K', '^k')),
        ('l', ('^L', '^l')),
        ('m', ('^M', '^m')),
        ('n', ('^N', '^n')),
        ('o', ('^O', '^o')),
        ('p', ('^P', '^p')),
        ('q', ('^Q', '^q')),
        ('r', ('^R', '^r')),
        ('s', ('^S', '^s')),
        ('t', ('^T', '^t')),
        ('u', ('^U', '^u')),
        ('v', ('^V', '^v')),
        ('w', ('^W', '^w')),
        ('x', ('^X', '^x')),
        ('y', ('^Y', '^y')),
        ('z', ('^Z', '^z')),
        ('{', '^0'),
        ('|', '^1'),
        ('}', '^2'),
        ('~', '^3'),
        (127, '^4'),
        ]
