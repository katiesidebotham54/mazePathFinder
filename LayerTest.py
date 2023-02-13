import numpy as np
import matplotlib.pyplot as plt
import main

n = 101

class state():
    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

pathdict = {"state0": state(None, (0,0))}

for x in range(1, n, 1):
	key = "state" + str(x)
	pathdict[key] = state(pathdict["state" + str(x-1)], (x,x))

path = np.zeros((n,n), dtype = int)
for x in pathdict.values():
	path[x.position[0]][x.position[1]] = 1

#MatPlotLib Experimentation

#Maze
plt.imshow(main.generate_maze(n), alpha = .75, cmap = 'binary')

#Masks all 0 values in the path to make only the actual path visible
path = np.ma.masked_where(path == 0, path)

#Path
plt.imshow(path, alpha = 1, cmap = 'autumn')

plt.show()