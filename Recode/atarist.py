# Conversion of files between different charsets and surfaces.
# Copyright © 1993, 94, 96, 97, 98, 99, 00, 02 Free Software Foundation, Inc.
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

declares = ['AtariST']

# RFC 1345 style description for AtariST (non official).
#
# NUSHSXEXETEQAKBLBSHTLFVTFFCRSOSIDLD1D2D3D4NKSYEBCNEMSBECFSGSRSUS
# SP! " NbDO% & ' ( ) * + , - . / 0 1 2 3 4 5 6 7 8 9 : ; < = > ?
# AtA B C D E F G H I J K L M N O P Q R S T U V W X Y Z <(//)>'>_
# '!a b c d e f g h i j k l m n o p q r s t u v w x y z (!!!!)'?DT
# C,u:e'a>a:a!aac,e>e:e!i:i>i!A:AAE'aeAEo>o:o!u>u!y:O:U:CtPdYessf2
# a'i'o'u'n?N?-a-o?ININO1214!I<<>>a?o?O/o/oeOEA!A?O?':''/-PICoRgTM
# ijIJA+B+G+D+H+W+Z+X+TjJ+K+L+M+N+S+E+P+ZJQ+R+ShT+N%K%M%P%ZjSECa00
# a*b*G*p*S*s*Myt*F*h*Omd*Iof*(-*P=3+->==<IuIl-:?2DGSb.MRTnS2S3S'm

# Andreas Schwab writes:
#
# There are some characters which I'm not sure about.  When compared with
# IBM865 (which I think is the original source for the Atari charset) the
# characters "bullet operator" and "middle dot" (dec 249/250) are swapped.
# This may be intentional or a bug in the table for IBM865.  Also character
# dec 238 looks more like "element of" than "greek small letter epsilon",
# actually it is a bit too large for both interpretations.  I suppose that
# the other changes were made for copyright reasons.
#
# Andreas later adds:
#
# This is a fix for the AtariST encoding table.  It was derived from the
# Omega unicode translation tables, which itself claims to be based on
# ftp://plan9.att.com/plan9/unixsrc/tcs.shar.Z.  Unfortunately i wasn't able
# to access this yet.

class Atarist(recode.StripStep):
    external_coding = 'AtariST'
    data = (
       '\u0000\u0001\u0002\u0003\u0004\u0005\u0006\u0007'  # 0
       '\u0008\u0009\u000A\u000B\u000C\u000D\u000E\u000F'  # 8
       '\u0010\u0011\u0012\u0013\u0014\u0015\u0016\u0017'  # 16
       '\u0018\u0019\u001A\u001B\u001C\u001D\u001E\u001F'  # 24
       '\u0020\u0021\u0022\u0023\u0024\u0025\u0026\u0027'  # 32
       '\u0028\u0029\u002A\u002B\u002C\u002D\u002E\u002F'  # 40
       '\u0030\u0031\u0032\u0033\u0034\u0035\u0036\u0037'  # 48
       '\u0038\u0039\u003A\u003B\u003C\u003D\u003E\u003F'  # 56
       '\u0040\u0041\u0042\u0043\u0044\u0045\u0046\u0047'  # 64
       '\u0048\u0049\u004A\u004B\u004C\u004D\u004E\u004F'  # 72
       '\u0050\u0051\u0052\u0053\u0054\u0055\u0056\u0057'  # 80
       '\u0058\u0059\u005A\u005B\u005C\u005D\u005E\u005F'  # 88
       '\u0060\u0061\u0062\u0063\u0064\u0065\u0066\u0067'  # 96
       '\u0068\u0069\u006A\u006B\u006C\u006D\u006E\u006F'  # 104
       '\u0070\u0071\u0072\u0073\u0074\u0075\u0076\u0077'  # 112
       '\u0078\u0079\u007A\u007B\u007C\u007D\u007E\u007F'  # 120
       '\u00C7\u00FC\u00E9\u00E2\u00E4\u00E0\u00E5\u00E7'  # 128
       '\u00EA\u00EB\u00E8\u00EF\u00EE\u00EC\u00C4\u00C5'  # 136
       '\u00C9\u00E6\u00C6\u00F4\u00F6\u00F2\u00FB\u00F9'  # 144
       '\u00FF\u00D6\u00DC\u00A2\u00A3\u00A5\u00DF\u0192'  # 152
       '\u00E1\u00ED\u00F3\u00FA\u00F1\u00D1\u00AA\u00BA'  # 160
       '\u00BF\u2310\u00AC\u00BD\u00BC\u00A1\u00AB\u00BB'  # 168
       '\u00E3\u00F5\u00D8\u00F8\u0153\u0152\u00C0\u00C3'  # 176
       '\u00D5\u00A8\u00B4\u2020\u00B6\u00A9\u00AE\u2122'  # 184
       '\u0133\u0132\u05D0\u05D1\u05D2\u05D3\u05D4\u05D5'  # 192
       '\u05D6\u05D7\u05D8\u05D9\u05DB\u05DC\u05DE\u05E0'  # 200
       '\u05E1\u05E2\u05E4\u05E6\u05E7\u05E8\u05E9\u05EA'  # 208
       '\u05DF\u05DA\u05DD\u05E3\u05E5\u00A7\u2038\u221E'  # 216
       '\u03B1\u03B2\u0393\u03C0\u03A3\u03C3\u00B5\u03C4'  # 224
       '\u03A6\u03B8\u2126\u03B4\u222E\u03C6\u2208\u220F'  # 232
       '\u2261\u00B1\u2265\u2264\u2320\u2321\u00F7\u2248'  # 240
       '\u00B0\u2022\u00B7\u221A\u207F\u00B2\u00B3\u00AF'  # 248
        )
