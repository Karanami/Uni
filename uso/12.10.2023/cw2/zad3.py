import numpy as np
import scipy.signal as sig
import scipy.integrate as itg
#import scipy.integrate.odeint as ode
import matplotlib.pyplot as plt

N = 500

R = 12
L = 1
c = 100 / 1000000 #uF

#3.1

sys1 = sig.TransferFunction([1, 0], [L, R , 1 / c])
t1s, o1s = sig.step(sys1, N=N)
t1i, o1i = sig.impulse(sys1, N=N)

#plt.figure(1)
#plt.subplot(211)
#plt.plot(t1s, o1s)
#plt.subplot(212)
#plt.plot(t1i, o1i)
#plt.show()

#3.2
A = np.array([ [0, 1], [-1 / ( L * c ), -R / L]])
B = np.array([[0], [1 / L]])
C = np.array([0, 1])
D = 0

sys2 = sig.StateSpace(A,B,C,D)
t2s, o2s = sig.step(sys2, N=N)
t2i, o2i = sig.impulse(sys2, N=N)

#plt.figure(2)
#plt.subplot(211)
#plt.plot(t1s, o1s)
#plt.subplot(212)
#plt.plot(t1i, o1i)
#plt.show()
plt.subplot(211)
plt.plot(t1s, o1s, label='1')
plt.plot(t2s, o2s, 'r:', label='2')
plt.legend()
plt.subplot(212)
plt.plot(t1i, o1i, label='1')
plt.plot(t2i, o2i, 'r:', label='2')
plt.legend()
plt.xlabel('t')
plt.show()

#print(sys1.poles)

#=================================================================================#
#Odp
#Tak odpowiedzi się pokrywają, obiekt ma charakter oscylacyjny ponieważ posiada dwa
#sprzężone bieguny na płaszczyźnie zmiennej s które nie leżą na osi rzeczywistej
#(-6 + 99.82j ; -6 - 99.82j) oraz odległość tych punktów od osi rzeczywistej jest
#kilkukrotnie większa od odległości od osi urojonej co nadaje obiektowi mocny 
#charakter oscylacyjny.
#Odpowiedzi impulsowe przyjmują niezerowe wartości początkowe, ponieważ nwm
# {{ transmitacja ma człon różniczkujący z innercją drugiego rzędu co ze względu
# na jego charakterystykę sprawia że system przyjmuje niezerową wartość początkową
# - całka w nieskończoności }}
#=================================================================================#

#3.3
print(sys1.num, " / ", sys1.den)
num, den = sig.ss2tf(A, B, C, D)
print(num, " / ", den)
print("")
print(sys2.A, sys2.B, sys2.C, sys2.D, sep="\n")
A, B, C, D = sig.tf2ss([1, 0], [L, R , 1 / c])
print("")
print(A, B, C, D, sep="\n")

#=================================================================================#
#Odp
#Nie, ss2tf nie zwraca transmitacji identycznej do podanej we wzorze 17 
# [1. 0.]  /  [1.0e+00 1.2e+01 1.0e+04] (sys1)
# [0.00000000e+00 1.00000000e+00 3.63797881e-12]  /  [1.0e+00 1.2e+01 1.0e+04] (ss2tf)
#jednakże porównając wyniki można stwierdzić że są one identyczne ponieważ błąd wyniku
#wynika najprawdopodobniej z błędu przybliżania liczby zmienno przecinkowej 
#"3.63797881e-12", którą można potraktować jako "0.0"
#=================================================================================#