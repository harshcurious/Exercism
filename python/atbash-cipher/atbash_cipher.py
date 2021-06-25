def encode(plain_text):
    lower_text = plain_text.lower()
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    counter = 0
    coded = ''
    for char in lower_text:
        if char.isalpha():
            # Reverse the alphabet
            if counter == 5:
                # Adding space every five characters
                coded += ' '
                counter = 0
            coded += alphabet[-alphabet.find(char)-1]
            counter += 1

        if char.isdigit():
            # Just print it
            if counter == 5:
                # Adding space every five characters
                coded += ' '
                counter = 0
            coded += char
            counter += 1

    return coded


def decode(ciphered_text):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    text = ''
    for char in ciphered_text:
        if char.isalpha():
            # Reverse the alphabet
            text += alphabet[-alphabet.find(char)-1]

        if char.isdigit():
            # Just print it
            text += char

    return text
