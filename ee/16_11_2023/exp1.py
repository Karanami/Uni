import numpy as np
from math import sqrt

fs = 500e3
L = 10e-6

Vout = np.array([24.0] * 3)
Vin = np.array([10.0, 15.0, 20.0])
Iout = np.array([0.2, 0.4, 0.9])

M = Vout / Vin

Idcm = Vout * (M - 1) / (2 * np.power(M, 3) * fs * L)

D = np.array([])

for iout, idcm, m, vout in zip(Iout, Idcm, M, Vout):
    if iout >= idcm:
        D = np.append(D, 1 - 1 /m)
    else:
        k = 2 * fs * iout * L / vout
        D = np.append(D, sqrt(m * (m-1) * k))
        
print(D)