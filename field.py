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
    def __init__(self, width, height, **kwargs):
        self.current = (0, 0)
        self.width, self.height = width, height
        self.symbols = kwargs
        self.next_level = (width - 1, height - 1)

    def __get_item__(self, position):
        if position == self.current:
            return Cell.current

        if position == self.next_level:
            return Cell.next_level

        for key in self.symbols:
            if position in self.symbols[key]:
                return Cell.eval(key)

        return Cell.white

    def is_valid_position(self, position):
        x, y = position
        if x < 0 or x >= self.width:
            return False
        if y < 0 or y >= self.height:
            return False
        return True
