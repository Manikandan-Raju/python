import unittest

from calculator import add, divide, multiply, subtract


class TestCalculatorAdvanced(unittest.TestCase):
    """Advanced unittest examples covering setup, subtests, and expected failures."""

    @classmethod
    def setUpClass(cls):
        cls.examples = [
            (1, 2, 3),
            (10, 5, 15),
            (-3, 3, 0),
        ]

    @classmethod
    def tearDownClass(cls):
        cls.examples = None

    def setUp(self):
        self.base = 100

    def tearDown(self):
        self.base = None

    def test_add_subtests(self):
        for a, b, expected in self.examples:
            with self.subTest(a=a, b=b):
                self.assertEqual(add(a, b), expected)

    def test_multiply_properties(self):
        self.assertEqual(multiply(5, 0), 0)
        self.assertTrue(multiply(1, 1) == 1)
        self.assertFalse(multiply(2, 3) == 5)

    def test_divide_by_zero(self):
        with self.assertRaisesRegex(ValueError, "zero"):
            divide(10, 0)

    @unittest.skip("Example skip marker for unittest")
    def test_skip_example(self):
        self.assertEqual(add(1, 1), 2)

    @unittest.expectedFailure
    def test_expected_failure_example(self):
        self.assertEqual(divide(9, 3), 4)

    def test_class_attribute(self):
        self.assertIsInstance(self.examples, list)
        self.assertEqual(self.base, 100)


if __name__ == "__main__":
    unittest.main()
