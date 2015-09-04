from field import Field
from player import Player
from matrices import Matrices
from game import Game
import gui

def main():
    matrices = Matrices()
    field = Field(matrices)
    player = Player()
    game = Game(field, player)

    ui = gui.UserInterface(game)

    ui.main_loop()

if __name__ == '__main__':
    main()
