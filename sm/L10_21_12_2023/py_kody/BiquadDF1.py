import numpy as np
import scipy.signal as sig

def generateBiquadDF1(name: str, tf_num : np.array, tf_den : np.array):
    sos_raw = sig.tf2sos(tf_num, tf_den)
    sos_raw = np.ndarray.astype(sos_raw, np.float32)

    num_of_stages = np.size(sos_raw, 0)

    sos_out = np.array([[b0, b1, b2, a1, a2] for b0, b1, b2, _, a1, a2 in sos_raw])
    
    sos_str = np.char.add(sos_out.astype(np.float32).astype(str).flatten(), 'f')
    sos_str = ', '.join(sos_out)

    h_file_content = np.array([
        f'#ifndef __INC_{name.upper()}_H__\n',
        f'#define __INC_{name.upper()}_H__\n',
        f'#include "arm_math.h"\n',
        f'extern uint32_t {name}_num_of_stages;\n'
        f'extern float32_t {name}_state[{4 * num_of_stages}];\n',
        f'extern float32_t {name}_coefs[{5 * num_of_stages}];\n',
        f'extern arm_biquad_casd_df1_inst_f32 {name};\n'
        f'#endif'
    ])
    file = open(f'{name}.h', 'w')
    file.writelines(h_file_content)
    file.close()

    c_file_content = np.array([
        f'#include "arm_math.h"\n',
        f'#include "{name}.h"\n',
        f'uint32_t {name}_num_of_stages = {num_of_stages};\n'
        f'float32_t {name}_state[{4 * num_of_stages}] = {{ }};\n',
        f'float32_t {name}_coefs[{5 * num_of_stages}] = {{ {sos_str} }};\n',
        f'arm_biquad_casd_df1_inst_f32 {name};\n'
    ])
    file = open(f'{name}.c', 'w')
    file.writelines(c_file_content)
    file.close()

    return sos_out

if __name__ == '__main__':
    generateBiquadDF1('myFilter', [0, 0.001, 0.001], [1, -1.9, 0.9])