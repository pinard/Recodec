# -*- coding: latin1 -*-
# Vietnamese charset processing.
# Copyright © 1999, 2000, 2002 Progiciels Bourbeau-Pinard inc.
# Contributed by François Pinard <pinard@iro.umontreal.ca>, 1999.
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

declares = ['TCVN', 'VIQR', 'VISCII', 'VNI', 'VPS']

class Tcvn(recode.StripStep):
    external_coding = 'TCVN'
    data = (
        u'\u0000\u00DA\u1EE4\u0003\u1EEA\u1EEC\u1EEE\u0007'  # 0
        u'\u0008\u0009\u000A\u000B\u000C\u000D\u000E\u000F'  # 8
        u'\u0010\u1EE8\u1EF0\u1EF2\u1EF6\u1EF8\u00DD\u1EF4'  # 16
        u'\u0018\u0019\u001A\u001B\u001C\u001D\u001E\u001F'  # 24
        u'\u0020\u0021\u0022\u0023\u0024\u0025\u0026\u0027'  # 32
        u'\u0028\u0029\u002A\u002B\u002C\u002D\u002E\u002F'  # 40
        u'\u0030\u0031\u0032\u0033\u0034\u0035\u0036\u0037'  # 48
        u'\u0038\u0039\u003A\u003B\u003C\u003D\u003E\u003F'  # 56
        u'\u0040\u0041\u0042\u0043\u0044\u0045\u0046\u0047'  # 64
        u'\u0048\u0049\u004A\u004B\u004C\u004D\u004E\u004F'  # 72
        u'\u0050\u0051\u0052\u0053\u0054\u0055\u0056\u0057'  # 80
        u'\u0058\u0059\u005A\u005B\u005C\u005D\u005E\u005F'  # 88
        u'\u0060\u0061\u0062\u0063\u0064\u0065\u0066\u0067'  # 96
        u'\u0068\u0069\u006A\u006B\u006C\u006D\u006E\u006F'  # 104
        u'\u0070\u0071\u0072\u0073\u0074\u0075\u0076\u0077'  # 112
        u'\u0078\u0079\u007A\u007B\u007C\u007D\u007E\u007F'  # 120
        u'\u00C0\u1EA2\u00C3\u00C1\u1EA0\u1EB6\u1EAC\u00C8'  # 128
        u'\u1EBA\u1EBC\u00C9\u1EB8\u1EC6\u00CC\u1EC8\u0128'  # 136
        u'\u00CD\u1ECA\u00D2\u1ECE\u00D5\u00D3\u1ECC\u1ED8'  # 144
        u'\u1EDC\u1EDE\u1EE0\u1EDA\u1EE2\u00D9\u1EE6\u0168'  # 152
        u'\uFFFF\u0102\u00C2\u00CA\u00D4\u01A0\u01AF\u0110'  # 160
        u'\u0103\u00E2\u00EA\u00F4\u01A1\u01B0\u0111\u1EB0'  # 168
        u'\uFFFF\uFFFF\uFFFF\uFFFF\uFFFF\u00E0\u1EA3\u00E3'  # 176
        u'\u00E1\u1EA1\u1EB2\u1EB1\u1EB3\u1EB5\u1EAF\u1EB4'  # 184
        u'\u1EAE\u1EA6\u1EA8\u1EAA\u1EA4\u1EC0\u1EB7\u1EA7'  # 192
        u'\u1EA9\u1EAB\u1EA5\u1EAD\u00E8\u1EC2\u1EBB\u1EBD'  # 200
        u'\u00E9\u1EB9\u1EC1\u1EC3\u1EC5\u1EBF\u1EC7\u00EC'  # 208
        u'\u1EC9\u1EC4\u1EBE\u1ED2\u0129\u00ED\u1ECB\u00F2'  # 216
        u'\u1ED4\u1ECF\u00F5\u00F3\u1ECD\u1ED3\u1ED5\u1ED7'  # 224
        u'\u1ED1\u1ED9\u1EDD\u1EDF\u1EE1\u1EDB\u1EE3\u00F9'  # 232
        u'\u1ED6\u1EE7\u0169\u00FA\u1EE5\u1EEB\u1EED\u1EEF'  # 240
        u'\u1EE9\u1EF1\u1EF3\u1EF7\u1EF9\u00FD\u1EF5\u1ED0'  # 248
        )

