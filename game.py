from enum import Enum
from field import Cell


class State(Enum):
    running = 'running'
    paused = 'paused'
    finished = 'finished'
    quit = 'quit'


class Game:
    def __init__(self, player, fields):
        self.player = player
        self.fields = fields
        self.state = State.running
