import pygame
import sys
import numpy as np
import asyncio

from game import Game

winW = 1000
winH = 1000

pygame.init()

root = pygame.display.set_mode((winW, winH))

pygame.display.set_caption("Conway's Game of Life")
async def main():

    num_cells_x = 100
    num_cells_y = 100

    cell_size = winW / num_cells_x


    initial_grid = np.zeros(shape=(num_cells_x, num_cells_y, 2)) 

    initial_grid[0:5, 0:5] = [[[0, 0], [0, 1], [1, 1], [0, 2], [0, 1]], [[0, 1], [0, 3], [0,4], [1,3], [
        0,2]], [[0, 1], [1, 1], [1, 3], [1, 2], [0, 2]], [[0, 1], [0, 2], [0, 3], [0, 2], [0, 1]], [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]]

    game = Game(num_cells_x, num_cells_y, initial_grid)

    clock = pygame.time.Clock()

    play = False
    mouse_pos = []
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if not play:
                    # store mouse position
                    mouse_pos.append(pygame.mouse.get_pos())
                    print(mouse_pos)
                    pass
            # switch between play vs change
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    play = not play

        # initial mode
        if not play: 
            for p in mouse_pos:
                game.add(int(p[0] / cell_size), int(p[1] // cell_size))
                mouse_pos.remove(p)

        # play mode
        else:
            game.iterate()

        grid = game.get_grid()
        grid = np.repeat(np.repeat(grid, cell_size, axis=0), cell_size, axis=1)
        grid *= 255

        surf = pygame.surfarray.make_surface(grid)
        root.blit(surf, (0, 0))
        pygame.display.update()
        await asyncio.sleep(0)

        # game.debug()

        clock.tick(10)

asyncio.run(main())