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

declares = [
    ('XML-standalone', 'h0'),
    ('HTML_1.1', 'h1'),
    ('HTML_2.0', 'h2', 'RFC1866', '1866'),
    ('HTML-i18n', 'h3', 'RFC2070', '2070'),
    'HTML_3.2',
    # `HTML' defaults to the highest level available.
    ('HTML_4.0', 'h4', 'HTML', 'h'),
    ]

# FIXME: Option `-d' is not supported yet.  If `-d', do not recode
# ordinals lesser than 128.
# '&quot;' -> 34  '&amp;' -> 38  '&lt;' -> 60  '&gt;' -> 62

# FIXME: An @code{HTML} text which has spurious semi-colons to end entities
# (in strict mode) or does not always have them (in non-strict mode)
# is not canonical.  */

# The following entities, said to be from Emacs-w3, are ignored for the
# time being, as recode is not too fond on graphical approximations:
#
#      &ensp;          \
#      &emsp;          \ \
#      &ndash;         -
#      &mdash;         --
#      &lsquo;         `
#      &rsquo;         '
#      &ldquo;         ``
#      &rdquo;         ''
#      &frac18;        1/8
#      &frac38;        3/8
#      &frac58;        5/8
#      &frac78;        7/8
#      &hellip;        . . .
#      &larr;          <--
#      &rarr;          -->
#      &trade;         (TM)

V00 = 1 << 0                            # XML with stand-alone=yes
V11 = 1 << 1                            # Old Emacs-W3, HTML 1.1 ?
V20 = 1 << 2                            # RFC1866, HTML 2.0
V27 = 1 << 3                            # RFC2070, HTML-i18n
V32 = 1 << 4                            # HTML 3.2
V40 = 1 << 5                            # HTML 4.0

