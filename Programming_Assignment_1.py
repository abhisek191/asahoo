##(1)Programto print hello
print("Hello Python")

n1 = int(input('Enter 1st number:'))
n2 = int(input('Enter 2nd number:'))
print('Addition: ',n1+n2)
#print('Subtraction: ',n1-n2)
print('Division: ',n1/n2)

##(2)Area of the triangle
b = int(input('Enter base:'))
h = int(input('Enter hight:'))

print('The area of the triangle is',(b*h)/2)

#(3.1)Swap two variables for string by using 3rd variable
a = input('Enter 1st value:')
b = input('Enter 2nd value:')
print('before swap the value of a is',a)
print('before swap the value of b is',b)

c = a
a = b
b = c
print('after swap the value of a is',a )
print('after swap the value of b is',b)
#(3.2)Swap two variables for number
a = int(input('Enter 1st value:'))
b = int(input('Enter 2nd value:'))
print('before swap the value of a is',a)
print('before swap the value of b is',b)
a = a+b
b = a-b
a = a-b
print('after swap the value of a is',a )
print('after swap the value of b is',b)

#(4) Program to generate a random number between 0 and 9
import random
print(random.randint(0,9))
