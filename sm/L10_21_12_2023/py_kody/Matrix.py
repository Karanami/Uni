import numpy as np
import scipy.signal as sig

def generateMatrix(name, x):
    rows = np.size(x, 0)
    cols = np.size(x, 1)
    x_out = np.ndarray.astype(np.array(x), np.float32).astype(str).flatten()
    x_out = np.char.add(x_out, 'f')
    x_str = ', '.join(x_out)

    h_file_content = np.array([
        f'#ifndef __INC_{name.upper()}_H__\n',
        f'#define __INC_{name.upper()}_H__\n',
        f'#include "arm_math.h"\n',
        f'extern uint32_t {name}_rows;\n'
        f'extern uint32_t {name}_cols;\n'
        f'extern float32_t {name}_data[{rows * cols}];\n'
        f'extern arm_matrix_instance_f32 {name};\n'
        f'#endif'
    ])
    file = open(f'{name}.h', 'w')
    file.writelines(h_file_content)
    file.close()

    c_file_content = np.array([
        f'#include "arm_math.h"\n',
        f'#include "{name}.h"\n',
        f'uint32_t {name}_rows = {rows};\n'
        f'uint32_t {name}_cols = {cols};\n'
        f'float32_t {name}_data[{rows * cols}] = {{ {x_str} }};\n'
        f'arm_matrix_instance_f32 {name};\n'
    ])
    file = open(f'{name}.c', 'w')
    file.writelines(c_file_content)
    file.close()

if __name__ == '__main__':
    generateMatrix('myFilter', [[0, 1, 2], [3, 4, 5]])