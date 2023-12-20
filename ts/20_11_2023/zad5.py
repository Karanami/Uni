import scipy.signal as sig
import numpy as np 
from scipy.integrate import odeint
import sympy as sp
from zad2 import k, m, b, A, B, C
import matplotlib.pyplot as plt

#zad 4.1

def getL(omega):
    L = sig.place_poles(A.transpose(), np.array([C]).transpose(), [-omega, -omega + 0.00000001], method='KNV0')
    return np.array([[round(l, 4) for l in L.gain_matrix[0]]]).transpose()

def u(t):
    return np.sin(np.pi * t)

def yd(t):
    return np.sin(4 * np.pi * t) ** 2

def ud(t):
    return np.sin(4 * np.pi * t) ** 2

def model(x, t, L):
    vx = np.array([x[2:4]]).transpose()
    x = np.array([x[:2]]).transpose()
    
    dx = A @ x + B * (u(t) + ud(t))
    y = C @ x
    dvx = A @ vx + B * u(t) + L * ( (y + yd(t)) - C @ vx )
    d = np.concatenate((dx.flatten(), dvx.flatten()))
    return d


omega_range = { 1, 5, 10 }

t = np.linspace(0, 5)

for omega in omega_range:
    x = odeint(model, [2, 0, 0, 0], t, tuple([getL(omega)]))
    x1 = np.array(x[:, 0])
    x2 = np.array([0])
    Tp = t[1] - t[0]
    for i in range(1, len(x1)):
        x2 = np.append(x2, (x1[i] - x1[i - 1]) / Tp )
    
    plt.plot(t, x[:, 0], 'r', label='x1')
    plt.plot(t, x[:, 1], 'g', label='x2')
    plt.plot(t, x[:, 2], 'b', label='^x1')
    plt.plot(t, x[:, 3], 'm', label='^x2')
    plt.plot(t, x2, 'c', label='num x2')
    plt.legend()
    plt.show()
    
# metoda numeryczna pozwoliła na najlepszą stymacje zeminnej sanu 
# typem zakłóceń które najmocniej wpływały by na tego typu estymacje
# są zakłócenia procesu, ponieważ estymacja numeryczna bezpośrednio
# opiera się na wynikach zmiennych stanów całego procesu