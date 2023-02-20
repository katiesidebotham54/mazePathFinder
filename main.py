import random
import numpy as np
import matplotlib.pyplot as plt


def generate_maze(n):
    maze = np.zeros((n, n), dtype=int)
    visited = [[False for j in range(n)] for i in range(n)]
    stack = []

    start_i, start_j = random.randint(0, n - 1), random.randint(0, n - 1)
    visited[start_i][start_j] = True
    stack.append((start_i, start_j))

    while stack:
        i, j = stack[-1]
        unvisited_neighbours = []
        if i > 0 and not visited[i - 1][j]:
            unvisited_neighbours.append((i - 1, j))
        if i < n - 1 and not visited[i + 1][j]:
            unvisited_neighbours.append((i + 1, j))
        if j > 0 and not visited[i][j - 1]:
            unvisited_neighbours.append((i, j - 1))
        if j < n - 1 and not visited[i][j + 1]:
            unvisited_neighbours.append((i, j + 1))

        if unvisited_neighbours:
            next_i, next_j = random.choice(unvisited_neighbours)
            if random.random() < 0.7:
                visited[next_i][next_j] = True
                stack.append((next_i, next_j))
            else:
                maze[next_i][next_j] = 1
        else:
            stack.pop()

    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                start_i, start_j = i, j
                break

    stack = []
    visited = [[False for j in range(n)] for i in range(n)]
    visited[start_i][start_j] = True
    stack.append((start_i, start_j))

    while stack:
        i, j = stack[-1]
        unvisited_neighbours = []
        if i > 0 and not visited[i - 1][j]:
            unvisited_neighbours.append((i - 1, j))
        if i < n - 1 and not visited[i + 1][j]:
            unvisited_neighbours.append((i + 1, j))
        if j > 0 and not visited[i][j - 1]:
            unvisited_neighbours.append((i, j - 1))
        if j < n - 1 and not visited[i][j + 1]:
            unvisited_neighbours.append((i, j + 1))

        if unvisited_neighbours:
            next_i, next_j = random.choice(unvisited_neighbours)
            visited[next_i][next_j] = True
            stack.append((next_i, next_j))
        else:
            stack.pop()

    maze[0][0] = 0
    maze[0][1] = 0
    maze[0][2] = 1
    maze[0][3] = 1
    maze[0][4] = 0
    maze[0][5] = 0
    maze[0][6] = 0
    maze[0][7] = 0
    maze[0][8] = 1
    maze[0][9] = 0

    maze[1][0] = 0
    maze[1][1] = 0
    maze[1][2] = 0
    maze[1][3] = 1
    maze[1][4] = 0
    maze[1][5] = 0
    maze[1][6] = 1
    maze[1][7] = 0
    maze[1][8] = 1
    maze[1][9] = 0

    maze[2][0] = 0
    maze[2][1] = 1
    maze[2][2] = 0
    maze[2][3] = 0
    maze[2][4] = 1
    maze[2][5] = 0
    maze[2][6] = 1
    maze[2][7] = 0
    maze[2][8] = 1
    maze[2][9] = 0

    maze[3][0] = 0
    maze[3][1] = 0
    maze[3][2] = 0
    maze[3][3] = 0
    maze[3][4] = 0
    maze[3][5] = 0
    maze[3][6] = 1
    maze[3][7] = 0
    maze[3][8] = 1
    maze[3][9] = 0

    maze[4][0] = 0
    maze[4][1] = 1
    maze[4][2] = 1
    maze[4][3] = 0
    maze[4][4] = 0
    maze[4][5] = 0
    maze[4][6] = 1
    maze[4][7] = 0
    maze[4][8] = 0
    maze[4][9] = 0

    maze[5][0] = 0
    maze[5][1] = 1
    maze[5][2] = 0
    maze[5][3] = 0
    maze[5][4] = 0
    maze[5][5] = 0
    maze[5][6] = 1
    maze[5][7] = 0
    maze[5][8] = 0
    maze[5][9] = 0

    maze[6][0] = 0
    maze[6][1] = 0
    maze[6][2] = 0
    maze[6][3] = 0
    maze[6][4] = 0
    maze[6][5] = 0
    maze[6][6] = 0
    maze[6][7] = 0
    maze[6][8] = 0
    maze[6][9] = 0

    maze[7][0] = 0
    maze[7][1] = 1
    maze[7][2] = 0
    maze[7][3] = 0
    maze[7][4] = 0
    maze[7][5] = 0
    maze[7][6] = 0
    maze[7][7] = 0
    maze[7][8] = 0
    maze[7][9] = 0

    maze[8][0] = 0
    maze[8][1] = 0
    maze[8][2] = 1
    maze[8][3] = 0
    maze[8][4] = 0
    maze[8][5] = 0
    maze[8][6] = 0
    maze[8][7] = 0
    maze[8][8] = 1
    maze[8][9] = 0

    maze[9][0] = 0
    maze[9][1] = 0
    maze[9][2] = 0
    maze[9][3] = 0
    maze[9][4] = 1
    maze[9][5] = 0
    maze[9][6] = 1
    maze[9][7] = 0
    maze[9][8] = 0
    maze[9][9] = 0

    maze[n-1][n-1] = 0

    return maze


# n = 101
# Generate 50 mazes with size 101x101
# maze = generate_maze(n)

# # Store the mazes in a numpy array
# mazes = np.array(mazes)

# Visualize the first maze
#plt.imshow(maze, cmap='binary')
# plt.show()
