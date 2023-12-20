import scipy.signal as sig
import scipy.optimize as opt
import scipy.linalg as lin
import scipy.integrate as itg
import scipy.interpolate as itp
import numpy as np
from gekko import GEKKO
import matplotlib.pyplot as plt
from zad2 import A, B, R, Q

def zad1_2():
    def riccati(p, t):
        P = np.array([p[0:2], p[2:4]])
        dP = -(P @ A - P @ B @ np.linalg.matrix_power(R, -1) @ B.transpose() @ P + A.transpose() @ P + Q)
        flatP = dP[0].tolist() + dP[1].tolist()
        return flatP
    
    t = np.linspace(0, 5)
    t = np.flip(t)

    y = itg.odeint(riccati, [1, 0, 0, 1], t)

    plt.plot(t, y)
    plt.title('zad1_2')
    plt.show()
    
    
def zad3():
    def riccati(p, t):
        P = np.array([p[0:2], p[2:4]])
        dP = -(P @ A - P @ B @ np.linalg.matrix_power(R, -1) @ B.transpose() @ P + A.transpose() @ P + Q)
        flatP = dP[0].tolist() + dP[1].tolist()
        return flatP
    
    t = np.linspace(0, 5)
    ft = np.flip(t)

    y = itg.odeint(riccati, [1, 0, 0, 1], ft)
    
    P = itp.interp1d(ft, y, axis=0, fill_value='extrapolate')
    
    def Pm(t):
        p = P(t)
        return np.array([p[0:2], p[2:4]])
    
    def K(t):
        return np.linalg.matrix_power(R, -1) @ B.transpose() @ Pm(t)
    
    def u(x):
        k = K(t)
        return -k @ x

    def model(x, t):
        xt = np.transpose([x])
        dx = A @ xt + B * u(xt)
        return np.transpose(dx).flatten()        

    y = itg.odeint(model, [0, 1], t)

    plt.plot(t, y)
    plt.title('zad3')
    plt.show()
    
if __name__ == '__main__':
    #zad1_2()
    zad3()