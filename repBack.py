from heapq import heappush, heappop
from main import n
from main import maze
from main import state
from main import actions
import numpy as np
import matplotlib.pyplot as plt
import time

start_s = None
goal_s = None
# priority queue which contains only the start state initially, 
# keeps track of all nodes to be visited --> binary heap using python libraries
# holds tuple (f-value, s)
OPEN_LIST = []
# set that keeps track of all nodes that have already been visited --> 
# put state s into list when expanding that node
CLOSED_LIST = set()
# array of potential actions taken by state s on grid
actions = ["up", "down", "left", "right"]
GRID = maze

def a_star(goal_s, start_s):

    heappush(OPEN_LIST, (goal_s.f, goal_s))

    while OPEN_LIST:
        # identify s with smallest f-value
        curr_f, curr_s = heappop(OPEN_LIST)
        CLOSED_LIST.add(curr_s)
        # found path from start to destination
        if curr_s == start_s:
            return create_path(curr_s)
        # for each neighbor of current node
        for a in actions:
            succ_s = succ(curr_s, a)
            if succ_s is None:
                continue
            else:
                new_g = curr_s.g + 1
                for closed_s in CLOSED_LIST:
                    if closed_s == succ_s:
                        break
                else:
                    succ_s.g = new_g
                    succ_s.h = calc_h(succ_s.position, start_s.position)
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
        path.append(s.position)
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
    return abs(b[0] - a[0]) + abs(b[1] - a[1])


def main():
    start = time.time()
    start_s = state(None, (0, 0))
    goal_s = state(None, (4, 4))
    goal_s.h = goal_s.g = 0

    # initialize OPEN and CLOSED list
    OPEN_LIST.clear()
    CLOSED_LIST.clear()
    path, min_cost = a_star(goal_s, start_s)
    print(path)
    print("min cost: " + str(min_cost))
    end = time.time()
    total_time = end - start
    print("\n" + str(total_time))


if __name__ == "__main__":
    main()
