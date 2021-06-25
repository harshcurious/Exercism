def rotate(text, key):
    alph_lower = ("abcdefghijklmnopqrstuvwxyz")
    alph_upper = ("abcdefghijklmnopqrstuvwxyz".upper())
    output = ''
    for char in text:
        if char in alph_lower:
            postition = alph_lower.find(char)
            output += alph_lower[(postition + key) % 26]
        elif char in alph_upper:
            postition = alph_upper.find(char)
            output += alph_upper[(postition + key) % 26]
        else:
            output += char
    return output
