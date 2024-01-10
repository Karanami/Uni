import numpy as np
import scipy.signal as sig
import matplotlib.pyplot as plt

ts = 0.001
fs = 1/ts 
tmax = 1
tvec = np.arange(0, tmax, ts) 
nvec = np.arange(0, len(tvec))

Tx = 0.1
xvec = (3.3/2) * (np.square(2 * np.pi * tvec/Tx) + 1)
frange = np.arange(-1/2, 1/2, 1/len(nvec)) 
fxvec = frange * fs         
Axvec = abs(np.fft.fftshift(np.fft.fft(xvec, len(nvec))))
Axvec = Axvec / len(nvec)

f1 = 10 
f2 = 50
df = f2 - f1
A = 50
N = round( (fs/df)*A / 22 )
w = f1 / (fs/2)
b = sig.firwin(N, w)
n = 10**4 
frange = np.arange(-1/2, 1/2, 1/n)
fhvec = frange * fs
_, Ahvec_v1 = np.abs(sig.freqz(b, 1, 2*np.pi*frange))
Ahvec_v1 = 20 * np.log10(Ahvec_v1)
Ahvec_v2 = np.abs(np.fft.fftshift(np.fft.fft(b,n)))
Ahvec_v2 = 20 * np.log10(Ahvec_v2)
xfvec = sig.lfilter(b, 1, xvec)
Axfvec = abs(np.fft.fftshift(np.fft.fft(xfvec, len(nvec)))) # [-]
Axfvec = Axfvec / len(nvec)
fminmax = [-10, fs/2]
tminmax = [0, tmax]
Aminmax = [-0.1, 3.5]
AdBminmax = [-120, 5]

plt.subplot(2,2,1)
plt.plot(nvec/fs, xvec, 'b')
plt.xlabel("Time [s]")
plt.ylabel("Amplitude [-]")
plt.title('Orginal test signal time series')

plt.subplot(2,2,2)
plt.plot(fxvec, Axvec, '-')
plt.xlabel("Frequency [Hz]")
plt.ylabel("Amplitude spectrum [-]")
plt.plot(fhvec, Ahvec_v1, '-')
plt.ylabel("Amplitude response [dB]") 
plt.plot([f1, f1], AdBminmax, 'k--')
plt.plot([f2, f2], AdBminmax, 'k--') 
plt.title('Original test signal ampltitude spectrum')

plt.subplot(2,2,3)
plt.plot(nvec/fs, xfvec, 'b')
plt.xlabel("Time [s]")
plt.ylabel("Amplitude [-]")
plt.title('Filtered test signal time series')


plt.subplot(2,2,4)
plt.plot(fxvec, Axfvec, '-')
plt.xlabel("Frequency [Hz]")
plt.ylabel("Amplitude spectrum [-]")
plt.plot(fhvec, Ahvec_v2, '-')  
plt.ylabel("Amplitude response [dB]") 
plt.plot([f1, f1], AdBminmax, 'k--')
plt.plot([f2, f2], AdBminmax, 'k--') 
plt.title('Filtered test signal ampltitude spectrum')
  
plt.show()