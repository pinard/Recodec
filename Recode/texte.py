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

declares = [('Texte', 'txte')]

# FIXME: `-c' processing not implemented yet.  The algorithm for proper
# processing of `-c' option depends on the fact that quotes to be changed
# in colons are exactly those which are in second position while the string
# is two characters in length.  This is sufficient for now.

# FIXME: Decoding is still quite rudimentary.  On this, `Free recode' is
# much more knowledgeable about French.

class Texte(recode.GenericStep):
    internal_coding = 'Latin-1'
    external_coding = 'Texte'
    data = [
        ((' ', 160), ' '),              # no-break space
        (171, '``'),                    # left angle quotation mark
        (187, '\'\''),                  # right angle quotation mark
        (192, 'A`'),                    # capital A with grave accent
        (194, 'A^'),                    # capital A with circumflex accent
        (196, 'A"'),                    # capital A diaeresis
        (199, 'C,'),                    # capital C with cedilla
        (200, 'E`'),                    # capital E with grave accent
        (201, 'E\''),                   # capital E with acute accent
        (202, 'E^'),                    # capital E with circumflex accent
        (203, 'E"'),                    # capital E with diaeresis
        (206, 'I^'),                    # capital I with circumflex accent
        (207, 'I"'),                    # capital I with diaeresis
        (210, 'O`'),                    # capital O with grave accent
        (212, 'O^'),                    # capital O with circumflex accent
        (214, 'O"'),                    # capital O with diaeresis
        (217, 'U`'),                    # capital U with grave accent
        (219, 'U^'),                    # capital U with circumflex accent
        (220, 'U"'),                    # capital U with diaeresis
        (224, 'a`'),                    # small a with grave accent
        (226, 'a^'),                    # small a with circumflex accent
        (228, 'a"'),                    # small a with diaeresis
        (231, 'c,'),                    # small c with cedilla
        (232, 'e`'),                    # small e with grave accent
        (233, 'e\''),                   # small e with acute accent
        (234, 'e^'),                    # small e with circumflex accent
        (235, 'e"'),                    # small e with diaeresis
        (238, 'i^'),                    # small i with circumflex accent
        (239, 'i"'),                    # small i with diaeresis
        (242, 'o`'),                    # small o with grave accent
        (244, 'o^'),                    # small o with circumflex accent
        (246, 'o"'),                    # small o with diaeresis
        (249, 'u`'),                    # small u with grave accent
        (251, 'u^'),                    # small u with circumflex accent
        (252, 'u"'),                    # small u with diaeresis
        ]
