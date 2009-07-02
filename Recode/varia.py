# Conversion of files between different charsets and surfaces.
# Copyright © 1999, 2000, 2002 Free Software Foundation, Inc.
# Contributed by François Pinard <pinard@iro.umontreal.ca>, 1993.
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

# This file contains various temporary tables.  These would ideally all go
# away once Keld will be given references, solid enough, to really integrate
# these tables in RFC1345 (.bis, .ter :-).

declares = [
    # Czesch tables.
    ('KEYBCS2', 'Kamenicky'),
    ('CORK', 'T1'),
    'KOI-8_CS2',
    # Suggested by Alexander L. Belikoff.  FIXME: `KOI8-R' twice.
    #('IBM866', '866', 'CP866', 'alt'),
    #('KOI8-R', '1489', 'RFC1489'),
    #('KOI8-R', '878', 'CP878', 'IBM878'),
    ]

# Czesch tables.

class Czesch(recode.GenericStep):
    external_coding = recode.UNICODE_STRING

# Lukas Petrlik <luki@pafos.zcu.cz>, 1996-04-02, and Martin Mares
# <mj@ucw.cz>, 1999-01-05, both sent Kamenicky and Cork tables.  The
# following two variables are used to document the contradicting spots.

LUKAS = True                            # for Lukas definitions
MARTIN = False                          # for Martin definitions

# These tables use standard latin alphabet with Czech accented letters.
# They use a subset of ISO-8859-2, plus a few strange characters.

# KEYBCS2, Kamenicky.  "Source: the Reality :-)", as says Lukas.  According
# to Martin, several sources list CP859 as being equivalent to the Kamenicky
# Brothers code, but neither of them seems to be authoritative enough.

