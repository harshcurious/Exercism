# numeral = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}
numeral = ['I', 'V', 'X', 'L', 'C', 'D', 'M']


# def _roman0_9(number):
#     if number == 9:
#         return numeral[1] + numeral[10]
#     elif number in [5, 6, 7, 8]:
#         r = numeral[5]
#         i = number - 5
#         while i > 0:
#             r += numeral[1]
#             i -= 1
#         return r
#     elif number == 4:
#         return numeral[1] + numeral[5]
#     elif number in [1, 2, 3, 4]:
#         r = ''
#         i = number
#         while i > 0:
#             r += numeral[1]
#             i -= 1
#         return r

def _romanize(number, order):
    # order in base 10
    if number == 9:
        return numeral[2*order-2] + numeral[2*order]
    elif number in [5, 6, 7, 8]:
        r = numeral[2*order-1]
        i = number - 5
        while i > 0:
            r += numeral[2*order-2]
            i -= 1
        return r
    elif number == 4:
        return numeral[2*order-2] + numeral[2*order-1]
    elif number in [1, 2, 3, 4]:
        r = ''
        i = number
        while i > 0:
            r += numeral[2*order - 2]
            i -= 1
        return r


# def _roman0_9(number):
#     digit_1 = number % 10
#     return _romanize(digit_1, 1)


# def _roman10_99(number):
#     digit_1 = number % 10
#     digit_2 = int(number/10) % 10
#     return _romanize(digit_2, 2)+_romanize(digit_1, 1)


def roman(number):
    # if number in range(10):
    #     # 0,1,2,...,9
    #     return _roman0_9(number)
    # elif number in range(10, 100):
    #     return _roman10_99(number)
    if number in range(1, 4000):
        output = ''
        counter = 1
        while number > 0:
            digit = number % 10
            if digit != 0:
                output = _romanize(digit, counter) + output
            number = int(number/10)
            counter += 1
        return output
    else:
        raise ValueError(number, ": is outside contemprory use")
