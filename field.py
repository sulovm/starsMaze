from enum import Enum


class Cell(Enum):
    current = '.'
    unreachable = '#'
    water = 'W'
    x = 'X'
    health = 'H'
    energy = 'E'
    star = '*'
    next_level = '>'
    white = '_'


class Field:
    def __init__(self, width, height, matrix):
        self.current = (0, 0)
        self.width, self.height = width, height
        self.matrix = matrix
        self.next_level = (width - 1, height - 1)

    def __get_item__(self, position):
        if position == self.current:
            return Cell.current

        return self.matrix[position[0]][position[1]]

    def is_valid_position(self, position):
        x, y = position
        if x < 0 or x >= self.width:
            return False
        if y < 0 or y >= self.height:
            return False
        return True
