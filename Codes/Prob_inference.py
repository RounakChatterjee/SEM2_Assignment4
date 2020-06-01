'''
PROBABILISTIC INFERENCE
==================================================
Author : Rounak Chatterjee
Date : 1/06/2020
==================================================
This Program does probabilistic inferencing of models to be fit on a 
data set.
The procedure followed is exactly same as described by sir in the last 
lecture.The program is written in two parts.
The first part finds the values of parameters using MCMC, the next part
deduces the best model out of these.

This program uses the emcee library to find the MCMC chains and corner 
library to find the true parameter values. This program plots the various graphs 
one by one, so make sure to close panels to get the others
'''
import numpy as np
import emcee
import corner
import matplotlib.pyplot as plt
import scipy.optimize as op
x_data = np.loadtxt("C:/Users/ROUNAK/Desktop/study/Numerical Assignment Codes/Assignment IV/Model_data.txt",delimiter = '&',dtype = np.float64,comments = '#',usecols = 1)
y_data = np.loadtxt("C:/Users/ROUNAK/Desktop/study/Numerical Assignment Codes/Assignment IV/Model_data.txt",delimiter = '&',dtype = np.float64,comments = '#',usecols = 2)
sigma_y = np.loadtxt("C:/Users/ROUNAK/Desktop/study/Numerical Assignment Codes/Assignment IV/Model_data.txt",delimiter = '&',dtype = np.float64,comments = '#',usecols = 3)

def f(x,args): #Model to be fitted
	return args[0]*x**2.0 + args[1]*x+args[2]


def log_likelihood(data_params, x, y, yerr):
	a,b,c = data_params
	model = a*x**2.0 + b*x+c
	sigma2 = yerr**2
	# Taking Gaussian Probaibility distribution to compute Likelihood
	return 0.5*np.sum((y-model)**2/sigma2+np.log(2*np.pi*sigma2))

def log_prior(data_params):
	a,b,c = data_params
	#taking uniform priors
	if (-200.0<a<200 and -500.0<b<500.0 and 0<c<1000.0):
		return 0.0
	return -np.inf
def log_probability(data_params, x, y, yerr):
	lp = log_prior(data_params)
	if(not np.isfinite(lp)):
		return -np.inf
	return lp - log_likelihood(data_params, x, y, yerr)

guess = (1.0,1.0,1.0)# initial guess of the parameters

soln = op.minimize(log_likelihood,guess,args=(x_data, y_data, sigma_y))
nwalkers, ndim = 50, 3 # 50 MCMC chains 3 parameters
pos = soln.x + 1e-4 * np.random.randn(nwalkers, ndim)
sampler = emcee.EnsembleSampler(nwalkers,ndim,log_probability,args=(x_data, y_data, sigma_y))
sampler.run_mcmc(pos,4000)# 4000 MCMC runs per chain
samples = sampler.get_chain()

#Plotting MCMC chains of the parameters.

fig = plt.figure(constrained_layout = True)
spec = fig.add_gridspec(3,1)
p1 = fig.add_subplot(spec[0,0])
p1.set_title("MCMC chains of a ")
p1.plot(samples[:, :, 0],color = 'blue') # a values
p1.set_ylabel("values of a")
p1.grid()
p2 = fig.add_subplot(spec[1,0])
p2.set_title("MCMC chains of b ")
p2.plot(samples[:, :, 1],color = 'blue') # b values
p2.set_ylabel("values of b")
p2.grid()
p3 = fig.add_subplot(spec[2,0],)
p3.set_title("MCMC chains of c ")
p3.plot(samples[:, :, 2],color = 'blue') # c values
p3.set_xlabel("steps")
p3.set_ylabel("values of c")
p3.grid()
plt.show()

# reshaping to incrporate all samples
sph = samples.shape
samples = np.reshape(np.ravel(samples),(sph[0]*sph[1],sph[2]))

# computing Medians for true values
medians = np.median(samples,axis = 0)
a_true,b_true,c_true = medians
print("True values of parameter\na: ",a_true)
print("b: ",b_true)
print("c: ",c_true)
# calculating 1-Sigma values
one_sigma_vals_a = corner.quantile(samples[:,0],q = [0.16,0.84])
one_sigma_vals_b = corner.quantile(samples[:,1],q = [0.16,0.84])
one_sigma_vals_c = corner.quantile(samples[:,2],q = [0.16,0.84])
print("One-Sigma Values of parameter 16th and 84th Percentile:\na: ",one_sigma_vals_a)
print("b: ",one_sigma_vals_b)
print("c: ",one_sigma_vals_c)
# Plotting the Variations
fig2 = corner.corner(samples,labels = ["a","b","c"],quantiles = [0.16,0.5,0.84],truths=[a_true,b_true,c_true])
fig2.show()
plt.show()

# Extarcting 200 Data set randomly
index = np.random.randint(0,sph[0]*sph[1]-1,size = 200)
model_param = np.zeros(shape = (200,3),dtype = np.float64)
for i in range(len(index)):
	model_param[i] = samples[index[i]]
x = np.linspace(30.0,300.0,200)
# Plotting random models
for i in range(len(index)):
	if(i == 0):
		plt.plot(x,f(x,model_param[i]),color = 'green',lw = 0.5,label = 'Random Chosen Models')
	else:
		plt.plot(x,f(x,model_param[i]),color = 'green',lw = 0.5)
# Plotting the model with true parameters
plt.title("Data with Model and Candidate Models",size = 14)
plt.plot(x,f(x,[a_true,b_true,c_true]),color = 'black',lw = 2,label = "True Model")
#Plotting Data with error bars	
plt.errorbar(x_data,y_data,yerr = sigma_y,fmt = 'o',ecolor = 'black',elinewidth = 0.75,lolims = True,uplims = True,label = "Data with error bars")
plt.grid()
plt.xlabel("X data")
plt.ylabel("Y data")
plt.legend()
plt.show()