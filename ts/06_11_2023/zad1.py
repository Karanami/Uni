import numpy as np
import matplotlib.pyplot as plt
from math import sin
from scipy.signal import TransferFunction, StateSpace, lsim, step

#vars
m = 1
k = 1
b_range = [0, 1/2, 2]
###################################################
#ustawić b
###################################################
b = b_range[0]

B = [[0],
     [1/m]]
C = [1, 0]
D = 0

#zad1.1
A = [[0, 1],
     [-k/m, -b/m]]
sys1_1_ss_1 = StateSpace(A, B, C, D)


#zda1.2
t_sin = np.linspace(0, 10, 500, endpoint=False)
u_sin = [sin(2 * i) for i in t_sin]

t1_2_step_1, o1_2_step_1 = step(sys1_1_ss_1)
t1_2_sin_1, o1_2sin_1, _ = lsim(sys1_1_ss_1, u_sin, t_sin)

plt.subplot(211)
plt.plot(t1_2_step_1, o1_2_step_1)
plt.subplot(212)
plt.plot(t1_2_sin_1, o1_2sin_1)
plt.show()

#zad1.3

# układ ma charakter oscylacyjny ponieważ układ jest
# typowym przykładem układu z podwójną innercją
# która w szczegulnych przypadkach (takich jak ten - 
# bloczek na sprężynie) charakteryzuje się transmitacją
# o charakteże oscylacyjnym - posiada dwa sprzężone ze sobą
# bieguny. W zależności od siły tłumienia owe bieguny będą
# tworzyły mniejszy lub większy kąt phi który mówi nam o
# jak mocno obiekt będzie przejawiał się oscylacjami w
# odpowiedzi skokowej