class Kamenicky(Czesch):
    internal_coding = 'KEYBCS2'
    data = []
    if MARTIN:
        data += [
            # Non-Czech characters copied from IBM charset.
            (1, u'\u263A'),             # white smiling face
            (2, u'\u263B'),             # black smiling face
            (3, u'\u2665'),             # black heart suit
            (4, u'\u2666'),             # black diamond suit
            (5, u'\u2663'),             # black club suit
            (6, u'\u2660'),             # black spade suit
            (7, u'\u2022'),             # bullet
            (8, u'\u25D8'),             # inverse bullet
            (9, u'\u25CB'),             # white circle
            (10, u'\u25D9'),            # inverse white circle
            (11, u'\u2642'),            # male sign
            (12, u'\u2640'),            # female sign
            (13, u'\u266A'),            # eighth note
            (14, u'\u266B'),            # beamed eighth notes
            (15, u'\u263C'),            # white sun with rays
            (16, u'\u25B6'),            # black right-pointing triangle
            (17, u'\u25C0'),            # black left-pointing triangle
            (18, u'\u2195'),            # up down arrow
            (19, u'\u203C'),            # double exclamation mark
            (20, u'\u00B6'),            # pilcrow sign
            (21, u'\u00A7'),            # section sign
            (22, u'\u25AC'),            # black rectangle
            (23, u'\u21A8'),            # up down arrow with base
            (24, u'\u2191'),            # upwards arrow
            (25, u'\u2193'),            # downwards arrow
            (26, u'\u2192'),            # rightwards arrow
            (27, u'\u2190'),            # leftwards arrow
            (28, u'\u221F'),            # right angle
            (29, u'\u2194'),            # left right arrow
            (30, u'\u25B2'),            # black up-pointing triangle
            (31, u'\u25BC'),            # black down-pointing triangle
            (127, u'\u2302'),           # house
            ]
    if True:
        data += [
            (128, u'\u010C'),
            (129, u'\u00FC'),
            (130, u'\u00E9'),
            (131, u'\u010F'),
            (132, u'\u00E4'),
            (133, u'\u010E'),
            (134, u'\u0164'),
            (135, u'\u010D'),
            (136, u'\u011B'),
            (137, u'\u011A'),
            (138, u'\u0139'),
            (139, u'\u00CD'),
            (140, u'\u013E'),
            (141, u'\u013A'),
            (142, u'\u00C4'),
            (143, u'\u00C1'),
            (144, u'\u00C9'),
            (145, u'\u017E'),
            (146, u'\u017D'),
            (147, u'\u00F4'),
            (148, u'\u00F6'),
            (149, u'\u00D3'),
            (150, u'\u016F'),
            (151, u'\u00DA'),
            (152, u'\u00FD'),
            (153, u'\u00D6'),
            (154, u'\u00DC'),
            (155, u'\u0160'),
            (156, u'\u013D'),
            (157, u'\u00DD'),
            (158, u'\u0158'),
            (159, u'\u0165'),           # latin small letter t with caron
            (160, u'\u00E1'),
            (161, u'\u00ED'),
            (162, u'\u00F3'),
            (163, u'\u00FA'),
            (164, u'\u0148'),
            (165, u'\u0147'),
            (166, u'\u016E'),
            (167, u'\u00D4'),
            (168, u'\u0161'),
            (169, u'\u0159'),
            (170, u'\u0155'),
            (171, u'\u0154'),
            (172, u'\u00BC'),
            (173, u'\u00A7'),
            ]
    if LUKAS:
        data += [
            (174, u'\u00AB'),
            (175, u'\u00BB'),
            ]
    if MARTIN:
        data += [
            (174, u'\u00BB'),     # right-pointing double angle quotation mark
            (175, u'\u00AB'),      # left-pointing double angle quotation mark
            ]
    if True:
        data += [
            (176, u'\u2591'),
            (177, u'\u2592'),
            (178, u'\u2593'),
            (179, u'\u2502'),
            (180, u'\u2524'),
            (181, u'\u2561'),
            (182, u'\u2562'),
            (183, u'\u2556'),
            (184, u'\u2555'),
            (185, u'\u2563'),
            (186, u'\u2551'),
            (187, u'\u2557'),
            (188, u'\u255D'),
            (189, u'\u255C'),
            (190, u'\u255B'),
            (191, u'\u2510'),
            (192, u'\u2514'),
            (193, u'\u2534'),
            (194, u'\u252C'),
            (195, u'\u251C'),
            (196, u'\u2500'),
            (197, u'\u253C'),
            (198, u'\u255E'),
            (199, u'\u255F'),
            (200, u'\u255A'),
            (201, u'\u2554'),
            (202, u'\u2569'),
            (203, u'\u2566'),
            (204, u'\u2560'),
            (205, u'\u2550'),
            (206, u'\u256C'),
            (207, u'\u2567'),
            (208, u'\u2568'),
            (209, u'\u2564'),
            (210, u'\u2565'),
            (211, u'\u2559'),
            (212, u'\u2558'),
            (213, u'\u2552'),
            (214, u'\u2553'),
            (215, u'\u256B'),
            (216, u'\u256A'),
            (217, u'\u2518'),
            (218, u'\u250C'),
            (219, u'\u2588'),
            (220, u'\u2584'),
            (221, u'\u258C'),
            (222, u'\u2590'),
            (223, u'\u2580'),
            (224, u'\u03B1'),
            (225, u'\u03B2'),
            ]
    if LUKAS:
        data += [
            (226, u'\u0393'),
            ]
    if MARTIN:
        data += [
            (226, u'\u0194'),           # latin capital letter gamma
            ]
    if True:
        data += [
            (227, u'\u03C0'),
            (228, u'\u03A3'),
            (229, u'\u03C3'),
            (230, u'\u03BC'),
            (231, u'\u03C4'),
            (232, u'\u03A6'),
            (233, u'\u0398'),
            (234, u'\u03A9'),
            (235, u'\u03B4'),
            (236, u'\u221E'),
            ]
    if LUKAS:
        data += [
            (237, u'\u2205'),
            (238, u'\u03B5'),
            (239, u'\u2229'),
            (240, u'\u2261'),
            ]
    if MARTIN:
        data += [
            (237, u'\u03C6'),           # greek small letter phi
            (238, u'\u2208'),           # element of
            (239, u'\u2229'),           # intersection
            (240, u'\u224D'),           # equivalent to
            ]
    if True:
        data += [
            (241, u'\u00B1'),
            (242, u'\u2265'),
            (243, u'\u2264'),
            (244, u'\u2320'),
            (245, u'\u2321'),
            (246, u'\u00F7'),
            (247, u'\u2248'),
            ]
    if LUKAS:
        data += [
            (248, u'\u2218'),
            (249, u'\u00B7'),
            (250, u'\u2219'),
            ]
    if MARTIN:
        data += [
            (248, u'\u00B0'),           # degree sign
            (249, u'\u2219'),           # bullet operator
            (250, u'\u00B7'),           # middle dot
            ]
    if True:
        data += [
            (251, u'\u221A'),
            (252, u'\u207F'),
            (253, u'\u00B2'),
            (254, u'\u25A0'),
            (255, u'\u00A0'),
            ]

