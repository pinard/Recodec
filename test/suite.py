#!/usr/bin/env python
# Validation suite for the Free `recode' program and library.
# Copyright © 1998, 1999, 2000, 2002 Progiciels Bourbeau-Pinard inc.
# François Pinard <pinard@iro.umontreal.ca>, 1998.

import unittest

# VERBOSITY may be 0 for silence, 1 for marching dots and 2 for full lines.
# The default is 2.
VERBOSITY = 2

# If DEFERRED is True, which is the default, tracebacks appear after all
# tests, and the exit status is non-zero if any test failed.  Otherwise,
# tracebacks are interspersed within tests, and the exit status is zero.
DEFERRED = True

def make_suite():
    # Decide the sequence of tests.  Tests in FIRST are run first, these
    # are for the basic engine and individual surfaces.  All remaining
    # tests are then executed in lexicographical order.
    first = ['names', 'listings', 'methods',
             'dumps', 'base64', 'quoted']
    # FIXME: 'endline', 'permut' tests are lacking.
    # FIXME: Some tests are inhibited for now.
    inhibit = ['testdump', 'utf7']
    import glob
    names = [name[2:-3] for name in glob.glob('t_*.py')
             if name[2:-3] not in first + inhibit]
    names.sort()
    return (unittest.defaultTestLoader.loadTestsFromNames(
        ['t_' + name for name in first + names]))

class ImmediateTestRunner(unittest.TextTestRunner):
    # By Jeremy Hylton <jeremy@alum.mit.edu>, 2002-01-21.

    class ImmediateTestResult(unittest._TextTestResult):

        def addError(self, test, error):
            self._print_traceback("Error in test %s" % test, error)

        def addFailure(self, test, error):
            self._print_traceback("Failure in test %s" % test, error)

        def _print_traceback(self, message, error):
            import traceback
            if self.showAll or self.dots:
                self.stream.writeln("\n")
            self.stream.writeln(message)
            self.stream.writeln(''.join(traceback.format_exception(*error)))

    def _makeResult(self):
        return self.ImmediateTestResult(self.stream, self.descriptions,
                                        self.verbosity)

def print_warning():
    import sys
    sys.stderr.write("""\
WARNING: The `bigauto' test will be skipped, as it takes a long time to
         complete.  To launch it, get into the `test/' directory
         and do either `make bigtest' or `make bigtest-strict'.  The
         later forces `-s' on all `recode' calls.
""")

if __name__ == '__main__':
    #print_warning()
    if DEFERRED:
        unittest.TextTestRunner(verbosity=VERBOSITY).run(make_suite())
    else:
        ImmediateTestRunner(verbosity=VERBOSITY).run(make_suite())
