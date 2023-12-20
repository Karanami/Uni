import numpy as np
import scipy.signal as sig
import scipy.integrate as itg
#import scipy.integrate.odeint as ode
import matplotlib.pyplot as plt
from math import *
from zad1 import A, B, C, u, t, ster, GetKalmanMatrix

    # L1, M1 = signal.ss2tf(A1, B1, C1, D1)
    # A1s = [[0, 1], [-0.25, -1]]
    # B1s = [[0], [1]]

L2, M2 = sig.ss2tf(A[1], B[1], C[1], 0)
A2s = np.array([[0, 1, 0], [0, 0, 1], [-M2[3], -M2[2], -M2[1]]])
B2s = np.array([[0], [0], [1]])
K2 = GetKalmanMatrix(A[1], B[1])
K2s = GetKalmanMatrix([1], B[1])

P2_inv = K2 @ np.linalg.inv(K2s)
P2 = np.linalg.inv(P2_inv)

L4, M4 = sig.ss2tf(A[3], B[3], C[3], 0)
A4s = np.array([[0, 1, 0], [0, 0, 1], [-M4[3], -M4[2], -M4[1]]])
B4s = np.array([[0], [0], [1]])
K4s = np.hstack((B4s, A4s @ B4s, A4s @ A4s @ B4s))

A2s = P2 @ A[1] @ P2_inv
B2s = P2 @ B[1]
C2s = C[1] @ P2_inv
D2s = 0

t2_ua, y2_ua, x2_ua = sig.lsim2([A[1], B[1], C[1], 0], u[0], t)
t2_ub, y2_ub, x2_ub = sig.lsim([A[1], B[1], C[1], 0], u[1], t)
t2_uc, y2_uc, x2_uc = sig.lsim([A[1], B[1], C[1], 0], u[2], t)
t2s_ua, y2s_ua, x2s_ua = sig.lsim([A2s, B2s, C2s, D2s], u[0], t)
t2s_ub, y2s_ub, x2s_ub = sig.lsim([A2s, B2s, C2s, D2s], u[1], t)
t2s_uc, y2s_uc, x2s_uc = sig.lsim([A2s, B2s, C2s, D2s], u[2], t)

plt.figure()
plt.subplot(1, 2, 1)
plt.plot(t2_ua, y2_ua, label=('y(t) u(t) = 1(t)'))
plt.plot(t2_ub, y2_ub, label=('y(t) u(t) = 2*1(t)'))
plt.plot(t2_ub, y2_uc, label=('y(t) u(t) = sint(t)*1(t) -1/2'))
plt.title('y2(t)')
plt.subplot(1, 2, 2)
plt.plot(t2s_ua, y2s_ua, label=('ys(t) u(t) = 1(t)'))
plt.plot(t2s_ub, y2s_ub, label=('ys(t) u(t) = 2*1(t)'))
plt.plot(t2s_ub, y2s_uc, label=('ys(t) u(t) = sint(t)*1(t) -1/2'))
plt.title('y2s(t)')
plt.show()