import scipy.signal as sig
import numpy as np 
from scipy.integrate import odeint
import sympy as sp
from zad2 import k, m, b, A, B, C
import matplotlib.pyplot as plt
# from sympy.interactive.printing import init_printing
# init_printing(use_unicode=False, wrap_line=False)

#3.1
# def u(t):
#     return 1

# def model(x, t):
#     dx = A @ np.array([x]).transpose() + B * u(t)
#     return dx.tolist()

#3.2
def getL(omega):
    L = sig.place_poles(A.transpose(), np.array([C]).transpose(), [-omega, -omega + 0.00000001], method='KNV0')
    return np.array([[round(l, 4) for l in L.gain_matrix[0]]]).transpose()

# 1. omegę należy dobierać w taki sposób aby minimalizowąć błąd estymacji - macierz H 
# 2. 

#3.3
def u(t):
    return np.sin(np.pi * t)

def model_v2(x, t, L):
    vx = np.array([x[2:4]]).transpose()
    x = np.array([x[:2]]).transpose()
    
    dx = A @ x + B * u(t)
    y = C @ x
    dvx = A @ vx + B * u(t) + L * ( y - C @ vx )
    d = np.concatenate((dx.flatten(), dvx.flatten()))
    return d

#3.4
t = np.linspace(0, 5)

x = odeint(model_v2, [0, 0, 0, 0], t, tuple([getL(1)]))
plt.plot(t, x[:, 0], 'r')
plt.plot(t, x[:, 1], 'g')
plt.plot(t, x[:, 2], 'b.')
plt.plot(t, x[:, 3], 'm.')
plt.show()

omega_range = { -1, 1, 5, 10 }

#3.5
for omega in omega_range:
    x = odeint(model_v2, [2, 0, 0, 0], t, tuple([getL(omega)]))
    plt.plot(t, x[:, 0], 'r', label='x1')
    plt.plot(t, x[:, 1], 'g', label='x2')
    plt.plot(t, x[:, 2], 'b.', label='^x1')
    plt.plot(t, x[:, 3], 'm.', label='^x2')
    plt.legend()
    plt.show()
    
#omega ma bezpośredni wpływ na stabilność obserwatora i nie właściwie
#dobrana może destabilizować uład obserwatora jak w przypadku omegi
#równej 10