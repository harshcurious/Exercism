class Clock:
    def __init__(self, hour, minute):
        # Do the floor division to deal properly  with negative numbers
        self.hour = (hour + int(minute // 60)
                     ) % 24 # if minute > 0 else (hour + int(minute / 60) - 1) % 24
        self.minute = minute % 60

    def __repr__(self):
        time = ""
        # right formating for the output string
        if self.hour < 10:
            time = f"0{self.hour}"
        else:
            time=f"{self.hour}"
        if self.minute < 10:
            time=f"{time}:0{self.minute}"
        else:
            time=f"{time}:{self.minute}"
        return time

    def __eq__(self, other):
        return self.hour == other.hour and self.minute == other.minute

    def __add__(self, minutes):
        self.hour = (self.hour + int((self.minute + minutes) // 60)) % 24
        self.minute = (self.minute + minutes) % 60
        return Clock(self.hour,self.minute)

    def __sub__(self, minutes):
        self.hour = (self.hour + int((self.minute - minutes) // 60)) % 24
        self.minute = (self.minute - minutes) % 60
        return Clock(self.hour, self.minute)


# print(str(Clock(0, 1723)))
# print(str(Clock(72, 8640)))
# print(str(Clock(-91, 0)))
# print(str(Clock(1, -160)))
# print(str(Clock(0, -59)))
# print(Clock(1, -4820))
# print(str(Clock(10, 3) - 70))
# print(str(Clock(6, 15) - 160))
print(Clock(13, 49) == Clock(-83, 49))
