import numpy as np

def idcmbm(vout, vin, fs, l):
    return vout * (1-vout/vin)/(2 * fs * l)
def vdcmbm(vout, iout, fs, l):
    return vout / (1 - 2 * fs * l * iout / vout)

def idcmbbm(vout, vin, fs, l):
    return vout / (2 * fs * l * (1 + vout/vin)**2)
def vdcmbbm(vout, iout, fs, l):
    return np.sqrt(vout) / (1 / np.sqrt(2 * fs * l) - 1/np.sqrt(vout))

def getdcmf(mode):
    if mode == 0:
        return (idcmbbm, vdcmbbm)
    elif mode == 1:
        return (idcmbm, vdcmbm)

vout = np.array([12] * 12)
vin = np.array([10] * 6 + [20] * 6)
fs = np.array(([150000] * 3 + [300000] * 3) * 2)
iout = np.array([0.1, 0.5, 1] * 4)
mode = np.array([0] * 6 + [1] * 6)
funs = np.array([getdcmf(m) for m in mode])
l = np.array([10e-6] * 12)
m = vout / vin

all_data = zip(vout, vin, iout, fs, l, funs)
is_dcm = np.array([])

for vo, vi, io, f, ll, fun in all_data:
    idcm = fun[0](vo, vi, f, ll)
    vdcm = fun[1](vo, io, f, ll)
    if io < idcm or vi > vdcm:
        is_dcm = np.append(is_dcm, 'DCM')
    else:
        is_dcm = np.append(is_dcm, 'CCM')


d = np.array([])
for is_d, mode, vo, io, f, ll in zip(is_dcm, mode, vout, iout, fs, l):
    if is_d == 'DCM':
        k = 2 * f * ll * io / vo
        if mode == 0:
            d = np.append(d, 12/10 * np.sqrt(k))
        else:
            d = np.append(d, 12/20 * np.sqrt(k / (1 - 12/20)))
    else:
        if mode == 0:
            d = np.append(d, (12/10) / (1 + 12/10))
        else:
            d = np.append(d, (12/20))
        

d = np.round(d, 2)

is_dcm_exp = ['DCM'] * 4 + ['CCM'] * 2 + ['DCM'] * 3 + ['CCM'] + ['DCM'] * 2
T = 1 / fs * 10e6
td = [1.44, 3.24, 3.8, 1.09, 2.05, 2.05, 1.08, 2.38, 3.34, 2.25, 1.65, 0.8]
d_exp = np.round(td / T * 10, 2)
print('is_dcm:\t\t', is_dcm.tolist())
print('is_dcm_exp:\t', is_dcm_exp)
print('d:\t\t', d.tolist())
print('d_exp:\t\t', d_exp.tolist())


