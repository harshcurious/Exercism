# Use this to create Anki cards

# print(1)
# print("\t\t\t\t\t\t\t\t\t\t".strip()=='')
# print(2)

# l = [1, 3, 3, 2, 5]
# print(sum(l))
# print(sorted((2,3)))

# from datetime import date
# import calendar

# print(type(date(2013, 5, 13).weekday()))

# my_dict = {0: "Monday", 1: "Tuesday", 2: "Wednesday",
#           3: "Thursday", 4: "Friday", 5: "Saturday", 6: "Sunday"}
# my_inverted_dict = dict(map(reversed, my_dict.items()))
# print(my_inverted_dict)
# print(calendar.monthrange(2013, 2))

# l = list("abcdefghijklmnopqrstuvwxyz")
# print(l)
# m =  list("abcdefghijklmnopqrstuvwxyz".upper())
# print(m)
# print(len(l))

# items = ["eggs", "peanuts", "shellfish", "strawberries",
#              "tomatoes", "chocolate", "pollen", "cats"]
# allergics = {items[i]:i for i in range(len(items))}
# print(allergics)

# print((0,2)+ (1,2))
# l = (0,1)
# l= l[0]+1,l[1]
# print(l)

# limit = 10
# numbers = list(range(2, limit))
# print(numbers)
# p = numbers.pop(0)
# print(p)

# alphabet = 'abcdefghijklmnopqrstuvwxyz'
# char = 'z'
# print(alphabet[-alphabet.find(char)-1])

# l = list(range(10, 100, 10))
# print(l)
# m = list(range(21, 100))
# print(m)
# print(int(22/10))
# print('_')

# import math
# l = [1, 2, 3, 4]
# print(math.prod(l))

# l = [0, 2, 2, 3, 8, 100, None, -2]
# print([i for i in l])

# legacy_data = {1: ["A", "E", "I", "O", "U"]}
# print(legacy_data.keys())

# s = "subject"
# print(s[s.find('u'):])
# p = "square"
# print(p[p.find('qu')+2:])

import secrets

r = secrets.choice(range(100, 150))
print(r)
