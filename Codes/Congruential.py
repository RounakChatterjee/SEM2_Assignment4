'''
LINEAR CONGRUENTIAL RANDOM NUMBER GENERATOR
=================================================================
Author: Rounak Chatterjee
Date : 29/05/2020
=================================================================
This program creates 10,000 random numbers bewteen 0 and 1 using A congruential method
 Given as X_(i+1) = (a*X_i+c)mod m 

 Now the values of a,c and X_0 are very important to make the genrator 
 sufficiently random. Thus we choose tge parameters that the rand() module
 of C program uses, that is a = 1103515245, c = 12345 and m = 2^31 with a seed of X_0 = 1
 We also time the code to get the amount of time taken. To get it between 0 and 1
 we divide every number obtained by 2^31

 The Time taken is quoted in this program only
'''
import matplotlib.pyplot as plt
import time as t
import numpy as np
a = 1103515245
c = 12345
m = 2e31
x_arr = np.zeros(10000,dtype = np.float64)
x = 1 # initial seed
t_val = np.float64(t.time())
for i in range(10000):
	x_arr[i] = x
	x = (a*x+c)%m
t_val = np.float64(t.time())-t_val
x_arr = x_arr/m
print("Time Taken = ",t_val)
plt.plot(np.linspace(0,1,2),np.ones(2),color = 'black',label = "True Uniform Distribution")
plt.hist(x_arr,20,density = True,facecolor = 'steelblue',label = "Distribution Density Histogram",histtype = 'stepfilled')
plt.title("Random Numbers using Linear Congruential Generator",size = 13)
plt.xlabel("x")
plt.ylabel("p(x)")
plt.grid()
plt.legend()
plt.show()
