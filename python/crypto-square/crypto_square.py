# The size of the rectangle (r x c) should be decided by the length of the message, such that c >= r and c - r <= 1, where c is the number of columns and r is the number of rows.
# ~~This severly restricts the sizes of message allowed!!!~~
# I am supposed to add spaces if needed
import re
from math import sqrt


def rectangle_size(num):
    ''' Calculates the length of rectangle (r,c) such that c >= r and c - r <= 1, where c is the number of columns and r is the number of rows.
    Takes the length of the string as the input.
    Returns r,c in that order!
    '''
    root_int = int(sqrt(num))
    if num == root_int*root_int:
        return root_int, root_int
    elif num <= root_int*(root_int+1):
        return root_int, root_int+1
    else:
        return (root_int + 1), (root_int+1)


def cipher_text(plain_text):
    if plain_text == '':
        return plain_text
    plain_text = plain_text.lower()
    plain_text = ''.join(re.findall(r'[a-z0-9]*', plain_text))
    # print(plain_text)
    if len(plain_text) == 1:
        return plain_text

    r, c = rectangle_size(len(plain_text))
    # print(r, c)
    # Addiing spaces when need using `ljust` string method
    plain_text = plain_text.ljust(r*c)
    encoded = ''
    # rectangle = [plain_text[i*c: (i+1)*c] for i in range(r)]
    for j in range(c):
        for i in range(r):
            encoded += plain_text[i*c + j]
        encoded += ' '
    # print(rectangle)

    # # # The loop adds an extra space at the end
    return encoded[:-1]


# Testing
if __name__ == "__main__":
    value = "A"
    print(cipher_text(value))
    value2 = "This is fun!"
    print(cipher_text(value2))
    value3 = "Chill out."
    print(cipher_text(value3))
    value4 = "If man was meant to stay on the ground, god would have given us roots."
    print(cipher_text(value4))
