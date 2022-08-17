import pygame
import sys
import random
import numpy as np

from game import Game
pygame.init()

winW = 1000
winH = 1000

num_cells_x = 100
num_cells_y = 100

cell_size = winW / num_cells_x

root = pygame.display.set_mode((winW, winH))

initial_grid = np.zeros(shape=(num_cells_x, num_cells_y, 2))

initial_grid[0:5, 0:5] = [[[0, 0], [0, 1], [1, 1], [0, 2], [0, 1]], [[0, 1], [0, 3], [0,4], [1,3], [
    0,2]], [[0, 1], [1, 1], [1, 3], [1, 2], [0, 2]], [[0, 1], [0, 2], [0, 3], [0, 2], [0, 1]], [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]]

game = Game(num_cells_x, num_cells_y, initial_grid)
# print(initial_grid)

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            pass

    grid = game.get_grid()
    grid = np.repeat(np.repeat(grid, cell_size, axis=0), cell_size, axis=1)
    grid *= 255

    surf = pygame.surfarray.make_surface(grid)
    root.blit(surf, (0, 0))
    pygame.display.update()

    # game.debug()
    game.iterate()

    clock.tick(10)
