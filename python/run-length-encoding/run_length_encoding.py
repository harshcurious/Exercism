def decode(string):
    decoded = ''
    has_num = False
    num_str = ''
    for i in range(len(string)):
        if string[i].isalpha() or string[i].isspace():
            if has_num:  # preceded by a number
                decoded += string[i] * int(num_str)
            else:  # not preceded by a number
                decoded += string[i]
            has_num = False
            num_str = ''
        if string[i].isdigit():
            has_num = True
            num_str += string[i]  # for dealing with numbers >=10
    return decoded


def encode(string):
    # Edge case empty string
    if string == '':
        return ''
    encoded = ''
    current_char = ''
    current_char_count = 0
    for char in string:
        if current_char == '':
            current_char = char
            current_char_count = 1
        elif current_char != char:
            if current_char_count == 1:  # encoded won't include a number
                encoded += current_char
                current_char = char
                current_char_count = 1
            else:  # count>1
                encoded += str(current_char_count) + current_char
                current_char = char
                current_char_count = 1
        else:  # current_char == char
            current_char_count += 1
    # Adding the last character
    if current_char_count == 1:  # encoded won't include a number
        encoded += current_char
        current_char = char
        current_char_count = 1
    else:  # count>1
        encoded += str(current_char_count) + current_char
        current_char = char
        current_char_count = 1
    return encoded
