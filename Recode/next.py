# Conversion of files between different charsets and surfaces.
# Copyright © 1993, 1994, 1997, 2002 Free Software Foundation, Inc.
# This file is part of the GNU C Library.
# Contributed by François Pinard <pinard@iro.umontreal.ca>, 1993.
#
# The `recode' Library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Library General Public License
# as published by the Free Software Foundation; either version 2 of the
# License, or (at your option) any later version.
#
# The `recode' Library is distributed in the hope that it will be
# useful, but WITHOUT ANY WARRANTY; without even the implied warranty
# of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Library General Public License for more details.
#
# You should have received a copy of the GNU Library General Public
# License along with the `recode' Library; see the file `COPYING.LIB'.
# If not, write to the Free Software Foundation, Inc., 59 Temple Place -
# Suite 330, Boston, MA 02111-1307, USA.

import recode

declares = ['NeXT']

# RFC 1345 style description for NeXTSTEP (non official).
#
# NUSHSXEXETEQAKBLBSHTLFVTFFCRSOSIDLD1D2D3D4NKSYEBCNEMSBECFSGSRSUS
# SP! " NbDO% & ' ( ) * + , - . / 0 1 2 3 4 5 6 7 8 9 : ; < = > ?
# AtA B C D E F G H I J K L M N O P Q R S T U V W X Y Z <(//)>'>_
# '!a b c d e f g h i j k l m n o p q r s t u v w x y z (!!!!)'?DT
# NSA!A'A>A?A:AAC,E!E'E>E:I!I'I>I:D-N?O!O'O>O?O:U!U'U>U:Y'THMy*X-:
# Co!ICtPd/fYef2SECu  "6<<    fiflRg-N/-/=.MBBPISb    "9>>.3%0NO?I
# 1S'!'''>'?'m'('.':2S'0',3S'"';'<-M+-141234a!a'a>a?a:aac,e!e'e>e:
# i!AEi'-ai>i:d-n?L/O/OE-oo!o'o>o?o:aeu!u'u>i.u:y'l/o/oessthy:

# In the following table, these codes are not represented:
#
#      Dec Oct     Character
#
#      169 251     single quote
#      172 254     gouillemot single left
#      173 255     gouillemot single right
#      184 270     single quote base
#      185 271     double quote base
#
# Keld also writes:
#
# * f2 (florin) was introduced after RFC1345, and it was done according
# to an official answer from ISO/IEC JTC1/SC2/WG2 to the Danish ballot
# on DIS.2 10646.  For now, it is translated to the Latin-1 currency sign.
#
# * '" (double acute accent) is the same as hungarian umlaut.

class Next(recode.StripStep):
    external_coding = 'Next'
    data = (
        u'\u0000\u0001\u0002\u0003\u0004\u0005\u0006\u0007'  # 0
        u'\u0008\u0009\u000A\u000B\u000C\u000D\u000E\u000F'  # 8
        u'\u0010\u0011\u0012\u0013\u0014\u0015\u0016\u0017'  # 16
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
        u'\u00A0\u00C0\u00C1\u00C2\u00C3\u00C4\u00C5\u00C7'  # 128
        u'\u00C8\u00C9\u00CA\u00CB\u00CC\u00CD\u00CE\u00CF'  # 136
        u'\u00D0\u00D1\u00D2\u00D3\u00D4\u00D5\u00D6\u00D9'  # 144
        u'\u00DA\u00DB\u00DC\u00DD\u00DE\u00B5\u00D7\u00F7'  # 152
        u'\u00A9\u00A1\u00A2\u00A3\u2215\u00A5\u0192\u00A7'  # 160
        u'\u00A4\uFFFF\u201C\u00AB\uFFFF\uFFFF\uFB01\uFB02'  # 168
        u'\u00AE\u2013\u2020\u2021\u00B7\u00A6\u00B6\u2022'  # 176
        u'\uFFFF\uFFFF\u201D\u00BB\u2026\u2030\u00AC\u00BF'  # 184
        u'\u00B9\u0060\u00B4\u005E\u007E\u00AF\u02D8\u02D9'  # 192
        u'\u00A8\u00B2\u02DA\u00B8\u00B3\u02DD\u02DB\u02C7'  # 200
        u'\u2014\u00B1\u00BC\u00BD\u00BE\u00E0\u00E1\u00E2'  # 208
        u'\u00E3\u00E4\u00E5\u00E7\u00E8\u00E9\u00EA\u00EB'  # 216
        u'\u00EC\u00C6\u00ED\u00AA\u00EE\u00EF\u00F0\u00F1'  # 224
        u'\u0141\u00D8\u0152\u00BA\u00F2\u00F3\u00F4\u00F5'  # 232
        u'\u00F6\u00E6\u00F9\u00FA\u00FB\u0131\u00FC\u00FD'  # 240
        u'\u0142\u00F8\u0153\u00DF\u00FE\u00FF\uFFFF\uFFFF'  # 248
        )
