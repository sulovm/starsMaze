class Player:
    def __init__(self):
        self.health = 5
        self.energy = 5
        self.stars = 0
        self.STARS = 10

    def decrease_health(self):
        if (self.health > 0):
            self.health -= 1

    def increase_health(self):
        if (self.health < 10):
            self.health += 1

    def decrease_energy(self):
        if (self.energy > 0):
            self.energy -= 1

    def increase_energy(self):
        if (self.energy < 10):
            self.energy += 1

    def max_energy(self):
        self.energy = 5

    def max_health(self):
        self.health = 5

    def increase_stars(self):
        self.stars += 1

    def get_stars(self):
        return self.stars

    def lost_stars(self):
        self.stars = 0

    def get_health(self):
        return self.health

    def get_energy(self):
        return self.energy

    def is_alive(self):
        return self.health > 0

    def is_rested(self):
        return self.energy > 0

    def enough_stars(self):
        return self.stars == self.STARS

    def die(self):
        self.health = 0
        self.energy = 0
