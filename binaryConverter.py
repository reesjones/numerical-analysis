import math


#Need:
#   Sign
#   Mantissa
#   Exponent

#Number to be converted
num = 963.2

###################
#LIBRARY FUNCTIONS#
###################


def intToBinary(x):
    out = []
    out = [x%2] + out
    x = math.floor(x/2)
    if(x >= 1):
        out = intToBinary(x) + out
    return out


def decimalToBinary(x):
    out = []
    out = out + [math.floor(x * 2)]
    x = (x * 2) - math.floor(x * 2)  #Should equal 0 when x becomes one, 1 - floor(1) = 0
    if(x != 0): #If not base case
        out = out + decimalToBinary(x - math.floor(x))
    return out
    


def getSign(x):
    if(x < 0):
        return 1
    return 0


#######################
#END LIBRARY FUNCTIONS#
#######################

print("Number:")
print(num)

#Gets sign
sign = [getSign(num)]
if(sign[0] == 1):
    num = -num


###########

#Splits into integer and decimal parts of num
integer = math.floor(num)
decimal = num - integer

#Converts to binary
integer = intToBinary(integer)
decimal = decimalToBinary(decimal)

print("\nInteger and decimal pieces:")
print(integer)
print(decimal)

mantissa = integer + decimal
mantissa = mantissa[1:]

#Add extra significant figures if needed
while(len(mantissa) < 23):
    mantissa += [0]


###########

#Exponent, base 10
exponent = len(integer) - 1

print("\nExponent:")
print(exponent)

#Exponent, shifted to IEEE single precision and converted to binary
exponent = intToBinary(exponent + 127)

print("\nExponent in binary & shifted:")
print(exponent)

###########

#Final result
print("\n\n\n###############")
print("#Final output:#")
print("###############")
print("sign=", sign)
print("exponent=", exponent)
print("mantissa=", mantissa)
