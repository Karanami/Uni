#2.1
import numpy as np
import scipy.signal as sig
import scipy.integrate as itg
#import scipy.integrate.odeint as ode
import matplotlib.pyplot as plt

kp = 3
T = 2
A = - 1 / T
B = kp / T
C = 1
D = 0

#2.2

sys = sig.TransferFunction([kp], [T, 1])
t1, o1 = sig.step(sys)
#plt.plot(t, o)
#plt.show()

#=================================================================================#
#Odp
#Tak wykres odpowiedzi skokowej odpowiada teoretycznym założeniom
#Odpowiedz skokowa systemu ustabilizowala się na wartości 3 - system jest stabliny 
#=================================================================================#

#2.3
sys = sig.StateSpace(A,B,C,D)
t2, o2 = sig.step(sys)
#plt.plot(t, o)
#plt.show()

#2.4
t3 = np.linspace(0, 15)
def model(t, y):
    return (kp - y) / T

#2.5
solution = itg.solve_ivp(model, (0, 15), [0], dense_output=True)
o3 = solution.sol(t3).T
#plt.plot(t, z.T)
#plt.show()

#2.6
plt.figure(1)
#plt.subplot(311)
plt.plot(t1, o1, label='1')
#plt.subplot(312)
plt.plot(t2, o2, 'r:', label='2')
#plt.subplot(313)
plt.plot(t3, o3, 'g.', label='3')
plt.legend()
plt.xlabel('t')
plt.show()

#=================================================================================#
#Odp
#Odpowiedzi skowe się pokrywaja
#Zastosowane przekształcenia nie zmieniają wyjść systemu
#=================================================================================#

