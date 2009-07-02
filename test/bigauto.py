#!/usr/bin/env python
# Copyright © 1997, 1999, 2000, 2002 Progiciels Bourbeau-Pinard inc.
# François Pinard <pinard@iro.umontreal.ca>, 1997.

"""\
Produce statistics from the results of the bigauto check.

Usage: bigauto [RECODE_OPTION]... [CHARSET_OPTION]...

This script makes a simple analysis for the connectivity of the various
charsets and produce a report on standard output.  The reports include
statistics about the number of steps before and after optimisation.
(FIXME: Currently, there is no step sequence optimisation in Recodec.)

The option `-hNAME' would affect the resulting output, because there are
more merging rules when this option is in effect.  Other options affect
the result: `-d', `-g' and, notably, `-s'.  (FIXME: Options are ignored!)

All non-option arguments are interpreted as charset names.  If any is
given, the study is limited to those recodings having any of the given
charsets both as a starting and ending points.  If there is no such
non-option argument, all possible recodings are considered.
"""

import os, sys
from Recode import recode

class Main:

    def main(self, *arguments):
        self.recode_options = []
        self.charset_options = []
        for argument in arguments:
            if arguments[0] == '-':
                self.recode_options.append(argument)
            else:
                self.charset_options.append(argument)
        self.produce_counts()
        self.produce_report(sys.stdout.write)

    def produce_counts(self):
        self.recode_calls = 0
        self.original = Stats()
        self.shrunk = Stats()
        # Get the list of charsets.
        if self.charset_options:
            befores = [(charset, charset) for charset in self.charset_options]
            afters = befores
        else:
            befores = {}
            afters = {}
            for before, after in recode.registry.methods:
                if recode.TRIVIAL_SURFACE not in (before, after):
                    befores[recode.cleaned_alias(before)] = before
                    afters[recode.cleaned_alias(after)] = after
            befores = befores.items()
            befores.sort()
            afters = afters.items()
            afters.sort()
        # Recode in all combinations.
        sys.stderr.write("Attempting %d (%d x %d) recodings.\n"
                         % (len(befores)*len(afters),
                            len(befores), len(afters)))
        count = 0
        for _, before in befores:
            count += 1
            sys.stderr.write("  %d/%d. %s..*\n"
                             % (count, len(befores), before))
            for _, after in afters:
                if after != before:
                    request = '%s..%s' % (before, after)
                    arcs = recode.Recodec(request).encoding_arcs()
                    self.recode_calls += 1
                    self.original.count_request(arcs)
                    self.shrunk.count_request(arcs)

    def produce_report(self, write):
        if self.recode_calls == 0:
            sys.stderr.write("No call to report\n")
            return
        write("\n"
              "Optimisation     Original  Shrunk\n"
              "              .-------------------\n"
              "Minimum       |  %2d        %2d\n"
              "Maximum       |  %2d        %2d\n"
              "Average       |  %4.1f      %4.1f\n"
              % (self.original.minimum, self.shrunk.minimum,
                 self.original.maximum, self.shrunk.maximum,
                 float(self.original.total) / float(self.recode_calls),
                 float(self.shrunk.total) / float(self.recode_calls)))
        self.original.write_histogram("Histogram for original requests", write)
        self.shrunk.write_histogram("Histogram for shrunk requests", write)

main = Main().main

class Stats:
    def __init__(self):
        self.count = {}
        self.example = {}
        self.total = 0

    def count_request(self, arcs):
        steps = len(arcs)
        if steps in self.count:
            self.count[steps] += 1
        else:
            self.count[steps] = 1
            self.example[steps] = arcs
            if self.total == 0:
                self.minimum = self.maximum = steps
            else:
                if steps < self.minimum:
                    self.minimum = steps
                if steps > self.maximum:
                    self.maximum = steps
        self.total += steps

    def write_histogram(self, title, write):
        write('\n%s\n' % title)
        for steps in range(self.minimum, self.maximum+1):
            if steps in self.count:
                write("%5d steps, %5d times  %s\n"
                      % (steps, self.count[steps],
                         edit_arcs(self.example[steps])))

def edit_arcs(arcs):
    fragments = []
    write = fragments.append
    before_surface = ''
    after_surface = ''
    current_charset = None
    for before, after in arcs:
        if before == recode.TRIVIAL_SURFACE:
            after_surface += '/' + after
        elif after == recode.TRIVIAL_SURFACE:
            before_surface = '/' + before + before_surface
        elif before == current_charset:
            write('..%s' % after)
            current_charset = after
        else:
            if current_charset is not None:
                write('%s,' % after_surface)
                after_surface = ''
            write('%s%s..%s' % (before, before_surface, after))
            before_surface = ''
            current_charset = after
    write(after_surface)
    return ''.join(fragments)

if __name__ == '__main__':
    main(*sys.argv[1:])
