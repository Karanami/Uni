import numpy as np
import scipy.signal as sig
import scipy.integrate as itg
#import scipy.integrate.odeint as ode
import matplotlib.pyplot as plt

#4.1

#A = np.array([[1.2, 1], [0, 0]])
A = np.array([[0, 1], [0, -1.2]])
B = np.array([[0], [12]])
C = np.array([1, 0])
D = 0

ss4_1 = sig.StateSpace(A, B, C, D)
tf4_1 = sig.TransferFunction([1], [12, 1.2, 0])

t4_1, o4_1 = sig.step(ss4_1)
t4_1tf, o4_1tf = sig.step(tf4_1)

# plt.plot(t4_1, o4_1)
# plt.show()

#=================================================================================#
# Odp
# Odpowiedź skokowa obiektu nie ustala się na konkretnej wartości lecz wykładniczo 
# narasta
#=================================================================================#

#4.2

ss4_2 = sig.StateSpace(A, B, C, D)

t = np.linspace(0, 1.25, 500, endpoint=False)
u = np.linspace(0, 1, 500, endpoint=False)

t4_2, o4_2, _ = sig.lsim(ss4_2, u, t)


#=================================================================================#
# Odp
# Odpowiedź skokowa obiektu nie ustala się na konkretnej wartości lecz wykładniczo  
# narasta
#=================================================================================#

#4.3

ss4_3 = sig.StateSpace(A, B, C, D)
w4_3, mag4_3, phase4_3 = sig.bode(ss4_3)

#=================================================================================#
# Odp
# tak, wykres aplitudowy bodego ma przegięcie w jednym miejscu ze względu na 
# zaistniałą całkę
# 
#=================================================================================#

plt.subplot(221)
plt.plot(t4_1, o4_1)
plt.xlabel('t')
plt.subplot(223)
plt.plot(t4_2, o4_2)
plt.xlabel('t')
plt.subplot(222)
plt.semilogx(w4_3, mag4_3, label='mag')
plt.legend()
plt.subplot(224)
plt.semilogx(w4_3, phase4_3, label='ph')
plt.legend()
plt.show()
