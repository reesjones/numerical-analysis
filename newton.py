import sys
from math import *

sys.setrecursionlimit(5000)



def newton(f,f2,start,error,iterations):
	x = start
	previous = x
	for z in range(iterations):
		x = x-(f(x)/f2(x))
		print("x = "+str(x)+" , f(x) = "+str(f(x))+" , error = "+str(x-previous))
		if abs(x-previous)<=error:
			return x
		previous = x
	return x


# Functions and corresponding derivatives
f4 = lambda x:x*x-5.3*x+6.72 
df4 = lambda x:2*x-5.3
f3= lambda x: .5*pi-asin(x)-x*(1-x*x)**.5-1.24
df3 = lambda x: -2*(1-x*x)**.5


print("Problem 3, Newton's method. Patrick Jennings and Mitch Rees-Jones.")
newton(f3 , df4, .5, 10e-7, 50)

