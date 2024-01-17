import numpy as np
import matplotlib.pyplot as plt

class data:
    def __init__(self, current_mode : str, vin : float, iin : float, vout : float, iout : float, fs : float, duty : float, iabs : float, ipk_iso : float, ivl_iso : float):
        self.current_mode = current_mode
        self.voltage_mode = ''
        if vin < vout:
            self.voltage_mode = 'BBM' #buckboost mode
        else:
            self.voltage_mode = "BM" #buckmode
        self.mode = self.voltage_mode + '-' + self.current_mode
        self.vin = vin
        self.iin = iin
        self.vout = vout
        self.iout = iout
        self.fs = fs
        self.duty = duty
        self.ipk = ipk_iso + iabs
        self.ivl = ivl_iso + iabs
    
