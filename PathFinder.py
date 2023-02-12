from heapq import heappush, heappop
import main

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
tree = {}


class s():
    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position


def ComputePath():
    global counter
    counter += 1
    # while g-value to get to goal is greater than the min f-value in open list
    while g_scores[s_goal] > min(f_scores[s] for s in OPEN_LIST):
        # identify s with smallest f-value
        s = heappop(OPEN_LIST, key=lambda s: f_scores[s])
        # remove it from open list
        OPEN_LIST.remove(s)
        # add to close list
        CLOSED_LIST.add(s)
        # expand state s for all possible successor states
        # check if it is in closed list or an obstacle then ignore it
        # otherwise add it to open list
        for a in actions(s):
            if search[succ(s, a)] < counter:
                # initialize value to infinity
                g_scores[succ(s, a)] = float("inf")
                search[succ(s, a)] = counter
            if g_scores[succ(s, a)] > g_scores[s] + cost(s, a):
                g_scores[succ(s, a)] = g_scores[s] + cost(s, a)
                tree[succ(s, a)] = s
                if succ(s, a) in OPEN_LIST:
                    OPEN_LIST.remove(succ(s, a))
                heappush(OPEN_LIST, (g_scores[succ(s, a)] +
                         h_scores[succ(s, a)], succ(s, a)))

# function for generating successor state s based on action a
# should return a state


def succ(curr_s, a):
    for i in range(n):
        for j in range(n):
            if a == "up" and i > 0:
                succ_s = s(curr_s, (curr_s.position[0]-1, curr_s.position[1]))
            elif a == "down" and i < n-1:
                succ_s = s(curr_s, (curr_s.position[0]+1, curr_s.position[1]))
            elif a == "left" and j > 0:
                succ_s = s(
                    curr_s, (curr_s.position[0], curr_s.position[1] - 1))
            elif j < n-1:
                succ_s = s(
                    curr_s, (curr_s.position[0], curr_s.position[1] + 1))
    return succ_s


def calc_h(start, goal):
    # use manhattan distance
    return sum(abs(val1-val2) for val1, val2 in zip(start, goal))


def Main():
    # initialize all states s to 0
    for s in states:
        search[s] = 0
    s_start = s(None, (0, 0))
    s_goal = s(None, (40, 80))

    # while we have not reached the path from start --> goal
    while s_start != s_goal:
        # initialize before putting into open list
        g_scores[s_start] = 0
        search[s_start] = counter
        # initialize each time for A* search to check for terminating condition
        g_scores[s_goal] = float("inf")
        search[s_goal] = counter
        print("g_scores" + g_scores)
        print("search" + search)
        # initialize OPEN and CLOSED list
        OPEN_LIST.clear()
        CLOSED_LIST.clear()
        # push start state into open list
        heappush(OPEN_LIST, (0, s_start))
        ComputePath()
        if not OPEN_LIST:
            print("I cannot reach the target.")
            return

    path = []
    s = s_goal
    while s != s_start:
        path.append(s)
        s = s.parent
    print("I reached the target.")
    return path[::-1]  # Return reversed path
