# prob.py
# This is

import random
import numpy as np
import queue
import math

from gridutil import *
from dixtra import dixtra
from a_star import a_star


class Agent:
    def __init__(self, size, walls, graph, loc, dir, goal):
        self.size = size
        self.walls = walls
        self.graph = graph
        # list of valid locations
        self.locations = list(self.graph.keys())
        # dictionary from location to its index in the list
        self.loc_to_idx = {loc: idx for idx, loc in enumerate(self.locations)}
        self.loc = loc
        self.dir = dir
        self.goal = goal

        self.t = 0
        self.path = self.find_path()

    def __call__(self):
        action = self.loc

        # select action to reach first location in self.path
        # TODO PUT YOUR CODE HERE

        action = self.path.pop()

        # ------------------

        return action

    def find_path(self):
        path = []

        # find path from sel.loc to self.goal
        # TODO PUT YOUR CODE HERE

        _, visited_d = dixtra(self.loc, self.goal, self.graph)
        path, visited_a = a_star(self.loc, self.goal, self.graph)
        self.path = path
        self.visited_d = visited_d
        self.visited_a = visited_a

        # ------------------

        return path

    def get_path(self):
        return self.path
