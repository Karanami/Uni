import scipy.signal as sig
import scipy.optimize as opt
import numpy as np
from gekko import GEKKO
import matplotlib.pyplot as plt

model = GEKKO()

model.options.IMODE = 5

model.time = np.linspace(0, 1, 100)

x = model.Var(1)
model.fix_initial(x, 1)
model.fix_final(x, 3)

t = model.Var(0)

J = model.Var(0)
Jf = model.FV()
Jf.STATUS = 1
model.Connection(Jf, J, pos2='end')

model.Equation(t.dt() == 1)
model.Equation(J.dt() == 24*x*t + 2*x.dt()**2 - 4*t)

model.Obj(Jf)
model.solve(disp=False)

t_disc = np.linspace(0, 1)
analitic = t_disc**3 + t_disc + 1 

plt.plot(t_disc, analitic, label = 'analitic')
plt.plot(t, x.value, label = 'dynamic')
plt.legend()
plt.show()

#print(Jf.value)