class Viscii(recode.StripStep):
    external_coding = 'VISCII'
    data = (
        u'\u0000\u0001\u1EB2\u0003\u0004\u1EB4\u1EAA\u0007'  # 0
        u'\u0008\u0009\u000A\u000B\u000C\u000D\u000E\u000F'  # 8
        u'\u0010\u0011\u0012\u0013\u1EF6\u0015\u0016\u0017'  # 16
        u'\u0018\u1EF8\u001A\u001B\u001C\u001D\u1EF4\u001F'  # 24
        u'\u0020\u0021\u0022\u0023\u0024\u0025\u0026\u0027'  # 32
        u'\u0028\u0029\u002A\u002B\u002C\u002D\u002E\u002F'  # 40
        u'\u0030\u0031\u0032\u0033\u0034\u0035\u0036\u0037'  # 48
        u'\u0038\u0039\u003A\u003B\u003C\u003D\u003E\u003F'  # 56
        u'\u0040\u0041\u0042\u0043\u0044\u0045\u0046\u0047'  # 64
        u'\u0048\u0049\u004A\u004B\u004C\u004D\u004E\u004F'  # 72
        u'\u0050\u0051\u0052\u0053\u0054\u0055\u0056\u0057'  # 80
        u'\u0058\u0059\u005A\u005B\u005C\u005D\u005E\u005F'  # 88
        u'\u0060\u0061\u0062\u0063\u0064\u0065\u0066\u0067'  # 96
        u'\u0068\u0069\u006A\u006B\u006C\u006D\u006E\u006F'  # 104
        u'\u0070\u0071\u0072\u0073\u0074\u0075\u0076\u0077'  # 112
        u'\u0078\u0079\u007A\u007B\u007C\u007D\u007E\u007F'  # 120
        u'\u1EA0\u1EAE\u1EB0\u1EB6\u1EA4\u1EA6\u1EA8\u1EAC'  # 128
        u'\u1EBC\u1EB8\u1EBE\u1EC0\u1EC2\u1EC4\u1EC6\u1ED0'  # 136
        u'\u1ED2\u1ED4\u1ED6\u1ED8\u1EE2\u1EDA\u1EDC\u1EDE'  # 144
        u'\u1ECA\u1ECE\u1ECC\u1EC8\u1EE6\u0168\u1EE4\u1EF2'  # 152
        u'\u00D5\u1EAF\u1EB1\u1EB7\u1EA5\u1EA7\u1EA9\u1EAD'  # 160
        u'\u1EBD\u1EB9\u1EBF\u1EC1\u1EC3\u1EC5\u1EC7\u1ED1'  # 168
        u'\u1ED3\u1ED5\u1ED7\u1EE0\u01A0\u1ED9\u1EDD\u1EDF'  # 176
        u'\u1ECB\u1EF0\u1EE8\u1EEA\u1EEC\u01A1\u1EDB\u01AF'  # 184
        u'\u00C0\u00C1\u00C2\u00C3\u1EA2\u0102\u1EB3\u1EB5'  # 192
        u'\u00C8\u00C9\u00CA\u1EBA\u00CC\u00CD\u0128\u1EF3'  # 200
        u'\u0110\u1EE9\u00D2\u00D3\u00D4\u1EA1\u1EF7\u1EEB'  # 208
        u'\u1EED\u00D9\u00DA\u1EF9\u1EF5\u00DD\u1EE1\u01B0'  # 216
        u'\u00E0\u00E1\u00E2\u00E3\u1EA3\u0103\u1EEF\u1EAB'  # 224
        u'\u00E8\u00E9\u00EA\u1EBB\u00EC\u00ED\u0129\u1EC9'  # 232
        u'\u0111\u1EF1\u00F2\u00F3\u00F4\u00F5\u1ECF\u1ECD'  # 240
        u'\u1EE5\u00F9\u00FA\u0169\u1EE7\u00FD\u1EE3\u1EEE'  # 248
        )

