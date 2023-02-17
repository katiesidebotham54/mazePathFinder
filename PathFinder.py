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
Fake_Closed_List = []
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

    def __init__(self, maze, clv_list, pv_list):

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

        #Closed List
        self.clv_list = clv_list

        #Path List
        self.pv_list = pv_list

        #Figure & Axis Init
        self.fig, self.ax = plt.subplots()

    def update_pv(self, i):

        i -= len(self.clv_list)

        self.pv[self.pv_list[i].position[0]][self.pv_list[i].position[1]] = 1

    def update_clv(self, i):

        self.clv[self.clv_list[i].position[0]][self.clv_list[i].position[1]] = 1

    def update_gsv(self, i):

        self.gsv[self.clv_list[i].position[0]][self.clv_list[i].position[1]] = 1

    def animate(self, i):

        if i >= len(self.clv_list) + len(self.pv_list):
            print('.', end = '')
            return

        elif i >= len(self.clv_list):
            self.update_path(i)

        elif i == (len(self.clv_list) - 1):
            self.update_gsv(i)

        else:
            self.update_clv(i)

        #Show All Layers
        self.ax.clear() 
        plt.imshow(self.maze, alpha = 1, cmap = 'binary')
        plt.imshow(self.clv, alpha = 1, cmap = 'cool')
        plt.imshow(self.pv, alpha = 1, cmap = 'summer')
        plt.imshow(self.gsv, alpha = 1, cmap = 'spring')

    def start_animation(self):
        anim = animation.FuncAnimation(self.fig, self.animate, frames = len(self.clv_list), interval = 50)
        plt.show()

def a_star(start_s, goal_s):

    heappush(OPEN_LIST, (start_s.f, start_s))

    while OPEN_LIST:
        global counter
        counter += 1
        # identify s with smallest f-value
        curr_f, curr_s = heappop(OPEN_LIST)
        print("iteration: " + str(counter))
        print(f"s_curr: {curr_s.position}")
        Fake_Closed_List.append(curr_s)
        if curr_s.equals(goal_s):
            path = []
            s = curr_s
            while s is not None:
                path.append(s)
                s = s.parent
            path.reverse()  
            return path, curr_s.g
        # add to close list
        CLOSED_LIST.add(curr_s)
        # for each neighbor of current node
        for a in actions:
            succ_s = succ(curr_s, a)
            if succ_s is None:
                print(f"succ_s: {succ_s}")
                continue
            else:
                print(f"succ_s: {succ_s.position}")
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
    goal_s = state(None, (2,3), float('inf'), float('inf'))
    # initialize OPEN and CLOSED list
    OPEN_LIST.clear()
    CLOSED_LIST.clear()
    path, min_cost = a_star(start_s, goal_s)
    if path:
        print([s.position for s in path])
    else:
        print(path)
    print("min cost: " + str(min_cost))

    # Visualize Closed List
    exploration = animated_path(GRID, Fake_Closed_List, path)
    exploration.start_animation()

    # Visualize Path
    # path_vis = animated_path(GRID, path)
    # path_vis.start_animation()


if __name__ == "__main__":
    main()