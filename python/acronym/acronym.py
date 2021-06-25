def abbreviate(words):
    # Step 1: clean the `words` so that you have nothing but alphbets and apostrophe; replace everything else by a space (_, & etc can be used as word separator)
    mod_words = ''.join(map(lambda x: x if x.isalpha() or x == "'" else " ", words))
    # Step 2 : turn it into a list of words
    word_ls = mod_words.split()
    # Step 3: initialize the variable `acronym` as an empty string. This deals with the case when the empty string is an input to the function
    acronym = ""
    # Step 4: Loop ove all the words in your list, and choose (while capitalizing) the first letter of the word
    for word in word_ls:
        if word[0] != "'":
            acronym = f"{acronym}{word[0].upper()}"
        else:
            # this whole if-else is unnecessary for the solution, but I wanted something more robust
            for i in range(len(word)):
                if word[i] != "'":
                    acronym = f"{acronym}{word[i].upper()}"
                    break
    return acronym

# # # checking...
# print(abbreviate("Complementary metal-oxide semiconductor"))
