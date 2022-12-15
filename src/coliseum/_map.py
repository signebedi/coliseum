### CHAT GPT SOLUTION ###
# from random import randint, choice

# # Define the dimensions of the maze
# MAZE_WIDTH = 100
# MAZE_HEIGHT = 100

# # Define the directions in which the algorithm can move
# directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

# # Create an empty maze
# maze = [[0] * MAZE_WIDTH for i in range(MAZE_HEIGHT)]

# # Initialize a stack to keep track of cells that have been visited
# stack = []

# # Choose a random starting cell
# current_cell = (randint(0, MAZE_WIDTH - 1), randint(0, MAZE_HEIGHT - 1))

# # Mark the starting cell as visited
# maze[current_cell[0]][current_cell[1]] = 1
# stack.append(current_cell)

# # Repeat until all cells have been visited
# while len(stack) > 0:
#     # Choose a random direction
#     direction = choice(directions)

#     # Calculate the next cell in that direction
#     next_cell = (current_cell[0] + direction[0], current_cell[1] + direction[1])

#     # Check if the next cell is within the bounds of the maze
#     if (0 <= next_cell[0] < MAZE_WIDTH and 0 <= next_cell[1] < MAZE_HEIGHT):
#         # Check if the next cell has not been visited
#         if maze[next_cell[0]][next_cell[1]] == 0:
#             # Mark the next cell as visited
#             maze[next_cell[0]][next_cell[1]] = 1
#             stack.append(next_cell)
#             current_cell = next_cell
#         else:
#             # If the next cell has been visited, remove it from the stack
#             stack.pop()

# print(maze)


###STACK OVERFLOW SOLUTION###
# https://stackoverflow.com/a/31634316/13301284
# http://rosettacode.org/wiki/Maze_generation#Python
# https://rosettacode.org/wiki/Maze_solving#Python 
# It uses the text characters for walls rather than hallways but the general concepts should still be useful.

from random import shuffle, randrange

def make_maze(w = 16, h = 8):
    vis = [[0] * w + [1] for _ in range(h)] + [[1] * (w + 1)]
    ver = [["|  "] * w + ['|'] for _ in range(h)] + [[]]
    hor = [["+--"] * w + ['+'] for _ in range(h + 1)]

    def walk(x, y):
        vis[y][x] = 1

        d = [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]
        shuffle(d)
        for (xx, yy) in d:
            if vis[yy][xx]: continue
            if xx == x: hor[max(y, yy)][x] = "+  "
            if yy == y: ver[y][max(x, xx)] = "   "
            walk(xx, yy)

    walk(randrange(w), randrange(h))
    for (a, b) in zip(hor, ver):
        print(''.join(a + ['\n'] + b))

make_maze()
