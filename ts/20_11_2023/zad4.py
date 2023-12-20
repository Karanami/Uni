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

def model_v2(x, t, L):
    vx = np.array([x[2:4]]).transpose()
    x = np.array([x[:2]]).transpose()
    
    dx = A @ x + B * u(t)
    y = C @ x
    dvx = A @ vx + B * u(t) + L * ( (y + yd(t)) - C @ vx )
    d = np.concatenate((dx.flatten(), dvx.flatten()))
    return d

omega_range = { 1, 5, 10 }

t = np.linspace(0, 5)

# for omega in omega_range:
#     x = odeint(model_v2, [2, 0, 0, 0], t, tuple([getL(omega)]))
#     plt.plot(t, x[:, 0], 'r', label='x1')
#     plt.plot(t, x[:, 1], 'g', label='x2')
#     plt.plot(t, x[:, 2], 'b', label='^x1')
#     plt.plot(t, x[:, 3], 'm', label='^x2')
#     plt.legend()
#     plt.show()
    
#przy wystąpieniu zakłóceń pomiarowych możliwa jest przybliżona estymacja
#zmiennych stanu
#wraz z wzrostem omegi zakłócenia zakłócenia pomiarowe zmiennych stanu są
#coraz mniej ofiltrowywane
#omega powinna być dobierana w taki sposób aby wszelkie zakłócenia pomiarowe
#były możliwie jak najbardziej odfiltrowywane

def ud(t):
    return np.sin(4 * np.pi * t) ** 2

def model_v3(x, t, L):
    vx = np.array([x[2:4]]).transpose()
    x = np.array([x[:2]]).transpose()
    
    dx = A @ x + B * (u(t) + ud(t))
    y = C @ x
    dvx = A @ vx + B * u(t) + L * ( (y) - C @ vx )
    d = np.concatenate((dx.flatten(), dvx.flatten()))
    return d

for omega in omega_range:
    x = odeint(model_v3, [2, 0, 0, 0], t, tuple([getL(omega)]))
    plt.plot(t, x[:, 0], 'r', label='x1')
    plt.plot(t, x[:, 1], 'g', label='x2')
    plt.plot(t, x[:, 2], 'b', label='^x1')
    plt.plot(t, x[:, 3], 'm', label='^x2')
    plt.legend()
    plt.show()

#przy wystąpieniu zakłóceń procesu możliwa jest całkiem dokładna estymacja
#zmiennych stanu
#wraz ze wzrostem omegi niwelowane były zakłucenia procesu, z pominięciem
#małych przeregulowań na na początku przebiegu obserwatorów
