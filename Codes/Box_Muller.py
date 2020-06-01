'''
BOX-MULLER METHOD OF PDF FINDING
================================================================
Author : Rounak CHtterjee
Date : 29/05/2020
================================================================
In this Program we use the Box Muller method to obtain a Gaussian distribution
from a uniform distribution.
The method uses higher dimension transformations to obtain lower dimension
distributions for which inverting the needed trnasformation function is 
hard. Given the transformation is that of a gaussian of mean = 0
variance = 1, which implies, the probability density as :

p(y) = 1/sqrt(2*Pi)*exp(-y^2/2). 

Now by box muller method if x1 and x2 are two uniform deviates
and 
y1 = sqrt(-2*ln(x1))cos(2*pi*x2)
y2 =  sqrt(-2*ln(x1))sin(2*pi*x2)
then by higher dimension transformation method we find
x1 = exp(-0.5(y1^2+y2^2)), x2 = (1/2*pi*arctan(y1/y2))
Evaluating the Jacobian of trnsformation yields

p(y1,y2) {joint probability distribution of y1,y2} = 

1/sqrt(2*Pi)*exp(-y1^2/2)*1/sqrt(2*Pi)*exp(-y2^2/2)

which is the independent Gaussian distribution of y1 and y2. This shows that
by the previous transformations we can obtain y1 and y2 which are random
points uniformly distributed as the gaussian.

This proves to be easier than inverting p(y) and this is called Box muller method.
In this program we will execute this to create 10000 points distributed
as gaussian.
'''
import numpy as np
import matplotlib.pyplot as plt
import numpy.random as r

def Gaussian(x):
	return (1.0/np.sqrt(2.0*np.pi))*np.exp(-x**2.0/2.0)
x1 = r.rand(10000)
x2 = r.rand(10000)
y1 = np.sqrt(-2.0*np.log(x1))*np.cos(2*np.pi*x2)
y2 = np.sqrt(-2.0*np.log(x1))*np.sin(2*np.pi*x2)

fig = plt.figure(constrained_layout = True)
spec = fig.add_gridspec(1,2)
p1 = fig.add_subplot(spec[0,0])
p1.set_title("Distribution of y$_1$",size = 13)
p1.plot(np.linspace(-5.0,5.0,200),Gaussian(np.linspace(-5.0,5.0,200)),color = 'black',label = "True Gaussian Distribution")
p1.hist(y1,20,density = True,facecolor = 'steelblue',label = "Distribution Density Histogram",histtype = 'stepfilled')
p1.set_xlabel("y$_1$")
p1.set_ylabel("p(y$_1$)")
p1.grid()
p1.legend()

p2 = fig.add_subplot(spec[0,1])
p2.set_title("Distribution of y$_2$",size = 13)
p2.plot(np.linspace(-5.0,5.0,200),Gaussian(np.linspace(-5.0,5.0,200)),color = 'black',label = "True Gaussian Distribution")
p2.hist(y2,20,density = True,facecolor = 'steelblue',label = "Distribution Density Histogram",histtype = 'stepfilled')
p2.set_xlabel("y$_2$")
p2.set_ylabel("p(y$_2$)")
p2.grid()
p2.legend()

plt.show()


