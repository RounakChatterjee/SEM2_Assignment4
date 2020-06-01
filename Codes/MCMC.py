'''
MCMC USING METROPOLIS ALGORITHM
============================================================
Author : Rounak Chatterjee
Date : 01/06/2020
============================================================
In the Metropolis Algorithm we choose a function that creates new random points from old random points, we call it
q(x'|x). If we have to sample a density function f(x)
then the steps to follow are :
 start at x = x_0
 for each step i
 1) using previous x_i find a new x' using q(x'|x) which suggests a new x' from the given x
 2) choose r from a uniform distribution [0,1]
 3) compute	 v = f(x')/f(x_i)
 4) if v > r : x_(i+1) = x' else : x_(i+1) = x_i

 Using this we can sample a number of points folllowing distribution f(x)

 for our case f(x) is a uniform distribution for x belonging to (3,7)
 we can choose q(x'|x) as a Gaussian distribution, for which case we can genrate a random position from a given x_i by adding a number randomly
 generated from from a gaussian distribution of mean zero and variance 1.
 Using these we create a markov chain that would uniformly sample f(x).
'''
import numpy as np
import matplotlib.pyplot as plt
import numpy.random as r

def f(x):
	if(3.0<x and x<7.0):
		return 1.0
	else:
		return 0.0

steps = 100000 # Number of MCMC steps 
x_0 = 5.0 # starting value>3.0
points_sampled = np.zeros(steps,dtype = np.float64)
markov_chain = np.array([],dtype = np.float64)
step_at = np.array([],dtype = np.float64)
x = x_0
for i in range(steps):
	x_p = x + r.normal(loc =0.0,scale = 0.25)
	points_sampled[i] = x_p
	if(f(x_p)/f(x)>r.rand()):
		x = x_p
		markov_chain = np.append(markov_chain,x_p)
		step_at = np.append(step_at,i+1)
	else:
		continue

fig = plt.figure(constrained_layout = True)
spec = fig.add_gridspec(1,2)
p1 = fig.add_subplot(spec[0,0])
p1.set_title("Distribution Density Historgarm form 100000 MCMC steps",size = 13)
p1.hist(markov_chain,20,density = True,facecolor = 'steelblue',label = 'Normalized Histogram')
p1.set_xlabel("x")
p1.set_ylabel("p(x)")
p1.grid()
p1.legend()

p2 = fig.add_subplot(spec[0,1])
p2.set_title("Sampled points and Markov chain ",size = 14)
p2.scatter(np.linspace(1,steps,steps),points_sampled,marker = '.',color = 'red',label = "Sampled points")
p2.scatter(step_at,markov_chain,marker = 'x',label = 'Markov Chain')
p2.set_xlabel("step index")
p2.set_ylabel("x value")
p2.legend()
p2.grid()

plt.show()


