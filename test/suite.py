#!/usr/bin/env python
# Copyright © 1998, 1999, 2000, 2002 Progiciels Bourbeau-Pinard inc.
# François Pinard <pinard@iro.umontreal.ca>, 1998.

"""\
Validation suite for the Free `recode' program and library.

Usage: python suite.py [OPTION]... [TEST]...

Options:
   -b  Also execute bigger, lengthy tests.
   -i  Produce tracebacks immediately.
   -p  Profile the testing suite.
   -q  Do not display marching dots.
   -v  Display one full line per test.

If one or more TEST are given, checking is limited to those.  See `unittest'
documentation for details.  Otherwise, all tests are executed.
"""

import sys, unittest

class Main:
    def __init__(self):
        self.bigger = False
        # If IMMEDIATE is False, which is the default, tracebacks appear
        # after all tests, and the exit status is non-zero if any test failed.
        # Otherwise, tracebacks are interspersed within tests, and the exit
        # status is zero.
        self.immediate = False
        # VERBOSITY may be 0 for silence, 1 for marching dots and 2 for
        # full lines.
        self.verbosity = 1
        # Profile is set when profiling is wanted.
        self.profile = False

    def main(self, *arguments):
        import getopt
        options, arguments = getopt.getopt(arguments, 'bipqv')
        for option, value in options:
            if option == '-b':
                self.bigger = True
            elif option == '-i':
                self.immediate = True
            elif option == '-p':
                self.profile = True
            elif option == '-q':
                self.verbosity = 0
            elif option == '-v':
                self.verbosity = 2
        self.print_warning()
        # Save remaining arguments for `unittest' to consider.
        sys.argv[1:] = list(arguments)
        self.prepare_suite()
        if self.profile:
            import profile, pstats
            global run_suite
            run_suite = self.run_suite
            profile.run('run_suite()', 'profile-data')
            stats = pstats.Stats('profile-data')
            stats.strip_dirs().sort_stats('time', 'cumulative').print_stats(10)
        else:
            self.run_suite()

    def run_suite(self):
        if self.immediate:
            ImmediateTestRunner(verbosity=self.verbosity).run(self.suite)
        else:
            unittest.TextTestRunner(verbosity=self.verbosity).run(self.suite)

    def print_warning(self):
        sys.stderr.write("""\
WARNING: The `bigauto' test will be skipped, as it takes many minutes to
         complete.  To launch it, type `python test/bigauto.py' in a shell.
""")

    def prepare_suite(self):
        # Decide the sequence of tests.  Tests in FIRST are run first.
        # All remaining tests are then executed in lexicographical order.
        # Test basic engine and individual surfaces, run the mini-suite.
        first = ['names', 'listings', 'methods',
                 'dumps', 'base64', 'quoted',
                 # FIXME: 'endline', 'permut' tests are lacking.
                 'minisuite']
        # FIXME: Some tests are going to be inhibited for now.
        inhibit = ['testdump', 'utf7']
        if not self.bigger:
            inhibit += ['names']
        import glob
        names = [name[2:-3] for name in glob.glob('t_*.py')
                 if name[2:-3] not in first]
        names.sort()
        self.suite = (unittest.defaultTestLoader.loadTestsFromNames(
            ['t_' + name for name in first + names if name not in inhibit]))

main = Main().main

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
