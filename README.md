## Mosaic to AMPL 
This script generates a file for a given mosaic board state that contains the constrains modelled in an LP solver language like AMPL.


### Game rules
The mosaic game is played as follows:
1. There is a grid of tiles which can be either black (1) or white (0).
2. Some of the tiles on the grid contain a number which means that the sum of the adjecent squares to that tile must equal the number inside.
Note: Adjecent means up-down, left-right, diagonally and the inside tile too.

### Dependencies
In order to use the GUI of the script you need to have pygame installed.
To install pygame run the following command in your terminal:
``pip install pygame``

### Instructions
To use this script with the provided Graphical User Interface:
1. Run the ***main.py*** script.
2. With left click increment the value to the tile, with right click decrement the value of the tile.<br />
An entry of value n (1, ..., 9) means the sum of the adjecent squares must equal n.
3. When satisfied with the specified values in the tiles close the window, the constraints are saved out in the ***output.txt*** file.
4. Copy the contents of the ***output.txt*** file into your solver of choice (for example, AMPL).

### Playing mosaic
To play the mosaic board you have created with the GUI:
1. Print the board you have created to the terminal by entering ***y*** when the program prompts you.
2. Copy the board into the ***starting_pos*** variable in the ***mosaic-game.py*** script on line 73.
3. Run the ***mosaic-game.py*** script.
4. To submit the solution of the board press ***ENTER***.
5. If your solution was elligible, you see ***You won!*** in the terminal, otherwise you see ***Keep trying!***.
