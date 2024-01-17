import numpy as np
import matplotlib.pyplot as plt
import csv

class DataRaw:
    def __init__(self, current_mode : str, vin : float, iin : float, vout : float, iout : float, fs : float, duty : float, iabs : float, ipk_iso : float, ivl_iso : float):
        self.current_mode = current_mode
        self.voltage_mode = ''
        if vin < vout:
            self.voltage_mode = 'BBM' #buckboost mode
        else:
            self.voltage_mode = "BM" #buckmode
        self.mode = self.voltage_mode + '-' + self.current_mode
        self.vin = vin
        self.iin = iin
        self.vout = vout
        self.iout = iout
        self.fs = fs
        self.duty = duty
        self.ipk = ipk_iso + iabs
        self.ivl = ivl_iso + iabs
    
class DataExp:
    def __init__(self, vin, iin, vout, iout):
        self.vin = vin
        self.iin = iin
        self.vout = vout
        self.iout = iout

data_raw = np.array()
with open('data_raw.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for i_mode, vin, iin, vout, iout, fs, duty, iabs, ipk_iso, ivl_iso in reader:
        d = DataRaw(i_mode, float(vin), float(iin), float(vout), float(iout), float(duty), float(iabs), float(ipk_iso), float(ivl_iso))
        data_raw = np.append(data_raw, d)

data_exp = np.array()
with open('data_exp.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for vin, iin, vout, iout in reader:
        d = DataExp(vin, iin, vout, iout)
        data_raw = np.append(data_raw, d)

L       = 10
Rs      = 7.5e-3
Rds     = 17e3
Qgsw    = 4.7e-9
Qg      = 14e-9
Vth     = 3
Rgint   = 13
gfs     = 62
Vdr     = 7
Rdr     = 3
Vf      = 0.8
Rl      = 1.86e3


def bmCcmLosses(d : DataRaw):
    #common
    M       = d.vout / d.vin
    Dcmb    = M
    Ilb     = d.iout
    dib     = (d.vin - d.vout) * Dcmb / (d.fs * L)
    Ipkb    = Ilb + dib
    Ivlb    = Ilb - dib
    ab      = 1 + dib**2 / (12 * Ilb**2)
    ton     = Qgsw * Rgint / (Vdr - Vth - Ivlb / gfs)
    toff    = Qgsw * Rgint / (Vth + Ipkb / gfs)

    #mosfet
    loss_mos_con    = Rds * Dcmb * Ilb**2 * ab
    loss_mos_sw     = 1 / 2 * d.vin * d.fs * (Ivlb * ton + Ipkb * toff)
    loss_mos_g      = Qg * Vdr * d.fs
    loss_mos        = loss_mos_con + loss_mos_sw + loss_mos_g
    #diode
    loss_d          = (Vf + Vf(1 - Dcmb)) * Ilb * ab
    #sensing resistor
    loss_rs         = Rs * (1 - Dcmb) * Ilb**2 * ab
    #inductor
    loss_l          = Rl * Ilb**2 * ab

    #total
    loss_total      = loss_mos + loss_d + loss_rs + loss_l
    
    return loss_total

def bmdcmLosses(d : DataRaw):
    #common
    K       = 2 * d.fs * L * d.iout / d.vout
    M       = d.vout / d.vin
    Ddmb    = M / np.sqrt(1 - M) * np.sqrt(K)
    Ipkb    = (d.vin - d.vout) * Ddmb / (d.fs * L)
    D2dbm   = Ipkb * d.fs * L / d.vout
    Ilb     = 1/2 * Ipkb * (Ddmb + D2dbm)
    #ton     = Qgsw * Rgint / (Vdr - Vth - Ivlb / gfs)
    toff    = Qgsw * Rgint / (Vth + Ipkb / gfs)

    #mosfet
    loss_mos_con    = 1 / 3 * Rds * Ipkb**2 * Ddmb
    loss_mos_sw     = 1 / 2 * d.vin * d.fs * Ipkb * toff
    loss_mos_g      = Qg * Vdr * d.fs
    loss_mos        = loss_mos_con + loss_mos_sw + loss_mos_g
    #diode
    loss_d          = (Ilb * Vf + 1/2 * D2dbm * Ipkb * Vf)
    #sensing resistor
    loss_rs         = 1/3 * Rs * Ipkb**2 * D2dbm
    #inductor
    loss_l          = 1/3 * Rl * Ipkb**2 * (Ddmb + D2dbm)

    #total
    loss_total = loss_mos + loss_d + loss_rs + loss_l
    
    return loss_total

def bbmCcmLosses(d : DataRaw):
    #common
    M       = d.vout / d.vin
    Dcmbb   = M / (1 + M)
    Ilbb    = d.iout / (1 - Dcmbb)
    dibb    = (d.vin * Dcmbb) / (d.fs * L)
    Ipkbb   = Ilbb + dibb
    Ivlbb   = Ilbb - dibb
    abb     = 1 + dibb**2 / (12 * Ilbb**2)
    ton     = Qgsw * Rgint / (Vdr - Vth - Ivlbb / gfs)
    toff    = Qgsw * Rgint / (Vth + Ipkbb / gfs)
    Vtot    = 1 #???

    #mosfet
    loss_mos_con    = 2 * Rds * Dcmbb * Ilbb**2 * abb
    loss_mos_sw     = 1 / 2 * Vtot * d.fs * (Ivlbb * ton + Ipkbb * toff)
    loss_mos_g      = 2 * Qg * Vdr * d.fs
    loss_mos        = loss_mos_con + loss_mos_sw + loss_mos_g
    #diode
    loss_d          = (Vf + Vf) * (1 - Dcmbb) * Ilbb * abb
    #sensing resistor
    loss_rs         = Rs * (1 - Dcmbb) * Ilbb**2 * abb
    #inductor
    loss_l          = Rl * Ilbb**2 * abb

    #total
    loss_total      = loss_mos + loss_d + loss_rs + loss_l
    
    return loss_total

def bmdcmLosses(d : DataRaw):
    #common
    K       = 2 * d.fs * L * d.iout / d.vout
    M       = d.vout / d.vin
    Ddmbb   = M * np.sqrt(K)
    Ipkbb   = d.vin * Ddmbb / (d.fs * L)
    D2dbbm  = Ipkbb * d.fs * L / d.vout
    Ilbb    = 1/2 * Ipkbb * (Ddmbb + D2dbbm)
    #ton     = Qgsw * Rgint / (Vdr - Vth - Ivlb / gfs)
    toff    = Qgsw * Rgint / (Vth + Ipkbb / gfs)
    Vtot    = 1 #???

    #mosfet
    loss_mos_con    = 2 / 3 * Rds * Ipkbb**2 * Ddmbb
    loss_mos_sw     = 1 / 2 * Vtot * d.fs * Ipkbb * toff
    loss_mos_g      = 2 * Qg * Vdr * d.fs
    loss_mos        = loss_mos_con + loss_mos_sw + loss_mos_g
    #diode
    loss_d          = 1/2 * (Vf + Vf) * D2dbbm * Ipkbb
    #sensing resistor
    loss_rs         = 1/3 * Rs * Ipkbb**2 * D2dbbm
    #inductor
    loss_l          = 1/3 * Rl * Ipkbb**2 * (Ddmbb + D2dbbm)

    #total
    loss_total = loss_mos + loss_d + loss_rs + loss_l
    
    return loss_total