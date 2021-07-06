"""
This exercise stub and the test suite contain several enumerated constants.

Since Python 2 does not have the enum module, the idiomatic way to write
enumerated constants has traditionally been a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = -1
SUPERLIST = 1
EQUAL = 2
UNEQUAL = 0


def actual_sublist(list_1, list_2):
    '''Tests is list_1 is a sublist of list_2'''
    if list_1 == []:
        return True
    if list_2 == []:
        return False
    if len(list_1) > len(list_2):
        return False
    length = len(list_1)
    j = 0
    while list_1[0] in list_2:
        j = list_2.index(list_1[0])
        list_2 = list_2[j:]
        if len(list_1) > len(list_2):
            break
        if list_1 == list_2[:length]:
            return True
        # print(list_2)
        list_2 = list_2[1:]
    return False


def sublist(list_one, list_two):
    '''More like compare list than sub list'''
    is_sublist = actual_sublist(list_one, list_two)
    is_superlist = actual_sublist(list_two, list_one)
    if is_sublist and is_superlist:
        return EQUAL
    elif is_sublist:
        return SUBLIST
    elif is_superlist:
        return SUPERLIST
    else:
        return UNEQUAL


if __name__ == "__main__":
    print("Is:", sublist([1, 2, 5], [0, 1, 2, 3, 1, 2, 5, 6]))
