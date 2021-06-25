class Garden:
    def __init__(self, diagram, students="Alice, Bob, Charlie, David, Eve, Fred, Ginny, Harriet, Ileana, Joseph, Kincaid, Larry".split(", ")):
        self.plantsDict = {'G': "Grass", 'C': "Clover", 'R': "Radishes", 'V': "Violets"}
        self.rows = diagram.splitlines()
        self.students = sorted(students)
    def plants(self, student):
        i = self.students.index(student)
        plant_letter = [self.rows[0][2*i], self.rows[0][(2*i) +1], self.rows[1][2*i], self.rows[1][(2*i) + 1]]
        plant = [self.plantsDict[char] for char in plant_letter]
        return plant

# # # Testing
# garden = Garden("VC\nRC", ["a"])
# print(garden.plants("Alice"))
