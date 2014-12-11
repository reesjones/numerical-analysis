numerical-analysis
==================

Numerical integration and rootfinding methods implemented at NCSSM. Some were implemented with the help
of [Patrick Jennings](https://github.com/JenningsPatrick).


# How to Use
The scripts in this project are mostly applied numerical techniques - namely numerical integration,
rootfinding, machine epsilon approximating, and binary conversions. Each file can be used for a specific
numerical application.

### Epsilon.java and epsilon.py
These approximate machine epsilon - the maximum error in binary representation of floating point numbers.
One is implemented in Java and one in Python.

### binaryConverter.py
Converts a decimal number to the IEEE single-precision binary floating point representation.
Set the ```num``` variable at the top of the file to the desired decimal number you want converted.

### integration.py
Uses romberg and trapezoidal integration to approximate integrals. Just use the defined function and 
print the returned value. Argument ```f``` is the function (use lambda if you wish), ```a``` and ```b```
are the boundaries of the integral, and ```n``` is the number of intervals to use in the approximation. 

### rootfinding.py
Uses numerical root finding techniques to find the zeroes (roots) of a function. Like ```integration.py```,
use the defined functions to approximate roots. Arguments are more self-explanatory in this case.

### newton.py
Uses Newton's method to approximate the roots of a function. Use in the same way as ```rootfinding.py```.




# Analysis of rootfinding algorithms - when to use what

### Newton’s Method
Newton’s method is a strong rootfinding method with a fairly simple concept. The rate of convergence can be very fast relative to Bisection and Secant. However, it has weaknesses. If the starting point is chosen at a vertex, the derivative at that point is zero and the method will never converge. Similarly, if a starting point is chosen that has a derivative with a very small magnitude, the method will take a long time to converge to a certain error tolerance.

### Bisection Method
Bisection method is the simplest, most reliable method of the three. It will always converge to a root (assuming a root exists and the initial points are chosen correctly). Its weakness is that the error reliably and definitely decreases by exactly half in each iteration. It cannot be more efficient. It is the least efficient but the simplest and most reliable of the three.

### Secant Method
Secant method is in between Newton’s method and Bisection method in terms of reliability and rate of convergence. It is has a lower rate of convergence than Newton’s method but a higher rate than Bisection. It is about as reliable as Bisection method and more reliable than Newton’s method.
