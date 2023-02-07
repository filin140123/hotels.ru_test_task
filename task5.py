def shared_numbers(a: list, b: list) -> list:
    array_a = [i for i in a if a.count(i) >= 2]
    array_b = [i for i in b if b.count(i) >= 2]
    intersection = set(array_a) & set(array_b)
    return list(intersection)
