from heapq import heappush, heappop
import main
import random
import numpy as np
import matplotlib.pyplot as plt


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
counter = 0


class state():
    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

    def __hash__(self):
        return hash((self.parent, self.position))

    def __eq__(self, other):
        if isinstance(other, state):
            return self.parent == other.parent and self.position == other.position
        return False


def a_star(start_s, goal_s, GRID):
    g_scores[start_s] = 0
    for i in g_scores:
        print("g_value: " + str(g_scores[i]) + " this is i: " + str(i))
        print("************************")
    while OPEN_LIST:
        # identify s with smallest f-value
        curr_s = heappop(OPEN_LIST)
        for i in g_scores:
            if (i == curr_s):
                print("there exists something that matches")
        print("nothing is in there that matches")
        print(f"s_curr: {curr_s}")
        if curr_s == goal_s:
            break
        # add to close list
        CLOSED_LIST.add(curr_s)
        for a in actions:
            # look at neighboring state
            succ_s = succ(curr_s, a)
            if succ_s in CLOSED_LIST:
                continue
            # means that it's blocked
            if not succ_s:
                # set f-value to infinity
                f_scores[succ_s] = float("inf")
                # add to closed list, AKA visited
                CLOSED_LIST.add(succ_s)
                continue
            if hash(curr_s) in g_scores:
                new_g = g_scores[hash(curr_s)] + 1
            else:
                print("its not here")
            new_g = g_scores[hash(curr_s)] + 1
            if g_scores[succ_s] == float("inf") or new_g < g_scores[succ_s]:
                g_scores[succ_s] = new_g
                h_scores[succ_s] = calc_h(succ_s, s_goal)
                f_scores[succ_s] = g_scores[succ_s] + h_scores[succ_s]
                heappush(OPEN_LIST, (f_scores[succ_s], succ_s))


# function for generating successor state s based on action a
def succ(curr_s, a):
    x = curr_s[1].position[0]
    y = curr_s[1].position[1]
    for i in range(n):
        for j in range(n):
            if a == "up" and i != 0 and GRID[i-1][j] == 0:
                succ_s = state(
                    curr_s, (x-1, y))
                print("checking up neighbor")
                return succ_s
            elif a == "down" and i < n-1 and GRID[i+1][j] == 0:
                succ_s = state(
                    curr_s, (x+1, y))
                print("checking down neighbor")
                return succ_s
            elif a == "left" and j > 0 and GRID[i][j-1] == 0:
                succ_s = state(
                    curr_s, (x, y - 1))
                print("checking left neighbor")
                return succ_s
            elif a == "right" and j < n-1 and GRID[i][j+1] == 0:
                succ_s = state(
                    curr_s, (x, y + 1))
                print("checking right neighbor")
                return succ_s

    return None


def calc_h(curr_s, goal):
    # use manhattan distance
    return sum(abs(val1-val2) for val1, val2 in zip(curr_s, goal))


def main():
    print("made it here")
    s_start = state(None, (0, 0))
    s_goal = state(None, (n-1, n-1))
    g_scores[s_goal] = float("inf")

    # initialize OPEN and CLOSED list
    OPEN_LIST.clear()
    CLOSED_LIST.clear()
    heappush(OPEN_LIST, (0, s_start))
    print("running a star")
    path, min_cost = a_star(s_start, s_goal, GRID)
    if not OPEN_LIST:
        print("I cannot reach the target.")
        return
    # go back up tree using parents until reach start state
    s = s_goal
    while s != s_start:
        path.append(s)
        s = s.parent
    print("I reached the target and the min cost is: " + str(min_cost))
    # Visualize the maze and path
    fig, ax = plt.subplots()
    ax.imshow(maze, cmap='binary')

    for i, j in path:
        ax.text(j, i, '.', ha='center', va='center', color='r', fontsize=10)

    plt.show()


if __name__ == "__main__":
    main()
