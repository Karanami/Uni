import numpy as np
import matplotlib.pyplot as plt
from math import sin
from scipy.signal import TransferFunction, StateSpace, lsim, step

R1 = 0.2
R2 = 0.5
L = 0.1
C = 0.05

#zad1 / zad2

A = [[-1/(R2*C) , 1/C],
     [-1/L      , -R1/L]]
B = [[0],
     [1/L]]
C = [-1/(R2*C) , 1/C]
D = 0

sys = StateSpace(A, B, C, D)

t = np.linspace(0, 2, 500, endpoint=False)

u_step = 2 * t
u_sin = [sin(i) for i in t]
t_step, o_step, _ = lsim(sys, u_step, t)
t_sin, o_sin, _ = lsim(sys, u_sin, t)

plt.subplot(211)
plt.plot(t_step, o_step)
plt.subplot(212)
plt.plot(t_sin, o_sin)
plt.show()