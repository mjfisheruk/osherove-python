import re


def _has_custom_delimiter(numbers_str):
    return re.match(r"//(.+?)\n", numbers_str) is not None


def _extract_delimiter(numbers_str):
    if not _has_custom_delimiter(numbers_str):
        return ","
    first_line = numbers_str.split("\n")[0]
    # Remove leading double slash:
    delimiter = first_line[2:]
    # Delimiter can be of any length, but is optionally
    # surrounded by square brackets:
    if delimiter.startswith("[") and delimiter.endswith("]"):
        delimiter = delimiter[1:-1]
    return delimiter


def _normalize_numbers_str(numbers_str, delimiter):
    if _has_custom_delimiter(numbers_str):
        # Remove the first line which specifies the custom
        # delimiter:
        numbers_str = "".join(numbers_str.split("\n")[1:])
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
