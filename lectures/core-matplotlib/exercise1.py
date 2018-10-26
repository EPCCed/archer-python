
import numpy as np
import matplotlib.pyplot as plt

data1 = np.genfromtxt("random1.dat")
data2 = np.genfromtxt("random2.dat")

plt.plot(data1[:,0], data1[:,1], "r+", label = "data1")
plt.plot(data2[:,0], data2[:,1], "go-", label = "data1")
plt.xlabel("Points")
plt.ylabel("Values")
plt.legend()
plt.show()
