import unittest
import calculator


class AddTest(unittest.TestCase):
    def test_returns_zero_with_empty_string(self):
        self.assertEqual(0, calculator.add(""))

    def test_returns_single_number_unmodified(self):
        self.assertEqual(2, calculator.add("2"))

    def test_returns_sum_of_two_comma_delimited_numbers(self):
        self.assertEqual(5, calculator.add("2,3"))

    def test_returns_sum_of_many_comma_delimited_numbers(self):
        self.assertEqual(13, calculator.add("2,3,1,7"))


if __name__ == '__main__':
    unittest.main()
