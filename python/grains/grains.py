def square(number):
    if number in range(1, 65):
        return 2 ** (number-1)
    else:
        raise ValueError("Invalid square number: ", number)


def total():
    return 2 ** 64 - 1
