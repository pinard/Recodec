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

declares = [('IBM437', 'IBM-PC', 'dos', 'MSDOS', 'pc', 'QNX-4', 'q4')]

implied_surfaces = [
    ('IBM-PC', 'CR-LF'),
    ('dos', 'CR-LF'),
    ('MSDOS', 'CR-LF'),
    ('pc', 'CR-LF')]

# FIXME: `-g' should either be re-implemented, or be replaced by a
# separate `ruler' encoding.

# FIXME: Allow ascii_graphics even with strict mapping.  Reported by
# David E. A. Wilson <david@osiris.cs.uow.edu.au>.

# Correspondance for IBM PC ruler graphics characters into ASCII graphics
# approximations.  The current principles are:
#
# - Single horizontal rulers are made up of dashes.
# - Double horizontal rulers are made up of equal signs.
# - Both single and double vertical are made up with `|'.
# - Both upper corners are rounded down with periods.
# - Lower corners are rounded up with grave/acute accent on left/right.
# - Other crossing rulers are approximated with plus signs, with exceptions
#   for double horizontal ruler crossings but not at corners: they are
#   equal signs inside a table, and `|' at left or right margin.

convert_rulers = [
    (176, '#'),
    (177, '#'),
    (178, '#'),
    (179, '|'),
    (180, '+'),
    (181, '|'),
    (182, '+'),
    (183, '.'),
    (184, '.'),
    (185, '|'),
    (186, '|'),
    (187, '.'),
    (188, '\''),
    (189, '\''),
    (190, '\''),
    (191, '.'),
    (192, '`'),
    (193, '+'),
    (194, '+'),
    (195, '+'),
    (196, '-'),
    (197, '+'),
    (198, '|'),
    (199, '+'),
    (200, '`'),
    (201, '.'),
    (202, '='),
    (203, '='),
    (204, '|'),
    (205, '='),
    (206, '='),
    (207, '='),
    (208, '+'),
    (209, '='),
    (210, '+'),
    (211, '`'),
    (212, '`'),
    (213, '.'),
    (214, '.'),
    (215, '+'),
    (216, '='),
    (217, '\''),
    (218, '.'),
    (219, '#'),
    (220, '#'),
    (221, '#'),
    (222, '#'),
    (223, '#'),
    ]

# Old data for `IBM-PC' to ISO `Latin-1' code conversions.
# FIXME: check incompatibilities with `IBM437', assumed for now.

known_pairs = [
    (20, 182),                          # pilcrow sign
    (21, 167),                          # section sign
    (128, 199),                         # capital letter C with cedilla
    (129, 252),                         # small letter u with diaeresis
    (130, 233),                         # small letter e with acute accent
    (131, 226),                       # small letter a with circumflex accent
    (132, 228),                         # small letter a with diaeresis
    (133, 224),                         # small letter a with grave accent
    (134, 229),                         # small letter a with ring above
    (135, 231),                         # small letter c with cedilla
    (136, 234),                       # small letter e with circumflex accent
    (137, 235),                         # small letter e with diaeresis
    (138, 232),                         # small letter e with grave accent
    (139, 239),                         # small letter i with diaeresis
    (140, 238),                       # small letter i with circumflex accent
    (141, 236),                         # small letter i with grave accent
    (142, 196),                         # capital letter A with diaeresis
    (143, 197),                         # capital letter A with ring above
    (144, 201),                         # capital letter E with acute accent
    (145, 230),                         # small ligature a with e
    (146, 198),                         # capital ligature A with E
    (147, 244),                       # small letter o with circumblex accent
    (148, 246),                         # small letter o with diaeresis
    (149, 242),                         # small letter o with grave accent
    (150, 251),                       # small letter u with circumflex accent
    (151, 249),                         # small letter u with grave accent
    (152, 255),                         # small letter y with diaeresis
    (153, 214),                         # capital letter O with diaeresis
    (154, 220),                         # capital letter U with diaeresis
    (155, 162),                         # cent sign
    (156, 163),                         # pound sign
    (157, 165),                         # yen sign
    (160, 225),                         # small letter a with acute accent
    (161, 237),                         # small letter i with acute accent
    (162, 243),                         # small letter o with acute accent
    (163, 250),                         # small letter u with acute accent
    (164, 241),                         # small letter n with tilde
    (165, 209),                         # capital letter N with tilde
    (166, 170),                         # feminine ordinal indicator
    (167, 186),                         # masculine ordinal indicator
    (168, 191),                         # inverted question mark
    (170, 172),                         # not sign
    (171, 189),                         # vulgar fraction one half
    (172, 188),                         # vulgar fraction one quarter
    (173, 161),                         # inverted exclamation mark
    (174, 171),                         # left angle quotation mark
    (175, 187),                         # right angle quotation mark
    (225, 223),                         # small german letter sharp s
    (230, 181),                         # small Greek letter mu micro sign
    (241, 177),                         # plus-minus sign
    (246, 247),                         # division sign
    (248, 176),                         # degree sign
    (250, 183),                         # middle dot
    (253, 178),                         # superscript two
    (255, 160),                         # no-break space
    ]
