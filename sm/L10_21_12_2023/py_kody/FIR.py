import numpy as np
import scipy.signal as sig

def generateFIR(name: str, fir_coeffs : np.array, block_size : np.array):

    fir_out = np.ndarray.astype(np.array(fir_coeffs), np.float32).astype(str)
    fir_str = np.char.add(fir_out, 'f')
    fir_str = ', '.join(fir_out)

    num_taps = len(fir_coeffs)

    h_file_content = np.array([
        f'#ifndef __INC_{name.upper()}_H__\n',
        f'#define __INC_{name.upper()}_H__\n',
        f'#include "arm_math.h"\n',
        f'extern uint32_t {name}_num_taps;\n'
        f'extern float32_t {name}_state[{num_taps + block_size - 1}];\n',
        f'extern float32_t {name}_coefs[{num_taps}];\n',
        f'extern arm_fir_instance_f32 {name};\n'
        f'#endif'
    ])
    file = open(f'{name}.h', 'w')
    file.writelines(h_file_content)
    file.close()

    c_file_content = np.array([
        f'#include "arm_math.h"\n',
        f'#include "{name}.h"\n',
        f'uint32_t {name}_num_taps = {num_taps};\n'
        f'float32_t {name}_state[{num_taps + block_size - 1}] = {{}};\n',
        f'float32_t {name}_coefs[{num_taps}] = {{ {fir_str} }};\n',
        f'arm_fir_instance_f32 {name};\n'
    ])
    file = open(f'{name}.c', 'w')
    file.writelines(c_file_content)
    file.close()

if __name__ == '__main__':
    generateFIR('myFilter', [1/3, 1/3, 1/3], 1)