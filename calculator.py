import re


def _extract_delimiter(numbers_str):
    m = re.match("^//(.)\n", numbers_str)
    if m:
        return m.group(1)
    return ","


def _split_into_numbers(numbers_str, delimiter):
    normalized_numbers_str = numbers_str.replace("\n", delimiter)
    parts = normalized_numbers_str.split(delimiter)
    return [int(n) for n in parts if n.isdigit()]


def add(numbers_str):
    delimiter = _extract_delimiter(numbers_str)
    numbers = _split_into_numbers(numbers_str, delimiter)
    return sum(numbers)
