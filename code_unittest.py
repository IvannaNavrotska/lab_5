import unittest
import code

class TestCode(unittest.TestCase):

    def test_gcd(self):
        self.assertEqual(code.gcd(0, 0), None)
        self.assertEqual(code.gcd(17, 32), 1)
        self.assertNotEqual(code.gcd(17, 32), 6)
        self.assertIsNone(code.gcd(4.5, 8))
        self.assertIsNone(code.gcd('one', 'five'))

    def test_fibonacci(self):
        self.assertEqual(code.fibonacci(0), 1)
        self.assertEqual(code.fibonacci(5), 8)
        self.assertNotEqual(code.fibonacci(5), 3)
        self.assertIsNone(code.fibonacci('five'))
        self.assertIsNone(code.fibonacci(-5))

if __name__ == '__main__':
    unittest.main()