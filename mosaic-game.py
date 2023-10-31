import pygame
from board import Board
from tile import BLACK, WHITE, GREY
import numpy as np
from main import player_made_board

pygame.init()

class Game:
    def __init__(self, starting_pos):
        self.display = pygame.display.set_mode((600, 600), pygame.RESIZABLE)
        self.board = Board(self.display, board=starting_pos)
        self.starting_pos = starting_pos
        self.running = True
        for tile in self.board.tiles_list:
            tile.draw_color = GREY

    
    def _draw(self):
        self.board.draw(self.display)


    def main(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.board.handle_click(event.pos[0], event.pos[1], event.button, game=True)
                if event.type == pygame.VIDEORESIZE:
                    self.screen = pygame.display.set_mode((event.w, event.w), pygame.RESIZABLE)
                    self.board.board_size = self.screen.get_width()
                    self.board.tile_size = self.board.board_size // self.board.num_tiles
                    self.board.tiles_list = self.board._generate_tiles()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        valid_solution = self.count_adjecent()
                        if valid_solution:
                            print('You won!')
                            self.running = False
                        else:
                            print('Keep trying!')

            self._draw()
            pygame.display.update()
        pygame.quit()

    
    def count_adjecent(self):
        mtx = np.array(self.board.tiles_list)
        mtx.shape = (self.board.num_tiles, self.board.num_tiles)

        for i in range(self.board.num_tiles):
            for j in range(self.board.num_tiles):
                if self.board.board[i][j] == -1:
                    continue
                count = 0
                for k in range(-1, 2):
                    for l in range(-1, 2):
                        if -1 < (i+k) and (i+k) < self.board.num_tiles and -1 < (j+l) and (j+l) < self.board.num_tiles:
                            if mtx[i+k][j+l].draw_color == BLACK:
                                count += 1
                if not count == self.board.board[i][j]:
                    return False
        return True


def main():
    try:
        starting_pos = player_made_board
    except:
        starting_pos = [[3, -1, -1, 2, 1], [-1, -1, -1, 2, -1], [-1, -1, 1, -1, 3], [-1, 2, 4, 4, -1], [-1, -1, -1, -1, -1]]
    newGame = Game(starting_pos)
    newGame.main()

if __name__ == '__main__':
    main()
    