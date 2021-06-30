# this works but I was tired so this will
# works but not robust

vowel_sound = ['a', 'e', 'i', 'o', 'u', 'xr', 'yt']


def translate(text):
    sentence = text.split()
    piged = []
    vowel_start = False
    for word in sentence:
        for vowel in vowel_sound:
            if word.startswith(vowel):
                word += 'ay'
                vowel_start = True
        if not(vowel_start):
            first_vowel = 10000
            for vowel in vowel_sound:
                vowel_position = word.find(vowel)
                if vowel_position != -1 and vowel_position < first_vowel:
                    first_vowel = vowel_position
            qu_position = word.find('qu')
            y_position = word.find('y')
            if (y_position != -1 and y_position < first_vowel and y_position != 0):
                temp = f"{word[y_position:]}{word[:y_position]}ay"
                word = temp
            elif (qu_position != -1 and qu_position < first_vowel):
                temp = f"{word[qu_position+2:]}{word[:qu_position+2]}ay"
                # print(temp)
                word = temp
                # print(word)
            elif first_vowel != 0:
                temp = f"{word[first_vowel:]}{word[:first_vowel]}ay"
                word = temp
        piged.append(word)
    return ' '.join(piged)


# print(translate("apple"))
# print(translate("equal"))
# print(translate("pig"))
# print(translate("square"))
# print(translate("quick fast run"))
