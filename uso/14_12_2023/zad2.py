import scipy.signal as sig
import scipy.optimize as opt
import scipy.linalg as lin
import scipy.integrate as itg
import numpy as np
from gekko import GEKKO
import matplotlib.pyplot as plt

L = .2
C = .5
R1 = .5

A = np.array([[0,           1],
              [-1/(L*C),    -R1/L]])
B = np.array([[0],
              [1/L]])

#zad 1
Q = np.identity(2)
R = np.array([[1]])

P = lin.solve_continuous_are(A, B, Q, R)

K = np.linalg.matrix_power(R, -1) @ B.transpose() @ P
print(K) 

def zad2():
    def u(t):
        return 1

    def model(x, t):
        xt = np.transpose([x])
        dx = A @ xt + B * u(t)
        return np.transpose(dx).flatten()

    t = np.linspace(0, 5)

    y = itg.odeint(model, [0, 0], t)

    plt.plot(t, y)
    plt.title('zad2')
    plt.show()
    
    
def zad3():
    def u(x):
        return -K @ x

    def model(x, t):
        xt = np.transpose([x])
        dx = A @ xt + B * u(xt)
        return np.transpose(dx).flatten()

    t = np.linspace(0, 5)

    y = itg.odeint(model, [1, 1], t)

    plt.plot(t, y)
    plt.title('zad3')
    plt.show()
    
    
def zad4():
    def u(x):
        return -K @ x

    def model(x, t):
        xt = np.transpose([x[0:2]])
        Kx = u(xt)
        dx = A @ xt + B * Kx
        dJ = np.transpose(xt) @ Q @ xt + Kx * R * Kx
        return np.append(np.transpose(dx).flatten(), dJ)

    t = np.linspace(0, 5)

    y = itg.odeint(model, [1, 1, 0], t)

    plt.plot(t, y[:, 2])
    plt.title('zad4')
    plt.show()
    return

if __name__ == '__main__':
    zad2()
    zad3()
    zad4()