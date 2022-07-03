##factorial of a number###
n1= int(input("Enter a number: "))
fact = 1
if n1 < 0:
    print(n1,"is negative intiger")
elif n1 == 0:
    print("factorial of 0 is 1")
else:
    for i in range(1,n1+1):
        fact = fact*i
        print(fact,end=",")
		
		
###multiplication table###
n1= int(input("Enter a number: "))
for i in range(1,11):
    print(n1,'X',i,'=',n1*i)
	
###Fibonaci series###
n1= int(input("Enter a number: "))
ct1,ct2=0,1
count = 0
if n1 <= 0:
    print("please give +ve number")
else:
    while count < n1:
        print(ct1)
        ct3 = ct1+ct2
        ct1 = ct2
        ct2 = ct3
        count+=1
		
###Armstrong number###

num = int(input("Enter a number: "))

sum = 0

temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp //= 10


if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")
