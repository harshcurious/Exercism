def is_armstrong_number(number):
    string = str(number)
    add = 0
    l = len(string)
    for char in string:
        add += int(char) ** l
    return add == number
