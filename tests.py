
import unittest
from field import Field
from field import Cell
from player import Player
from game import Game

class FieldTest(unittest.TestCase):
    def setUp(self):
        self.field = Field()

    def test_hit(self):
        hit = Cell.hit.value
        self.assertEqual(hit, self.field.check_moved(Cell.current.value, Cell.x.value, Cell.current.value))
        self.assertEqual(hit, self.field.check_moved(Cell.current.value, Cell.current.value, Cell.x.value))
        self.assertEqual(hit, self.field.check_moved(Cell.current.value, Cell.hit.value, Cell.x.value))

    def test_after_hit(self):
        current = Cell.current.value
        x = Cell.x.value
        self.assertEqual(current, self.field.check_left(Cell.x.value, Cell.hit.value))
        self.assertEqual(x, self.field.check_left(Cell.current.value, Cell.hit.value))

    def test_drown(self):
        drown = Cell.drown.value
        self.assertEqual(drown, self.field.check_moved(Cell.drown.value, Cell.current.value, Cell.water.value))
        self.assertEqual(drown, self.field.check_moved(Cell.drown.value, Cell.hit.value, Cell.water.value))


class PlayerTest(unittest.TestCase):
    def setUp(self):
        self.player = Player()

    def test_max_energy(self):
        self.player.max_energy()
        self.asertEqual(self.player.get_energy(), 5)

    def test_max_health(self):
        self.player.max_health()
        self.asertEqual(self.player.get_health(), 5)

    def test_die(self):
        self.player.die()
        self.assertEqual(self.player.get_energy(), 0)
        self.assertEqual(self.player.get_health(), 0)

class GameTest(unittest.TestCase):
    def setUp(self):
        self.game = Game()

    def test_new_level(self):
        self.game.new_level()
        self.assertEqual(self.game.x, 0)
        self.assertEqual(self.game.y, 0)