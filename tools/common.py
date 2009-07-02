# Handling basic input and output.

import sys

class Input:
    def __init__(self, name):
        self.name = name
        self.input = file(name)
        self.line_count = 0
        sys.stderr.write("Reading %s\n" % name)

    def __iter__(self):
        return self

    def next(self):
        line = self.input.readline()
        if line:
            self.line_count += 1
            return line
        raise StopIteration

    def readline(self):
        line = self.input.readline()
        if line:
            self.line_count += 1
        return line

    def warn(self, format, *args):
        sys.stderr.write('%s:%s: %s\n'
                         % (self.name, self.line_count, format % args))

    def die(self, format, *args):
        sys.stderr.write('%s:%s: %s\n'
                         % (self.name, self.line_count, format % args))
        raise 'Fatal'

class Output:
    def __init__(self, name, header=None):
        self.name = name
        self.write = file(name, 'w').write
        sys.stderr.write("Writing %s\n" % name)
        if header == 'C':
            self.write("""\
/* DO NOT MODIFY THIS FILE!  It was automatically generated.  */

/* Conversion between different charsets, surfaces and structures.
   Copyright © 1993, 1997, 1999, 2002 Free Software Foundation, Inc.
   Contributed by François Pinard <pinard@iro.umontreal.ca>, 1993.

   This library is free software; you can redistribute it and/or
   modify it under the terms of the GNU Lesser General Public License
   as published by the Free Software Foundation; either version 2 of the
   License, or (at your option) any later version.

   This library is distributed in the hope that it will be
   useful, but WITHOUT ANY WARRANTY; without even the implied warranty
   of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
   Lesser General Public License for more details.

   You should have received a copy of the GNU Lesser General Public
   License along with the `recode' Library; see the file `COPYING.LIB'.
   If not, write to the Free Software Foundation, Inc., 59 Temple Place -
   Suite 330, Boston, MA 02111-1307, USA.  */
""")
        elif header in ('Perl', 'Python'):
            self.write("""\
# DO NOT MODIFY THIS FILE!  It was automatically generated.

# Conversion between different charsets, surfaces and structures.
# Copyright © 1993, 1997, 1999, 2002 Free Software Foundation, Inc.
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
""")
        elif header is not None:
            assert False, "Unknown language `%s'" % header