class Cork(Czesch):
    internal_coding = 'CORK'
    data = []
    if LUKAS:
        data += [
            # I suspect, not sure, that Lukas used this mapping to convey T1
            # and CORK in a single table, which may not be such a good thing.
            (0, u'\u0060'),
            (1, u'\u00B4'),
            (2, u'\u005E'),
            (3, u'\u007E'),
            (4, u'\u00A8'),
            (5, u'\u02DD'),
            (6, u'\u02DA'),
            (7, u'\u02C7'),
            (8, u'\u02D8'),
            (9, u'\u00AF'),
            (10, u'\u02D9'),
            (11, u'\u00B8'),
            (12, u'\u02DB'),
            (13, u'\u201A'),
            (14, u'\u2039'),
            (15, u'\u203A'),
            (16, u'\u201C'),
            (17, u'\u201D'),
            (18, u'\u201E'),
            (19, u'\u00AB'),
            (20, u'\u00BB'),
            (21, u'\u2013'),
            (22, u'\u2014'),
            (23, ''),                   # FIXME: Should I use None for error?
            (24, u'\u2080'),
            (25, u'\u0131'),
            (26, ''),                   # latin small letter j dotless, FIXME!
            (27, u'\uFB00'),
            (28, u'\uFB01'),
            (29, u'\uFB02'),
            (30, u'\uFB03'),
            (31, u'\uFB04'),
            ]
    if True:
        data += [
            (127, u'\u2010'),
            (128, u'\u0102'),
            (129, u'\u0104'),
            (130, u'\u0106'),
            (131, u'\u010C'),
            (132, u'\u010E'),
            (133, u'\u011A'),
            (134, u'\u0118'),
            (135, u'\u011E'),
            (136, u'\u0139'),
            (137, u'\u013D'),
            (138, u'\u0141'),
            (139, u'\u0143'),
            (140, u'\u0147'),
            (141, u'\u014A'),
            (142, u'\u0150'),
            (143, u'\u0154'),
            (144, u'\u0158'),
            (145, u'\u015A'),
            (146, u'\u0160'),
            (147, u'\u015E'),
            (148, u'\u0164'),
            (149, u'\u0162'),
            (150, u'\u0170'),
            (151, u'\u016E'),
            (152, u'\u0178'),
            (153, u'\u0179'),
            (154, u'\u017D'),
            (155, u'\u017B'),
            (156, u'\u0132'),
            (157, u'\u0130'),
            (158, u'\u00F0'),
            (159, u'\u00A7'),
            (160, u'\u0103'),
            (161, u'\u0105'),
            (162, u'\u0107'),
            (163, u'\u010D'),
            (164, u'\u010F'),
            (165, u'\u011B'),
            (166, u'\u0119'),
            (167, u'\u011F'),
            (168, u'\u013A'),
            (169, u'\u013E'),
            (170, u'\u0142'),
            (171, u'\u0144'),
            (172, u'\u0148'),
            (173, u'\u014B'),
            (174, u'\u0151'),
            (175, u'\u0155'),
            (176, u'\u0159'),
            (177, u'\u015B'),
            (178, u'\u0161'),
            (179, u'\u015F'),
            (180, u'\u0165'),
            (181, u'\u0163'),
            (182, u'\u0171'),
            (183, u'\u016F'),
            (184, u'\u00FF'),
            (185, u'\u017A'),
            (186, u'\u017E'),
            (187, u'\u017C'),
            (188, u'\u0133'),
            (189, u'\u00A1'),
            (190, u'\u00BF'),
            (191, u'\u00A3'),
            (215, u'\u0152'),
            (223, ''),                  # latin capital letter sharp s (german)
                                        # (it is the SS ligature), FIXME! */
            (247, u'\u0153'),
            (255, u'\u00DF'),
            ]

