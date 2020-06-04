'''
CHI SQUARED TEST FOR RANDOM NUMBERS
=============================================================
Author : Rounak Chatterjee
Date : 01/06/2020
=============================================================
The Chi squared test is one of the ways to check whether a random number generator's
performance. If we consider a problem in which we know the analyitcal probability of 
outcome of an event as p_i and by the random number genrator we produce
n samples using the requisite probability distribution and get event i as
Y_i times, then we define a value V as:
V = Sum{i = 1 to N}{(Y_i-n*p_i)^2/n*p_i}, where n is the number of samples
generated by the random numer and N is the totalnumber of possible events.

Once we have V we can use it to calculate The Chi Squared statistics from it.
To to that we can use scipy module stats.chi2.cdf and depending on the output we can
write whether the genrator is good or bad.
The criterions are :
if value of V = v(obtained)
then p(V>v) = 1.0 - chi squared stat(V) = x (say)
then:
 x<0.01 : "Not Sufficient"
 0.01<x<0.05 : "suspect"
 0.05<x<0.1 : "almost suspect"
 0.1<x<0.9 : "sufficiently Random"

 For our problem we have twpo dice system so N = 12 and given two observed 
 counts. On them we perform the chi square test.
 '''
import numpy as np
import scipy.stats as s
def criterion(v):
	x = 1.0 - s.chi2.cdf(v,10.0)	
	if(x<0.01): 
		return "Not Sufficiently Random"
	elif(0.01<x and x<0.05): 
 		return "Suspect"
	elif(0.05<x and x<0.1): 
 		return"Almost Suspect"
	else: 
 		return "Sufficiently Random"

dice_prob = np.array([1.0,2.0,3.0,4.0,5.0,6.0,5.0,4.0,3.0,2.0,1.0],dtype = np.float64)
dice_prob = dice_prob/36.0
Y_1 = np.array([4,10,10,13,20,18,18,11,13,14,13],dtype = np.float64)
Y_2 = np.array([3,7,11,15,19,24,21,17,13,9,5],dtype = np.float64)
n1 = sum(Y_1)
n2 = sum(Y_2)
v1 = 0.0
v2 = 0.0
for i in range(len(dice_prob)):
	v1 = v1+ (Y_1[i]-n1*dice_prob[i])**2.0/(n1*dice_prob[i])
	v2 = v2+ (Y_2[i]-n2*dice_prob[i])**2.0/(n2*dice_prob[i])
print("The Test results are :\nSet1 :",criterion(v1))
print("Set2 : ",criterion(v2))








