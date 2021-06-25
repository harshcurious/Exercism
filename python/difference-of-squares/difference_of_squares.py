def square_of_sum(number):
    # (1 + 2 + 3 + ... + n) = (n*(n+1))/2
    return (number ** 2 * (number+1) ** 2)/4


def sum_of_squares(number):
    # (1^2 + 2^2 + 3^2 + ... + n^2) = (n*(n+1)*(2n+1))/6
    return (number * (number + 1) * (2 * number + 1))/6


def difference_of_squares(number):
    # There is a formula but I doubt it will save much time
    return square_of_sum(number) - sum_of_squares(number)
