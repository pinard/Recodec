# Handling basic input and output.
# -*- coding: utf-8 -*-

from __future__ import generators
import sys

HEADER = """\
%(l)sDO NOT MODIFY THIS FILE!  It was automatically generated.  %(r)s
%(l)s-*- coding: utf-8 -*- %(r)s
%(e)s
%(l)sConversion between different charsets, surfaces and structures.
%(c)sCopyright © 1993, 1997, 1999, 2002, 2004 Free Software Foundation, Inc.
%(c)sContributed by François Pinard <pinard@iro.umontreal.ca>, 1993.
%(e)s
%(c)sThis library is free software; you can redistribute it and/or
%(c)smodify it under the terms of the GNU Lesser General Public License
%(c)sas published by the Free Software Foundation; either version 2 of the
%(c)sLicense, or (at your option) any later version.
%(e)s
%(c)sThis library is distributed in the hope that it will be
%(c)suseful, but WITHOUT ANY WARRANTY; without even the implied warranty
%(c)sof MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
%(c)sLesser General Public License for more details.
%(e)s
%(c)sYou should have received a copy of the GNU Lesser General Public
%(c)sLicense along with the `recode' Library; see the file `COPYING.LIB'.
%(c)sIf not, write to the Free Software Foundation, Inc., 59 Temple Place -
%(c)sSuite 330, Boston, MA 02111-1307, USA.  %(r)s
"""

def all_strip_data():
    # Save all data from known StripStep classes.
    from Recode import recode
    for (before, after), method in recode.registry.methods.iteritems():
        if after == recode.UNICODE_STRING:
            if isinstance(method, tuple):
                if len(method) != 3:
                    continue
                module_name, codec_name, use_encode = method
                module = getattr(__import__('Recode.' + module_name),
                                 module_name)
                step = getattr(module, codec_name)
            else:
                step = method.im_class
            if issubclass(step, recode.StripStep):
                yield before, step.data, step.indices

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
    def __init__(self, name, header=None, margin=''):
        self.name = name
        self.write = file(name, 'w').write
        sys.stderr.write("Writing %s\n" % name)
        if header == 'C':
            e = ''
            l = margin + '/* '
            c = margin + '   '
            r = '*/'
        elif header in ('Perl', 'Python'):
            e = ''
            l = margin + '# '
            c = margin + '# '
            r = ''
        elif header == 'ReST':
            e = margin + '..'
            l = margin + '   '
            c = margin + '   '
            r = ''
            self.write(e + '\n')
        elif header is not None:
            assert False, "Unknown language `%s'" % header
        for line in (HEADER % locals()).splitlines():
            self.write(line.rstrip() + '\n')
