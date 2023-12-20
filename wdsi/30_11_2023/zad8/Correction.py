import numpy as np

def correction(epsilon_true, epsilon_false, percept, P_previous):
    P_current = [0] * 32    
    percept_error = [-2, -1, 0, 1, 2]
    percept_error_probability = [1 - epsilon_true, epsilon_true, 1 - epsilon_false, epsilon_false]
    for p_err, p_err_p in zip(percept_error, percept_error_probability):
        if 0 <= percept + p_err < 32:
            P_current[percept + p_err] = p_err_p
    P_current = np.multiply(P_current, P_previous)
    P_current /= np.sum(P_current)
    return P_current
