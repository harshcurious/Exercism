class School:
    def __init__(self):
        self.student_dict = {}
        for i in range(10):
            self.student_dict[i] = []

    def add_student(self, name, grade):
        self.student_dict[grade].append(name)

    def roster(self):
        rost = []
        for i in range(10):
            if self.student_dict[i] != []:
                rost.extend(sorted(self.student_dict[i]))
        return rost

    def grade(self, grade_number):
        return sorted(self.student_dict[grade_number])

# # # Testing
# school = School()
# school.add_student(name="Franklin", grade=5)
# school.add_student(name="Bradley", grade=5)
# school.add_student(name="Jeff", grade=1)
# print(school.grade(5))
# print(school.roster())

#  Defaultdict is a container like dictionaries present in the module collections. Defaultdict is a sub-class of the dict class that returns a dictionary-like object. The functionality of both dictionaries and defualtdict are almost same except for the fact that defualtdict never raises a KeyError. It provides a default value for the key that does not exists.

# https://exercism.io/tracks/python/exercises/grade-school/solutions/296036cc615e43c2976863636bea0a1d is an excellent solution avoiding the loop in __init__
