import unittest

from calculator import add, power


class CalculatorTest(unittest.TestCase):
    def test_add(self) -> None:
        self.assertEqual(add(2, 3), 5)

    def test_power(self) -> None:
        self.assertEqual(power(2, 3), 8)


if __name__ == "__main__":
    unittest.main()
