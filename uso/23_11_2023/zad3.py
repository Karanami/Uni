import scipy.signal as sig
import scipy.optimize as opt
import numpy as np
from gekko import GEKKO

model = GEKKO()

x = model.Var(1, lb = 0)

model.Minimize(x**4 - 4*x**3 - 2*x**2 + 12*x + 9)

model.solve(disp=False)

print(x.value)