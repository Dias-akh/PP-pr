#1
import math
degree=int(input())
rad = math.radians(degree)
print("Result 1: ")
print(rad)

#2
import math
h=int(input())
b1=int(input())
b2=int(input())
print("Result 2: ")
print((b1+b2)/2*h)

#3
import math
num=int(input())
leng=int(input())
apothem=leng/(2*math.tan(math.pi/num))
perim=num*leng
print("Result 3: ")
print((perim*apothem)/2)

#4
import math
a=int(input())
b=int(input())
print(a*b)

