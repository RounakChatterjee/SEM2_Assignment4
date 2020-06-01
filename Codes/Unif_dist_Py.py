'''
CREATING UNIFORM DISTRIBUTION WITH PYTHON
=======================================================================
Author: Rounak Chatterjee
Date : 25/05/2020
=======================================================================
This Program creates a uniform distribution using numpy's random number genrator 
and compare the distribution with true distribution

 The time required is quoted in this program itself
'''
import numpy as np
import matplotlib.pyplot as plt
import time as t
t_val = np.float64(t.time())
x = np.random.rand(10000) # creates 10000 points in unifrom distribution [0,1]
t_val = np.float64(t.time())-t_val
print("Time Taken = ",t_val)
plt.plot(np.linspace(0,1,2),np.ones(2),color = 'black',label = "True Uniform Distribution")
plt.hist(x,20,density = True,facecolor = 'steelblue',label = "Distribution Density Histogram",histtype = 'stepfilled')
plt.title("Random numbers using Numpy",size = 13)
plt.xlabel("x")
plt.ylabel("p(x)")
plt.grid()
plt.legend()
plt.show()