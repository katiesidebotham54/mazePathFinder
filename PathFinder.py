def man_dist(n1, n2):

	return n1[0] - n2[0] + n1[1] - n2[1] # (x1 - x2) + (y1 - y2)

def f(state, agent, goal):

	return man_dist(state, agent) + man_dist(state, goal) # f(s) = g(s) + h(s)

def repeated_forward_a_star(mazes):

	while mazes:

		maze = mazes[0]





		mazes.pop(0)

		

	return None