class Vps(recode.StripStep):
    external_coding = 'VPS'
    data = (
        u'\u0000\u0001\u1EA0\u1EAC\u1EB6\u1EB8\u1EC6\u0007'  # 0
        u'\u0008\u0009\u000A\u000B\u000C\u000D\u000E\u000F'  # 8
        u'\u1ECA\u1ECC\u1ED8\u1EE2\u1EE4\u1EF0\u0016\u0017'  # 16
        u'\u0018\u1EF4\u001A\u001B\u1EAA\u1EEE\u001E\u001F'  # 24
        u'\u0020\u0021\u0022\u0023\u0024\u0025\u0026\u0027'  # 32
        u'\u0028\u0029\u002A\u002B\u002C\u002D\u002E\u002F'  # 40
        u'\u0030\u0031\u0032\u0033\u0034\u0035\u0036\u0037'  # 48
        u'\u0038\u0039\u003A\u003B\u003C\u003D\u003E\u003F'  # 56
        u'\u0040\u0041\u0042\u0043\u0044\u0045\u0046\u0047'  # 64
        u'\u0048\u0049\u004A\u004B\u004C\u004D\u004E\u004F'  # 72
        u'\u0050\u0051\u0052\u0053\u0054\u0055\u0056\u0057'  # 80
        u'\u0058\u0059\u005A\u005B\u005C\u005D\u005E\u005F'  # 88
        u'\u0060\u0061\u0062\u0063\u0064\u0065\u0066\u0067'  # 96
        u'\u0068\u0069\u006A\u006B\u006C\u006D\u006E\u006F'  # 104
        u'\u0070\u0071\u0072\u0073\u0074\u0075\u0076\u0077'  # 112
        u'\u0078\u0079\u007A\u007B\u007C\u007D\u007E\u007F'  # 120
        u'\u00C0\u1EA2\u00C3\u1EA4\u1EA6\u1EA8\u1ECD\u1ED7'  # 128
        u'\u0102\u1EBF\u1EC1\u1EC3\u1EC7\u1EAE\u1EB0\u1EB2'  # 136
        u'\u1EBE\uFFFF\uFFFF\u1EC0\u1EC2\u1EC4\u1ED0\u1ED2'  # 144
        u'\u1ED4\uFFFF\u00FD\u1EF7\u1EF5\u1EDA\u1EDC\u1EDE'  # 152
        u'\uFFFF\u1EAF\u1EB1\u1EB3\u1EB5\u1EB7\u1EE0\u1EDB'  # 160
        u'\u00D9\u1EDD\u1EDF\u1EE1\u0168\u1EE8\u1EE3\u1EEA'  # 168
        u'\u1ED5\u1EEC\u1EF2\u1EF8\u00CD\u00CC\u1ED9\u1EC8'  # 176
        u'\u0128\u00D3\u1EED\u1EEF\u00D2\u1ECE\u00D5\u1EF1'  # 184
        u'\u1EA7\u00C1\u00C2\u1EA5\u1EA9\u1EAB\u1EAD\u0111'  # 192
        u'\u1EBB\u00C9\u00CA\u1EB9\u1EC9\u1EC5\u1ECB\u1EF9'  # 200
        u'\u01AF\u1EE6\u1ED3\u1ED1\u00D4\u1ECF\u01A1\u00C8'  # 208
        u'\u1EEB\u1EE9\u00DA\u0169\u01B0\u00DD\u1EBA\uFFFF'  # 216
        u'\u00E0\u00E1\u00E2\u00E3\u1EA3\u1EA1\u0103\uFFFF'  # 224
        u'\u00E8\u00E9\u00EA\u1EBD\u00EC\u00ED\uFFFF\u0129'  # 232
        u'\u1EB4\u0110\u00F2\u00F3\u00F4\u00F5\uFFFF\u01A0'  # 240
        u'\u1EE5\u00F9\u00FA\u1EE7\uFFFF\u1EF6\u1EBC\u1EF3'  # 248
        )

