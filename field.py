
from enum import Enum


class Cell(Enum):
    current = '☺'
    unreachable = '#'
    water = 'W'
    drown = '<b>@</b>'
    x = '<b>X</b>'
    hit = '<b>$</b>'
    health = '♥'
    energy = '<b>NRJ</b>'
    star = '<b>*</b>'
    white = ''


HEIGHT = 10
WIDTH = 10


class Field:
    def __init__(self, matrices):
        self.height, self.width = HEIGHT, WIDTH
        self.matrices = matrices.matrices
        self.mat = self.matrices[0]
        self.x, self.y = 0, 0

    def get_height(self):
        return self.height

    def get_width(self):
        return self.width

    def check_left(self, symbol, current_s):
        """Specifies the remaining symbol in a tile after departing of the player or a X."""
        if current_s == Cell.hit.value:
            if symbol == Cell.current.value:
                return Cell.x.value
            if symbol == Cell.x.value:
                return Cell.current.value
            return Cell.white.value
        return Cell.white.value

    def check_moved(self, symbol, current_s, next_s):
        """Specifies the destination tile after moving of the player or a X."""
        if current_s == Cell.current.value:
            if next_s == Cell.water.value:
                return Cell.drown.value
            if next_s == Cell.x.value:
                return Cell.hit.value
            return Cell.current.value
        if current_s == Cell.x.value:
            if next_s == Cell.current.value:
                return Cell.hit.value
            return Cell.x.value
        if current_s == Cell.hit.value:
            if next_s == Cell.water.value:
                return Cell.drown.value
            if next_s == Cell.x.value:
                return Cell.hit.value
            return symbol
        return symbol

    def move_sth_up(self, place, symbol):
        """Transforms the matrix for moving whatever up."""
        if place[0] > 0:
            x = place[0]
            y = place[1]
            value = self.check_moved(symbol, self.mat[x][y], self.mat[x - 1][y])
            left = self.check_left(symbol, self.mat[x][y])
            self.mat[x - 1][y] = value
            self.mat[x][y] = left
            place[0] -= 1

    def move_sth_down(self, place, symbol):
        """Transforms the matrix for moving whatever down."""
        if place[0] < self.height - 1:
            x = place[0]
            y = place[1]
            value = self.check_moved(symbol, self.mat[x][y], self.mat[x + 1][y])
            left = self.check_left(symbol, self.mat[x][y])
            self.mat[x + 1][y] = value
            self.mat[x][y] = left
            place[0] += 1

    def move_sth_left(self, place, symbol):
        """Transforms the matrix for moving whatever left."""
        if place[1] > 0:
            x = place[0]
            y = place[1]
            value = self.check_moved(symbol, self.mat[x][y], self.mat[x][y - 1])
            left = self.check_left(symbol, self.mat[x][y])
            self.mat[x][y - 1] = value
            self.mat[x][y] = left
            place[1] -= 1

    def move_sth_right(self, place, symbol):
        """Transforms the matrix for moving whatever right."""
        if place[1] < self.width - 1:
            x = place[0]
            y = place[1]
            value = self.check_moved(symbol, self.mat[x][y], self.mat[x][y + 1])
            left = self.check_left(symbol, self.mat[x][y])
            self.mat[x][y + 1] = value
            self.mat[x][y] = left
            place[1] += 1

    def move_current_up(self):
        """Moves the player up and sets its coordinates."""
        if self.x > 0:
            current_pos = [self.x, self.y]
            self.move_sth_up(current_pos, Cell.current.value)
            self.x = current_pos[0]
            self.y = current_pos[1]

    def move_current_down(self):
        """Moves the player down and sets its coordinates."""
        if self.x < self.height - 1:
            current_pos = [self.x, self.y]
            self.move_sth_down(current_pos, Cell.current.value)
            self.x = current_pos[0]
            self.y = current_pos[1]

    def move_current_left(self):
        """Moves the player left and sets its coordinates."""
        if self.y > 0:
            current_pos = [self.x, self.y]
            self.move_sth_left(current_pos, Cell.current.value)
            self.x = current_pos[0]
            self.y = current_pos[1]

    def move_current_right(self):
        """Moves the player right and sets its coordinates."""
        if self.y < self.width - 1:
            current_pos = [self.x, self.y]
            self.move_sth_right(current_pos, Cell.current.value)
            self.x = current_pos[0]
            self.y = current_pos[1]

    def new_level(self, level):
        """Sets the matrix for a new level."""
        self.mat = self.matrices[level]
        self.x, self.y = 0, 0
