from heapq import heappush, heappop
import main
import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time


start_s = None
goal_s = None
# priority queue which contains only the start state initially, keeps track of all nodes to be visited --> binary heap using python libraries
# holds tuple (f-value, s)
OPEN_LIST = []
# set that keeps track of all nodes that have already been visited --> put state s into list when expanding that node
CLOSED_LIST = set()
# array of potential actions taken by state s on grid
actions = ["up", "down", "left", "right"]
n = 101
GRID = main.generate_maze(n)
pathlist = []
counter = 0


class state():
    def __init__(self, parent=None, position=None, g=None, h=None):
        self.parent = parent
        self.position = position
        self.g = g
        self.h = h
        self.f = self.g + self.h

    def __lt__(self, other):
        return self.f < other.f

    def equals(self, other):
        return self.position == other.position


class animated_path():

    def __init__(self, maze, pathlist, color):
        self.maze = maze
        self.path = np.zeros(maze.shape, dtype = int)
        self.path = np.ma.masked_where(self.path == 0, self.path)
        self.color = color
        self.pathlist = pathlist
        self.fig, self.ax = plt.subplots()

    def animate(self, i):
        if i >= len(self.pathlist):
            print('.', end = '')
            return
        else:
            self.path[self.pathlist[i].position[0]][self.pathlist[i].position[1]] = 1
            self.ax.clear()
            plt.imshow(self.maze, alpha = 1, cmap = 'binary')
            self.im = plt.imshow(self.path, alpha = 1, cmap = self.color, animated = True)
            return self.im

    def start_animation(self, name):
        ani = animation.FuncAnimation(self.fig, self.animate, frames = len(self.path), interval = 1)
        plt.show()
        # ani.save(name)


def a_star(start_s, goal_s):

    heappush(OPEN_LIST, (start_s.f, start_s))

    while OPEN_LIST:
        global counter
        counter += 1
        # identify s with smallest f-value
        curr_f, curr_s = heappop(OPEN_LIST)
        print("iteration: " + str(counter))
        print(f"s_curr: {curr_s.position}")
        pathlist.append(curr_s)
        if curr_s.equals(goal_s):
            path = []
            s = goal_s
            while s is not None:
                path.append(s.position)
                s = s.parent
                path.reverse()
            return path, curr_s.g
        # add to close list
        CLOSED_LIST.add(curr_s)
        # for each neighbor of current node
        for a in actions:
            succ_s = succ(curr_s, a)
            print(f"succ_s: {succ_s}")
            if succ_s is None:
                continue
            else:
                new_g = curr_s.g + 1
                if succ_s.position in [s.position for s in CLOSED_LIST] and new_g >= succ_s.g:
                    continue
                if any(succ_s.position == s[1].position for s in OPEN_LIST) and new_g >= [s[1].g for s in OPEN_LIST if succ_s.position == s[1].position][0]:
                    continue
                succ_s.g = new_g
                succ_s.h = calc_h(succ_s.position, goal_s.position)
                succ_s.f = succ_s.g + succ_s.h
                if succ_s.position not in OPEN_LIST:
                    heappush(OPEN_LIST, (succ_s.f, succ_s))
                else:
                    # update priority of existing state in open list dictionary
                    for i, (f, s) in enumerate(OPEN_LIST):
                        if s.position == succ_s.position:
                            OPEN_LIST[i] = (succ_s.f, succ_s)
                            heapify(OPEN_LIST)
                            break

    print("No valid path found.")
    return None, None


# function for generating successor state s based on action a
# function for generating successor state s based on action a
def succ(curr_s, a):
    x = curr_s.position[0]
    y = curr_s.position[1]
    if a == "up" and x > 0 and GRID[x-1][y] == 0:
        succ_s = state(curr_s, (x-1, y), float('inf'), float('inf'))
        return succ_s

    elif a == "down" and x < n-1 and GRID[x+1][y] == 0:
        succ_s = state(curr_s, (x+1, y), float('inf'), float('inf'))
        return succ_s

    elif a == "left" and y > 0 and GRID[x][y-1] == 0:
        succ_s = state(curr_s, (x, y-1), float('inf'), float('inf'))
        return succ_s

    elif a == "right" and y < n-1 and GRID[x][y+1] == 0:
        succ_s = state(curr_s, (x, y+1), float('inf'), float('inf'))
        return succ_s

    return None


def calc_h(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def main():
    start_s = state(None, (0, 0), 0, 0)
    goal_s = state(None, (100,100), float('inf'), float('inf'))
    # initialize OPEN and CLOSED list
    OPEN_LIST.clear()
    CLOSED_LIST.clear()
    path, min_cost = a_star(start_s, goal_s)
    print(path)
    print("min cost: " + str(min_cost))

    # Visualize Traversal
    exploration = animated_path(GRID, pathlist, "cool")
    exploration.start_animation("test.mp4")

if __name__ == "__main__":
    main()