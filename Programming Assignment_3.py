####-ve and +ve####
n1 = int(input("Enter a number: "))
if n1>0:
    print("+ve number",n1)
elif n1<0:
    print("-ve number",n1)
else:
    print("it's 0")
	
###odd and even number###
n1 = int(input("Enter a number: "))
if n1%2==0:
    print("it's an even number:", n1)
elif n1%2!=0:
    print("it's an odd number:", n1)


####prime number###
n1 = int(input("Enter a number: "))
for i in range(2,n1):
    if n1%i==0:
        print(n1,"is not a prime number and it's devided by",i)
        break
else:
    print(n1,"is a prime number")


###prime list range###
l1 = []
l2 = []
for j in range(2,10001):
    for i in range(2,j):
        if j%i==0:
            l1.append(j)
            break
    else:
        l2.append(j)
        #print(n1,"is a prime number",end=",")
print("non prime list",l1)
print("prime list",l2)
