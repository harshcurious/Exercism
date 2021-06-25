def is_isogram(string):
    string = string.lower()
    i = 0
    while i < len(string):
        if string[i] in [" ", "-"]:
            i += 1
            continue
        if string[i] in string[i+1:]:
            return False
        i += 1
    return True
