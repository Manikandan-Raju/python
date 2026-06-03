import unittest

from calculator import add, subtract, multiply, divide


class TestCalculator(unittest.TestCase):
    """Unittest examples for calculator functions."""

    def test_add(self):
        self.assertEqual(add(4, 5), 9)
        self.assertEqual(add(-1, 1), 0)

    def test_subtract(self):
        self.assertEqual(subtract(10, 3), 7)
        self.assertEqual(subtract(0, 5), -5)

    def test_multiply(self):
        self.assertEqual(multiply(6, 7), 42)
        self.assertEqual(multiply(-3, 4), -12)

    def test_divide(self):
        self.assertAlmostEqual(divide(8, 4), 2.0)
        self.assertAlmostEqual(divide(3, 2), 1.5)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            divide(5, 0)


if __name__ == "__main__":
    unittest.main()
