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


# Score categories.
# Change the values as you see fit.
YACHT = 0
ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = 7
FOUR_OF_A_KIND = 8
LITTLE_STRAIGHT = 9
BIG_STRAIGHT = 10
CHOICE = 11


def score(dice, category):
    dice.sort()
    if category == 0:
        if dice.count(dice[0]) == 5:
            return 50
        else:
            return 0
    elif category == 1:
        return dice.count(1)
    elif category == 2:
        return 2 * dice.count(2)
    elif category == 3:
        return 3 * dice.count(3)
    elif category == 4:
        return 4 * dice.count(4)
    elif category == 5:
        return 5 * dice.count(5)
    elif category == 6:
        return 6 * dice.count(6)
    elif category == 7:
        # since is the list is sorted
        if sorted((dice.count(dice[0]), dice.count(dice[4]))) == [2, 3]:
            return sum(dice)
        else:
            return 0
    elif category == 8:
        # Pigeonhole principle (could do this for any two elements of the list `dice`)
        if dice.count(dice[0]) >= 4:
            return 4 * dice[0]
        elif dice.count(dice[1]) == 4:
            return 4 * dice[1]
        else:
            return 0
    elif category == 9:
        if dice == [1, 2, 3, 4, 5]:
            return 30
        else:
            return 0
    elif category == 10:
        if dice == [2, 3, 4, 5, 6]:
            return 30
        else:
            return 0
    elif category == 11:
        return sum(dice)
