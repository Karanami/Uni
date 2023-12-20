import csv
import matplotlib.pyplot as plt

file = open("dane.csv", "r")
data = list(csv.reader(file, delimiter=";"))
file.close()

temp = list()

for t, p in data:
    temp.append(float(t))


plt.plot(range(len(temp)), temp, 'r')
plt.show()