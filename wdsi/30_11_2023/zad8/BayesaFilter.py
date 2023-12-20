def bel(epsilon, action, P_previous):
    P_current = [0] * 32    
    for current_location in range(32):
        action_error = [-2, -1, 0, 1, 2]
        action_error_probability = [epsilon, 2 * epsilon, 1 - 6 * epsilon, 2 * epsilon, epsilon]
        for previous_location in range(32):
            for a_err, a_err_p in zip(action_error, action_error_probability):
                location = previous_location + action + a_err
                if location >= 31:
                    location -= 32
                if location < 0:
                    location += 32
                if location == current_location:
                    P_current[current_location] += a_err_p * P_previous[previous_location]
    return P_current
