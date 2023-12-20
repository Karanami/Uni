import matplotlib.pyplot as plt

iout_250 = [0.1, 0.2, 0.3, 0.35, 0.4, 0.45, 0.5, 0.6] 
iout_250_rev = iout_250.copy()
iout_250_rev.reverse()
i_250 = iout_250 + iout_250_rev
vmin_250 = [7.6, 7.6, 8.7, 9.4, 10.3, 11.3, 12.3, 15.3] 
vmax_250 = [24.2, 23.9, 23.1, 22.8, 22.5, 22, 21.6, 20]
vmax_250.reverse()
v_250 = vmin_250 + vmax_250

iout_500 = [0.05, 0.1, 0.15, 0.2, 0.25, 0.3]
iout_500_rev = iout_500.copy()
iout_500_rev.reverse()
i_500 = iout_500 + iout_500_rev
vmin_500 = [7.5, 8.2, 10.1, 11.9, 12.2, 14.2]
vmax_500 = [22.6, 22.8, 22.6, 22.3, 21.2, 19.9]
vmax_500.reverse()
v_500 = vmin_500 + vmax_500

plt.plot(i_250, v_250, color='r', label = '250kHz')
plt.plot(i_500, v_500, color='b', label = '500kHz')
plt.legend()
plt.show()