class Luhn:
    def __init__(self, card_num):
        self.card_num = card_num # storing as astring not a number!

    def valid(self):
        clean_card_num = "" # store the clean number string here
        for char in self.card_num:
            if char.isnumeric(): # check if character is number and add it to clean_card_num
                clean_card_num = f"{clean_card_num}{char}"
            elif char == " ": # ignore spaces
                continue
            else: # if there is a character other than number return False
                return False
        if len(clean_card_num) == 1:  # Strings of length 1 or less are not valid
            return False
        Luhn_sum = 0
        j = 1
        while j <= len(clean_card_num):
            integer = int(clean_card_num[-j])
            if j % 2 == 0:
                if integer*2 < 9:
                    Luhn_sum += integer*2
                else:
                    Luhn_sum += integer*2 - 9
            else:
                Luhn_sum += integer
            j += 1
        return Luhn_sum % 10 == 0


print(Luhn("1").valid())
print(Luhn("055 444 285").valid())
print(Luhn(" 0").valid())
print(Luhn("0").valid())
print(Luhn("059a").valid())
