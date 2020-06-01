/*
TRANSFORMATION METHOD
==========================================================
Author: Rounak Chatterjee
Date : 29/05/2020 
==========================================================
This Method finds a non- uniform distribution from a uniform distribution
from the principle of "Conservation of measure", which says

p(y)dy = p(x)dx, where x and y are deviates from two different types of
distribution function p(x) and p(y). For ourcase we need to find random points
from an exponential distribution given by p(y) = m*exp(-my), to do this
we consider x to be drawn from an uniform distribution, which makes p(x) = 1

and by p(y)dy = p(x)dx we can write |dx/dy| = p(y){Mod taken since measure of probability is positive}, for our case, it is
|dx/dy| = (1/m)*exp(-y/m), which when  evaluated gives

x = exp(-y/m)

This when inverted yields y = -m*ln(x)

for our case m = 0.5

thus if we yield 10000 random x from an unifrom distribution and apply 
to y, then 10000 y will be distributed as exponential distribution of mean m = 0.5
The histogram plot is made in a corresponding python program.
*/
#include<stdio.h>
#include<stdlib.h>
#include<math.h>
float m = 0.5;
float f(float x)
{
	return -m*log(x);
}
 int main()
 {
 	float x;
 	FILE* fp;
 	x = 0.0;
 	fp = fopen("C:/Users/ROUNAK/Desktop/study/Numerical Assignment Codes/Assignment IV/Transform_dat.txt","w");
 	printf("Random Numbers in exponential Distribution are:\n");
 	for(int i = 0;i<10000;i++)
 	{
 		x = rand()/(32767.0);// We did this since them max value rand produce is 32767
 		fprintf(fp, "%f\n",f(x));
 		printf("%f\n",f(x));
 	}
 fclose(fp);
 }