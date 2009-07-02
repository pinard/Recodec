#!/usr/bin/env python

from distutils.core import setup

import sys
sys.path.insert(0, '.')
from Recode import version

setup(name=version.package,
      version=version.version,
      description="Conversion between charsets, surfaces and structures.",
      author='François Pinard',
      author_email='pinard@iro.umontreal.ca',
      url='http://www.iro.umontreal.ca/contrib/recode/HTML',
      scripts=['recodec'],
      packages=['Recode'])