translations = [
    (33, 'excl',      0                                    ),
    (34, 'quot',      0 | V00       | V20 | V27 | V32 | V40),
    (35, 'num',       0                                    ),
    (36, 'dollar',    0                                    ),
    (37, 'percnt',    0                                    ),
    (38, 'amp',       0 | V00 | V11 | V20 | V27 | V32 | V40),
    (39, 'apos',      0 | V00                              ),
    (40, 'lpar',      0                                    ),
    (41, 'rpar',      0                                    ),
    (42, 'ast',       0                                    ),
    (43, 'plus',      0                                    ),
    (44, 'comma',     0                                    ),
    (45, 'horbar',    0                                    ),
    (46, 'period',    0                                    ),
    (58, 'colon',     0                                    ),
    (59, 'semi',      0                                    ),
    (60, 'lt',        0 | V00 | V11 | V20 | V27 | V32 | V40),
    (61, 'equals',    0                                    ),
    (62, 'gt',        0 | V00 | V11 | V20 | V27 | V32 | V40),
    (63, 'quest',     0                                    ),
    (64, 'commat',    0                                    ),
    (91, 'lsqb',      0                                    ),
    (93, 'rsqb',      0                                    ),
    (94, 'uarr',      0                                    ),
    (95, 'lowbar',    0                                    ),
    (96, 'grave',     0                                    ),
    (123, 'lcub',     0                                    ),
    (124, 'verbar',   0                                    ),
    (125, 'rcub',     0                                    ),
    (126, 'tilde',    0                                    ),
    (160, 'nbsp',     0                   | V27 | V32 | V40),
    (161, 'iexcl',    0                   | V27 | V32 | V40),
    (162, 'cent',     0                   | V27 | V32 | V40),
    (163, 'pound',    0                   | V27 | V32 | V40),
    (164, 'curren',   0                   | V27 | V32 | V40),
    (165, 'yen',      0                   | V27 | V32 | V40),
    (166, 'brkbar',   0       | V11                        ),
    (166, 'brvbar',   0                   | V27 | V32 | V40),
    (167, 'sect',     0                   | V27 | V32 | V40),
    (168, 'die',      0       | V11                        ),
    (168, 'uml',      0                   | V27 | V32 | V40),
    (169, 'copy',     0                   | V27 | V32 | V40),
    (170, 'ordf',     0                   | V27 | V32 | V40),
    (171, 'laquo',    0                   | V27 | V32 | V40),
    (172, 'not',      0                   | V27 | V32 | V40),
    (173, 'hyphen',   0       | V11                        ),
    (173, 'shy',      0                   | V27 | V32 | V40),
    (174, 'reg',      0                   | V27 | V32 | V40),
    (175, 'hibar',    0       | V11                        ),
    (175, 'macr',     0                   | V27 | V32 | V40),
    (176, 'deg',      0                   | V27 | V32 | V40),
    (177, 'plusmn',   0                   | V27 | V32 | V40),
    (178, 'sup2',     0                   | V27 | V32 | V40),
    (179, 'sup3',     0                   | V27 | V32 | V40),
    (180, 'acute',    0                   | V27 | V32 | V40),
    (181, 'micro',    0                   | V27 | V32 | V40),
    (182, 'para',     0                   | V27 | V32 | V40),
    (183, 'middot',   0                   | V27 | V32 | V40),
    (184, 'cedil',    0                   | V27 | V32 | V40),
    (185, 'sup1',     0                   | V27 | V32 | V40),
    (186, 'ordm',     0                   | V27 | V32 | V40),
    (187, 'raquo',    0                   | V27 | V32 | V40),
    (188, 'frac14',   0                   | V27 | V32 | V40),
    (189, 'half',     0       | V11                        ),
    (189, 'frac12',   0                   | V27 | V32 | V40),
    (190, 'frac34',   0                   | V27 | V32 | V40),
    (191, 'iquest',   0                   | V27 | V32 | V40),
    (192, 'Agrave',   0       | V11 | V20 | V27 | V32 | V40),
    (193, 'Aacute',   0       | V11 | V20 | V27 | V32 | V40),
    (194, 'Acircu',   0       | V11                        ),
    (194, 'Acirc',    0             | V20 | V27 | V32 | V40),
    (195, 'Atilde',   0       | V11 | V20 | V27 | V32 | V40),
    (196, 'Adiaer',   0       | V11                        ),
    (196, 'Auml',     0             | V20 | V27 | V32 | V40),
    (197, 'Aring',    0       | V11 | V20 | V27 | V32 | V40),
    (198, 'AE',       0       | V11                        ),
    (198, 'AElig',    0             | V20 | V27 | V32 | V40),
    (199, 'Ccedil',   0       | V11 | V20 | V27 | V32 | V40),
    (200, 'Egrave',   0       | V11 | V20 | V27 | V32 | V40),
    (201, 'Eacute',   0       | V11 | V20 | V27 | V32 | V40),
    (202, 'Ecircu',   0       | V11                        ),
    (202, 'Ecirc',    0             | V20 | V27 | V32 | V40),
    (203, 'Ediaer',   0       | V11                        ),
    (203, 'Euml',     0             | V20 | V27 | V32 | V40),
    (204, 'Igrave',   0       | V11 | V20 | V27 | V32 | V40),
    (205, 'Iacute',   0       | V11 | V20 | V27 | V32 | V40),
    (206, 'Icircu',   0       | V11                        ),
    (206, 'Icirc',    0             | V20 | V27 | V32 | V40),
    (207, 'Idiaer',   0       | V11                        ),
    (207, 'Iuml',     0             | V20 | V27 | V32 | V40),
    (208, 'ETH',      0       | V11 | V20 | V27 | V32 | V40),
    (209, 'Ntilde',   0       | V11 | V20 | V27 | V32 | V40),
    (210, 'Ograve',   0       | V11 | V20 | V27 | V32 | V40),
    (211, 'Oacute',   0       | V11 | V20 | V27 | V32 | V40),
    (212, 'Ocircu',   0       | V11                        ),
    (212, 'Ocirc',    0             | V20 | V27 | V32 | V40),
    (213, 'Otilde',   0       | V11 | V20 | V27 | V32 | V40),
    (214, 'Odiaer',   0       | V11                        ),
    (214, 'Ouml',     0             | V20 | V27 | V32 | V40),
    (215, 'MULT',     0       | V11                        ),
    (215, 'times',    0           | V27 | V32 | V40),
    (216, 'Ostroke',  0       | V11                        ),
    (216, 'Oslash',   0             | V20 | V27 | V32 | V40),
    (217, 'Ugrave',   0       | V11 | V20 | V27 | V32 | V40),
    (218, 'Uacute',   0       | V11 | V20 | V27 | V32 | V40),
    (219, 'Ucircu',   0       | V11                        ),
    (219, 'Ucirc',    0             | V20 | V27 | V32 | V40),
    (220, 'Udiaer',   0       | V11                        ),
    (220, 'Uuml',     0             | V20 | V27 | V32 | V40),
    (221, 'Yacute',   0       | V11 | V20 | V27 | V32 | V40),
    (222, 'THORN',    0       | V11 | V20 | V27 | V32 | V40),
    (223, 'ssharp',   0       | V11                        ),
    (223, 'szlig',    0             | V20 | V27 | V32 | V40),
    (224, 'agrave',   0       | V11 | V20 | V27 | V32 | V40),
    (225, 'aacute',   0       | V11 | V20 | V27 | V32 | V40),
    (226, 'acircu',   0       | V11                        ),
    (226, 'acirc',    0             | V20 | V27 | V32 | V40),
    (227, 'atilde',   0       | V11 | V20 | V27 | V32 | V40),
    (228, 'adiaer',   0       | V11                        ),
    (228, 'auml',     0             | V20 | V27 | V32 | V40),
    (229, 'aring',    0       | V11 | V20 | V27 | V32 | V40),
    (230, 'ae',       0       | V11                        ),
    (230, 'aelig',    0             | V20 | V27 | V32 | V40),
    (231, 'ccedil',   0       | V11 | V20 | V27 | V32 | V40),
    (232, 'egrave',   0       | V11 | V20 | V27 | V32 | V40),
    (233, 'eacute',   0       | V11 | V20 | V27 | V32 | V40),
    (234, 'ecircu',   0       | V11                        ),
    (234, 'ecirc',    0             | V20 | V27 | V32 | V40),
    (235, 'ediaer',   0       | V11                        ),
    (235, 'euml',     0             | V20 | V27 | V32 | V40),
    (236, 'igrave',   0       | V11 | V20 | V27 | V32 | V40),
    (237, 'iacute',   0       | V11 | V20 | V27 | V32 | V40),
    (238, 'icircu',   0       | V11                        ),
    (238, 'icirc',    0             | V20 | V27 | V32 | V40),
    (239, 'idiaer',   0       | V11                        ),
    (239, 'iuml',     0             | V20 | V27 | V32 | V40),
    (240, 'eth',      0       | V11 | V20 | V27 | V32 | V40),
    (241, 'ntilde',   0       | V11 | V20 | V27 | V32 | V40),
    (242, 'ograve',   0       | V11 | V20 | V27 | V32 | V40),
    (243, 'oacute',   0       | V11 | V20 | V27 | V32 | V40),
    (244, 'ocircu',   0       | V11                        ),
    (244, 'ocirc',    0             | V20 | V27 | V32 | V40),
    (245, 'otilde',   0       | V11 | V20 | V27 | V32 | V40),
    (246, 'odiaer',   0       | V11                        ),
    (246, 'ouml',     0             | V20 | V27 | V32 | V40),
    (247, 'DIVIS',    0       | V11                        ),
    (247, 'divide',   0                   | V27 | V32 | V40),
    (248, 'ostroke',  0       | V11                        ),
    (248, 'oslash',   0             | V20 | V27 | V32 | V40),
    (249, 'ugrave',   0       | V11 | V20 | V27 | V32 | V40),
    (250, 'uacute',   0       | V11 | V20 | V27 | V32 | V40),
    (251, 'ucircu',   0       | V11                        ),
    (251, 'ucirc',    0             | V20 | V27 | V32 | V40),
    (252, 'udiaer',   0       | V11                        ),
    (252, 'uuml',     0             | V20 | V27 | V32 | V40),
    (253, 'yacute',   0       | V11 | V20 | V27 | V32 | V40),
    (254, 'thorn',    0       | V11 | V20 | V27 | V32 | V40),
    (255, 'ydiaer',   0       | V11                        ),
    (255, 'yuml',     0             | V20 | V27 | V32 | V40),
    (338, 'OElig',    0                               | V40),
    (339, 'oelig',    0                               | V40),
    (352, 'Scaron',   0                               | V40),
    (353, 'scaron',   0                               | V40),
    (376, 'Yuml',     0                               | V40),
    (402, 'fnof',     0                               | V40),
    (710, 'circ',     0                               | V40),
    (732, 'tilde',    0                               | V40),
    (913, 'Alpha',    0                               | V40),
    (914, 'Beta',     0                               | V40),
    (915, 'Gamma',    0                               | V40),
    (916, 'Delta',    0                               | V40),
    (917, 'Epsilon',  0                               | V40),
    (918, 'Zeta',     0                               | V40),
    (919, 'Eta',      0                               | V40),
    (920, 'Theta',    0                               | V40),
    (921, 'Iota',     0                               | V40),
    (922, 'Kappa',    0                               | V40),
    (923, 'Lambda',   0                               | V40),
    (924, 'Mu',       0                               | V40),
    (925, 'Nu',       0                               | V40),
    (926, 'Xi',       0                               | V40),
    (927, 'Omicron',  0                               | V40),
    (928, 'Pi',       0                               | V40),
    (929, 'Rho',      0                               | V40),
    (931, 'Sigma',    0                               | V40),
    (932, 'Tau',      0                               | V40),
    (933, 'Upsilon',  0                               | V40),
    (934, 'Phi',      0                               | V40),
    (935, 'Chi',      0                               | V40),
    (936, 'Psi',      0                               | V40),
    (937, 'Omega',    0                               | V40),
    (945, 'alpha',    0                               | V40),
    (946, 'beta',     0                               | V40),
    (947, 'gamma',    0                               | V40),
    (948, 'delta',    0                               | V40),
    (949, 'epsilon',  0                               | V40),
    (950, 'zeta',     0                               | V40),
    (951, 'eta',      0                               | V40),
    (952, 'theta',    0                               | V40),
    (953, 'iota',     0                               | V40),
    (954, 'kappa',    0                               | V40),
    (955, 'lambda',   0                               | V40),
    (956, 'mu',       0                               | V40),
    (957, 'nu',       0                               | V40),
    (958, 'xi',       0                               | V40),
    (959, 'omicron',  0                               | V40),
    (960, 'pi',       0                               | V40),
    (961, 'rho',      0                               | V40),
    (962, 'sigmaf',   0                               | V40),
    (963, 'sigma',    0                               | V40),
    (964, 'tau',      0                               | V40),
    (965, 'upsilon',  0                               | V40),
    (966, 'phi',      0                               | V40),
    (967, 'chi',      0                               | V40),
    (968, 'psi',      0                               | V40),
    (969, 'omega',    0                               | V40),
    (977, 'thetasym', 0                               | V40),
    (978, 'upsih',    0                               | V40),
    (982, 'piv',      0                               | V40),
    (8194, 'ensp',    0                               | V40),
    (8195, 'emsp',    0                               | V40),
    (8201, 'thinsp',  0                               | V40),
    (8204, 'zwnj',    0                   | V27       | V40),
    (8205, 'zwj',     0                   | V27       | V40),
    (8206, 'lrm',     0                   | V27       | V40),
    (8207, 'rlm',     0                   | V27       | V40),
    (8211, 'ndash',   0                               | V40),
    (8212, 'mdash',   0                               | V40),
    (8216, 'lsquo',   0                               | V40),
    (8217, 'rsquo',   0                               | V40),
    (8218, 'sbquo',   0                               | V40),
    (8220, 'ldquo',   0                               | V40),
    (8221, 'rdquo',   0                               | V40),
    (8222, 'bdquo',   0                               | V40),
    (8224, 'dagger',  0                               | V40),
    (8225, 'Dagger',  0                               | V40),
    (8226, 'bull',    0                               | V40),
    (8230, 'hellip',  0                               | V40),
    (8240, 'permil',  0                               | V40),
    (8242, 'prime',   0                               | V40),
    (8243, 'Prime',   0                               | V40),
    (8249, 'lsaquo',  0                               | V40),
    (8250, 'rsaquo',  0                               | V40),
    (8254, 'oline',   0                               | V40),
    (8260, 'frasl',   0                               | V40),
    (8364, 'euro',    0                               | V40),
    (8465, 'image',   0                               | V40),
    (8472, 'weierp',  0                               | V40),
    (8476, 'real',    0                               | V40),
    (8482, 'trade',   0                               | V40),
    (8501, 'alefsym', 0                               | V40),
    (8592, 'larr',    0                               | V40),
    (8593, 'uarr',    0                               | V40),
    (8594, 'rarr',    0                               | V40),
    (8595, 'darr',    0                               | V40),
    (8596, 'harr',    0                               | V40),
    (8629, 'crarr',   0                               | V40),
    (8656, 'lArr',    0                               | V40),
    (8657, 'uArr',    0                               | V40),
    (8658, 'rArr',    0                               | V40),
    (8659, 'dArr',    0                               | V40),
    (8660, 'hArr',    0                               | V40),
    (8704, 'forall',  0                               | V40),
    (8706, 'part',    0                               | V40),
    (8707, 'exist',   0                               | V40),
    (8709, 'empty',   0                               | V40),
    (8711, 'nabla',   0                               | V40),
    (8712, 'isin',    0                               | V40),
    (8713, 'notin',   0                               | V40),
    (8715, 'ni',      0                               | V40),
    (8719, 'prod',    0                               | V40),
    (8721, 'sum',     0                               | V40),
    (8722, 'minus',   0                               | V40),
    (8727, 'lowast',  0                               | V40),
    (8730, 'radic',   0                               | V40),
    (8733, 'prop',    0                               | V40),
    (8734, 'infin',   0                               | V40),
    (8736, 'ang',     0                               | V40),
    (8743, 'and',     0                               | V40),
    (8744, 'or',      0                               | V40),
    (8745, 'cap',     0                               | V40),
    (8746, 'cup',     0                               | V40),
    (8747, 'int',     0                               | V40),
    (8756, 'there4',  0                               | V40),
    (8764, 'sim',     0                               | V40),
    (8773, 'cong',    0                               | V40),
    (8776, 'asymp',   0                               | V40),
    (8800, 'ne',      0                               | V40),
    (8801, 'equiv',   0                               | V40),
    (8804, 'le',      0                               | V40),
    (8805, 'ge',      0                               | V40),
    (8834, 'sub',     0                               | V40),
    (8835, 'sup',     0                               | V40),
    (8836, 'nsub',    0                               | V40),
    (8838, 'sube',    0                               | V40),
    (8839, 'supe',    0                               | V40),
    (8853, 'oplus',   0                               | V40),
    (8855, 'otimes',  0                               | V40),
    (8869, 'perp',    0                               | V40),
    (8901, 'sdot',    0                               | V40),
    (8968, 'lceil',   0                               | V40),
    (8969, 'rceil',   0                               | V40),
    (8970, 'lfloor',  0                               | V40),
    (8971, 'rfloor',  0                               | V40),
    (9001, 'lang',    0                               | V40),
    (9002, 'rang',    0                               | V40),
    (9674, 'loz',     0                               | V40),
    (9824, 'spades',  0                               | V40),
    (9827, 'clubs',   0                               | V40),
    (9829, 'hearts',  0                               | V40),
    (9830, 'diams',   0                               | V40),
    ]

