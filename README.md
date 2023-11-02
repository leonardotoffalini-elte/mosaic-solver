## Mosaic to AMPL

This script generates a file for a given mosaic board state that contains the constraints modelled in an LP solver language like AMPL.

### Game rules

The mosaic game is played as follows:

1. There is a grid of tiles which can be either black (1) or white (0).
2. Some of the tiles on the grid contain a number which means that the sum of the adjacent black squares to that tile must equal the number inside. <br />
   ***NOTE:*** Adjacent means up-down, left-right, diagonally and the inside tile too.

### Dependencies

In order to use the GUI of the script you need to have pygame installed.
To install pygame run the following command in your terminal:
`pip install pygame`

### Instructions

To use this script with the provided Graphical User Interface:

1. Run the **_main.py_** script.
2. With left click increment the value to the tile, with right click decrement the value of the tile.<br />
   An entry of value n (1, ..., 9) means the sum of the adjacent squares must equal n.
3. When satisfied with the specified values in the tiles close the window, the constraints are saved out in the **_output.txt_** file.
4. Copy the contents of the **_output.txt_** file into your solver of choice (for example, AMPL).

### Playing mosaic

To play the mosaic board you have created with the GUI:

1. Create a board with the GUI as outlined in **Instructions**.
2. The last board you have created with the GUI will be sent to the **_mosaic-game.py_** script.
3. Run the **_mosaic-game.py_** script.
4. To submit the solution of the board press **_ENTER_**.
5. If your solution was elligible, you see **_You won!_** in the terminal, otherwise you see **_Keep trying!_**.
