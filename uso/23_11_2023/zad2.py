import scipy.signal as sig
import scipy.optimize as opt
import numpy as np
from gekko import GEKKO

model = GEKKO()

x = model.Var(0)
y = model.Var(0)

model.Equations([2*x - y <= 4, y + x > 3, y + 4*x >= -2])
model.Maximize(-y)

model.solve(disp=False)

print(x.value, y.value)