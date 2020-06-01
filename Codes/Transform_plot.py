'''
This Program produces the plot for the C program named Transform.c that produces
points from an exponential distribution and compares it with true distribution
'''
import numpy as np
import matplotlib.pyplot as plt
data = np.loadtxt("C:/Users/ROUNAK/Desktop/study/Numerical Assignment Codes/Assignment IV/Transform_dat.txt",comments = '#')

plt.title("Depiction of Transformation Method",size = 15)
plt.plot(np.linspace(0.0,5.0,100),(1.0/0.5)*np.exp(-(1.0/0.5)*np.linspace(0.0,5.0,100)),color = 'black',label = "Required Distribution")
plt.hist(data,20,density = True,facecolor = 'steelblue',label = 'Normalized Histogram')
plt.xlabel("x")
plt.ylabel("p(x)")
plt.legend()
plt.grid()
plt.show()