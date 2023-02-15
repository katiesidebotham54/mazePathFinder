import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import main
import time

class state():

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

class animate_path():

	def __init__(self, maze, pathdict):
		self.maze = maze
		self.path = np.zeros(maze.shape, dtype = int)
		self.path = np.ma.masked_where(self.path == 0, self.path)
		self.pathdict = pathdict
		self.fig, self.ax = plt.subplots()

	def animate(self, i):
		if i == len(self.pathdict):
			print( '.', end = '')
		else:
			# self.path[list(self.pathdict.values())[i].position[0]]\
			# 	[list(self.pathdict.values())[i].position[1]] = 1
			self.path[self.pathlist[i].position[0]]\
				[self.pathlist[i].position[1]] = 1
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

#PathList - list containing test states
pathlist = [state(pathdict["state" + str(x)], (x,x)) for x in range(n)]

maze = main.generate_maze(n)

path = np.zeros((n,n), dtype = int)
path = np.ma.masked_where(path == 0, path)

animation1 = animate_path(maze, pathlist)

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