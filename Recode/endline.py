# Conversion of files between different charsets and surfaces.
# Copyright © 1990, 93, 94, 97, 98, 99, 02 Free Software Foundation, Inc.
# This file is part of the GNU C Library.
# Contributed by François Pinard <pinard@iro.umontreal.ca>, 1988.
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

declares = ['CR', ('CR-LF', 'cl')]

class Cr(recode.GenericStep):
    internal_coding = recode.TRIVIAL_SURFACE
    external_coding = 'CR'
    data = [('\n', '\r')]

class Crlf(recode.GenericStep):
    internal_coding = recode.TRIVIAL_SURFACE
    external_coding = 'CR-LF'
    data = [('\n', '\r\n')]
