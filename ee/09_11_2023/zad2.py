from math import *
import matplotlib.pyplot as plt

################################################################################################################
Vin = 6
f_s = 500 #kHz
################################################################################################################
R_ds = 180e-3 #mOhm
Q_g = 3e-9 #C
alpha_sw = 0.25e-9 #s/V
#t_sw = alpha_sw * Vin
def t_sw(Vin):
    return alpha_sw * Vin
V_dr = 6 #V
R_sns = R_ds
I_u = 116e-6 #A

def V_f(i):
    return 0.14286 * i + 0.33571

L = 18e-6
ESR_L = 80e-3
K_1 = 0.261
K_2 = 0.92
x = 1.21
y = 2.01
C_in = 4.7e-6
ESR_cin = 5e-3
Cout = 220e-6
ESR_cout = 25e-3
T_s = 1 / f_s

################################################################################################################

def D(Vout, Vin):
    return Vout / Vin

def delta_i_pp(Vout, Vin):
    d = (1 - D(Vout, Vin))
    dom = (f_s * L)
    res = Vout *  d / dom
    return res / 1000

def alpha_pp(Iout, Vout, Vin):
    ipp = delta_i_pp(Vout, Vin)
    return 1 + (ipp / Iout)**2 / 12

def P_MOSc(Iout, Vout, Vin):
    app = alpha_pp(Iout, Vout, Vin)
    d = D(Vout, Vin)
    return R_ds * d * Iout**2 * app

def P_MOSsw(Iout, Vin):
    return Vin * Iout * f_s * t_sw(Vin)

def P_MOSg():
    return Q_g * V_dr * f_s

def P_diode(Iout, Vout, Vin):
    return V_f(Iout) * (1 - D(Vout, Vin)) * Iout

def P_Lw(Iout, Vout, Vin):
    return ESR_L * Iout**2 * alpha_pp(Iout, Vout, Vin)

def P_Lc(Vout, Vin):
    return (K_1 * f_s**x * (K_2 * delta_i_pp(Vout, Vin))**y) * 10**-3

def P_Cin(Iout, Vout, Vin):
    return ESR_cin * Iout**2 * (1 - D(Vout, Vin)) * D(Vout, Vin)

def P_Cout(Vout, Vin):
    return ESR_cout * delta_i_pp(Vout, Vin)**2 / 12

def P_IC(Vin):
    return Vin * I_u

################################################################################################################

def P_loss(Iout, Vout, Vin):
    pmosc = P_MOSc(Iout, Vout, Vin) 
    pmossw = P_MOSsw(Iout, Vin) 
    pmosg = P_MOSg() 
    pdiode = P_diode(Iout, Vout, Vin) 
    plw = P_Lw(Iout, Vout, Vin) 
    plc = P_Lc(Vout, Vin) 
    pcin = P_Cin(Iout, Vout, Vin) 
    pcout = P_Cout(Vout, Vin) 
    pic = P_IC(Vin)
    return pmosc + pmossw + pmosg + pdiode + plw + plc + pcin + pcout + pic

def P_mos(Iout, Vout, Vin):
    pmosc = P_MOSc(Iout, Vout, Vin) 
    pmossw = P_MOSsw(Iout, Vin) 
    pmosg = P_MOSg() 
    return pmosc + pmossw + pmosg

def P_L(Iout, Vout, Vin):
    plw = P_Lw(Iout, Vout, Vin) 
    plc = P_Lc(Vout, Vin)
    return plw + plc
    

def P_out(Iout, Vout):
    return Iout * Vout

def n_theo(Iout, Vout, Vin):
    pout = P_out(Iout, Vout)
    ploss =  P_loss(Iout, Vout, Vin)
    return pout / (pout + ploss) * 100

################################################################################################################

vin = [6, 6, 6, 6, 6, 6, 24, 24, 24, 24, 24, 24]
vout = [3.3] * len(vin)
iout = [100, 200, 500, 1000, 1200, 1500, 100, 200, 500, 1000, 1200, 1500]
iout = [i / 1000 for i in iout]

n_theo_all = [n_theo(iout[i], vout[i], vin[i]) for i in range(len(vin))]
n_exp_all = [ 85.84333333, 89.22102981, 88.95821429, 84.95139234, 83.11599493, 80.77813425, 67.748625, 72.30333333, 77.88795455, 78.63790709, 77.72569115, 76.62990012]
ripple = [delta_i_pp(vout[i], vin[i]) for i in range(len(vin))]

if __name__ == '__main__':
    plt.subplot(211)
    plt.axis([0, 1.6, 65, 100])
    plt.plot(iout[0:6], n_theo_all[0:6], label='theo')
    plt.plot(iout[0:6], n_exp_all[0:6], label='exp')
    plt.ylabel('%')
    plt.xlabel('A')
    plt.legend()
    plt.title('6V')
    plt.subplot(212)
    plt.axis([0, 1.6, 65, 100])
    plt.plot(iout[6:12], n_theo_all[6:12], label='theo')
    plt.plot(iout[6:12], n_exp_all[6:12], label='exp')
    plt.ylabel('%')
    plt.xlabel('A')
    plt.legend()
    plt.title('24V')
    plt.show()

    pmos = [P_mos(iout[i], vout[i], vin[i]) for i in range(len(vin))]
    pdiode = [P_diode(iout[i], vout[i], vin[i]) for i in range(len(vin))]
    pl = [P_L(iout[i], vout[i], vin[i]) for i in range(len(vin))]
    pcin = [P_Cin(iout[i], vout[i], vin[i]) for i in range(len(vin))]
    pout = [P_Cout(vout[i], vin[i]) for i in range(len(vin))]
    pic = [P_IC(vin[i]) for i in range(len(vin))]

    plt.subplot(211)
    plt.plot(iout[0:6], pmos[0:6], label='mos')
    plt.plot(iout[0:6], pdiode[0:6], label='diode')
    plt.plot(iout[0:6], pl[0:6], label='l')
    plt.plot(iout[0:6], pcin[0:6], label='cin')
    plt.plot(iout[0:6], pout[0:6], label='cout')
    plt.plot(iout[0:6], pic[0:6], label='ic')
    plt.ylabel('W')
    plt.xlabel('A')
    plt.legend()
    plt.title('6V')
    plt.subplot(212)
    plt.plot(iout[6:12], pmos[6:12], label='mos')
    plt.plot(iout[6:12], pdiode[6:12], label='diode')
    plt.plot(iout[6:12], pl[6:12], label='l')
    plt.plot(iout[6:12], pcin[6:12], label='cin')
    plt.plot(iout[6:12], pout[6:12], label='cout')
    plt.plot(iout[6:12], pic[6:12], label='ic')
    plt.ylabel('W')
    plt.xlabel('A')
    plt.legend()
    plt.title('24V')
    plt.show()

#print(n_theo_all)