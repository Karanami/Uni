import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.linspace(0, 50, 1000)

kp = 2
omega = 4
epsilon = 0.25
def u(t):
    return 1

def model(x, t):
    y, dy = x
    dy2 = -2 * epsilon / omega * dy - 1 / omega * np.sqrt(y) + kp / omega**2 * u(t)
    return dy, dy2

y = odeint(model, [0, 0], t)
plt.plot(t, y[:, 0])
plt.xlabel('czas')
plt.ylabel('y(t)')
plt.show()  

# Odpowiedź: Charakter odpowiedzi układu na wymuszenie jest oscylacyjny, z tego wnioskujemy, że obiekt  również jest typu oscylacyjnego.