class Viqr(recode.GenericStep):
    internal_coding = 'VISCII'
    external_coding = 'VIQR'
    data = [
        (2, 'A(?'),
        (5, 'A(~'),
        (6, 'A^~'),
        (20, 'Y?'),
        (25, 'Y~'),
        (30, 'Y.'),
        (128, 'A.'),
        (129, 'A(\''),
        (130, 'A(`'),
        (131, 'A(.'),
        (132, 'A^\''),
        (133, 'A^`'),
        (134, 'A^?'),
        (135, 'A^.'),
        (136, 'E~'),
        (137, 'E.'),
        (138, 'E^\''),
        (139, 'E^`'),
        (140, 'E^?'),
        (141, 'E^~'),
        (142, 'E^.'),
        (143, 'O^\''),
        (144, 'O^`'),
        (145, 'O^?'),
        (146, 'O^~'),
        (147, 'O^.'),
        (148, 'O+.'),
        (149, 'O+\''),
        (150, 'O+`'),
        (151, 'O+?'),
        (152, 'I.'),
        (153, 'O?'),
        (154, 'O.'),
        (155, 'I?'),
        (156, 'U?'),
        (157, 'U~'),
        (158, 'U.'),
        (159, 'Y`'),
        (160, 'O~'),
        (161, 'a(\''),
        (162, 'a(`'),
        (163, 'a(.'),
        (164, 'a^\''),
        (165, 'a^`'),
        (166, 'a^?'),
        (167, 'a^.'),
        (168, 'e~'),
        (169, 'e.'),
        (170, 'e^\''),
        (171, 'e^`'),
        (172, 'e^?'),
        (173, 'e^~'),
        (174, 'e^.'),
        (175, 'o^\''),
        (176, 'o^`'),
        (177, 'o^?'),
        (178, 'o^~'),
        (179, 'O+~'),
        (180, 'O+'),
        (181, 'o^.'),
        (182, 'o+`'),
        (183, 'o+?'),
        (184, 'i.'),
        (185, 'U+.'),
        (186, 'U+\''),
        (187, 'U+`'),
        (188, 'U+?'),
        (189, 'o+'),
        (190, 'o+\''),
        (191, 'U+'),
        (192, 'A`'),
        (193, 'A\''),
        (194, 'A^'),
        (195, 'A~'),
        (196, 'A?'),
        (197, 'A('),
        (198, 'a(?'),
        (199, 'a(~'),
        (200, 'E`'),
        (201, 'E\''),
        (202, 'E^'),
        (203, 'E?'),
        (204, 'I`'),
        (205, 'I\''),
        (206, 'I~'),
        (207, 'y`'),
        (208, ('DD', 'Dd', 'dD')),
        (209, 'u+\''),
        (210, 'O`'),
        (211, 'O\''),
        (212, 'O^'),
        (213, 'a.'),
        (214, 'y?'),
        (215, 'u+`'),
        (216, 'u+?'),
        (217, 'U`'),
        (218, 'U\''),
        (219, 'y~'),
        (220, 'y.'),
        (221, 'Y\''),
        (222, 'o+~'),
        (223, 'u+'),
        (224, 'a`'),
        (225, 'a\''),
        (226, 'a^'),
        (227, 'a~'),
        (228, 'a?'),
        (229, 'a('),
        (230, 'u+~'),
        (231, 'a^~'),
        (232, 'e`'),
        (233, 'e\''),
        (234, 'e^'),
        (235, 'e?'),
        (236, 'i`'),
        (237, 'i\''),
        (238, 'i~'),
        (239, 'i?'),
        (240, 'dd'),
        (241, 'u+.'),
        (242, 'o`'),
        (243, 'o\''),
        (244, 'o^'),
        (245, 'o~'),
        (246, 'o?'),
        (247, 'o.'),
        (248, 'u.'),
        (249, 'u`'),
        (250, 'u\''),
        (251, 'u~'),
        (252, 'u?'),
        (253, 'y\''),
        (254, 'o+.'),
        (255, 'U+~'),
        ]

