import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import main
import time

class state():

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

class anime():

	def __init__(self, maze, path, pathdict):
		self.maze = maze
		self.path = path
		self.pathdict = pathdict
		self.fig, self.ax = plt.subplots()

	def animate(self, i):
		if i == len(self.pathdict):
			print( '.', end = '')
		else:
			self.path[list(self.pathdict.values())[i].position[0]]\
				[list(self.pathdict.values())[i].position[1]] = 1
			self.ax.clear()
			plt.imshow(self.maze, alpha = .5, cmap = 'binary')
			self.im = plt.imshow(self.path, alpha = 1, cmap = 'autumn', animated = True)
			return self.im

	def start_animation(self):
		# plt.close()
		self.ani = animation.FuncAnimation(self.fig, self.animate, \
			frames = len(self.path), interval = 50)
		plt.show()

#Array Size
n = 101

#PathDict - Dictionary containing test states
pathdict = {"state0": state(None, (0,0))}
for x in range(1, n, 1):
	key = "state" + str(x)
	pathdict[key] = state(pathdict["state" + str(x-1)], (x,x))

maze = main.generate_maze(n)

path = np.zeros((n,n), dtype = int)
path = np.ma.masked_where(path == 0, path)

animation1 = anime(maze, path, pathdict)

animation1.start_animation()

#Figure
# fig,ax = plt.subplots()

#Animated Path
# im = plt.imshow(path, alpha = 1, cmap = 'autumn',\
# 				interpolation='none', aspect='auto', vmin=0, vmax=1)

#Update the figure with one additional node
# def animate(i):
# 	if i == len(pathdict):
# 		print( '.', end = '')
# 	else:
# 		path[list(pathdict.values())[i].position[0]]\
# 			[list(pathdict.values())[i].position[1]] = 1
# 		ax.clear()
# 		plt.imshow(maze, alpha = .5, cmap = 'binary')
# 		im = plt.imshow(path, alpha = 1, cmap = 'autumn', animated = True)

# ani = animation.FuncAnimation(fig, anime.animate(), frames = len(pathdict), interval = 50)
# plt.imshow(maze, alpha = .75, cmap = 'binary')
# plt.show()


#End Result
# plt.imshow(maze, alpha = .75, cmap = 'binary')
# plt.imshow(path, alpha = 1, cmap = 'autumn')
# plt.show()