class HtmlStep(recode.Step):
    internal_coding = recode.UNICODE_STRING

    # The following tables are defaulted as base class attributes, and are
    # later overridden, as needed, by derived class attributes instead of
    # instance attributes, so they get built at most once per derived class.
    encoding_table = None
    decoding_table = None

    def encode(self, input, errors='strict'):
        table = self.encoding_table
        if table is None:
            table = self.__class__.encoding_table = {}
            mask = self.selection_mask
            for code, entity, flags in translations:
                # if (cursor->flags & mask
                #     && (!request->diacritics_only || cursor->code > 128))
                if flags & mask:
                    table[unichr(code)] = entity
        output = []
        for character in input:
            try:
                value = table[character]
            except KeyError:
                if 32 <= ord(character) < 127 or character in '\n\t':
                    output.append(character)
                else:
                    output.append('&#%d;' % ord(character))
            else:
                output.append('&' + value + ';')
        return ''.join(output), len(input)

    def decode(self, input, errors='strict'):
        table = self.decoding_table
        if table is None:
            import re
            self.match_hex = re.compile('&#[xX]([0-9a-fA-F]+);?').match
            self.match_dec = re.compile('&#([0-9]+);?').match
            self.match_name = re.compile('&([A-Za-z][A-Za-z0-9]*);?').match
            table = self.__class__.decoding_table = {}
            mask = self.selection_mask
            for code, entity, flags in translations:
                # if (cursor->flags & mask
                #     && (!request->diacritics_only || cursor->code > 128))
                if flags & mask:
                    table[entity] = unichr(code)
        match_hex = self.match_hex
        match_dec = self.match_dec
        match_name = self.match_name
        output = []
        start = end = 0
        while start < len(input):
            end = input.find('&', start)
            if end < 0:
                output.append(input[start:])
                break
            if end > start:
                output.append(input[start:end])
            match = match_hex(input, end)
            if match:
                try:
                    value = unichr(int(match.group(1), 16))
                except ValueError:
                    pass
                else:
                    output.append(value)
                    start = match.end()
                    continue
            match = match_dec(input, end)
            if match:
                try:
                    value = unichr(int(match.group(1), 10))
                except ValueError:
                    pass
                else:
                    output.append(value)
                    start = match.end()
                    continue
            match = match_name(input, end)
            if match:
                try:
                    value = table[match.group(1)]
                except KeyError:
                    pass
                else:
                    output.append(value)
                    start = match.end()
                    continue
            output.append('&')
            start += 1
        return ''.join(output), len(input)

class Xmlstandalone(HtmlStep):
    external_coding = 'XML-standalone'
    selection_mask = V00

class Html11(HtmlStep):
    external_coding = 'HTML_1.1'
    selection_mask = V11

class Html20(HtmlStep):
    external_coding = 'HTML_2.0'
    selection_mask = V20

class Htmli18n(HtmlStep):
    external_coding = 'HTML-i18n'
    selection_mask = V27

class Html32(HtmlStep):
    external_coding = 'HTML_3.2'
    selection_mask = V32

class Html40(HtmlStep):
    external_coding = 'HTML_4.0'
    selection_mask = V40
