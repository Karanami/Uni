# prob.py
# This is

import random
import numpy as np
import queue
import math

from gridutil import *


class Agent:
    def __init__(self, size, landmarks, sigma_move_fwd, sigma_move_turn, sigma_perc):
        self.size = size
        self.landmarks = landmarks
        self.sigma_move_fwd = sigma_move_fwd
        self.sigma_move_turn = sigma_move_turn
        self.sigma_perc = sigma_perc

        self.t = 0
        self.n = 500
        # create an initial particle set as 2-D numpy array with size (self.n, 3) (self.p)
        # and initial weights as 1-D numpy array (self.w)
        # TODO PUT YOUR CODE HERE
        self.p = np.random.random((self.n, 3))
        self.w = np.zeros(self.n)
        # ------------------

    def __call__(self):
        # turn by -pi/20.0 and move forward by 1
        action = (-math.pi/20, 1.0)
        # no turn, only move forward by 1.0
        # action = (0.0, 1.0)

        # use information about requested action to update posterior
        # TODO PUT YOUR CODE HERE
        self.predict_posterior(action)
        # ------------------

        self.t += 1

        return action

    def predict_posterior(self, action):
        # predict posterior using requested action
        # TODO PUT YOUR CODE HERE
        rot, dist = action
        x, y = moveForward(0, rot, dist)
        # ------------------

        # this function does not return anything
        return

    def calculate_weights(self, percept):
        # calculate weights using percept
        # TODO PUT YOUR CODE HERE

        # ------------------

        # this function does not return anything
        return

    def correct_posterior(self):
        # correct posterior using measurements
        # TODO PUT YOUR CODE HERE

        # ------------------

        # this function does not return anything
        return

    def get_particles(self):
        return self.p

    def get_weights(self):
        return self.w
