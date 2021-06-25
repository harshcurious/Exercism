# Globals for the directions
# Change the values as you see fit
EAST = 0
NORTH = 1
WEST = 2
SOUTH = 3


class Robot:
    def __init__(self, direction=NORTH, x=0, y=0):
        self.direction = direction
        self.coordinates = x, y

    def _turn(self, turn):
        # Left turn --> increase direction value by 1 up to mod 4
        # Right turn --> decrease direction value by 1 up to mod 4
        if turn == 'L':
            self.direction += 1
        elif turn == 'R':
            self.direction -= 1
        else:
            raise ValueError("Wrong Move: ", turn)
        self.direction = self.direction % 4

    def _advance_once(self):
        if self.direction == EAST:
            # x+1
            self.coordinates = self.coordinates[0]+1, self.coordinates[1]
        elif self.direction == NORTH:
            # y+1
            self.coordinates = self.coordinates[0], self.coordinates[1]+1
        elif self.direction == WEST:
            # x-1
            self.coordinates = self.coordinates[0]-1, self.coordinates[1]
        elif self.direction == SOUTH:
            # y-1
            self.coordinates = self.coordinates[0], self.coordinates[1]-1
        else:
            raise ValueError(self.direction)

    def move(self, string):
        for char in string:
            if char == 'A':
                self._advance_once()
            else:
                self._turn(char)


# Testing
# robot = Robot(NORTH, 0, 0)
# print(robot.coordinates)

# Ideal solution will use the imaginary numbers
