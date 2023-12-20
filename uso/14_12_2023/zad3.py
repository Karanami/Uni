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

    y = itg.odeint(riccati, [100, 0, 0, 100], t)

    plt.plot(t, y)
    plt.title('zad1_2')
    plt.show()
    
    
def zad3():
    S = np.array([1, 0, 0, 1])  # nwm u mnie niczego ta macierz nie zmienia? mam wrażenie że to zasługa interpolacji
                                # bo jak patrzyłem w wywoływania odeinit dla ricati to już wdrugiej iteracj p
                                # ma wartości około 1 
    Q = np.identity(2) # innercja
    R = np.array([[100]]) # oscylacje

    def riccati(p, t):
        P = np.array([p[0:2], p[2:4]])
        dP = -(P @ A - P @ B @ np.linalg.matrix_power(R, -1) @ B.transpose() @ P + A.transpose() @ P + Q)
        flatP = dP[0].tolist() + dP[1].tolist()
        return flatP
    
    t = np.linspace(0, 5)
    ft = np.flip(t)

    y = itg.odeint(riccati, S, ft)
    
    P = itp.interp1d(ft, y, axis=0, fill_value='extrapolate')
    kek = P(1)
    def Pm(t):
        p = P(t)
        return np.array([p[0:2], p[2:4]])
    
    def K(t):
        return np.linalg.matrix_power(R, -1) @ B.transpose() @ Pm(t)
    
    def u(x, t):
        k = K(t)
        return -k @ x

    def model(x, t):
        xt = np.transpose([x])
        dx = A @ xt + B * u(xt, t)
        return np.transpose(dx).flatten()        

    y = itg.odeint(model, [0, 1], t)

    plt.plot(t, y)
    plt.title('zad3')
    plt.show()
    
def zad4():
    
    SS = [[1, 0, 0, 1], [100, 0, 0, 100]]
    Sname = ['I', '100I']
    Q = np.identity(2)
    R = np.array([[1]])
    for S, name in zip(SS, Sname):
        def riccati(p, t):
            P = np.array([p[0:2], p[2:4]])
            dP = -(P @ A - P @ B @ np.linalg.matrix_power(R, -1) @ B.transpose() @ P + A.transpose() @ P + Q)
            flatP = dP[0].tolist() + dP[1].tolist()
            return flatP
        
        t = np.linspace(0, 5)
        ft = np.flip(t)

        y = itg.odeint(riccati, S, ft)
        
        P = itp.interp1d(ft, y, axis=0, fill_value='extrapolate')

        def modelFiniteT(x, t):
            def Pm(t):
                p = P(t)
                return np.array([p[0:2], p[2:4]])
            
            def K(t):
                return np.linalg.matrix_power(R, -1) @ B.transpose() @ Pm(t)
            
            def u(x, t):
                k = K(t)
                return -k @ x

            xt = np.transpose([x])
            dx = A @ xt + B * u(xt, t)
            return np.transpose(dx).flatten()        

        Pinne = lin.solve_continuous_are(A, B, Q, R)
        Kinne = np.linalg.matrix_power(R, -1) @ B.transpose() @ Pinne

        def modelInifiniteT(x, t):
            def u(x):
                return -Kinne @ x

            xt = np.transpose([x])
            dx = A @ xt + B * u(xt)
            return np.transpose(dx).flatten()

        tend = [1, 2, 5]

        for te, p in zip(tend, [1, 2, 3]):
            t = np.linspace(0, te)
            yfinite   = itg.odeint(modelFiniteT, [0, 1], t)
            yifinite = itg.odeint(modelInifiniteT, [0, 1], t)
            plt.subplot(130 + p)
            plt.plot(t, yfinite, 'r', label='finite')
            plt.plot(t, yifinite, 'b.', label='ifinite')
            plt.title('zad4 - ' + name + ' tend: ' + str(te))
            
        plt.legend()
        plt.show()

if __name__ == '__main__':
    zad1_2()
    #zad3()
    ##zad4()