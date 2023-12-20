import csv
import matplotlib.pyplot as plt

file = open("dane.csv", "r")
data = list(csv.reader(file, delimiter=";"))
file.close()

temp = list()
pres = list()

for temp, pres in data:
    temp.append(int(temp))
    pres.append(int(pres))
    
plt.plot(temp, pres, 'r')
plt.show()