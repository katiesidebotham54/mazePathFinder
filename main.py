import random
import numpy as np
import matplotlib.pyplot as plt
import time
from generate_maze import generate_maze

class state():
    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position
        self.g = float('inf')
        self.h = float('inf')
        self.f = self.g + self.h

    def __eq__(self, other):
        return self.position == other.position

    def __hash__(self):
        return hash(self.position)

    def __lt__(self, other):
        return self.f < other.f

actions = ["up", "down", "left", "right"]

n = 101

maze = generate_maze(n)