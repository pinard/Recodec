import common

class Tests(common.Test):
    inputs = [
        '\n',
        'A+ImIDkQ.\n',
        'Hi Mom +Jjo!\n',
        '+ZeVnLIqe\n',
        'Item 3 is +AKM-1.\n',
        ]

    def test_1(self):
        # Single lines from UTF-7.
        self.request('u7..u6/x2')
        outputs = ['''\
0xFEFF, 0x000A
''', '''\
0xFEFF, 0x0041, 0x2262, 0x0391, 0x002E, 0x000A
''', '''\
0xFEFF, 0x0048, 0x0069, 0x0020, 0x004D, 0x006F, 0x006D, 0x0020,
0x263A, 0x0021, 0x000A
''', '''\
0xFEFF, 0x65E5, 0x672C, 0x8A9E, 0x000A
''', '''\
0xFEFF, 0x0049, 0x0074, 0x0065, 0x006D, 0x0020, 0x0033, 0x0020,
0x0069, 0x0073, 0x0020, 0x00A3, 0x0031, 0x002E, 0x000A
'''
                   ]
        for input, output in zip(self.inputs, outputs):
            self.assertEqual(self.encode(input), output)

    def test_2(self):
        # Single lines from UTF-7 and back.
        self.request('u7..u6/x2')
        for input in self.inputs:
            self.assertEqual(self.decode(self.encode(input)), input)

if __name__ == '__main__':
    import unittest
    unittest.main()
