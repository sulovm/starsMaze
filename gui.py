import sys
from game import State
from field import Cell
from matrices import Ways

from PyQt5.QtCore import Qt, QBasicTimer
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox, QGridLayout, QLabel, \
    QWidgetItem, QSpacerItem


class Tile(QLabel):
    tile_size = 35

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setFixedSize(self.tile_size, self.tile_size)
        self.setAlignment(Qt.AlignCenter)

    def setWaterStyle(self):
        self.setStyleSheet("""QLabel {
            background-color : blue;
            color : blue;
        }""")

    def setDrownedStyle(self):
        self.setStyleSheet("""QLabel {
            background-color : blue;
            color : white;
        }""")

    def setUnreachableStyle(self):
        self.setStyleSheet("""QLabel {
            background-color : brown;
            color : brown;
        }""")

    def setReachableStyle(self):
        self.setStyleSheet("""QLabel {
            background-color : white;
            color : black;
        }""")

    def setHealthStyle(self):
        self.setStyleSheet("""QLabel {
            background-color : white;
            color : red;
        }""")

    def setEnergyStarStyle(self):
        self.setStyleSheet("""QLabel {
            background-color : white;
            color : orange;
        }""")

    def setStyle(self, symbol):
        """The style of a tile depends on the coresponding symbol."""
        if symbol == Cell.water.value:
            self.setWaterStyle()
            return
        if symbol == Cell.drown.value:
            self.setDrownedStyle()
            return
        if symbol == Cell.unreachable.value:
            self.setUnreachableStyle()
            return
        if symbol == Cell.health.value:
            self.setHealthStyle()
            return
        if symbol == Cell.energy.value:
            self.setEnergyStarStyle()
            return
        if symbol == Cell.star.value:
            self.setEnergyStarStyle()
            return
        self.setReachableStyle()


class Field(QWidget):

    def __init__(self, game):
        super().__init__()
        self.init_field(game)

    def init_field(self, game):
        self.game = game
        self.ways = Ways()
        self.timer = QBasicTimer()
        self.height = self.game.field.get_height()
        self.width = self.game.field.get_width()
        self.mat = self.game.field
        grid = QGridLayout()
        self.setLayout(grid)
        grid.setSpacing(1)
        self.draw()
        self.timer.start(600, self)

    def draw(self):
        """Draws the game field each time a change occurs."""
        grid = self.layout()
        width, height = self.width, self.height
        mat = self.game.field.mat

        for i in range(height):
            for j in range(width):
                tile = Tile(str(mat[i][j]))
                tile.setStyle(mat[i][j])
                grid.addWidget(tile, i, j)

        label1 = QLabel('Health: {} Energy: {} Stars: {}'.format(
            self.game.player.get_health(),
            self.game.player.get_energy(),
            self.game.player.get_stars()))
        grid.addWidget(label1, height, 0, 1, width - 1)
        label2 = QLabel('>>')
        label2.setStyleSheet("qproperty-alignment: AlignRight;")
        grid.addWidget(label2, height, width - 1, 1, width)
        if (self.game.state is not State.running):
            lev_num = ''
        else:
            lev_num = str(self.game.level)
        label3 = QLabel('{}{}'.format(self.game.state.value, lev_num))
        grid.addWidget(label3, height + 1, 0, 1, width)

    def clear(self):
        """Removes all widgets before each drawing."""
        grid = self.layout()
        width, height = self.width, self.height

        grid.itemAt(height + 1).widget().setParent(None)
        grid.itemAt(height + width - 1).widget().setParent(None)
        grid.itemAt(height).widget().setParent(None)
        for i in reversed(range(height)):
            for j in reversed(range(width)):
                grid.itemAt(i * height + j).widget().setParent(None)


    def move_current_up(self):
        """Moves the player up and draws the new field."""
        self.game.move_current_up()
        self.clear()
        self.draw()
        if self.game.state is State.won:
            self.message(1)
        if self.game.state is State.lost:
            self.message(2)

    def move_current_down(self):
        """Moves the player down, draws the new field and checks for end of level."""
        self.game.move_current_down()
        self.clear()
        self.draw()
        if self.game.x == self.height - 1 and self.game.y == self.width - 1:
            if self.game.player.enough_stars():
                self.switch_levels()
            else:
                self.message(0)
        if self.game.state is State.won:
            self.message(1)
        if self.game.state is State.lost:
            self.message(2)

    def move_current_left(self):
        """Moves the player left and draws the new field."""
        self.game.move_current_left()
        self.clear()
        self.draw()
        if self.game.state is State.won:
            self.message(1)
        if self.game.state is State.lost:
            self.message(2)

    def move_current_right(self):
        """Moves the player right, draws the new field and checks for end of level."""
        self.game.move_current_right()
        self.clear()
        self.draw()
        if self.game.x == self.height - 1 and self.game.y == self.width - 1:
            if self.game.player.enough_stars():
                self.switch_levels()
            else:
                self.message(0)
        if self.game.state is State.won:
            self.message(1)
        if self.game.state is State.lost:
            self.message(2)

    def move_x(self, place, way):
        """Specifies the direction of moving of a X."""
        letter = way[0]
        if letter == 'u':
            self.game.move_x_up(place)
        if letter == 'd':
            self.game.move_x_down(place)
        if letter == 'l':
            self.game.move_x_left(place)
        if letter == 'r':
            self.game.move_x_right(place)
        way += letter
        way.pop(0)

    def keyPressEvent(self, event):
        if self.game.state is State.paused:
            key = event.key()
            if key == Qt.Key_P:
                self.unpause()
            else:
                super(Field, self).keyPressEvent(event)
            return
        if self.game.state is not State.running:
            super(Field, self).keyPressEvent(event)
            return
        key = event.key()
        if key == Qt.Key_Up:
            self.move_current_up()
        elif key == Qt.Key_Down:
            self.move_current_down()
        elif key == Qt.Key_Left:
            self.move_current_left()
        elif key == Qt.Key_Right:
            self.move_current_right()
        elif key == Qt.Key_P:
            self.pause()
        else:
            super(Field, self).keyPressEvent(event)

    def timerEvent(self, event):
        if self.game.state is not State.running:
            super(Field, self).timerEvent(event)
            return
        lev = self.game.level - 1
        if event.timerId() == self.timer.timerId() and self.ways.ways[lev] != []:
            for moving_x in self.ways.ways[lev]:
                self.move_x(moving_x['place'], moving_x['way'])
            self.clear()
            self.draw()
            if self.game.state is State.lost:
                self.message(2)
        else:
            super(Field, self).timerEvent(event)

    def switch_levels(self):
        self.game.new_level()
        self.mat = self.game.field
        self.clear()
        self.draw()

    def pause(self):
        self.game.pause()
        self.clear()
        self.draw()

    def unpause(self):
        self.game.unpause()
        self.clear()
        self.draw()

    def message(self, text_no):
        texts = [
            "You must collect all {} stars to continue!".format(self.game.player.STARS),
            "You win! Congratulations!",
            "Game over! Good luck next time!"]
        msgBox = QMessageBox()
        msgBox.setText(texts[text_no])
        msgBox.exec_()


class UserInterface:
    def __init__(self, game):
        self.game = game

    def main_loop(self):
        app = QApplication(sys.argv)

        w = Field(self.game)
        w.setWindowTitle('StarsMaze')
        w.show()
        app.exec_()
