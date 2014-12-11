numerical-analysis
==================

Numerical integration and rootfinding methods at NCSSM


## How to Use
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
