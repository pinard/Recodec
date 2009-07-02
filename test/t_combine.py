import common

class Tests(common.Test):

    def test_1(self):
        # Check that combine does not crash.
        self.request('co..l1')
        self.assertEqual(self.encode(''), '')

if __name__ == '__main__':
    import unittest
    unittest.main()
