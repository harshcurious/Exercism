def score(word):
    # before I do anything I turn word into capitals
    word = word.upper()
    letter_values = {}
    # # # l = "A, E, I, O, U, L, N, R, S, T ".split(", ")
    # # # print(l)
    # # # output > ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S', 'T ']
    # # # p = list(filter(lambda char: char.isalpha(), "A, E, I, O, U, L, N, R, S, T "))
    # # # print(p)
    # # # output > ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S', 'T']
    # # # print({char: 1 for char in p})
    # # # output > {'A': 1, 'E': 1, 'I': 1, 'O': 1, 'U': 1, 'L': 1, 'N': 1, 'R': 1, 'S': 1, 'T': 1}
    # # # bingo 🙌🏾
    # # #
    # # # I am going to covert that table into a dictionary and use that to count the score, using my lambda function
    # # #
    # temp_list = list(filter(lambda char: char.isalpha(),
    #                      "A, E, I, O, U, L, N, R, S, T "))
    # # # # next I update letter_values using dictionary comprehension
    # letter_values.update({char:1 for char in temp_list})
    # temp_list = list(filter(lambda char: char.isalpha(),
    #                         "D, G"))
    # # # Let's loop instead
    letters = """A, E, I, O, U, L, N, R, S, T
    D, G
    B, C, M, P
    F, H, V, W, Y
    K
    J, X
    Q, Z"""
    letter_list = letters.splitlines()
    values = "1 2 3 4 5 8 10".split()
    values = [int(x) for x in values]
    counter = 0
    for counter in range(len(letter_list)):
        temp_list = list(filter(lambda char: char.isalpha(), letter_list[counter]))
        letter_values.update({char: values[counter] for char in temp_list})
    # # # Now I have the dictonary I needed. Let's use it
    score = 0
    for char in word:
        score += letter_values[char]
    return score

# print(score("cabbage"))
