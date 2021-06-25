def count_words(sentence):
    # I turn the sentence into lower case
    lower_sentence = sentence.lower()
    # # Next I replace all characters that are not alphanumeric or apostrophe with spaces
    # filtered_sentence = ''.join(map(lambda x: x if x.isdigit() or x == "'" or x.isalpha() else " ", lower_sentence))
    # word_list = filtered_sentence.split()
    word_list = []
    word = ""
    j = 0
    # Let me construct the word_list myself; don't rely on string methods
    for i in range(len(lower_sentence)):
        if lower_sentence[i].isdigit() or lower_sentence[i].isalpha():
            word = f"{word}{lower_sentence[i]}"
            j = 1
        if lower_sentence[i] == "'":
            if i > 0 and i < len(lower_sentence)-1: # ignoring at the start and end of sentences
                if lower_sentence[i-1].isalpha() and lower_sentence[i+1].isalpha(): # ignoring apostrophe not between two alphabets
                    word = f"{word}{lower_sentence[i]}"
            #to ignore the apostrophe at the start and end of a word
        if (lower_sentence[i].isspace() or lower_sentence[i] == "," or lower_sentence[i] == "_") and j == 1:
            word_list.append(word)
            word = ""
            j = 0
    # to take the last word into account
    if j == 1:
        word_list.append(word)
        word = ""
        j = 0
    
    print(word_list)
    word_count = {}
    for word in word_list:
        if word in word_count:
            # If string corresponding to the word is already in our dictionary, we increase its count
            word_count[word] += 1
        else:
            # If the word is not in our dictionary we add it and assign it the value of 1 (for first occurrence)
            word_count[word] = 1
    return word_count


# used  <https://stackoverflow.com/questions/8689795/how-can-i-remove-non-ascii-characters-but-leave-periods-and-spaces>
# and <https://thispointer.com/python-how-to-use-if-else-elif-in-lambda-functions/> to learn about lambda if-else statement
# Big mistake I made was using `filter` instead of `map`
print(count_words("Joe can't tell between 'large' and large."))
print(count_words(",\n,one,\n ,two \n 'three'"))
print(count_words("one of each"))
