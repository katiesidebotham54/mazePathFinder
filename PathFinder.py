from heapq import heappush, heappop
import main
<<<<<<< Updated upstream
=======
import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
>>>>>>> Stashed changes

# Global variables
# each g value is initially 1
g_scores = {}
h_scores = {}
# dict for holding all f values
f_scores = {}
s_start = None
s_goal = None
# dict for keeping track of g-values of visited nodes (to avoid repetitive g calculation)
# holds (state: counter)
search = {}
# priority queue which contains only the start state initially, keeps track of all nodes to be visited --> binary heap using python libraries
# holds tuple (f-value, s)
OPEN_LIST = []
# set that keeps track of all nodes that have already been visited --> put state s into list when expanding that node
CLOSED_LIST = set()
# array of potential actions taken by state s on grid
actions = ["up", "down", "left", "right"]
counter = 0
n = 101
GRID = main.maze
pathlist = []
counter = 0


class state():
    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position


<<<<<<< Updated upstream
def a_star():
    global counter
    counter += 1
=======
class animated_path():

	def __init__(self, maze, pathlist, color):
		self.maze = maze
		self.path = np.zeros(maze.shape, dtype = int)
		self.path = np.ma.masked_where(self.path == 0, self.path)
		self.color = color
		self.pathlist = pathlist
		self.fig, self.ax = plt.subplots()

	def animate(self, i):
		if i == len(self.pathlist):
			print( '.', end = '')
		else:
			self.path[self.pathlist[i].position[0]]\
				[self.pathlist[i].position[1]] = 1
			self.ax.clear()
			plt.imshow(self.maze, alpha = 1, cmap = 'binary')
			self.im = plt.imshow(self.path, alpha = 1, cmap = self.color, animated = True)
			return self.im

	def start_animation(self):
		self.ani = animation.FuncAnimation(self.fig, self.animate, \
			frames = len(self.path), interval = 50)
		plt.show()


def a_star(start_s, goal_s):

    heappush(OPEN_LIST, (start_s.f, start_s))

>>>>>>> Stashed changes
    while OPEN_LIST:
        # identify s with smallest f-value
<<<<<<< Updated upstream
        s_curr = heappop(OPEN_LIST)[1]
        print("item popped" + s_curr)
        # remove it from open list
        OPEN_LIST.remove(s_curr)
=======
        curr_f, curr_s = heappop(OPEN_LIST)
        print("iteration: " + str(counter))
        print(f"s_curr: {curr_s.position}")
        # found path from start to destination
        pathlist.append(curr_s)
        if curr_s.equals(goal_s):
            path = []
            s = goal_s
            while s is not None:
                path.append(s.position)
                s = s.parent
                path.reverse()
            return path, curr_s.g
>>>>>>> Stashed changes
        # add to close list
        CLOSED_LIST.add(s_curr)
        for a in actions:
            # look at neighboring state
            succ_s = succ(s_curr, a)
            # means that it's blocked
            if not succ_s:
                # set f-value to infinity
                f_scores[succ_s] = float("inf")
                # add to closed list, AKA visited
                CLOSED_LIST.add(succ_s)
            # if the g-value of succ_s has not been initialized yet
            if search[succ_s] < counter:
                # initialize value to infinity
                g_scores[succ_s] = float("inf")
                search[succ_s] = counter
            if g_scores[succ_s] > g_scores[s_curr] + 1:
                h_scores[succ_s] = calc_h(succ_s, s_goal)
                g_scores[succ_s] = g_scores[s_curr] + 1
                f_scores[succ_s] = g_scores[succ_s] + h_scores[succ_s]
                if (f_scores[succ_s], succ_s) in OPEN_LIST:
                    OPEN_LIST.remove((f_scores[succ_s], succ_s))
                heappush(OPEN_LIST, (f_scores[succ_s], succ_s))


# function for generating successor state s based on action a
def succ(curr_s, a):
    for i in range(n):
        for j in range(n):
            if a == "up" and i > 0 and GRID[i-1][j] == 0:
                succ_s = state(
                    curr_s, (curr_s.position[0]-1, curr_s.position[1]))
            elif a == "down" and i < n-1 and GRID[i+1][j] == 0:
                succ_s = state(
                    curr_s, (curr_s.position[0]+1, curr_s.position[1]))
            elif a == "left" and j > 0 and GRID[i][j-1] == 0:
                succ_s = state(
                    curr_s, (curr_s.position[0], curr_s.position[1] - 1))
            elif j < n-1 and GRID[i][j+1] == 0:
                succ_s = state(
                    curr_s, (curr_s.position[0], curr_s.position[1] + 1))
            else:
                return None
    return succ_s


def calc_h(curr_s, goal):
    # use manhattan distance
    return sum(abs(val1-val2) for val1, val2 in zip(curr_s, goal))


def main():
    print("made it here")
    counter = 0
    s_start = state(None, (0, 0))
    s_goal = state(None, (40, 80))
    # initialize before putting into open list
    g_scores[s_start] = 0
    # initialize start and goal states to counter (0)
    search[s_start] = counter
    search[s_goal] = counter
    g_scores[s_goal] = float("inf")

    # initialize OPEN and CLOSED list
    OPEN_LIST.clear()
    CLOSED_LIST.clear()
<<<<<<< Updated upstream
    heappush(OPEN_LIST, (0, s_start))
    for element in OPEN_LIST:
        print(element)
    print("running a star")
    a_star()
    if not OPEN_LIST:
        print("I cannot reach the target.")
        return
    # go back up tree using parents until reach start state
    path = []
    s = s_goal
    while s != s_start:
        path.append(s)
        s = s.parent
    print("I reached the target.")
    return path[::-1]  # Return reversed path
=======
    path, min_cost = a_star(start_s, goal_s)
    print(path)
    # Visualize Traversal
    exploration = animated_path(GRID, pathlist, "cool")
    exploration.start_animation()
    print("min cost: " + str(min_cost))
>>>>>>> Stashed changes


if __name__ == "__main__":
    main()