# KOI-8_CS2.  Source: CSN 36 9103.
# From Lukas Petrlik <luki@pafos.zcu.cz>, 1996-04-02.
# &g1esc x2d49 &g2esc x2e49 &g3esc x2f49

class Koi8cs2(Czesch):
    internal_coding = 'KOI-8_CS2'
    data = [
        (36, u'\u00A4'),
        (161, ''),
        (162, u'\u00B4'),
        (163, ''),
        (164, u'\u007E'),
        (165, ''),
        (166, u'\u02D8'),
        (167, u'\u02D9'),
        (169, ''),
        (170, u'\u02DA'),
        (171, u'\u00B8'),
        (172, ''),
        (173, u'\u02DD'),
        (174, u'\u02DB'),
        (175, u'\u02C7'),
        (176, u'\u00A9'),
        (177, u'\u2122'),
        (178, u'\u250C'),
        (179, u'\u2510'),
        (180, u'\u2514'),
        (181, u'\u2518'),
        (182, u'\u2500'),
        (183, u'\u2193'),
        (184, u'\u03A9'),
        (185, u'\u00A7'),
        (186, u'\u03B1'),
        (187, u'\u03B3'),
        (188, u'\u03B5'),
        (189, u'\u03BC'),
        (190, u'\u03C0'),
        (191, u'\u03C9'),
        (192, u'\u00E0'),
        (193, u'\u00E1'),
        (194, u'\u01CE'),
        (195, u'\u010D'),
        (196, u'\u010F'),
        (197, u'\u011B'),
        (198, u'\u0155'),
        (199, ''),                      # ch digraph as a single character,
                                        # as used in the Czech alphabet, FIXME!
        (200, u'\u00FC'),
        (201, u'\u00ED'),
        (202, u'\u016F'),
        (203, u'\u013A'),
        (204, u'\u013E'),
        (205, u'\u00F6'),
        (206, u'\u0148'),
        (207, u'\u00F3'),
        (208, u'\u00F4'),
        (209, u'\u00E4'),
        (210, u'\u0159'),
        (211, u'\u0161'),
        (212, u'\u0165'),
        (213, u'\u00FA'),
        (214, u'\u00EB'),
        (215, u'\u00E9'),
        (216, u'\u0171'),
        (217, u'\u00FD'),
        (218, u'\u017E'),
        (219, ''),
        (220, ''),
        (221, u'\u0151'),
        (222, u'\u0117'),
        (224, u'\u00C0'),
        (225, u'\u00C1'),
        (226, u'\u01CD'),
        (227, u'\u010C'),
        (228, u'\u010E'),
        (229, u'\u011A'),
        (230, u'\u0154'),
        (231, ''),                      # CH digraph as a single character,
                                        # as used in the Czech alphabet, FIXME!
        (232, u'\u00DC'),
        (233, u'\u00CD'),
        (234, u'\u016E'),
        (235, u'\u0139'),
        (236, u'\u013D'),
        (237, u'\u00D6'),
        (238, u'\u0147'),
        (239, u'\u00D3'),
        (240, u'\u00D4'),
        (241, u'\u00C4'),
        (242, u'\u0158'),
        (243, u'\u0160'),
        (244, u'\u0164'),
        (245, u'\u00DA'),
        (246, u'\u00CB'),
        (247, u'\u00C9'),
        (248, u'\u0170'),
        (249, u'\u00DD'),
        (250, u'\u017D'),
        (251, ''),
        (252, ''),
        (253, u'\u0150'),
        (254, u'\u0116'),
        (255, ''),
        ]

# Cyrillic tables?

# Helping people.
#
# "Alexander L. Belikoff" <abel@bfr.co.il>
# Andrey A. Chernov <ache@null.net>
# Andries Brouwer <Andries.Brouwer@cwi.nl>
# Roman Czyborra <czyborra@cs.tu-berlin.de>

# What is apparently still missing, from various mail I got, is:
#
# IBM866               CP866, alt
# KOI8-Unified
#
# Here are various sources of information.
#
# Andrey A. Chernov <ache@null.net>
# http://www.nagual.pp.ru/~ache/
#
# &charset KOI8-Unified
# &rem source: http://www.cyrillic.com/ref/cyrillic/koi8-uni.html

