class Player:
    def __init__(self):
        self.health = 5
        self.energy = 5
        self.money = 0

    def decrease_health(self):
        if (self.health > 0):
            self.health -= 1

    def increase_health(self):
        if (self.health < 5):
            self.health += 1

    def decrease_energy(self):
        if (self.energy > 0):
            self.energy -= 1

    def increase_energy(self):
        if (self.energy < 5):
            self.energy += 1

    def increase_property(self):
        self.money += 1

    def get_money(self):
        return self.money

    def lost_money(self, loss):
        if (loss >= self.money):
            self.money = 0
        else:
            self.money -= loss

    def is_alive(self):
        return self.health > 0

    def is_rested(self):
        return self.energy > 0

    def die(self):
        self.health = 0
