# I completely don't understand what they are talking about. What am I supposed to implement. I am confused. What is key???
# <http://pi.math.cornell.edu/~mec/2003-2004/cryptography/polyalpha/polyalpha.html>
# has the best explanation of this cipher
import string
import secrets


class Cipher:
    letters = string.ascii_lowercase

    def __init__(self, key=None):
        if key != None:
            self.key = key
        else:
            r = secrets.choice(range(100, 150))
            self.key = ''.join(secrets.choice(Cipher.letters)
                               for i in range(r))
            # Double randomness

    def char_encoding(self, char, i):
        if i >= len(self.key):
            i = i % len(self.key)
        point = (Cipher.letters.find(char) +
                 Cipher.letters.find(self.key[i])) % len(Cipher.letters)
        return Cipher.letters[point]

    def char_decoding(self, char, i):
        if i >= len(self.key):
            i = i % len(self.key)
        point = (Cipher.letters.find(char) -
                 Cipher.letters.find(self.key[i])) % len(Cipher.letters)
        return Cipher.letters[point]

    def encode(self, text):
        encoded = ''
        for i in range(len(text)):
            if text[i].islower() and text[i].isascii():
                encoded += self.char_encoding(text[i], i)
            else:
                # Don't change anything if the character is not lowercase alphabet
                encoded += text[i]
        return encoded

    def decode(self, text):
        decoded = ''
        for i in range(len(text)):
            if text[i].islower() and text[i].isascii():
                decoded += self.char_decoding(text[i], i)
            else:
                # Don't change anything if the character is not lowercase alphabet
                decoded += text[i]
        return decoded
