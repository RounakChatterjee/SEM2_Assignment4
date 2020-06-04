'''
DISTRIBUTION BY REJECTION
=========================================================
Author: Rounak Chatterjee
Date: 25/05/2020
=========================================================
To find the distribution by rejection method, we use a known PDF and sample it and try to find the points that lie inside the
distribution function we aim to sample.
The Criterion of the Enveloping function is that, it must complete envelop the dsitribution function we seek.
Since we're given a Gaussian, we try to find an enveloping function, that not only takes in a small area, but also envelopes the 
function under consideration.

We chose the enveloping function as :
 env(x) = c*exp(-x), where we have chosen an optimal value for c, to better save area.

 By transformation we can easily find that the c*exp(-x) is given by evaluating P(x)dx = P(y)dy
 since we sample s from a uniform distribution , hence P(x) = 1.0, but P(y) = c*exp(-y)

 thus direct evaluation yields y = -ln(x/c), where x will be uniformly sampled from a uniform distribution between [0,c]
 Using this sampler we use the rejection scheme to sample points for f(x) = Gaussian
 '''
import numpy as np
import numpy.random as r
import matplotlib.pyplot as plt
c = 1.40# c = 1.40 seems a good optimisation
def f(x): #Distribution function
 	return np.sqrt(2.0/np.pi)*np.exp(-0.5*x**2.0)
def env(x): # Enclosing function
 	return c*np.exp(-x) 
def sampler(x):
	return -np.log(x)

x = np.linspace(0.0,10.0,200)
rand_x = r.rand(10000)
rand_x = sampler(rand_x)
y = r.rand(len(rand_x))*env(rand_x)
dist_pts = []
y_pts=[]
for i in range(len(rand_x)):
	if(y[i]<f(rand_x[i])):
		dist_pts.append(rand_x[i])
		y_pts.append(y[i])
plt.title("Depiction of Rejection Method",size = 15)
plt.plot(x,f(x),color = "#00FF00",label = "Required Distribution")
plt.plot(x,env(x),color = 'black',label = "Enveloping function")
plt.hist(dist_pts,20,density = True,facecolor = 'steelblue',label = 'Normalized Histogram')
plt.xlabel("x")
plt.ylabel("p(x)")
plt.legend()
plt.grid()
plt.show()