from math import prod


def largest_product(series, size):
    if size > len(series) or size < 0:
        raise ValueError(series, size)
    if size == 0:
        return 1
    curr_max_prod = 0
    for i in range(len(series) - size + 1):
        product = prod([int(char) for char in series[i:i+size]])
        if product > curr_max_prod:
            curr_max_prod = product
    return curr_max_prod
