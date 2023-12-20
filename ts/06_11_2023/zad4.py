import numpy as np
import matplotlib.pyplot as plt
import scipy.signal
from math import sin, cos
from scipy.signal import TransferFunction, StateSpace, lsim, lsim2
from scipy.integrate import odeint

R1 = 0.2
L = 0.1
C = 0.05

def u_f(t):
    return 2

def i2(u):
    return 0.25 * u / (5 - u)

def sys(x, t):
    u = u_f(t)
    
    dx1 = 1/C * x[1] - 1/C * i2(u) 
    dx2 = 1/L * u - R1/L * x[1] - 1/L * x[0]
       
    return [dx1, dx2]

t = np.linspace(0, 2, 500, endpoint=False)

x = odeint(sys, [0, 0], t, rtol = 1e-10)

y = [-1/C * i2(2) + 1/C * x[i, 1] for i in range(500)]

plt.plot(t, y)
plt.show()

def u_f2(t):
    return -2

def sys2(x, t):
    u = u_f2(t)
    
    dx1 = 1/C * x[1] - 1/C * i2(u) 
    dx2 = 1/L * u - R1/L * x[1] - 1/L * x[0]
       
    return [dx1, dx2]

t = np.linspace(0, 2, 500, endpoint=False)

x = odeint(sys2, [0, 0], t, rtol = 1e-10)

y = [-1/C * i2(-2) + 1/C * x[i, 1] for i in range(500)]

plt.plot(t, y)
plt.show()