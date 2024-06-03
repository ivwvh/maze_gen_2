import pygame
from generator import WALL, EMPTY, COLS, ROWS
# ИГРОК В ЛЕВОМ НИЖНЕМ УГЛУ
# ВЫХОД ИЗ ПРОГРАМЫ

class Player:
    def __init__(self) -> None:
            pass
        

class Game:
    def __init__(self,
                 maze: list[list],
                 width=None,
                 height=None,
                 ) -> None:
        pygame.init()
        self.maze = maze
        if width and height:
            self.width = width
            self.height = height
            self.screen = pygame.display.set_mode((width,
                                                   height))
        else:
            self.width = pygame.display.Info().current_w
            self.height = pygame.display.Info().current_h
            self.screen = pygame.display.set_mode(self.width, self.height,
                                                  pygame.FULLSCREEN)
        self.clock = pygame.time.Clock()
        self.tilesize = min(
            self.width // COLS,
            self.height // ROWS
        )

    def draw_maze(self) -> None:
        for i_row, row in enumerate(self.maze):
            for i_col, col in enumerate(row):
                if col == WALL:
                    pygame.draw.rect(self.screen, pygame.Color('white'),
                                     (self.tilesize * i_col,
                                      self.tilesize * i_row,
                                      self.tilesize,
                                      self.tilesize))
                if col == EMPTY:
                    pygame.draw.rect(self.screen, pygame.Color('black'),
                                     (self.tilesize * i_col,
                                      self.tilesize * i_row,
                                      self.tilesize,
                                      self.tilesize))

    def mainloop(self) -> None:
        while True:
            self.screen.fill(pygame.Color('black'))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
            self.draw_maze()
            pygame.display.flip()
            self.clock.tick(30)
