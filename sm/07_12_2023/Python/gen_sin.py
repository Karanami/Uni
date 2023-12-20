from math import *
import numpy as np

import numpy as np
import matplotlib.pyplot as plt
from dataclasses import dataclass


amplitude=1000.0
phase=0.0
frequency=10.0
offset=1500.0
sample_time=0.001
time = sample_time * np.linspace(0, 99, 100)  
values = amplitude*np.sin(2*np.pi*frequency*time + phase) + offset
sine_wave = (4095/3300)*values
sine_wave = sine_wave.astype(np.int16)
out = ','.join(str(x) for x in sine_wave)
file = open('sin.h', 'w')
file.write('extern uint16_t sin_wave[] = {')
file.write(out)
file.write('};')
file.close()

print(len(sine_wave))