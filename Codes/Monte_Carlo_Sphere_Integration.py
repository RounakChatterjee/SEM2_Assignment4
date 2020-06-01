'''
VOLUME OF N-DIM SPHERE USING MONTE CARLO
===========================================================================
Author: Rounak CHatterjee
Date : 25/05/2020
===========================================================================
This program uses monte carlo integration scheme to compute the n-dim volume enclosed by an n-dim sphere.
We know that an unit n-dim sphere follows the relationship 
y = Sqrt(1-Sum{i=1 to n-1}(x_i^2))
Now to make this a single valued function we can only confine our sphere to the positive sector of our n-dim space and by symmetry consideration, 
find this n-dim volume by monte carlo scheme and multiply it with the number of sectors in the dimension under consideration which is 2^n sectors.

'''
import numpy as np
import numpy.random as r

def n_dim_unit_sphere(dim,rand_no):
	x = 0.0
	c = 0 # counts the number of points in the unit volume
	for i in range(rand_no):
		y = r.rand()
		yc = 1.0
		for j in range(dim-1):
			x = r.rand()
			yc =yc - x**2.0
		yc = np.sqrt(yc)
		if(y<yc):
			c=c+1
	area = 2.0**dim*(c/rand_no) # we can do this since area enclosing has volume = unity
	return area
print("Area of a unit circle is:\n",n_dim_unit_sphere(2,100000))
print("Volume of 10 dimensional unit sphere:\n",n_dim_unit_sphere(10,1000000))


