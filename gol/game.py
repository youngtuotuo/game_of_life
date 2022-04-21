import logging
import pygame
from pygame import (
    QUIT,
    KEYDOWN,
    K_ESCAPE,
    K_q,
    K_p,
    K_r,
)
import numpy as np
from gol.constants import (
    rows,
    cols,
    grid_size,
    start_x,
    start_y,
    gosper_glider_gun,
)
import sys


log = logging.getLogger(__name__)


class GameOfLife:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((grid_size * rows, grid_size * cols))
        self.window.fill((0, 0, 0))
        self.generation = 0
        self.start_pattern = np.array(gosper_glider_gun)
        self.grids = np.zeros((rows, cols))
        self.grids[
            start_x : start_x + self.start_pattern.shape[0],
            start_y : start_y + self.start_pattern.shape[1],
        ] = self.start_pattern
        self.run = True
        self.pause = False

    def play(self):
        self.key_press()
        self.display()

    def display(self):
        next = np.zeros((rows, cols))
        for row, col in np.ndindex(self.grids.shape):
            num_alive = (
                np.sum(self.grids[row - 1 : row + 2, col - 1 : col + 2])
                - self.grids[row, col]
            )
            if self.grids[row, col] == 1 and num_alive < 2 or num_alive > 3:
                color = (200, 200, 225) # about to die
            elif (self.grids[row, col] == 1 and 2 <= num_alive <= 3) or (
                self.grids[row, col] == 0 and num_alive == 3
            ):
                next[row, col] = 1
                color = (255, 255, 215) # alive
            color = color if self.grids[row, col] == 1 else (10, 10, 40) # die
            pygame.draw.rect(
                self.window,
                color,
                (col * grid_size, row * grid_size, grid_size - 1, grid_size - 1),
            )

        self.grids = next
        pygame.display.update()

    def pause_game(self):
        self.pause = True
        while self.pause:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.run = False
                if event.type == KEYDOWN:
                    key = event.key
                    if key == K_p:
                        self.pause = False
                    if key == K_r:
                        ...
                    if key == K_ESCAPE or key == K_q:
                        self.run = False
                        self.pause = False

    def key_press(self):
        if pygame.event.get(QUIT):
            self.run = False
        events = pygame.event.get(KEYDOWN)
        for event in events:
            key = event.key
            if key == K_ESCAPE or key == K_q:
                self.run = False
            if key == K_p:
                self.pause_game()
            if key == K_r:
                ...

    def quit(self):
        pygame.quit()
        sys.exit()
