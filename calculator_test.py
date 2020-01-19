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

    def test_numbers_greater_than_nine_add_correctly(self):
        self.assertEqual(18, calculator.add("1,2,12,3"))

    def test_allows_comma_and_newline_as_delimiters(self):
        self.assertEqual(6, calculator.add("1\n2,3"))

    def test_allow_custom_delimiter(self):
        self.assertEqual(3, calculator.add("//;\n1;2"))

    def test_custom_delimiter_as_digit_is_allowed(self):
        self.assertEqual(6, calculator.add("//1\n313"))


if __name__ == '__main__':
    unittest.main()
