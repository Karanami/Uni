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
        flatP = dP.flatten()
        return flatP
    
    t = np.linspace(0, 5)
    t = np.flip(t)

    y = itg.odeint(riccati, [1, 0, 0, 1], t)

    plt.plot(t, y, label=['p1', 'p2', 'p3', 'p4'])
    plt.title('zad1_2')
    plt.legend()
    #plt.show()
    plt.savefig('zad3_1-2.png')
    
    
def zad3():
    S = np.array([[1, 0], [0, 1]])  # nwm u mnie niczego ta macierz nie zmienia? mam wrażenie że to zasługa interpolacji
                                # bo jak patrzyłem w wywoływania odeinit dla ricati to już wdrugiej iteracj p
                                # ma wartości około 1 
    Q = np.identity(2) # innercja
    R = np.array([[100]]) # oscylacje

    def riccati(p, t):
        P = np.array([p[0:2], p[2:4]])
        dP = -(P @ A - P @ B @ np.linalg.matrix_power(R, -1) @ B.transpose() @ P + A.transpose() @ P + Q)
        flatP = dP.flatten()
        return flatP
    
    t = np.linspace(0, 5)
    ft = np.flip(t)

    y = itg.odeint(riccati, S.flatten(), ft)
    
    P = itp.interp1d(ft, y, axis=0, fill_value='extrapolate')
    kek = P(1)
    def Pm(t):
        p = P(t)
        return np.array([p[0:2], p[2:4]])
    
    def K(t):
        return np.linalg.matrix_power(R, -1) @ B.transpose() @ Pm(t)
    
    def u(x, t):
        k = K(t)
        u = -k @ x
        return u

    def model(x, t):
        xt = np.transpose([x])
        dx = A @ xt + B * u(xt, t)
        return dx.transpose().flatten()        

    y = itg.odeint(model, [0, 1], t)

    plt.clf()
    plt.plot(t, y, label=['x1', 'x2'])
    plt.title('zad3')
    plt.legend()
    plt.savefig('zad3_3.png')
    
def zad4():
    plt.clf()
    SS = [[1, 0, 0, 1], [100, 0, 0, 100]]
    Sname = ['I', '100I']
    Q = np.identity(2)
    R = np.array([[1]])
    for S, name in zip(SS, Sname):
        def riccati(p, t):
            P = np.array([p[0:2], p[2:4]])
            dP = -(P @ A - P @ B @ np.linalg.inv(R) @ B.transpose() @ P + A.transpose() @ P + Q)
            flatP = dP.flatten()
            return flatP  

        Pinne = lin.solve_continuous_are(A, B, Q, R)
        Kinne = np.linalg.inv(R) @ B.transpose() @ Pinne

        def modelInifiniteT(x, t):
            def u(x):
                return -Kinne @ x

            xt = np.transpose([x])
            dx = A @ xt + B * u(xt)
            return np.transpose(dx).flatten()

        tend = [1, 2, 5]

        for te, p in zip(tend, [1, 2, 3]):
            
            t = np.linspace(0, te)
            ft = np.flip(t)

            y = itg.odeint(riccati, S, ft)
            
            P = itp.interp1d(ft, y, axis=0, fill_value='extrapolate')

            def modelFiniteT(x, t):
                def Pm(t):
                    p = P(t)
                    return np.array([p[0:2], p[2:4]])
                
                def K(t):
                    return np.linalg.inv(R) @ B.transpose() @ Pm(t)
                
                def u(x, t):
                    k = K(t)
                    return -k @ x

                xt = np.transpose([x])
                dx = A @ xt + B * u(xt, t)
                return np.transpose(dx).flatten()      

            yfinite  = itg.odeint(modelFiniteT, [0, 1], t)
            yifinite = itg.odeint(modelInifiniteT, [0, 1], t)
            plt.subplot(3, 1, p)
            plt.plot(t, yfinite, label=['x1 - finite',  'x2 - finite'])
            plt.plot(t, yifinite, '.', label=['x1 - infinite', 'x2 - infinite'])
            plt.title('zad4 - ' + name + ' tend: ' + str(te))
            plt.legend()
        plt.savefig('zad3_4_' + name + '.png')
        plt.clf()

if __name__ == '__main__':
    zad1_2()
    zad3()
    zad4()

########################################################################################################
# 3.2. 
# tak spełniony jest warunek zmieżności wartości macierzy P(t) do S
########################################################################################################
# 3.3
# Podobnie jak w poprzednim zadaniu, macierz R zwiększa oscylacje w odpowiedzi skowej, a macierz Q 
# zwiększa jej czas regulacji, natomiast macierz S niezdaje się mieć aż tak dużego wpływu na uchyb 
# uchyb regulacji
########################################################################################################
# 3.4
# a) 
########################################################################################################