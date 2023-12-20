import numpy as np
import scipy.signal as sig
import scipy.integrate as itg
#import scipy.integrate.odeint as ode
import matplotlib.pyplot as plt
from math import *
from zad2 import As, Bs, Cs


#zad 3.2
j = 0
s = [ -1, -2, -5 ]

As0 = As[j]
Bs0 = Bs[j]
Cs0 = Cs[j]

K = sig.place_poles(As0, Bs0, s).gain_matrix
A_ = (As0 - (Bs0 @ K))
B_ = [[0], [0], [0]]
C_ = (Cs0)

#zad 3.3
t = np.linspace(0, 10, 500, endpoint=False)

sys = sig.StateSpace(A_, B_, C_, 0)
t, o, _ = sig.lsim(sys, 0, t, [1, 1, 1])

plt.plot(t, o)
plt.show()

