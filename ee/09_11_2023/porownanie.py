from zad1 import n_theo_all as nt_250
from zad1 import n_exp_all as ne_250
from zad2 import ripple as r_250
from zad2 import n_theo_all as nt_500
from zad2 import n_exp_all as ne_500
from zad2 import ripple as r_500
import matplotlib.pyplot as plt

iout = [100, 200, 500, 1000, 1200, 1500, 100, 200, 500, 1000, 1200, 1500]

plt.figure()
#plt.axis([0, 1.5, 65, 100])
plt.plot(iout[0:6], nt_250[0:6], 'b:', label='theo 250')
plt.plot(iout[0:6], ne_250[0:6], 'b-', label='exp 250')
plt.plot(iout[0:6], nt_500[0:6], 'r:', label='theo 500')
plt.plot(iout[0:6], ne_500[0:6], 'r-', label='exp 500')
plt.ylabel('%')
plt.xlabel('A')
plt.legend()
plt.title('6V', pad = 12.0)
plt.figure()
#plt.axis([0, 1.5, 65, 100])
plt.plot(iout[6:12], nt_250[6:12], 'b:', label='theo 250')
plt.plot(iout[6:12], ne_250[6:12], 'b-', label='exp 250')
plt.plot(iout[6:12], nt_500[6:12], 'r:', label='theo 500')
plt.plot(iout[6:12], ne_500[6:12], 'r-', label='exp 500')
plt.ylabel('%')
plt.xlabel('A')
plt.legend()
plt.title('24V', pad = 12.0)
plt.show()
plt.figure()
#plt.axis([0, 1.5, 65, 100])
plt.plot(r_250[0], nt_250[0], 'ro', label='theo 250 6V')
plt.plot(r_500[0], nt_500[0], 'b.', label='theo 500 6V')
plt.ylabel('%')
plt.xlabel('mA')
plt.legend()
#plt.axis([0, 1.5, 65, 100])
plt.plot(r_250[6], nt_250[6], 'go', label='theo 250 24V')
plt.plot(r_500[6], nt_500[6], 'm.', label='theo 500 24V')
plt.ylabel('%')
plt.xlabel('mA')
plt.legend()
plt.show()
