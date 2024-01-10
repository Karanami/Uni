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

    plt.plot(t, y, label=['x1', 'x2'])
    plt.title('zad2')
    plt.legend()
    plt.show()
    
    
def zad3():

    QR = [(np.identity(2), np.array([[1]]), 'norm', 1), (np.identity(2) * 100, np.array([[1]]), 'Q100', 2), (np.identity(2), np.array([[100]]), 'R100', 3)]
    for Q, R, name, subplt in QR:
        P = lin.solve_continuous_are(A, B, Q, R)
        K = np.linalg.matrix_power(R, -1) @ B.transpose() @ P

        def u(x):
            return -K @ x

        def model(x, t):
            xt = np.transpose([x])
            dx = A @ xt + B * u(xt)
            return np.transpose(dx).flatten()

        t = np.linspace(0, 5)

        y = itg.odeint(model, [1, 1], t)

        plt.subplot(3, 1, subplt)
        plt.plot(t, y, label=[f'x1-{name}', f'x2-{name}'])
        plt.title(f'zad3-{name}')
        plt.legend()
    plt.show()
    
    
def zad4():

    QR = [(np.identity(2), np.array([[1]]), 'norm', 1), (np.identity(2) * 100, np.array([[1]]), 'Q100', 2), (np.identity(2), np.array([[100]]), 'R100', 3)]
    for Q, R, name, subplt in QR:
        P = lin.solve_continuous_are(A, B, Q, R)
        K = np.linalg.matrix_power(R, -1) @ B.transpose() @ P

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

        plt.subplot(3, 1, subplt)
        plt.plot(t, y[:, 2], label=f'J-{name}')
        plt.title(f'zad4-{name}')
        plt.legend()
    plt.show()
    t = np.linspace(0, 5)
    return

if __name__ == '__main__':
    zad2()
    zad3()
    zad4()


########################################################################################################
# 2.1. 
# Algorytm solve_continuous_are używa rokładu QZ
########################################################################################################
# 2.2. 
# Odpowiedź skokowa obiektu w przypadku zmiennej x2 (i) stabilizuje się na wartości 0, natomiast 
# zmienna x1 (qc) stabilizuje sie na wartości ~0.5. Można także zawuważyć początkowe przeregulowanie 
# oraz podregulowanie (małe oscylacje układu) w pierwszych chwilach czasowych
########################################################################################################
# 2.3
# a) tak wszystkie wartości zbiegają do wartości zadanych (0)
# b) macierz R zwiększa oscylacje w odpowiedzi skowej, a macierz Q zwiększa jej czas regulacji
########################################################################################################
# 2.4
# a) tak dla wyznaczonych wzmocnień LQR wartość wskaźnika jest najmniejsza
# b) wskaźnik jakości został wyznaczony w horyzoncie 5s
########################################################################################################