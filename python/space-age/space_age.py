import math


def round_half_up(n, decimals=0):
    # Defined this because the default `round()` is an even round, i.e. round up/down to even numbers
    # Using the default round does not affect the solution
    multiplier = 10 ** decimals
    return math.floor(n*multiplier + 0.5) / multiplier


orb_period = {'earth': 1, 'mercury': 0.2408467,
              'venus': 0.61519726, 'mars': 1.8808158, 'jupiter': 11.862615, 'saturn': 29.447498, 'uranus': 84.016846, 'neptune': 164.79132}


class SpaceAge:
    def __init__(self, seconds):
        self.seconds = seconds

    def on_earth(self):
        return round_half_up(self.seconds/31557600, 2)

    def on_mercury(self):
        return round_half_up((self.seconds/31557600)/orb_period['mercury'], 2)

    def on_venus(self):
        return round_half_up((self.seconds/31557600)/orb_period['venus'], 2)

    def on_mars(self):
        return round_half_up((self.seconds/31557600)/orb_period['mars'], 2)

    def on_jupiter(self):
        return round_half_up((self.seconds/31557600)/orb_period['jupiter'], 2)

    def on_saturn(self):
        return round_half_up((self.seconds/31557600)/orb_period['saturn'], 2)

    def on_uranus(self):
        return round_half_up((self.seconds/31557600)/orb_period['uranus'], 2)

    def on_neptune(self):
        return round_half_up((self.seconds/31557600)/orb_period['neptune'], 2)
