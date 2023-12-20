import numpy as np

def correction(epsilon, percept, P_previous):
    P_current = [0] * 32    
    percept_error = [-2, -1, 0, 1, 2]
    percept_error_probability = [epsilon, 2*epsilon, 1 - 6*epsilon, 2*epsilon, epsilon]
    for p_err, p_err_p in zip(percept_error, percept_error_probability):
        if 0 <= percept + p_err < 32:
            P_current[percept + p_err] = p_err_p
    P_current = np.multiply(P_current, P_previous)
    P_current /= np.sum(P_current)
    return P_current
