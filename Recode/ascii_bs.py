# Conversion of files between different charsets and surfaces.
# Copyright © 1990, 93, 94, 97, 98, 99, 00, 02 Free Software Foundation, Inc.
# This file is part of the GNU C Library.
# Contributed by François Pinard <pinard@iro.umontreal.ca>, 1988.
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Library General Public License
# as published by the Free Software Foundation; either version 2 of the
# License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be
# useful, but WITHOUT ANY WARRANTY; without even the implied warranty
# of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Library General Public License for more details.
#
# You should have received a copy of the GNU Library General Public
# License along with the `recode' Library; see the file `COPYING.LIB'.
# If not, write to the Free Software Foundation, Inc., 59 Temple Place -
# Suite 330, Boston, MA 02111-1307, USA.

import recode

declares = [('ASCII-BS', 'bs')]

class Ascii_Bs(recode.GenericStep):
    internal_coding = 'Latin-1'
    external_coding = 'ASCII-BS'
    data = [
        (171, ('<\b\"', '\"\b<')),
        (187, ('>\b"', '"\b>')),
        (192, ('A\b`', '`\bA')),
        (193, ('A\b\'', '\'\bA')),
        (194, ('A\b^', '^\bA')),
        (195, ('A\b~', '~\bA')),
        (196, ('A\b"', '"\bA')),
        (199, ('C\b,', ',\bC')),
        (200, ('E\b`', '`\bE')),
        (201, ('E\b\'', '\'\bE')),
        (202, ('E\b^', '^\bE')),
        (203, ('E\b"', '"\bE')),
        (204, ('I\b`', '`\bI')),
        (205, ('I\b\'', '\'\bI')),
        (206, ('I\b^', '^\bI')),
        (207, ('I\b"', '"\bI')),
        (209, ('N\b~', '~\bN')),
        (210, ('O\b`', '`\bO')),
        (211, ('O\b\'', '\'\bO')),
        (212, ('O\b^', '^\bO')),
        (213, ('O\b~', '~\bO')),
        (214, ('O\b"', '"\bO')),
        (216, ('O\b\/', '\/\bO')),
        (217, ('U\b`', '`\bU')),
        (218, ('U\b\'', '\'\bU')),
        (219, ('U\b^', '^\bU')),
        (220, ('U\b"', '"\bU')),
        (221, ('Y\b\'', '\'\bY')),
        (223, ('s\b"', '"\bs')),
        (224, ('a\b`', '`\ba')),
        (225, ('a\b\'', '\'\ba')),
        (226, ('a\b^', '^\ba')),
        (227, ('a\b~', '~\ba')),
        (228, ('a\b"', '"\ba')),
        (231, ('c\b,', ',\bc')),
        (232, ('e\b`', '`\be')),
        (233, ('e\b\'', '\'\be')),
        (234, ('e\b^', '^\be')),
        (235, ('e\b"', '"\be')),
        (236, ('i\b`', '`\bi')),
        (237, ('i\b\'', '\'\bi')),
        (238, ('i\b^', '^\bi')),
        (239, ('i\b"', '"\bi')),
        (241, ('n\b~', '~\bn')),
        (242, ('o\b`', '`\bo')),
        (243, ('o\b\'', '\'\bo')),
        (244, ('o\b^', '^\bo')),
        (245, ('o\b~', '~\bo')),
        (246, ('o\b"', '"\bo')),
        (248, ('o\b\/', '\/\bo')),
        (249, ('u\b`', '`\bu')),
        (250, ('u\b\'', '\'\bu')),
        (251, ('u\b^', '^\bu')),
        (252, ('u\b"', '"\bu')),
        (253, ('y\b\'', '\'\by')),
        (255, ('y\b"', '"\by')),
    ]
