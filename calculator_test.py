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

    def test_negative_numbers_raises_value_error(self):
        self.assertRaises(ValueError, calculator.add, "3,-1,2")

    def test_negative_numbers_returned_in_value_error(self):
        with self.assertRaises(ValueError) as context:
            calculator.add("2,-1,4,-4")
        self.assertListEqual([-1, -4], context.exception.args[0])

    def test_numbers_bigger_than_1000_ignored(self):
        self.assertEqual(2, calculator.add("2,1001"))

    def test_numbers_equal_to_1000_not_ignored(self):
        self.assertEqual(1002, calculator.add("2,1000"))

    def test_delimiters_can_be_any_length(self):
        self.assertEqual(6, calculator.add("//[***]\n1***2***3"))

    def test_can_specify_multiple_delimiters(self):
        self.assertEqual(6, calculator.add("//[*][%]\n1*2%3"))

    def test_can_specify_multiple_delimiters_longer_than_one_char(self):
        self.assertEqual(6, calculator.add("//[*][%%]\n1*2%%3"))


if __name__ == '__main__':
    unittest.main()
