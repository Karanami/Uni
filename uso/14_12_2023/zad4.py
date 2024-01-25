import scipy.signal as sig
import scipy.optimize as opt
import scipy.linalg as lin
import scipy.integrate as itg
import scipy.interpolate as itp
import numpy as np
from gekko import GEKKO
import matplotlib.pyplot as plt
from zad2 import A, B, C

Q = np.identity(2)
R = np.array([[1]])

P = lin.solve_continuous_are(A, B, Q, R)

K = np.linalg.matrix_power(R, -1) @ B.transpose() @ P

def zad1():
    def model(e, t, q):
        et = np.transpose([e])
        ue = -K @ et
        uc = np.array([[0, 1/C]]) @ q
        u = uc - ue
        de = A @ et - B @ u - A @ q
        return de.flatten()
    
    t = np.linspace(0, 5)

    Qd = [1, 2, 5]
    for qd in Qd:
        y = itg.odeint(model, [0, 0], t, args=tuple([np.array([[0], [qd]])]))
        plt.plot(t, y[:, 0], label='e1, qd=' + str(qd))
        plt.plot(t, y[:, 1], label='e2, qd=' + str(qd))
        plt.title('zad1')
        plt.legend()
        plt.savefig('zad4_1'+str(qd)+'.png')
        plt.clf()

def zad2():    
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

        def modelFiniteT(e, t, q):
            def K(t):
                p = P(t)
                p = np.array([p[0:2], p[2:4]])
                return np.linalg.matrix_power(R, -1) @ B.transpose() @ p

            et = np.transpose([e])
            ue = -K(t) @ et
            uc = np.array([[0, 1/C]]) @ q
            u = uc - ue
            de = A @ et - B @ u - A @ q
            return de.flatten()

        P_ = lin.solve_continuous_are(A, B, Q, R)
        K_ = np.linalg.matrix_power(R, -1) @ B.transpose() @ P_

        def modelInifiniteT(e, t, q):
            et = np.transpose([e])
            ue = -K_ @ et
            uc = np.array([[0, 1/C]]) @ q
            u = uc - ue
            de = A @ et - B @ u - A @ q
            return de.flatten()

        t = np.linspace(0, 5)
        Qd = [1, 2, 5]
        for qd in Qd:
            yfinite  = itg.odeint(modelFiniteT, [0, 1], t, args=tuple([np.array([[0], [qd]])]))
            yinfinite = itg.odeint(modelInifiniteT, [0, 1], t, args=tuple([np.array([[0], [qd]])]))
            plt.plot(t, yfinite[:, 0], label='fin, e1')
            plt.plot(t, yfinite[:, 1], label='fin, e2')
            plt.plot(t, yinfinite[:, 0], label='inf, e1')
            plt.plot(t, yinfinite[:, 1], label='inf, e2')
            plt.title('qd=' + str(qd) +', S=' + name)
            plt.legend()
            plt.savefig('zad4_2_'+name+'.png')
            plt.clf()

if __name__ == '__main__':
    zad1()
    zad2()

########################################################################################################
# 4.1
# tak regulator LQR z nieskończonym horyzontem czasowym można wykorzystać do realizacji zadań innych
# niż x = 0, ponieważ regulator stabilizował się na zadanej wartości
########################################################################################################
# 4.2
# nie regulator LQR ze skończonym horyzontem czasowym nio można wykorzystać do realizacji zadań innych
# niż x = 0, ponieważ regulator mimo iż początkowo zachowuje sie poprawnie to w ostatnich chwilach 
# czasowych regulator dąży do wartości zero, jest to spowodowane, tym że obliczając nastawy macierzy P,
# z założenia w ostatnich chwilach czasowych P dąży do wartości 0
########################################################################################################