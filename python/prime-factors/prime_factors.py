# # # I intend to use some asyncronous method to calculate primes quickly
# # # This will allow me to learn a lot more about those methods
# # # There is a prime calculation method here <https://buel.me/multiprocessing-in-python/>
# # # But my laptop returned a lot of errors

import math


def check_prime(num):
    i = 2
    while i <= math.sqrt(num):
        if num % i == 0:
            return False
        i += 1
    return True


def factors(value):
    factor = []
    i = 2
    while i <= math.sqrt(value):
        if value % i == 0 and check_prime(i):
            factor.append(i)
            value = value / i
            continue
        i += 1
    if value > 1:
        factor.append(value)
    return factor


print(factors(1))
