# prob.py
# This is

import random
import numpy as np
import queue
import math

from gridutil import *


class Agent:
    def __init__(self, size, walls, loc, dir, sigma_move, sigma_perc, dt):
        self.size = size
        self.walls = walls
        # list of valid locations
        self.locations = list({*locations(self.size)}.difference(self.walls))
        # dictionary from location to its index in the list
        self.loc_to_idx = {loc: idx for idx, loc in enumerate(self.locations)}
        self.loc = loc
        self.dir = dir
        self.dt = dt
        self.action_dir = 1

        self.t = 0

        # create matrices used in Kalman filter
        # TODO PUT YOUR CODE HERE
        self.sigma_move = sigma_move
        self.sigma_perc = sigma_perc
        self.mu = np.array([[0], [0]])
        self.Sigma = np.array([[1, 0],
                               [0, 10]])
        self.F = np.array([[1, dt],
                           [0, 1]])
        self.Q = np.array([[1/4 * dt**4, 1/2 * dt**3],
                           [1/2 * dt**3, dt**2]]) * sigma_move**2

        # ------------------

    def __call__(self):
        # use information about requested action to update posterior
        # TODO PUT YOUR CODE HERE

        self.predict_posterior()
        # ------------------

        # this function does not return anything
        return

    def predict_posterior(self):
        # predict posterior
        # TODO PUT YOUR CODE HERE

        self.mu = self.F @ self.mu
        self.Sigma = self.F @ self.Sigma @ self.F.transpose() + self.Q
        # ------------------

        # this function does not return anything
        return

    def correct_posterior(self, percept):
        # correct posterior using measurements
        # TODO PUT YOUR CODE HERE

        H = np.array([[1, 0]])
        R = self.sigma_perc**2
        y = percept - H @ self.mu
        K = self.Sigma @ H.transpose() * (H @ self.Sigma @ H.transpose() + R)**-1
        self.mu = self.mu + K @ y
        self.Sigma = (np.identity(2) - K @ H) @ self.Sigma
        

        # ------------------

        # this function does not return anything
        return

    def get_posterior(self):
        return self.mu, self.Sigma
