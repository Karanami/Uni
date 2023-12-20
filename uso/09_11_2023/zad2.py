import numpy as np
import scipy.signal as sig
import scipy.integrate as itg
#import scipy.integrate.odeint as ode
import matplotlib.pyplot as plt
from math import *
from zad1 import A, B, C, u, t, ster, GetKalmanMatrix

As = []
Bs = []
Cs = []
index = []

def getAs(den) -> np.array:
    l = len(den) - 1
    temp1 = []
    for i in range(l - 1):
        temp2 = [0] * l
        temp2[i + 1] = 1
        temp1.append(temp2)
    temp3 = den * -1
    temp3 = temp3.tolist()
    temp3.reverse()
    temp1.append(temp3[0:l])
    return np.array(temp1)

def getBs(den) -> np.array:
    l = len(den) - 1
    temp1 = [[0]] * l
    temp1[-1] = [1]
    return np.array(temp1)

def getPT(A : np.array, B : np.array, As : np.array, Bs : np.array) -> np.array:
    n = A.shape[0]
    temp1 = GetKalmanMatrix(A, B)
    temp2 = np.linalg.inv(GetKalmanMatrix(As, Bs))
    temp3 = temp1 @ temp2
    return temp3


for i in range(4):
    if ster[i]:
        _, den = sig.ss2tf(A[i], B[i], C[i], 0)
        ast = getAs(den)
        bst = getBs(den)
        p_inv = getPT(A[i], B[i], ast, bst)
        p = np.linalg.inv(p_inv)
        As.append(p @ A[i] @ p_inv)
        Bs.append(p @ B[i])
        Cs.append(C[i] @ p_inv)
        index.append(i)

if(__name__ == "__main__"):
    for ui in u:
        for a, b, c, i in zip(As, Bs, Cs, index):
            sys = sig.StateSpace(a, b, c, 0)
            t, o, x = sig.lsim(sys, ui, t)
            plt.plot(t, x, label=str(i)+'.1')
            sys = sig.StateSpace(A[i], B[i], C[i], 0)
            t, o, x = sig.lsim(sys, ui, t)
            plt.plot(t, x, ':', label=str(i)+'.2')
        
        plt.legend()
        plt.show()
