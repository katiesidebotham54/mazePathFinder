import numpy as np
import matplotlib.pyplot as plt
import main

n = 101

class state():
    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

maze = main.generate_maze(n)

pathdict = {"state0": state(None, (0,0))}

for x in range(1, n, 1):
	key = "state" + str(x)
	pathdict[key] = state(pathdict["state" + str(x-1)], (x,x))

path = np.zeros((n,n), dtype = int)
for x in pathdict.values():
	path[x.position[0]][x.position[1]] = 1

plt.imshow(maze, alpha = .5, cmap = 'binary', color = red)
plt.imshow(path, alpha = .5, cmap = 'binary')
plt.show()