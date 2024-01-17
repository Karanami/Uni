import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import scipy.signal as sig

t = np.linspace(0,10, 200)

kp = 2
T = 2
kob = 4

def feedback(x, t, xd):
    x, x_sat = x
    
    u       = kp * (xd - x)
    u_sat   = np.clip(kp * (xd - x_sat), -0.1, 0.1)

    dy      = kob / T  * u      -   1 / T * x
    dy_sat  = kob / T * u_sat   -   1 / T * x_sat
    return dy, dy_sat


y1 = odeint(feedback, [0,0], t, args = tuple([1]))
y2 = odeint(feedback, [0,0], t, args = tuple([2]))
y3 = odeint(feedback, [0,0], t, args = tuple([3]))

plt.plot(t, y1[:, 0], label = 'xd = 1')
plt.plot(t, y2[:, 0], label = 'xd = 2')
plt.plot(t, y3[:, 0], label = 'xd = 3')
plt.xlabel('czas')
plt.ylabel('y(t)')
plt.legend()
plt.title('Z ograniczeniami')
plt.show()

plt.plot(t, y1[:, 1], label = 'xd = 1')
# mały offset żeby było widac wykresy
plt.plot(t, y2[:, 1] - 0.001, label = 'xd = 2')
plt.plot(t, y3[:, 1] + 0.001, label = 'xd = 3')
plt.xlabel('czas')
plt.ylabel('y(t)')
plt.legend()
plt.title('Bez ograniczen')
plt.show() 

#zad 2
# Odpowiedź: W wyniku zastosowania ograniczeń wartości sygnału sterującego wchodzi on w nasycenie w wuniku czego
# zasada superpozycji i skalowania nie jest zachowana, obiekt nie ma charakteru liniowego, mimo iż zachowuje się jak linowy.

#zad 3
# OdpowiedźTak układ ma charakter liniowy po wyeliminowaniu ograniczeń na sygnale 