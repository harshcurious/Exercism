def is_pangram(sentence):
    text = sentence.lower()
    for char in "abcdefghijklmnopqrstuvwxyz":
        if char not in text:
            return False
    return True
