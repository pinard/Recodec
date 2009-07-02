import common

class Tests(common.Test):

    def test_1(self):
        # Submitted by Martin Jaburek.
        input = 'p=F8=EDli=9A =9Elu=9Dou=E8k=FD k=F9=F2'
        output = 'prilis zlutoucky kun'
        self.request('1250/qp..flat')
        self.assertEqual(self.encode(input), output)

    def test_2(self):
        # Submitted by Yann Dirson.
        inputs = ['m=E4k=E8e=F2', '=A3=F3d=BF', 'm=E0tv=FD']
        outputs = ['makcen', 'Lodz', 'mrtvy']
        self.request('l2/qp..flat')
        for input, output in zip(inputs, outputs):
            self.assertEqual(self.encode(input), output)

if __name__ == '__main__':
    import unittest
    unittest.main()
