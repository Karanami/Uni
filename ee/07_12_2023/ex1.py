from math import *
import matplotlib.pyplot as plt 
import numpy as np

fs = 0.5e6
L = 10e-6
Vout = 24

def Dcm(Vin, Iout):
    M = Vin / Vout
    return M
def Ddm(Vin, Iout):
    M = Vin / Vout
    K = 2 * fs * Iout * L / Vout
    return sqrt(M ** 2 * K)

def Idcm(Vin):
    M = Vout / Vin
    return Vout * (M - 1) / (2 * M**3 * fs * L)

def Duty(x : tuple()):
    Vin, Iout = x
    duty = 0
    if Iout < Idcm(Vin):
        duty = Ddm(Vin, Iout)
    else:
        duty = Dcm(Vin, Iout)
    return duty

u = [10, 15, 20, 10, 15, 20, 10, 15, 20, 10, 15, 20, 10, 15, 20, 10, 15, 20, 10, 15, 20, 10, 15, 20]
i = [0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
data = [[u[k], i[k // 3]] for k in range(len(u))]

duty = [ [x[0], x[1], Duty(x)] for x in data ]
# print(duty)

bars = []
values_dcm = []
values_ccm = []

for vin, iout, duty in duty:
    bars.append('v:' + str(vin) + '\ni:' + str(iout))
    if iout < Idcm(vin):
        values_dcm.append(duty)
        values_ccm.append(0)
    else:
        values_dcm.append(0)
        values_ccm.append(duty)
        

values_exp_ccm = [0] * 9 + [0.38, 0.57, 0.77, 0.38, 0.58, 0.76, 0.38, 0.57, 0.76, 0.38, 0.56, 0.75, 0.37, 0.56, 0.76]
values_exp_dcm = [0.47, 0.73, 0.84, 0.37, 0.66, 0.81, 0.37, 0.65, 0.79] + [0] * 15
x = np.arange(len(bars))
width = 0.2
plt.bar(x - width / 2, values_dcm, width, color = 'r', alpha=0.5, label = 'Theo_dcm')
plt.bar(x - width / 2, values_ccm, width, color = 'g', alpha=0.5, label = 'Theo_ccm')
plt.bar(x + width / 2, values_exp_ccm, width, color = 'b', alpha=0.5, label = 'Exp')
plt.bar(x + width / 2, values_exp_dcm, width, color = 'm', alpha=0.5, label = 'Exp')
plt.xticks(x, bars)
plt.legend()
plt.show()