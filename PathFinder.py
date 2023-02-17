from heapq import heappush, heappop
import main
import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from IPython import display
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
n = 11
GRID = main.generate_maze(n)
clv_list = []
counter = 0


class state():
    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position
        self.g = float('inf')
        self.h = float('inf')
        self.f = self.g + self.h

    def __eq__(self, other):
        return self.position == other.position

    def __hash__(self):
        return hash(self.position)

    def __lt__(self, other):
        return self.f < other.f

class animated_path():

    def __init__(self, maze, clv_list, pv_list, start_s, goal_s):

        #Goal & Start States
        self.goal_s = goal_s
        self.start_s = start_s

        #Layer 0: Start State Visualization
        self.ssv = np.zeros(maze.shape, dtype = int)
        self.ssv = np.ma.masked_where(self.ssv == 0, self.ssv)
        self.ssv[self.start_s.position[0]][self.start_s.position[1]] = 1

        #Layer 1: Maze (AKA GRID) Visualization
        self.maze = maze

        #Layer 2: Closed List Visualization
        self.clv = np.zeros(maze.shape, dtype = int)
        self.clv = np.ma.masked_where(self.clv == 0, self.clv)

        #Layer 3: Path Visualization
        self.pv = np.zeros(maze.shape, dtype = int)
        self.pv = np.ma.masked_where(self.pv == 0, self.pv)

        #Layer 4: Goal State Visualization
        self.gsv = np.zeros(maze.shape, dtype = int)
        self.gsv = np.ma.masked_where(self.gsv == 0, self.gsv)
        self.gsv[self.goal_s.position[0]][self.goal_s.position[1]] = 1

        #Closed List
        self.clv_list = clv_list

        #Path List
        if pv_list:
            self.pv_list = pv_list
        else:
            self.pv_list = []

        #Figure & Axis Init
        self.fig, self.ax = plt.subplots()

    def animate(self, i):

        self.ax.clear()

        if i < len(self.clv_list):

            self.clv[self.clv_list[i].position[0]][self.clv_list[i].position[1]] = 1 #Update clv with searched states

        elif i - len(self.clv_list) < len(self.pv_list):

            i -= len(self.clv_list) 
            self.pv[self.pv_list[i].position[0]][self.pv_list[i].position[1]] = 1 #Update pv with path states

        else:
            print('.', end = '')
            return

        #Show All Layers
        plt.imshow(self.maze, alpha = 1, cmap = 'Greys')
        plt.imshow(self.clv, alpha = .5, cmap = 'tab20c')
        plt.imshow(self.pv, alpha = .5, cmap = 'summer')
        plt.imshow(self.ssv, alpha = .5, cmap = 'cool')
        plt.imshow(self.gsv, alpha = .5, cmap = 'autumn')

    def start_animation(self):
        anim = animation.FuncAnimation(self.fig, self.animate, frames = len(self.clv_list) + len(self.pv_list), interval = 1)
        plt.show()

def a_star(start_s, goal_s):

    heappush(OPEN_LIST, (start_s.f, start_s))

    while OPEN_LIST:
        global counter
        counter += 1
        # identify s with smallest f-value
        curr_f, curr_s = heappop(OPEN_LIST)
        CLOSED_LIST.add(curr_s)
        print("iteration: " + str(counter))
        print(f"s_curr: {curr_s}")
        clv_list.append(curr_s)
        # found path from start to destination
        if curr_s == goal_s:
            print("curr is it!")
            return create_path(curr_s)
        # for each neighbor of current node
        for a in actions:
            succ_s = succ(curr_s, a)
            print(f"succ_s: {succ_s}")
            if succ_s is None:
                continue
            else:
                print(f"succ_s: {succ_s}")
                print(f"s_curr: {succ_s.position}")
                new_g = curr_s.g + 1
                for closed_s in CLOSED_LIST:
                    if closed_s == succ_s:
                        break
                else:
                    succ_s.g = new_g
                    succ_s.h = calc_h(succ_s.position, goal_s.position)
                    succ_s.f = succ_s.g + succ_s.h
                    for open_s in OPEN_LIST:
                        if open_s[1] == succ_s:
                            if open_s[0] > succ_s.f:
                                OPEN_LIST.remove(open_s)
                                heappush(OPEN_LIST, (succ_s.f, succ_s))
                            break
                    else:
                        heappush(OPEN_LIST, (succ_s.f, succ_s))
    print("No valid path found.")
    return None, None


def create_path(curr_s):
    path = []
    s = curr_s
    while s is not None:
        path.append(s)
        s = s.parent
    path.reverse()
    return path, curr_s.g

# function for generating successor state s based on action a


def succ(curr_s, a):
    x = curr_s.position[0]
    y = curr_s.position[1]
    if a == "up" and x > 0 and GRID[x-1][y] == 0:
        succ_s = state(curr_s, (x-1, y))
        return succ_s

    elif a == "down" and x < n-1 and GRID[x+1][y] == 0:
        succ_s = state(curr_s, (x+1, y))
        return succ_s

    elif a == "left" and y > 0 and GRID[x][y-1] == 0:
        succ_s = state(curr_s, (x, y-1))
        return succ_s

    elif a == "right" and y < n-1 and GRID[x][y+1] == 0:
        succ_s = state(curr_s, (x, y+1))
        return succ_s

    return None


def calc_h(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def main():
    start_s = state(None, (0, 0))
    start_s.h = start_s.g = 0
    goal_s = state(None, (9,9))
    # initialize OPEN and CLOSED list
    OPEN_LIST.clear()
    CLOSED_LIST.clear()
    path, min_cost = a_star(start_s, goal_s)
    if path:
        print([s.position for s in path])
    print("min cost: " + str(min_cost))

    ###Animation Call###
    visualization = animated_path(GRID, clv_list, path, start_s, goal_s)
    visualization.start_animation()


if __name__ == "__main__":
    main()
