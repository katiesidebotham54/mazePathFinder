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
GRID = main.maze
counter = 0


class state():
    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position


def a_star():
    global counter
    counter += 1
    while OPEN_LIST:
        # identify s with smallest f-value
        curr_s = heappop(OPEN_LIST)
        print(f"s_curr: {curr_s}")
        # add to close list
        CLOSED_LIST.add(curr_s)
        for a in actions:
            # look at neighboring state
            succ_s = succ(curr_s, a)
            print(f"succ_s: {succ_s}")
            # means that it's blocked
            if not succ_s:
                # set f-value to infinity
                f_scores[succ_s] = float("inf")
                # add to closed list, AKA visited
                CLOSED_LIST.add(succ_s)
                continue
            # if the g-value of succ_s has not been initialized yet
            if search[succ_s] < counter:
                # initialize value to infinity
                g_scores[succ_s] = float("inf")
                search[succ_s] = counter
            if g_scores[succ_s] > g_scores[curr_s] + 1:
                h_scores[succ_s] = calc_h(succ_s, s_goal)
                g_scores[succ_s] = g_scores[curr_s] + 1
                f_scores[succ_s] = g_scores[succ_s] + h_scores[succ_s]
                if (f_scores[succ_s], succ_s) in OPEN_LIST:
                    OPEN_LIST.remove((f_scores[succ_s], succ_s))
                heappush(OPEN_LIST, (f_scores[succ_s], succ_s))


# function for generating successor state s based on action a
def succ(curr_s, a):
    for i in range(n):
        for j in range(n):
            print("i: " + str(i))
            if a == "up" and i != 0 and GRID[i-1][j] == 0:
                succ_s = state(
                    curr_s, (curr_s[1].position[0]-1, curr_s[1].position[1]))
                print("checking up neighbor")
                return succ_s
            elif a == "down" and i < n-1 and GRID[i+1][j] == 0:
                succ_s = state(
                    curr_s, (curr_s[1].position[0]+1, curr_s[1].position[1]))
                print("checking down neighbor")
                return succ_s
            elif a == "left" and j > 0 and GRID[i][j-1] == 0:
                succ_s = state(
                    curr_s, (curr_s[1].position[0], curr_s[1].position[1] - 1))
                print("checking left neighbor")
                return succ_s
            elif a == "right" and j < n-1 and GRID[i][j+1] == 0:
                succ_s = state(
                    curr_s, (curr_s[1].position[0], curr_s[1].position[1] + 1))
                print("checking right neighbor")
                return succ_s

    return None


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
    heappush(OPEN_LIST, (0, s_start))
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


if __name__ == "__main__":
    main()
