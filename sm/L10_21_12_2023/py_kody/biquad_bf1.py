import numpy as np
import scipy.signal as sig

def genSos(tf_num : np.array, tf_den : np.array):
    sos = sig.tf2sos(tf_num, tf_den)
    sos = np.ndarray.astype(sos, float)
    
    out = [[b0, b1, b2, a1, a2] for b0, b1, b2, a0, a1, a2 in sos]
    
    return out

print(genSos([15, 2, 3], [2, 3]))