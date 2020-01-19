def _split_into_numbers(numbers_str):
    normalized_numbers_str = numbers_str.replace("\n", ",")
    parts = normalized_numbers_str.split(",")
    return [int(n) for n in parts if n.isdigit()]


def add(numbers_str):
    numbers = _split_into_numbers(numbers_str)
    return sum(numbers)
