# Conversion of files between different charsets and surfaces.
# -*- coding: UTF-8 -*-
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

declares = [('LaTeX', 'TeX', 'ltex')]

# FIXME: Option `-d' is not supported yet.

class Latex(recode.GenericStep):
    internal_coding = recode.UNICODE_STRING
    external_coding = 'LaTeX'
    data_diacritics = [
        (u'\u00C0', '\\`A'),           # capital A with grave accent
        (u'\u00C1', '\\\'A'),          # capital A with acute accent
        (u'\u00C2', '\\^A'),           # capital A with circumflex accent
        (u'\u00C3', '\\~A'),           # capital A with tilde
        (u'\u00C4', '\\"A'),           # capital A diaeresis
        (u'\u00C5', '\\AA{}'),         # capital A with ring above
        (u'\u00C6', '\\AE{}'),         # capital diphthong A with E
        (u'\u00C7', '\\c{C}'),         # capital C with cedilla
        (u'\u00C8', '\\`E'),           # capital E with grave accent
        (u'\u00C9', '\\\'E'),          # capital E with acute accent
        (u'\u00CA', '\\^E'),           # capital E with circumflex accent
        (u'\u00CB', '\\"E'),           # capital E with diaeresis
        (u'\u00CC', '\\`I'),           # capital I with grave accent
        (u'\u00CD', '\\\'I'),          # capital I with acute accent
        (u'\u00CE', '\\^I'),           # capital I with circumflex accent
        (u'\u00CF', '\\"I'),           # capital I with diaeresis
        (u'\u00D1', '\\~N'),           # capital N with tilde
        (u'\u00D2', '\\`O'),           # capital O with grave accent
        (u'\u00D3', '\\\'O'),          # capital O with acute accent
        (u'\u00D4', '\\^O'),           # capital O with circumflex accent
        (u'\u00D5', '\\~O'),           # capital O with tilde
        (u'\u00D6', '\\"O'),           # capital O with diaeresis
        (u'\u00D8', '\\O{}'),          # capital O with oblique stroke
        (u'\u00D9', '\\`U'),           # capital U with grave accent
        (u'\u00DA', '\\\'U'),          # capital U with acute accent
        (u'\u00DB', '\\^U'),           # capital U with circumflex accent
        (u'\u00DC', '\\"U'),           # capital U with diaeresis
        (u'\u00DD', '\\\'Y'),          # capital Y with acute accent
        (u'\u00DF', '\\ss{}'),         # small german sharp s
        (u'\u00E0', '\\`a'),           # small a with grave accent
        (u'\u00E1', '\\\'a'),          # small a with acute accent
        (u'\u00E2', '\\^a'),           # small a with circumflex accent
        (u'\u00E3', '\\~a'),           # small a with tilde
        (u'\u00E4', '\\"a'),           # small a with diaeresis
        (u'\u00E5', '\\aa{}'),         # small a with ring above
        (u'\u00E6', '\\ae{}'),         # small diphthong a with e
        (u'\u00E7', '\\c{c}'),         # small c with cedilla
        (u'\u00E8', '\\`e'),           # small e with grave accent
        (u'\u00E9', '\\\'e'),          # small e with acute accent
        (u'\u00EA', '\\^e'),           # small e with circumflex accent
        (u'\u00EB', '\\"e'),           # small e with diaeresis
        (u'\u00EC', '\\`{\\i}'),       # small i with grave accent
        (u'\u00ED', '\\\'{\\i}'),      # small i with acute accent
        (u'\u00EE', '\\^{\\i}'),       # small i with circumflex accent
        (u'\u00EF', '\\"{\\i}'),       # small i with diaeresis
        (u'\u00F1', '\\~n'),           # small n with tilde
        (u'\u00F2', '\\`o'),           # small o with grave accent
        (u'\u00F3', '\\\'o'),          # small o with acute accent
        (u'\u00F4', '\\^o'),           # small o with circumflex accent
        (u'\u00F5', '\\~o'),           # small o with tilde
        (u'\u00F6', '\\"o'),           # small o with diaeresis
        (u'\u00F8', '\\o{}'),          # small o with oblique stroke
        (u'\u00F9', '\\`u'),           # small u with grave accent
        (u'\u00FA', '\\\'u'),          # small u with acute accent
        (u'\u00FB', '\\^u'),           # small u with circumflex accent
        (u'\u00FC', '\\"u'),           # small u with diaeresis
        (u'\u00FD', '\\\'y'),          # small y with acute accent
        (u'\u00FF', '\\"y'),           # small y with diaeresis
        ]
    data_others = [
        (u'#', '\\\#'),
        (u'$', '\\$'),
        (u'%', '\\%'),
        (u'&', '\\&'),
        (u'\\', '\\backslash{}'),
        (u'_', '\\_'),
        (u'{', '\\{'),
        (u'}', '\\}'),
        (u'\u00A0', '~'),                  # no-break space
        (u'\u00A1', '!`'),                 # inverted exclamation mark
        (u'\u00A3', '\\pound{}'),          # pound sign
        (u'\u00A7', '\\S{}'),              # paragraph sign, section sign
        (u'\u00A8', '\\"{}'),              # diaeresis
        (u'\u00A9', '\\copyright{}'),      # copyright sign
        (u'\u00AB', '``'),                 # left angle quotation mark
        (u'\u00AC', '\\neg{}'),            # not sign
        (u'\u00AD', '\\-'),                # soft hyphen
        (u'\u00B0', '\\mbox{$^\\circ$}'),  # degree sign
        (u'\u00B1', '\\mbox{$\\pm$}'),     # plus-minus sign
        (u'\u00B2', '\\mbox{$^2$}'),       # superscript two
        (u'\u00B3', '\\mbox{$^3$}'),       # superscript three
        (u'\u00B4', '\\\'{}'),             # acute accent
        (u'\u00B5', '\\mbox{$\\mu$}'),     # small greek mu, micro sign
        (u'\u00B7', '\\cdotp'),            # middle dot
        (u'\u00B8', '\\,{}'),              # cedilla
        (u'\u00B9', '\\mbox{$^1$}'),       # superscript one
        (u'\u00BB', '\'\''),               # right angle quotation mark
        (u'\u00BC', '\\frac1/4{}'),        # vulgar fraction one quarter
        (u'\u00BD', '\\frac1/2{}'),        # vulgar fraction one half
        (u'\u00BE', '\\frac3/4{}'),        # vulgar fraction three quarters
        (u'\u00BF', '?`'),                 # inverted question mark
        ]
    data = data_diacritics + data_others
