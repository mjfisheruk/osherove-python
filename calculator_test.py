import unittest
import calculator


class AddTest(unittest.TestCase):
    def test_returns_zero_with_empty_string(self):
        self.assertEqual(calculator.add(""), 0)

    def test_returns_single_number_unmodified(self):
        self.assertEqual(calculator.add("2"), 2)

    def test_returns_sum_of_comma_delimited_numbers(self):
        self.assertEqual(calculator.add("2,3"), 5)


if __name__ == '__main__':
    unittest.main()
