import pygame

pygame.init() 
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (122, 122, 122)

class Tile:
    def __init__(self, row:int, col:int, tile_size:int, screen):
        self.tile_size = tile_size
        self.font = pygame.font.Font('freesansbold.ttf', self.tile_size // 2)
        self.x_abs = col * self.tile_size # absolute x position
        self.y_abs = row * self.tile_size # absolute y position

        self.screen = screen

        self.x_index = col # column index
        self.y_index = row # row index

        self.color = 'dark' if (row + col) % 2 else 'light'
        self.draw_color = (220, 189, 194) if self.color == 'light' else (92, 75, 75)
        self.highlight_color = (100, 249, 83) if self.color == 'light' else (0, 200, 10)
        self.highlight = False
        self.number_color = BLACK

        self.value = None

        self.rect = pygame.Rect(
            self.x_abs,
            self.y_abs,
            self.tile_size,
            self.tile_size
        )

    def __repr__(self):
        return f'Tile at position {self.x_abs, self.y_abs}'

    def draw(self, display):
        """ Draws a rectangle for each tile and renders the image of a piece on top of the tile if applicable """
        if self.highlight:
            pygame.draw.rect(display, self.highlight_color, self.rect, 0, border_radius=5)
            pygame.draw.rect(display, BLACK, self.rect, 1, border_radius=5)
        else:
            pygame.draw.rect(display, self.draw_color, self.rect, 0, border_radius=5)
            pygame.draw.rect(display, BLACK, self.rect, 1, border_radius=5)

        if self.value is not None and self.value != -1:
            number = self.font.render(str(self.value), True, self.number_color)
            number_rect = number.get_rect(center=(self.rect.centerx, self.rect.centery))
            self.screen.blit(number, number_rect)