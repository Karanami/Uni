import csv
import matplotlib.pyplot as plt

file = open("dane.csv", "r")
data = list(csv.reader(file, delimiter=";"))
file.close()

pwms = list()
luxs = list()

for lux, pwm in data:
    pwms.append(int(pwm))
    luxs.append(int(lux))
    
plt.plot(pwms, luxs, 'r')
plt.show()