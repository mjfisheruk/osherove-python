import re


def _extract_delimiter(numbers_str):
    m = re.match("^//(.)\n", numbers_str)
    if m:
        return m.group(1)
    return ","


def _normalize_numbers_str(numbers_str, delimiter):
    m = re.match("^//(.)\n", numbers_str)
    if m:
        numbers_str = numbers_str[m.end():]
    return numbers_str.replace("\n", delimiter)


def _split_into_numbers(numbers_str, delimiter):
    normalized_numbers_str = _normalize_numbers_str(numbers_str, delimiter)
    parts = normalized_numbers_str.split(delimiter)
    valid_numbers = []
    invalid_numbers = []
    for n in parts:
        if n == '':
            continue
        value = int(n)
        if value > 1000:
            continue
        elif value < 0:
            invalid_numbers.append(value)
        else:
            valid_numbers.append(value)
    if len(invalid_numbers) > 0:
        raise ValueError(invalid_numbers)
    return valid_numbers


def add(numbers_str):
    delimiter = _extract_delimiter(numbers_str)
    numbers = _split_into_numbers(numbers_str, delimiter)
    return sum(numbers)