# @item IBM866
# @code{866}, @code{cp866}, and @code{alt} are aliases for this charset.
# source: unknown
#
# @item KOI8-R
# @code{878}, @code{cp878}, @code{ibm878}, @code{koi8r}, and
# @code{rfc1489} are aliases for this charset.
# source: RFC1489

# 'KOI8-R', 'IBM866',

koi8r_to_ibm866 = [
    196, 179, 218, 191, 192, 217, 195, 180, # 128 - 135
    194, 193, 197, 223, 220, 219, 221, 222, # 136 - 143
    176, 177, 178, 244, 254, 249, 251, 247, # 144 - 151
    243, 242, 255, 245, 248, 253, 250, 246, # 152 - 159
    205, 186, 213, 241, 214, 201, 184, 183, # 160 - 167
    187, 212, 211, 200, 190, 189, 188, 198, # 168 - 175
    199, 204, 181, 240, 182, 185, 209, 210, # 176 - 183
    203, 207, 208, 202, 216, 215, 206, 252, # 184 - 191
    238, 160, 161, 230, 164, 165, 228, 163, # 192 - 199
    229, 168, 169, 170, 171, 172, 173, 174, # 200 - 207
    175, 239, 224, 225, 226, 227, 166, 162, # 208 - 215
    236, 235, 167, 232, 237, 233, 231, 234, # 216 - 223
    158, 128, 129, 150, 132, 133, 148, 131, # 224 - 231
    149, 136, 137, 138, 139, 140, 141, 142, # 232 - 239
    143, 159, 144, 145, 146, 147, 134, 130, # 240 - 247
    156, 155, 135, 152, 157, 153, 151, 154  # 248 - 255
    ]

koi8r_to_cp1251 = [
    128, 129, 130, 131, 132, 133, 134, 135, # 128 - 135
    136, 137, 138, 139, 140, 141, 142, 143, # 136 - 143
    144, 145, 146, 147, 148, 149, 150, 151, # 144 - 151
    152, 153, 154, 155, 156, 157, 158, 159, # 152 - 159
    160, 161, 162, 163, 164, 165, 166, 167, # 160 - 167
    168, 169, 170, 171, 172, 173, 174, 175, # 168 - 175
    176, 177, 178, 179, 180, 181, 182, 183, # 176 - 183
    184, 185, 186, 187, 188, 189, 190, 191, # 184 - 191
    254, 224, 225, 246, 228, 229, 244, 227, # 192 - 199
    245, 232, 233, 234, 235, 236, 237, 238, # 200 - 207
    239, 255, 240, 241, 242, 243, 230, 226, # 208 - 215
    252, 251, 231, 248, 253, 249, 247, 250, # 216 - 223
    222, 192, 193, 214, 196, 197, 212, 195, # 224 - 231
    213, 200, 201, 202, 203, 204, 205, 206, # 232 - 239
    207, 223, 208, 209, 210, 211, 198, 194, # 240 - 247
    220, 219, 199, 216, 221, 217, 215, 218  # 248 - 255
]

koi8r_to_iso8859_5 = [
    128, 129, 130, 131, 132, 133, 134, 135, # 128 - 135
    136, 137, 138, 139, 140, 141, 142, 143, # 136 - 143
    144, 145, 146, 147, 148, 149, 150, 151, # 144 - 151
    152, 153, 154, 155, 156, 157, 158, 159, # 152 - 159
    160, 161, 162, 163, 164, 165, 166, 167, # 160 - 167
    168, 169, 170, 171, 172, 173, 174, 175, # 168 - 175
    240, 241, 242, 243, 244, 245, 246, 247, # 176 - 183
    248, 249, 250, 251, 252, 253, 254, 255, # 184 - 191
    238, 208, 209, 230, 212, 213, 228, 211, # 192 - 199
    229, 216, 217, 218, 219, 220, 221, 222, # 200 - 207
    223, 239, 224, 225, 226, 227, 214, 210, # 208 - 215
    236, 235, 215, 232, 237, 233, 231, 234, # 216 - 223
    206, 176, 177, 198, 180, 181, 196, 179, # 224 - 231
    197, 184, 185, 186, 187, 188, 189, 190, # 232 - 239
    191, 207, 192, 193, 194, 195, 182, 178, # 240 - 247
    204, 203, 183, 200, 205, 201, 199, 202  # 248 - 255
]
