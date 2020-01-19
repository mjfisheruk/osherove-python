def add(numbers_str):
    parts = numbers_str.split(",")
    numbers = [int(n) for n in parts if n.isdigit()]
    return sum(numbers)
