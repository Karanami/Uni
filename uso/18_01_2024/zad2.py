import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

#zad 1 & 2
t = np.linspace(0,10, 200)
def model(x,t):
    dy = t**2
    return dy

y2 = (t**3) / 3
y = odeint(model, [0], t)
plt.plot(t, y, '.r', label = "numeryczne")
plt.plot(t, y2, label = "analityczne")
plt.legend()
plt.xlabel('czas')
plt.ylabel('y(t)')
plt.show()

# Odpowiedź: Rozwiązania się pokrywają, do obliczenia rozwiązania odeint używa algorytmu lsoda.