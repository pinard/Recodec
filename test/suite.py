#!/usr/bin/env python
# Copyright © 1998, 1999, 2000, 2002 Progiciels Bourbeau-Pinard inc.
# François Pinard <pinard@iro.umontreal.ca>, 1998.

"""\
Validation suite for the Free `recode' program and library.

Usage: python suite.py [OPTION]... [TEST]...

Options:
   -b  Also execute bigger, lengthy tests.
   -i  Produce tracebacks immediately.
   -q  Do not display marching dots.
   -v  Display one full line per test.

If one or more TEST are given, checking is limited to those.  See `unittest'
documentation for details.  Otherwise, all tests are executed.
"""

import sys, unittest

def main(*arguments):
    import getopt
    options, arguments = getopt.getopt(arguments, 'biqv')
    bigger = False
    # If IMMEDIATE is False, which is the default, tracebacks appear
    # after all tests, and the exit status is non-zero if any test failed.
    # Otherwise, tracebacks are interspersed within tests, and the exit
    # status is zero.
    immediate = False
    # VERBOSITY may be 0 for silence, 1 for marching dots and 2 for
    # full lines.
    verbosity = 1
    for option, value in options:
        if option == '-b':
            bigger = True
	elif option == '-i':
	    immediate = True
	elif option == '-q':
	    verbosity = 0
	elif option == '-v':
	    verbosity = 2
    print_warning()
    # Save remaining arguments for `unittest' to consider.
    sys.argv[1:] = list(arguments)
    suite = make_suite(bigger)
    if immediate:
	ImmediateTestRunner(verbosity=verbosity).run(suite)
    else:
	unittest.TextTestRunner(verbosity=verbosity).run(suite)

def print_warning():
    sys.stderr.write("""\
WARNING: The `bigauto' test will be skipped, as it takes quite a long time to
	 complete.  To launch it, type `python test/bigauto.py' in a shell.
""")

def make_suite(bigger=False):
    # Decide the sequence of tests.  Tests in FIRST are run first.
    # All remaining tests are then executed in lexicographical order.
    first = []
    # Test basic engine.
    if bigger:
        first += ['names', 'listings', 'methods']
    else:
        first += ['listings', 'methods']
    # Test individual surfaces.
    first += ['dumps', 'base64', 'quoted']
    # FIXME: 'endline', 'permut' tests are lacking above.
    # Run the mini-suite.
    first += ['minisuite']
    # FIXME: Some tests are going to be inhibited for now.
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

if __name__ == '__main__':
    main(*sys.argv[1:])
