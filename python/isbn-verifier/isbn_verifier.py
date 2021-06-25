def is_valid(isbn):
    isbn = isbn.replace('-', '')
    # Running a few checks to make sure we have the right kind of input
    if len(isbn) != 10:
        return False
    isbn_list = [0]
    for i in range(10):
        if i < 9:
            if isbn[i].isdigit():
                isbn_list.append(int(isbn[i]))
            else:
                return False
        else:
            if isbn[9].isdigit() or isbn[9].upper() == 'X':
                if isbn[9].upper() == 'X':
                    isbn_list.append(10)
                else:
                    isbn_list.append(int(isbn[i]))
            else:
                return False

    validate = (isbn_list[1] * 10 + isbn_list[2] * 9 + isbn_list[3] * 8 + isbn_list[4] * 7 + isbn_list[5] *
                6 + isbn_list[6] * 5 + isbn_list[7] * 4 + isbn_list[8] * 3 + isbn_list[9] * 2 + isbn_list[10] * 1)
    # print(validate)
    if validate % 11 == 0:
        return True
    else:
        return False


# print(is_valid("3-598-21507-X"))
# print(is_valid("3-598-21508-8"))
