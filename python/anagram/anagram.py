def find_anagrams(word, candidates):
    anagrams = []
    for candidate in candidates:
        # if lengths of words are unequal in length then ignore
        if len(candidate) != len(word):
            continue
        # Ignore if candidate is the same as the word
        if candidate.lower() == word.lower():
            continue
        word_list = list(word.lower())
        for char in candidate.lower():
            if char in word_list:
                word_list.remove(char)
            else:
                break
        if word_list == []:
            anagrams.append(candidate)
    return anagrams
