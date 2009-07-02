import common

class Tests(common.Test):
    input = "Fran=E7ois=20et=20l'=EEle!".decode('quopri')

    def test_437(self):
        self.two_way('l1..437/qp', "Fran=87ois et l'=8Cle!")

    def test_flat(self):
        self.one_way('l1..flat', "Francois et l'ile!")

    def test_html(self):
        self.two_way('l1..html', "Fran&ccedil;ois et l'&icirc;le!")

    def test_mac(self):
        self.two_way('l1..mac/qp', "Fran=8Dois et l'=94le!")

    def test_tlin(self):
        self.two_way('l1..t-lin', "Franc\,ois et l'i^le!")

    def test_tjuca(self):
        self.two_way('l1..tjuca', "Franc\,ois et l'i^le!")

    def test_ue(self):
        self.two_way('l1..ue', "Fran\\u00E7ois et l'\\u00EEle!")

    def test_dump(self):
        output = """\
UCS2   Mne   Description

0046   F     latin capital letter f
0072   r     latin small letter r
0061   a     latin small letter a
006E   n     latin small letter n
00E7   c,    latin small letter c with cedilla
006F   o     latin small letter o
0069   i     latin small letter i
0073   s     latin small letter s
0020   SP    space
0065   e     latin small letter e
0074   t     latin small letter t
0020   SP    space
006C   l     latin small letter l
0027   '     apostrophe
00EE   i>    latin small letter i with circumflex
006C   l     latin small letter l
0065   e     latin small letter e
0021   !     exclamation mark
"""
        self.one_way('l1..dump/qp', output)

    def two_way(self, request, output):
        self.one_way(request, output)
        self.assertEqual(self.decode(output), self.input)

    def one_way(self, request, output):
        self.request(request)
        if request.endswith('/qp'):
            self.assertQuotedEqual(self.encode(self.input), output)
        else:
            self.assertEqual(self.encode(self.input), output)

if __name__ == '__main__':
    import unittest
    unittest.main()
