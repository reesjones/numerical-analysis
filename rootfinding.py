import math

def secant(f, x0, x1, tolerance, iterationLimit): #If no error is set to zero, program may return a divide by ero error
    for z in range(iterationLimit):
        slope=(f(x0)-f(x1))/(x0-x1)
        x1=x0
        x0 = x0-(f(x0)/slope)
        print(x0)
        print("approx. error (x(n) - x(n-1)): ", x1-x0)
        if abs(f(x0))<=tolerance:
            return x0
    return x0

def bisection(f, left, right, tolerance, iterationLimit):
    for i in range(iterationLimit):
        middle = (left + right)/2
        print(middle, "         approx. error: ", (right - left)/2)
        if((f(left) > 0) != (f(middle) > 0)):      #If left is + and middle is - or the other way around
            right = middle
        elif((f(middle) > 0) != (f(right) > 0)):   #If right is + and middle is - or other way around
            left = middle
        if(abs((right - left)/2) <= tolerance):
            return middle
    print("ITERATION LIMIT REACHED")
    return middle  #Once iterationLimit has been reached


# Approximates to -0.7780895986786011
#print(secant(lambda x:x**6-x-1 , -1000000, 10000000, .0000000000001, 1000))

# Approximates to 23.08553703239628
print(bisection(lambda x: math.log(x**2 - 2*x - 3) - math.log(x + 1) - 3, 3.0000001, 25000000000000, .0000001, 100))


