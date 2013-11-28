# -*- coding: utf-8 -*-
import common

class Tests(common.Test):
    # Testing and counting.

    def test_1(self):
        self.request('test7..us/x,us..count')
        output = '''\
 11  000A LF   117  0020 SP   127  002C ,    152  0030 0     24  0031 1
 24  0032 2     24  0033 3     24  0034 4     24  0035 5     24  0036 6
 24  0037 7      8  0038 8      8  0039 9      8  0041 A      8  0042 B
  8  0043 C      8  0044 D      8  0045 E      8  0046 F    128  0078 x
'''
        self.assertEqual(self.encode(''), output)

    def test_2(self):
        self.request('test8..us/x,us..count')
        output = '''\
 22  000A LF   234  0020 SP   255  002C ,    288  0030 0     32  0031 1
 32  0032 2     32  0033 3     32  0034 4     32  0035 5     32  0036 6
 32  0037 7     32  0038 8     32  0039 9     32  0041 A     32  0042 B
 32  0043 C     32  0044 D     32  0045 E     32  0046 F    256  0078 x
'''
        self.assertEqual(self.encode(''), output)

    def test_3(self):
        self.request('test15..u2/x2,us..count')
        output = '''\
 8064  000A LF   56445  0020 SP   64508  002C ,    80765  0030 0
16256  0031 1    16256  0032 2    16256  0033 3    16256  0034 4
16256  0035 5    16256  0036 6    16256  0037 7    16256  0038 8
16256  0039 9    16256  0041 A    16256  0042 B    16000  0043 C
14975  0044 D    15999  0045 E    15990  0046 F    64509  0078 x
'''
        self.assertEqual(self.encode(''), output)

    def test_4(self):
        self.request('test16..u2/x2,us..count')
        output = '''\
 8192  000A LF   57344  0020 SP   65535  002C ,    81920  0030 0
16384  0031 1    16384  0032 2    16384  0033 3    16384  0034 4
16384  0035 5    16384  0036 6    16384  0037 7    16384  0038 8
16384  0039 9    16384  0041 A    16384  0042 B    16384  0043 C
16384  0044 D    16384  0045 E    16384  0046 F    65536  0078 x
'''
        self.assertEqual(self.encode(''), output)

if __name__ == '__main__':
    import unittest
    unittest.main()
