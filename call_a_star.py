import PathFinder
import repBack
import repForLarge
import repForSmall
import adaptiveA
from main import state, OPEN_LIST, CLOSED_LIST, GRID, clv_list
import visualization
import time

def call_a_star(a_star):
    start = time.time()
    start_s = state(None, (0, 0))
    goal_s = state(None, (10,10))
    if a_star == adaptiveA.a_star:
        start_s.h = abs(start_s.position[0] - goal_s.position[0]) + \
        abs(start_s.position[1] - goal_s.position[1])
    else:
        start_s.h = 0
    start_s.g = 0
    # initialize OPEN and CLOSED list
    OPEN_LIST.clear()
    CLOSED_LIST.clear()
    clv_list.clear()
    path, min_cost = a_star(start_s, goal_s)
    if path:
        print([s.position for s in path])
    print("min cost: " + str(min_cost))
    end = time.time()
    total_time = end - start
    print("\n" + str(total_time))


    ###Animation Call###
    vis = visualization.animated_path(GRID, clv_list, path, start_s, goal_s)
    vis.start_animation()

# call_a_star(PathFinder.a_star)
# call_a_star(repBack.a_star)
call_a_star(repForLarge.a_star)
# call_a_star(repForSmall.a_star)
# call_a_star(adaptiveA.a_star)