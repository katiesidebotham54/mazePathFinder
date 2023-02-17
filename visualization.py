import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from IPython import display
import time

class animated_path():

    def __init__(self, maze, closed_list, path, start_s, goal_s):

        #Animation Speed
        self.interval = 100 / maze.shape[0]

        #Goal & Start States
        self.goal_s = goal_s
        self.start_s = start_s

        #Layer 0: Start State Visualization
        self.ssv = np.ones(maze.shape, dtype = bool)
        self.ssv = np.ma.masked_where(self.ssv == 1, self.ssv)
        self.ssv[self.start_s.position[0]][self.start_s.position[1]] = 0

        #Layer 1: Maze (AKA GRID) Visualization
        self.maze = maze

        #Layer 2: Closed List Visualization
        self.clv = np.zeros(maze.shape, dtype = float)
        self.clv = np.ma.masked_where(self.clv == 0, self.clv)

        #Layer 3: Path Visualization
        self.pv = np.zeros(maze.shape, dtype = float)
        self.pv = np.ma.masked_where(self.pv == 0, self.pv)

        #Layer 4: Goal State Visualization
        self.gsv = np.zeros(maze.shape, dtype = bool)
        self.gsv = np.ma.masked_where(self.gsv == 0, self.gsv)
        self.gsv[self.goal_s.position[0]][self.goal_s.position[1]] = 1

        #Closed List
        self.closed_list = closed_list

        #Path List
        if path:
            self.path = path
        else:
            self.path = []

        #Max g of Lists (for gradient purposes)
        self.c_max_g = max([state.g for state in self.closed_list])

        #Figure & Axis Init
        self.fig, self.ax = plt.subplots()

    def animate(self, i):

        self.ax.clear()

        if i < len(self.closed_list):

            if self.c_max_g != 0:

                self.clv[self.closed_list[i].position[0]][self.closed_list[i].position[1]] = self.closed_list[i].g / self.c_max_g
            
            else:

                self.clv[self.closed_list[i].position[0]][self.closed_list[i].position[1]] = 1

        elif i - len(self.closed_list) < len(self.path):

            i -= len(self.closed_list)

            self.pv[self.path[i].position[0]][self.path[i].position[1]] = 1 - i / len(self.path)

 #Update pv with path states

        else:
            print('.', end = '')
            return

        #Show All Layers
        plt.imshow(self.maze, alpha = 1, cmap = 'Greys')
        plt.imshow(self.clv, alpha = .5, cmap = 'Wistia')
        plt.imshow(self.pv, alpha = 1, cmap = 'cool')
        plt.imshow(self.ssv, alpha = 1, cmap = 'spring')
        plt.imshow(self.gsv, alpha = 1, cmap = 'cool')

    def start_animation(self):
        anim = animation.FuncAnimation(self.fig, self.animate, frames = len(self.closed_list) + len(self.path), interval = self.interval)
        plt.show()