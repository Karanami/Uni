import numpy as np
import matplotlib.pyplot as plt
import scipy.signal
from math import sin, cos
from scipy.signal import TransferFunction, StateSpace, lsim, lsim2
from scipy.integrate import odeint

#zad 3.2
m = 1
l = 0.5
J = 0.05
b_range = [0, .1, .5]
###################################################
#ustawić b
###################################################
b = b_range[1]
g = 9.81

def u_f(t):
    return 0

def sys(x, t):
    u = u_f(t)
    
    dx1 = x[1]
    dx2 = 1/(m*l**2+J) * u - b/(m*l**2 + J) * x[1] - m*g*l/(m*l**2+J) * sin(x[0])
       
    return [dx1, dx2]


t = np.linspace(0, 60, 5000, endpoint=False)

x = odeint(sys, [np.pi / 2 ,0], t, rtol = 1e-10)

_x = [sin(x1) * l for x1 in x[:,0]]
_y = [cos(x1) * l for x1 in x[:,0]]

plt.plot(t, _x)
plt.plot(t, _y)
plt.show()

#zad 3.4

b = b_range[1]

frange = [2, 0.65, 0.2]

###################################################
#ustawić f
###################################################
f = frange[2]
def u_f2(t):
     return 0.1 * sin(2 * np.pi * f * t)

def sys2(x, t):
    u = u_f2(t)
    
    dx1 = x[1]
    dx2 = 1/(m*l**2+J) * u - b/(m*l**2 + J) * x[1] - m*g*l/(m*l**2+J) * sin(x[0])
       
    return [dx1, dx2]

x = odeint(sys2, [0, 0], t, rtol = 1e-10)

_x = [sin(x1) * l for x1 in x[:,0]]
_y = [cos(x1) * l for x1 in x[:,0]]

plt.subplot(211)
plt.plot(t, x[:,0])
plt.subplot(212)
plt.plot(t, _x)
plt.plot(t, _y)
plt.show()