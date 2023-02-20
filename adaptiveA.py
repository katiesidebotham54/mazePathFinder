from heapq import heappush, heappop
from main import n, GRID, state, actions, OPEN_LIST, CLOSED_LIST, clv_list


class forstate(state):
    # define additional comparison to account for same f-values
    # favors higher g-values
    def __lt__(self, other):
        if self.f == other.f:
            return self.g > other.g
        return self.f < other.f


def a_star(start_s, goal_s):
    c = -1  # constant c to account for states with same f-values
    # push start node into OPEN_LIST
    heappush(OPEN_LIST, (c*start_s.f-start_s.g, start_s))
    g_values = {}  # keep track of the g-values of expanded states
    min_cost = float('inf')  # initailize min_cost variable

    while OPEN_LIST:
        # identify s with smallest f-value and pop from OPEN_LIST
        curr_f, curr_s = heappop(OPEN_LIST)
        CLOSED_LIST.add(curr_s)  # expand state by putting it in CLOSED_LIST
        clv_list.append(curr_s)
        # update the g-value dictionary with the expanded state
        g_values[curr_s] = curr_s.g
        # if path found from start to destination
        if curr_s == goal_s:
            if curr_s.g < min_cost:
                min_cost = curr_s.g
            return create_path(curr_s)  # return path to terminal
        # for each neighbor of current node
        for a in actions:
            # create neighbor state
            succ_s = succ(curr_s, a)
            if succ_s is None:  # not a valid node due to gridworld boundaries or obstacle
                continue
            # update the h-value if a lower g-value is found
            if succ_s in g_values and g_values[succ_s] <= curr_s.g:
                continue
            else:
                succ_s.g = curr_s.g + 1
                succ_s.h = heuristic(succ_s.position, goal_s.position)
                succ_s.f = succ_s.g + succ_s.h
                for open_f, open_s in OPEN_LIST:
                    if open_s == succ_s and open_f <= succ_s.f:
                        break
                else:
                    heappush(OPEN_LIST, (c*succ_s.f-succ_s.g, succ_s))
        # adaptively update the h-values of states in the OPEN_LIST
        for i in range(len(OPEN_LIST)):
            open_f, open_s = OPEN_LIST[i]
            if open_s not in g_values:
                continue
            new_h = heuristic(open_s.position, goal_s.position) + \
                g_values[open_s] - start_s.g
            if new_h < open_s.h:
                OPEN_LIST[i] = (open_s.g + new_h, open_s)
                heapify(OPEN_LIST)
    if min_cost == float('inf'):
        # print("No valid path found.")
        return None, None

# function for creating path from goal state to start state based on corresponding parent of curr_s


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
        succ_s = forstate(curr_s, (x-1, y))
        return succ_s

    elif a == "down" and x < n-1 and GRID[x+1][y] == 0:
        succ_s = forstate(curr_s, (x+1, y))
        return succ_s

    elif a == "left" and y > 0 and GRID[x][y-1] == 0:
        succ_s = forstate(curr_s, (x, y-1))
        return succ_s

    elif a == "right" and y < n-1 and GRID[x][y+1] == 0:
        succ_s = forstate(curr_s, (x, y+1))
        return succ_s

    return None


def calc_h(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def heuristic(pos, goal):
    return calc_h(pos, goal)
