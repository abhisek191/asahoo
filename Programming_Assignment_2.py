###KM to miles 
km = int(input("Enter km value: "))

km_to_miles = float(0.6214)
miles = km * km_to_miles

print(km,'k.m. =',miles,'miles')

###Celsius to Fahrenheit

Tcel = int(input("Enter a Temperature in Celsius: "))
Tfar = ((9 * Tcel)/5) + 32

print(Tcel,'degree Celsius is',Tfar,'degree Fahrenheit')

###calender


###Number swap

a1 = int(input('Enter a number: '))
a2 = int(input('Enter another number: '))
print('Beore swap a1 =',a1,'and a2 =',a2)
a1 = a1+a2
a2 = a1-a2
a1 = a1-a2
print('After swap a1 =',a1,'and a2 =',a2)

