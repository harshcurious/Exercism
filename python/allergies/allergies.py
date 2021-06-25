class Allergies:
    # items = ["eggs", "peanuts", "shellfish", "strawberries"
    #          "tomatoes", "chocolate", "pollen", "cats"]
    # allergics = {Allergies.items[i]: i for i in range(len(Allergies.items))}
    allergics = {'eggs': 0, 'peanuts': 1, 'shellfish': 2, 'strawberries': 3,
                 'tomatoes': 4, 'chocolate': 5, 'pollen': 6, 'cats': 7}

    def __init__(self, score):
        self.score = score

    def allergic_to(self, item):
        num = bin(self.score)
        binstr = str(num)
        if len(binstr) < Allergies.allergics[item] + 1:
            return False
        if binstr[-1-Allergies.allergics[item]] == '1':
            return True
        else:
            return False

    @property
    def lst(self):
        output = []
        for item in Allergies.allergics.keys():
            if self.allergic_to(item):
                output.append(item)
        return output
