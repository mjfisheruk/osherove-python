import re

default_delimiter = ","


def _has_custom_delimiter(numbers_str):
    return re.match(r"//(.+?)\n", numbers_str) is not None


def _extract_delimiters(numbers_str):
    if not _has_custom_delimiter(numbers_str):
        return [","]
    first_line = numbers_str.split("\n")[0]
    # Remove leading double slash:
    delimiter = first_line[2:]

    # Delimiter can be of any length, but is optionally
    # surrounded by square brackets. There can be multiple
    # delimiters surrounded by multiple square brackets
    matches = re.findall(r"\[(.+?)\]", delimiter)
    if matches:
        return matches

    # If there are no square brackets, just use
    # the extracted delimiter string
    return [delimiter]


def _normalize_numbers_str(numbers_str, delimiters):
    """
    Removes any custom delimiter first line, and replaces
    all custom delimiters with default delimiters
    """
    if _has_custom_delimiter(numbers_str):
        # Remove the first line which specifies the custom
        # delimiter:
        numbers_str = "".join(numbers_str.split("\n")[1:])
    for delimiter in delimiters:
        numbers_str = numbers_str.replace(delimiter, default_delimiter)
    return numbers_str.replace("\n", default_delimiter)


def _split_into_numbers(numbers_str):
    parts = numbers_str.split(default_delimiter)
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
    delimiters = _extract_delimiters(numbers_str)
    normalized_str = _normalize_numbers_str(numbers_str, delimiters)
    numbers = _split_into_numbers(normalized_str)
    return sum(numbers)
