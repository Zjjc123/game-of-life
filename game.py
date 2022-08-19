import numpy as np

class Game:
    def __init__(self, x, y, initial=[]):
        # [alive, neighbors]
        self.x = x
        self.y = y
        if len(initial) == 0:
            self.grid = np.zeros(shape=(x, y, 2))
        else:
            self.grid = initial

    def iterate(self):
        next_grid = np.zeros(shape=(self.x + 2, self.y + 2, 2))
        for x in range(1, self.x + 1):
            for y in range(1, self.y + 1):
                # corresponding cell
                cell = self.grid[x - 1][y - 1]

                # live
                if cell[0] == 1 and cell[1] > 1 and cell[1] < 4:
                    self.add_next(next_grid, x, y)

                # reproduction
                elif cell[0] == 0 and cell[1] == 3:
                    self.add_next(next_grid, x, y)

        self.grid = next_grid[1:self.x+1, 1:self.y+1]

    def add(self, x, y):
        self.grid[x][y][0] = 1
        # update neighbors
        for i in range(x-1, x+2):
            for j in range(y-1, y+2):
                if i != x or j != y:
                    self.grid[i][j][1] += 1

    def add_next(self, next_grid, x, y):
        next_grid[x][y][0] = 1

        # update neighbors
        for i in range(x-1, x+2):
            for j in range(y-1, y+2):
                if i != x or j != y:
                    next_grid[i][j][1] += 1

    def get_grid(self):
        return self.grid[:, :, 0]

    def debug(self):
        print(self.grid)
