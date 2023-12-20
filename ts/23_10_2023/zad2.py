import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
import math
from scipy.signal import TransferFunction, StateSpace

#punkt 1

#punkt 2
G1_tf = TransferFunction([10], [1, 2])
G2_tf = TransferFunction([4], [2, 0, 1])
G3_tf = TransferFunction([-2, 6], [1, 7, 16, 12])  

g1_ss = StateSpace(-2, 1, 10, 0)
g2_ss = StateSpace([0, 0.5], [1, 0], 1, 0)
g3_ss = StateSpace([[-7, 1, 0], [-16, 0, 1], [-12, 0, 0]])

print(g1_ss)
print(g2_ss)
print(g3_ss)