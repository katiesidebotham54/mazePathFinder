import heapq
import numpy as np
import random
import matplotlib.pyplot as plt

# Generate maze
n = 101
maze = generate_maze(n)

# Define heuristic function for A*


def heuristic(current, goal):
    # Use manhattan distance as heuristic
    return abs(current[0] - goal[0]) + abs(current[1] - goal[1])

# Define A* search algorithm with priority queue using BFS


def astar_bfs(maze, start, goal):
    frontier = []
    heapq.heappush(frontier, (0, start))
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0

    while frontier:
        current = heapq.heappop(frontier)[1]

        if current == goal:
            break

        for next in get_neighbors(maze, current):
            new_cost = cost_so_far[current] + 1
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost + heuristic(next, goal)
                heapq.heappush(frontier, (priority, next))
                came_from[next] = current

    return came_from, cost_so_far

# Define helper function to get neighboring nodes


def get_neighbors(maze, current):
    i, j = current
    neighbors = []
    if i > 0 and maze[i - 1][j] == 0:
        neighbors.append((i - 1, j))
    if i < len(maze) - 1 and maze[i + 1][j] == 0:
        neighbors.append((i + 1, j))
    if j > 0 and maze[i][j - 1] == 0:
        neighbors.append((i, j - 1))
    if j < len(maze) - 1 and maze[i][j + 1] == 0:
        neighbors.append((i, j + 1))
    return neighbors


# Define start and goal nodes
start = (0, 0)
goal = (n-1, n-1)

# Run A* search with priority queue using BFS
came_from, cost_so_far = astar_bfs(maze, start, goal)

# Generate path from start to goal
current = goal
path = [current]
while current != start:
    current = came_from[current]
    path.append(current)
path.reverse()

# Visualize the maze and path
fig, ax = plt.subplots()
ax.imshow(maze, cmap='binary')

for i, j in path:
    ax.text(j, i, '.', ha='center', va='center', color='r', fontsize=10)

plt.show()
