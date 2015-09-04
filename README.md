##StarsMaze

##About the Game

StarsMaze is a simple game for one player. The aim is to go through the levels and to collect all of the stars around the field. The field is a table with 10 
tiles in a row and 10 tiles in a column. The player must stay only in the white tiles, the blue ones are "water", in which the player "drowns". The brown tiles
cannot be reached. The start tile is in the upper left corner. The player is navigated by the arrow keys.

The player has three values - health, energy and stars. While collecting the stars, he should be carefull about the black X-es around the field. Contact with a X
decreases health by 1. Some of these disguisting things even move! Also, every ten moves decrease energy by 1 and if energy reaches 0, health decreases by
1. If health becomes 0, it is the same as the "drowning" - the game is over and lost. Fortunately, there are things around the field that increase health and energy. 
On each level, the player must collect 10 stars in order to be able to continue. Having the necessary amount, the player can reach the next level by entering the
tile in the lower right corner. One wins the game if he reaches the final tile on the last eighth level.

The game can be paused and unpaused every time by clicking 'P'.

##Running the Game

The game requires at least Python 3.4 and PyQt 5.x. It can be started by typing "python full_path" in the console where "full_path" is the full path to StarsMaze.py.