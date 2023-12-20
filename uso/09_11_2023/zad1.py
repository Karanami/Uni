import numpy as np
import scipy.signal as sig
import scipy.integrate as itg
#import scipy.integrate.odeint as ode
import matplotlib.pyplot as plt
from math import *

#############################################################################
#zad 1.1                                                                    #
#############################################################################

def GetKalmanMatrix(A : np.array, B : np.array):
    n = A.shape[0]
    Ohm = [A**i @ B for i in range(n)]
    Ohm = np.concatenate(Ohm, axis=1)
    return Ohm

#1
R1 = 2
C1 = 1
R2 = 4
C2 = 0.5

A1 = np.array( [[-1/(R1*C1), 0],
                [0, -1/(R2*C2)]])
B1 = np.array( [[1/(R1*C1)],
                [1/(R2*C2)]])
ster1 = False


#rank1 = np.linalg.matrix_rank()
K = GetKalmanMatrix(A1, B1)
if np.linalg.matrix_rank(K) == A1.shape[0]:
     ster1 = True
#2
R = 1
C1 = 1
C2 = 2
C3 = 3

A2 = np.array( [[-1/(R*C1), 0, 0],
                [0, -1/(R*C2), 0],
                [0, 0, -1/(R*C3)]] )
B2 = np.array( [[1/(R*C1)],
                [1/(R*C2)],
                [1/(R*C3)]] )
ster2 = False

K = GetKalmanMatrix(A2, B2)
if np.linalg.matrix_rank(K) == A2.shape[0]:
     ster2 = True
#3
R = 1
L1 = 0.1
L2 = 0.1
C1 = 0.1
C2 = 0.1

A3 = np.array( [[0, 1/L1, 0, 0],
                [-1/C1, -1/(R*C1), 0, -1/(R*C1)],
                [0, 0, 0, 1/L2],
                [0, -1/(R*C2), -1/C2, -1/(R*C2)]] )
B3 = np.array( [[0],
                [1/(R*C1)],
                [0],
                [1/(R*C2)]] )
ster3 = False

K = GetKalmanMatrix(A3, B3)
if np.linalg.matrix_rank(K) == A3.shape[0]:
    ster3 = True

#4
R1 = 2
L1 = 0.5
R2 = 1
L2 = 1
C = 2

A4 = np.array( [[-R1/L1, 0, -1/L1],
                [0, 0, 1/L2],
                [1/C, -1/C, -R2/C]] )
B4 = np.array( [[1/L1],
                [0],
                [0]] )
ster4 = False

K = GetKalmanMatrix(A4, B4)
if np.linalg.matrix_rank(K) == A4.shape[0]:
    ster4 = True


#############################################################################
#zad 1.2                                                                    #
#############################################################################
C1 = np.array([1, 1])
C2 = np.array([1, 1, 1])
C3 = np.array([1, 1, 1, 1])
C4 = C2

t = np.linspace(0, 10, 500, endpoint=False)

u_step = [1] * len(t)
u_2step = [2] * len(t)
u_sin = [sin(ti) * (-1/2) for ti in t]

u = [u_step, u_2step, u_sin]

A = [A1, A2, A3, A4]
B = [B1, B2, B3, B4]
C = [C1, C2, C3, C4]
color = ['r', 'g', 'b', 'c']
ster = [ster1, ster2, ster3, ster4]

if(__name__ == "__main__"):
    for ui in u:
        for i in range(4):
            sys = sig.StateSpace(A[i], B[i], C[i], 0)
            t, o, _ = sig.lsim(sys, ui, t)
            plt.plot(t, o)
        plt.show()
