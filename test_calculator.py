import unittest

from calculator import add, divide


class CalculatorTest(unittest.TestCase):
    def test_add(self) -> None:
        self.assertEqual(add(2, 3), 5)

    def test_divide(self) -> None:
        self.assertEqual(divide(6, 3), 2)

    def test_divide_by_zero(self) -> None:
        with self.assertRaises(ZeroDivisionError):
            divide(6, 0)


if __name__ == "__main__":
    unittest.main()
