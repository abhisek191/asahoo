####LCM###
def lcm_value(x, y):

   if x > y:
       higher = x
   else:
       higher = y

   while(True):
       if((higher % x == 0) and (higher % y == 0)):
           lcm = higher
           break
       higher += 1

   return lcm

num1 = 72
num2 = 54

print("The L.C.M. is", lcm_value(num1, num2))

##HCF###
def hcf_value(x, y):


    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller+1):
        if((x % i == 0) and (y % i == 0)):
            hcf = i 
    return hcf

num1 = 54 
num2 = 24

print("The H.C.F. is", hcf_value(num1, num2))


####Decimal to binary###
dec = 344

print("The decimal value of", dec, "is:")
print(bin(dec), "in binary.")
print(oct(dec), "in octal.")
print(hex(dec), "in hexadecimal.")

####Calculator###

# Program make a simple calculator

# This function adds two numbers
def add(x, y):
    return x + y

# This function subtracts two numbers
def subtract(x, y):
    return x - y

# This function multiplies two numbers
def multiply(x, y):
    return x * y

# This function divides two numbers
def divide(x, y):
    return x / y
	
num1 = 7
num2 = 5

add(num1,num2)
subtract(num1,num2)
divide(num1,num2)
multiply(num1,num2)
