from enum import Enum
from field import Cell


class State(Enum):
    running = 'Level: '
    paused = 'Paused'
    won = 'You win!'
    lost = 'Game over!'


class Game:
    def __init__(self, field, player):
        self.player = player
        self.field = field
        self.x, self.y = 0, 0
        self.level = 1
        self.turns = 0
        self.state = State.running

    def move_current_up(self):
        """Moves the player up and plays the turn."""
        if (self.x > 0 and
                self.field.mat[self.x - 1][self.y] != Cell.unreachable.value):
            self.turn(self.field.mat[self.x - 1][self.y])
            self.field.move_current_up()
            self.x = self.field.x
            self.y = self.field.y

    def move_current_down(self):
        """Moves the player down and plays the turn."""
        if (self.x < self.field.height - 1 and
                self.field.mat[self.x + 1][self.y] != Cell.unreachable.value):
            self.turn(self.field.mat[self.x + 1][self.y])
            self.field.move_current_down()
            self.x = self.field.x
            self.y = self.field.y

    def move_current_left(self):
        """Moves the player left and plays the turn."""
        if (self.y > 0 and
                self.field.mat[self.x][self.y - 1] != Cell.unreachable.value):
            self.turn(self.field.mat[self.x][self.y - 1])
            self.field.move_current_left()
            self.x = self.field.x
            self.y = self.field.y

    def move_current_right(self):
        """Moves the player right and plays the turn."""
        if (self.y < self.field.width - 1 and
                self.field.mat[self.x][self.y + 1] != Cell.unreachable.value):
            self.turn(self.field.mat[self.x][self.y + 1])
            self.field.move_current_right()
            self.x = self.field.x
            self.y = self.field.y

    def move_x_up(self, place):
        """Moves a X up and plays the turn."""
        if place[0] > 0:
            if self.field.mat[place[0] - 1][place[1]] == Cell.current.value:
                self.turn(Cell.x.value)
            self.field.move_sth_up(place, Cell.x.value)

    def move_x_down(self, place):
        """Moves a X down and plays the turn."""
        if place[0] < self.field.height - 1:
            if self.field.mat[place[0] + 1][place[1]] == Cell.current.value:
                self.turn(Cell.x.value)
            self.field.move_sth_down(place, Cell.x.value)

    def move_x_left(self, place):
        """Moves a X left and plays the turn."""
        if place[1] > 0:
            if self.field.mat[place[0]][place[1] - 1] == Cell.current.value:
                self.turn(Cell.x.value)
            self.field.move_sth_left(place, Cell.x.value)

    def move_x_right(self, place):
        """Moves a X right and plays the turn."""
        if place[1] < self.field.width - 1:
            if self.field.mat[place[0]][place[1] + 1] == Cell.current.value:
                self.turn(Cell.x.value)
            self.field.move_sth_right(place, Cell.x.value)

    def turn(self, symbol):
        """Specifies what to happen to the player depending on the reached tile."""
        self.turns += 1

        if symbol == Cell.x.value:
            self.player.decrease_health()
        elif symbol == Cell.energy.value:
            self.player.increase_energy()
            self.turns = 0
        elif symbol == Cell.health.value:
            self.player.increase_health()
        elif symbol == Cell.star.value:
            self.player.increase_stars()
        elif symbol == Cell.water.value:
            self.player.die()
            self.state = State.lost

        if self.turns == 10:
            self.player.decrease_energy()
            self.turns = 0
        if not self.player.is_rested():
            self.player.decrease_health()
            if self.player.is_alive():
                self.player.max_energy()
        if not self.player.is_alive():
            self.state = State.lost

    def pause(self):
        if self.state is not State.paused:
            self.state = State.paused

    def unpause(self):
        if self.state is State.paused:
            self.state = State.running

    def new_level(self):
        """Changes the level or ends the game winning."""
        if self.level > len(self.field.matrices):
            return
        if self.level == len(self.field.matrices):
            self.state = State.won
            return
        self.field.new_level(self.level)
        self.level += 1
        self.x, self.y = 0, 0
        self.player.lost_stars()
