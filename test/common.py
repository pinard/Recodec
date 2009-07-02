# -*- coding: UTF-8 -*-
import os, unittest

for variable in 'LANG', 'LANGUAGE', 'LC_ALL', 'LC_MESSAGES':
    if variable in os.environ:
        del os.environ[variable]
del variable

class Test(unittest.TestCase):
    ordinal = 0

    def __init__(self, *arguments):
        unittest.TestCase.__init__(self, *arguments)
        Test.ordinal += 1
        self.ordinal = Test.ordinal

    def __str__(self):
        total = str(Test.ordinal)
        return '%*d/%s  %s' % (len(total), self.ordinal, total, self.id())

    def request(self, request):
        from Recode import Recodec
        self.codec = Recodec(request)

    def encode(self, input):
        output, length = self.codec.encode(input)
        self.assertEqual(length, len(input))
        return output

    def decode(self, input):
        output, length = self.codec.decode(input)
        self.assertEqual(length, len(input))
        return output

    def assertQuotedEqual(self, first, second, message=None):
        self.assertEqual(first.replace('=\n', '').replace('\n', ''),
                         second.replace('=\n', '').replace('\n', ''),
                         message)
