import numpy as np
from scipy.linalg import expm, solve_continuous_are, solve_continuous_lyapunov
from scipy import signal
import matplotlib.pyplot as plt


m = 1
k = 1
b = 1/2

A = np.array([[0, 1],
              [-k/m, -b/m]])

B = np.array([[0],
              [1/m]])

C = np.array([1, 0])

T_s = 0.1

A_disk = expm(A * T_s)
B_disk = np.dot(np.dot(np.linalg.inv(A), (A_disk - np.eye(2))), B)

sys_d = signal.dlti(A_disk, B_disk, C, 0, dt=T_s)
sys_c = signal.lti(A, B, C, 0)

t = np.arange(0, 10, T_s)

u = np.ones_like(t)

t_disk, y_disk, x_ddisk = signal.dlsim(sys_d, u, t)
t_conti, y_cconti, x_cconti = signal.lsim(sys_c, u, t)


plt.plot(t_disk, y_disk, label='dyskretny')
plt.plot(t_conti, y_cconti, '.r', label='ciagly')
plt.legend()
plt.xlabel('czas')
plt.ylabel('odpowiedz')
plt.title('modele')
plt.grid()
plt.show()


# 1.    Mniejszy okres próbkowania polepsza jakość modelu dyskretnego, jednakże zwiększa to złożoność obliczeniową
# 2.    Model dyskretny nie zawsze odwzorowuje model ciągły przy różnych wartościach okresu próbkowania. 
#       Szczególnie przy małych okresach, mogą pojawić się problemy numeryczne spowodowane niedokładnością liczb 
#       zmienno przecinkowych

Q = 0.001 * np.eye(2)
R = 0.01 * np.eye(1)

x = np.array([[2], [0]])
P = 0.2 * np.eye(2)

T_s = 0.1
t = np.arange(0, 10, T_s)

u = np.sin(np.pi*t)

sys = signal.TransferFunction([1], [1, 1, 0.5])
t, y_rzeczywiste, x_rzeczywiste = signal.lsim(sys, u, t)

y_mierzone = y_rzeczywiste + np.random.normal(0, np.sqrt(R[0, 0]), len(t))

x_estymowane = []
P_poprzednie = []

for k in range(len(t)):
    x_przew = A * x + B * u[k]
    P_minus = A * P * A.T + Q

    korekta = y_mierzone[k] - C * x_przew
    S = C * P_minus * C.T + R
    K = P_minus * C.T * np.linalg.inv(S)

    x = x_przew + K * korekta
    P = (np.eye(2) - K * C) * P_minus

    x_estymowane.append(x.flatten())
    P_poprzednie.append(P.flatten())

x_estymowane = np.array(x_estymowane)
P_poprzednie = np.array(P_poprzednie)

plt.figure(figsize=(12, 6))
plt.subplot(211)
plt.plot(t, y_rzeczywiste, label='rzeczywiste')
plt.plot(t, y_mierzone, 'r.', label='mierzone')
plt.plot(t, x_estymowane[:, 0], 'g-', label='estymowane')
plt.title('wyjścia')
plt.xlabel('czas')
plt.grid()
plt.legend()

plt.subplot(212)
plt.plot(t, x_rzeczywiste[:, 0], label='rzeczywisty')
plt.plot(t, x_estymowane[:, 0], 'g-', label='estymowany')
plt.title('stany')
plt.xlabel('czas')
plt.legend()
plt.grid()

plt.tight_layout()
plt.show()

# tak można poprawić jakość estymacji