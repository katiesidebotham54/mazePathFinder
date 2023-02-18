import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from IPython import display
import time

class animated_path():

    def __init__(self, maze, closed_list, path, start_s, goal_s):

        #Layer 1: Maze (Input as a np array)
        self.maze = maze

        #Layer 2: Closed List (Input as a list of states)
        self.closed_list = closed_list
        self.c_max_g = max([state.g for state in self.closed_list])
        self.clv = np.zeros(maze.shape, dtype = float)
        self.clv = np.ma.masked_where(self.clv == 0, self.clv)

        #Layer 3: Path (Input as a list of states), start_s and goal_s
        if path: self.path = path
        else: self.path = []
        self.pv = np.full(maze.shape, fill_value = -1, dtype = float)
        self.pv = np.ma.masked_where(self.pv == -1, self.pv)
        self.pv[start_s.position[0]][start_s.position[1]] = 0
        self.pv[goal_s.position[0]][goal_s.position[1]] = 1 

        #Animation Init
        self.fig, self.ax = plt.subplots()
        self.interval = 100 / maze.shape[0]

    def animate(self, i):

        if i < len(self.closed_list):

            if self.c_max_g != 0:

                self.clv[self.closed_list[i].position[0]][self.closed_list[i].position[1]] = self.closed_list[i].g / self.c_max_g
            
            else:

                self.clv[self.closed_list[i].position[0]][self.closed_list[i].position[1]] = 1

        elif i - len(self.closed_list) < len(self.path):

            i -= len(self.closed_list)

            self.pv[self.path[i].position[0]][self.path[i].position[1]] = i / len(self.path)

        else:
            print('.', end = '')
            return

        #Show
        self.ax.clear()
        plt.imshow(self.maze, alpha = 1, cmap = 'Greys')
        plt.imshow(self.clv, alpha = .5, cmap = 'Wistia')
        plt.imshow(self.pv, alpha = 1, cmap = 'cool')

    def start_animation(self):
        anim = animation.FuncAnimation(self.fig, self.animate, frames = len(self.closed_list) + len(self.path), interval = self.interval)
        plt.show()