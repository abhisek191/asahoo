####Fibonacci series####
def fibonacci(n, second_last, last):
    if n-1 == 0:
        return second_last
    else:
        new_last = second_last + last
        second_last = last
        return fibonacci(n-1, second_last, new_last)
 
 
if __name__ == "__main__":
    print(fibonacci(10, 0, 1))
	
	
	
# Factorial of a number using recursion

def recur_factorial(n):
   if n == 1:
       return n
   else:
       return n*recur_factorial(n-1)

num = 7


####calculate the natural logarithm of any number###
import math
print ("math.log(100.12) : ", math.log(100.12))
print ("math.log(100.72) : ", math.log(100.72))
print ("math.log(math.pi) : ", math.log(math.pi))


####cube sum of first n natural numbers?###

def sumOfSeries(n):
    sum = 0
    for i in range(1, n+1):
        sum +=i*i*i
         
    return sum
 
  
# Driver Function
n = 5
print(sumOfSeries(n))
