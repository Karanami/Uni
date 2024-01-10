import numpy as np
import scipy.signal as sig

def generatePID(name, Kp, Ki, Kd, Ts):
    gains_out = np.array([Kp, Ki * Ts, Kd * Ts])

    gains_out = np.ndarray.astype(gains_out, np.float32).astype(str)
    gains_str = np.char.add(gains_out, 'f')
    gains_str = ', '.join(gains_str)

    h_file_content = np.array([
        f'#ifndef __INC_{name.upper()}_H__\n',
        f'#define __INC_{name.upper()}_H__\n',
        f'#include "arm_math.h"\n',
        f'extern uint32_t {name}_gains[3];\n'
        f'extern arm_pid_instance_f32 {name};\n',
        f'#endif'
    ])
    file = open(f'{name}.h', 'w')
    file.writelines(h_file_content)
    file.close()

    c_file_content = np.array([
        f'#include "arm_math.h"\n',
        f'#include "{name}.h"\n',
        f'uint32_t {name}_gains[3] = {{ {gains_str} }};\n'
        f'arm_pid_instance_f32 {name};\n'
    ])
    file = open(f'{name}.c', 'w')
    file.writelines(c_file_content)
    file.close()

    return gains_out

if __name__ == '__main__':
    generatePID('myFilter', 10, 0.1, 1, 0.01)