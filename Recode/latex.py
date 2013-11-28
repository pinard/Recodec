# Conversion of files between different charsets and surfaces.
# -*- coding: utf-8 -*-
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
    data_knappens = [
        (u'\u0045\u0331', '\\b E'),
        (u'\u004F\u0331', '\\b O'),
        (u'\u0060', '\\`{}'),
        (u'\u0065\u0331', '\\b e'),
        (u'\u0066\u0069', 'fj'),
        (u'\u006F\u0331', '\\b o'),
        (u'\u00A1', '\\textexclamdown{}'),
        (u'\u00A8', '\\"{}'),
        (u'\u00AB', '\\guillemotleft{}'),
        (u'\u00AC', '$\\lnot$'),
        (u'\u00B1', '$\\pm$'),
        (u'\u00B4', '\\\'{}'),
        (u'\u00B7', '$\\cdot$'),
        (u'\u00B8', '\\c{}'),
        (u'\u00BB', '\\guillemotright{}'),
        (u'\u00BF', '\\textquestiondown{}'),
        (u'\u00C3', '\\~A'),
        (u'\u00C6', '\\AE{}'),
        (u'\u00C7', '\\c C'),
        (u'\u00C8', '\\`E'),
        #(u'\u00C8', '\\O{}'), REVOIR!
        (u'\u00C9', '\\\'E'),
        (u'\u00CA', '\\^E'),
        (u'\u00CB', '\\"E'),
        (u'\u00D1', '\\~N'),
        (u'\u00D2', '\\`O'),
        (u'\u00D3', '\\\'O'),
        (u'\u00D4', '\\^O'),
        (u'\u00D5', '\\~O'),
        (u'\u00D6', '\\"O'),
        (u'\u00D8', '\\O{}'),
        (u'\u00DF', '\\ss{}'),
        (u'\u00E3', '\\~a'),
        (u'\u00E6', '\\ae{}'),
        (u'\u00E7', '\\c c'),
        (u'\u00E8', '\\`e'),
        (u'\u00E9', '\\\'e'),
        (u'\u00EA', '\\^e'),
        (u'\u00EB', '\\"e'),
        (u'\u00F1', '\\~n'),
        (u'\u00F2', '\\`o'),
        (u'\u00F3', '\\\'o'),
        (u'\u00F4', '\\^o'),
        (u'\u00F5', '\\~o'),
        (u'\u00F6', '\\"o'),
        (u'\u00F8', '\\o{}'),
        (u'\u0104', '\\k{A}'),
        (u'\u0105', '\\k{a}'),
        (u'\u0106', '\\\'C'),
        (u'\u0107', '\\\'c'),
        (u'\u0111', '\\dj{}'),
        (u'\u0112', '\\=E'),
        (u'\u0113', '\\=e'),
        (u'\u0117', '\\.e'),
        (u'\u0118', '\\k{E}'),
        (u'\u0119', '\\k{e}'),
        (u'\u011A', '\\v E'),
        (u'\u011B', '\\v e'),
        (u'\u0126', '\\B H'),
        (u'\u0127', '\\B h'),
        (u'\u0128', '\\~I'),
        (u'\u0129', '\\~\\i'),
        (u'\u0131', '\\i{}'),
        (u'\u0134', '\\\'N'),
        #(u'\u0141', '\\L'), REVOIR!
        (u'\u0141', '\\L{}'),
        (u'\u0142', '\\l{}'),
        (u'\u0143', '\\\'N'),
        (u'\u0144', '\\\'n'),
        (u'\u014A', '\\NG{}'),
        (u'\u014B', '\\m u'),
        (u'\u014C', '\\=O'),
        (u'\u014D', '\\=o'),
        (u'\u0152', '\\OE{}'),
        (u'\u0153', '\\oe{}'),
        (u'\u015A', '\\\'S'),
        (u'\u015B', '\\\'s'),
        (u'\u0160', '\\v S'),
        (u'\u0161', '\\v s'),
        (u'\u0166', '\\.E'),
        #(u'\u0166', '\\B T'), REVOIR!
        #(u'\u0167', '\\B t'), REVOIR!
        (u'\u0167', '\\m Z'),
        (u'\u0168', '\\~U'),
        (u'\u0169', '\\~u'),
        (u'\u0179', '\\\'Z'),
        (u'\u017A', '\\\'z'),
        (u'\u017B', '\\.Z'),
        (u'\u017C', '\\.z'),
        (u'\u0181', '\\m B'),
        (u'\u0186', '\\m O'),
        (u'\u0186\u0303', '\\~{\\m O}'),
        (u'\u0187', '\\m C'),
        (u'\u0188', '\\m c'),
        (u'\u0189', '\\M D'),
        (u'\u018A', '\\m D'),
        (u'\u018E', '\\M E'),
        (u'\u0190', '\\m E'),
        (u'\u0190\u0303', '\\~{\\m E}'),
        (u'\u0191', '\\m F'),
        (u'\u0192', '\\m f'),
        (u'\u0194', '\\m G'),
        (u'\u0196', '\\m I'),
        (u'\u0198', '\\m K'),
        (u'\u0199', '\\m k'),
        (u'\u019D', '\\m J'),
        (u'\u01A4', '\\m P'),
        (u'\u01A5', '\\m p'),
        (u'\u01A9', '\\m S'),
        (u'\u01AC', '\\m T'),
        (u'\u01AD', '\\m t'),
        (u'\u01AE', '\\M T'),
        (u'\u01B2', '\\m U'),
        (u'\u01B3', '\\m Y'),
        (u'\u01B4', '\\m y'),
        (u'\u01D1', '\\v O'),
        (u'\u01D2', '\\v o'),
        (u'\u01DD', '\\M e'),
        (u'\u022E', '\\.O'),
        (u'\u022F', '\\.o'),
        (u'\u0237', '\\j{}'),
        (u'\u0253', '\\m b'),
        (u'\u0254', '\\m o'),
        (u'\u0254\u0303', '\\~{\\m o}'),
        (u'\u0256', '\\M d'),
        (u'\u0257', '\\m d'),
        (u'\u0258', '\\m e'),
        (u'\u0258\u0303', '\\~{\\m e}'),
        (u'\u0263', '\\m g'),
        (u'\u0269', '\\m i'),
        (u'\u0272', '\\m j'),
        (u'\u0288', '\\M t'),
        (u'\u028B', '\\ng{}'),
        (u'\u0292', '\\m z'),
        (u'\u02A7', '\\tsh{}'),
        (u'\u02C7', '\\v{}'),
        (u'\u02C9', '\\={}'),
        (u'\u02D8', '\\u{}'),
        (u'\u02DA', '\\r{}'),
        (u'\u030D', '\\textvbaraccent{}'),
        (u'\u030E', '\\U{}'),
        (u'\u030F', '\\G{}'),
        (u'\u0337', '{\\fontencoding[T4]\\selectfont \\char223}'),
        (u'\u0393', '\\ensuremath{\\Gamma}'),
        (u'\u0394', '\\ensuremath{\\Delta}'),
        (u'\u0398', '\\ensuremath{\\Theta}'),
        (u'\u039B', '\\ensuremath{\\Lambda}'),
        (u'\u039E', '\\ensuremath{\\Xi}'),
        (u'\u03A0', '\\ensuremath{\\Pi}'),
        (u'\u03A3', '\\m s'),
        #(u'\u03A3', '\\ensuremath{\\Sigma}'), REVOIR!
        (u'\u03A6', '\\ensuremath{\\Phi}'),
        (u'\u03A8', '\\ensuremath{\\Psi}'),
        (u'\u03A9', '\\ensuremath{\\Omega}'),
        (u'\u03B1', '$\\alpha$'),
        (u'\u03B2', '$\\beta$'),
        (u'\u03B3', '$\\gamma$'),
        (u'\u03B4', '$\\delta$'),
        (u'\u03BB', '$\\lambda$'),
        (u'\u03C0', '$\\pi$'),
        (u'\u03D2', '\\ensuremath{\\Upsilon}'),
        (u'\u1E3E', '\\\'M'),
        (u'\u1E3F', '\\\'m'),
        (u'\u1E44', '\\.N'),
        (u'\u1E45', '\\.n'),
        (u'\u1E48', '\\b N'),
        (u'\u1E49', '\\b n'),
        (u'\u1E62', '\\d S'),
        (u'\u1E63', '\\d s'),
        (u'\u1EB8', '\\d E'),
        (u'\u1EB9', '\\d e'),
        (u'\u1EBC', '\\~E'),
        (u'\u1EBD', '\\~e'),
        (u'\u1ECA', '\\d I'),
        (u'\u1ECB', '\\d i'),
        (u'\u1ECC', '\\d O'),
        (u'\u1ECD', '\\d o'),
        (u'\u1EE4', '\\d U'),
        (u'\u1EE5', '\\.u'),
        (u'\u200C', '\\textcompwordmark{}'),
        (u'\u201E', '\\textquotedblbase{}'),
        (u'\u2030', '\\textpermill'),
        (u'\u2031', '\\textpertenthousand'),
        (u'\u2190', '$\\leftarrow$'),
        (u'\u2191', '$\\uparrow$'),
        (u'\u2192', '$\\rightarrow$'),
        (u'\u2193', '$\\downarrow$'),
        (u'\u21C6', '$\\leftrightarrows$'),
        (u'\u2200', '$\\forall$'),
        (u'\u2202', '$\\partial$'),
        (u'\u2203', '$\\exists$'),
        (u'\u2208', '$\\in$'),
        (u'\u221E', '$\\infty$'),
        (u'\u2227', '$\\wedge$'),
        (u'\u2228', '$\\ve$'),
        (u'\u2229', '$\\cap$'),
        (u'\u222A', '$\\cup$'),
        (u'\u222B', '$\\int$'),
        (u'\u2260', '$\\neq$'),
        (u'\u2261', '$\\equiv$'),
        (u'\u2264', '$\\leq$'),
        (u'\u2265', '$\\geq$'),
        (u'\u2282', '$\\subset$'),
        (u'\u2283', '$\\supset$'),
        (u'\u2295', '$\\oplus$'),
        (u'\u2297', '$\\otimes$'),
        (u'\u22C4', '$\\diamond$'),
        (u'\uE026', '\\SS{}'),
        (u'\uE027', '{\\fontencoding{T1}\\selectfont \\char 24}'),
        (u'\uFB00', 'ff'),
        (u'\uFB01', 'fi'),
        (u'\uFB02', 'fl'),
        (u'\uFB03', 'ffi'),
        (u'\uFB04', 'ffl'),
    ]
    data = data_diacritics + data_others
    #data = data_knappens
