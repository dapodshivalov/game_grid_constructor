import unittest

from pair import Pair


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(Pair('A', 'B'), Pair('B', 'A'))
        self.assertNotEqual(Pair('A', 'C'), Pair('A', 'B'))


if __name__ == '__main__':
    unittest.main()
