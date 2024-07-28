import math

a=int(input("enter a side: "))
b=int(input("enter another side: "))
c=int(input("enter another side: "))

s=(a+b+c)/2
print(s)

A=math.sqrt(s*(s-a)*(s-b)*(s-c))
print("Area of a triangle: ",A)