class Vni(recode.GenericStep):
    internal_coding = 'VISCII'
    external_coding = 'VNI'
    data = [
        (2, 'AÚ'),
        (5, 'AÜ'),
        (6, 'AÃ'),
        (20, 'YÛ'),
        (25, 'YÕ'),
        (30, 'Î'),
        (128, 'AÏ'),
        (129, 'AÈ'),
        (130, 'AÉ'),
        (131, 'AË'),
        (132, 'AÁ'),
        (133, 'AÀ'),
        (134, 'AÅ'),
        (135, 'AÄ'),
        (136, 'EÕ'),
        (137, 'EÏ'),
        (138, 'EÁ'),
        (139, 'EÀ'),
        (140, 'EÅ'),
        (141, 'EÃ'),
        (142, 'EÄ'),
        (143, 'OÁ'),
        (144, 'OÀ'),
        (145, 'OÅ'),
        (146, 'OÃ'),
        (147, 'OÄ'),
        (148, 'ÔÏ'),
        (149, 'ÔÙ'),
        (150, 'ÔØ'),
        (151, 'ÔÛ'),
        (152, 'Ò'),
        (153, 'OÛ'),
        (154, 'OÏ'),
        (155, 'Æ'),
        (156, 'UÛ'),
        (157, 'UÕ'),
        (158, 'UÏ'),
        (159, 'YØ'),
        (160, 'OÕ'),
        (161, 'aé'),
        (162, 'aè'),
        (163, 'aë'),
        (164, 'aá'),
        (165, 'aà'),
        (166, 'aå'),
        (167, 'aä'),
        (168, 'eõ'),
        (169, 'eï'),
        (170, 'eá'),
        (171, 'eà'),
        (172, 'eå'),
        (173, 'eã'),
        (174, 'eä'),
        (175, 'oá'),
        (176, 'oà'),
        (177, 'oå'),
        (178, 'oã'),
        (179, 'ÔÕ'),
        (180, 'Ô'),
        (181, 'oä'),
        (182, 'ôø'),
        (183, 'ôû'),
        (184, 'ò'),
        (185, 'ÖÏ'),
        (186, 'ÖÙ'),
        (187, 'ÖØ'),
        (188, 'ÖÛ'),
        (189, 'ô'),
        (190, 'ôù'),
        (191, 'Ö'),
        (192, 'AØ'),
        (193, 'AÙ'),
        (194, 'AÂ'),
        (195, 'AÕ'),
        (196, 'AÛ'),
        (197, 'AÊ'),
        (198, 'aú'),
        (199, 'aü'),
        (200, 'EØ'),
        (201, 'EÙ'),
        (202, 'EÂ'),
        (203, 'EÛ'),
        (204, 'Ì'),
        (205, 'Í'),
        (206, 'Ó'),
        (207, 'yø'),
        (208, 'Ñ'),
        (209, 'öù'),
        (210, 'OØ'),
        (211, 'OÙ'),
        (212, 'OÂ'),
        (213, 'aï'),
        (214, 'yû'),
        (215, 'öø'),
        (216, 'öû'),
        (217, 'UØ'),
        (218, 'UÙ'),
        (219, 'yõ'),
        (220, 'î'),
        (221, 'YÙ'),
        (222, 'ôõ'),
        (223, 'ö'),
        (224, 'aø'),
        (225, 'aù'),
        (226, 'aâ'),
        (227, 'aõ'),
        (228, 'aû'),
        (229, 'aê'),
        (230, 'öõ'),
        (231, 'aã'),
        (232, 'eø'),
        (233, 'eù'),
        (234, 'eâ'),
        (235, 'eû'),
        (236, 'ì'),
        (237, 'í'),
        (238, 'ó'),
        (239, 'æ'),
        (240, 'ñ'),
        (241, 'öï'),
        (242, 'oø'),
        (243, 'où'),
        (244, 'oâ'),
        (245, 'oõ'),
        (246, 'oû'),
        (247, 'oï'),
        (248, 'uï'),
        (249, 'uø'),
        (250, 'uù'),
        (251, 'uõ'),
        (252, 'uû'),
        (253, 'yù'),
        (254, 'ôï'),
        (255, 'ÖÕ'),
        ]
