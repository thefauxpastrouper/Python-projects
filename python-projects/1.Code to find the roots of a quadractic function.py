#importing a library cmath
import cmath

#giving values of a,b,c
a=int(input("enter value a: "))
b=int(input("enter a value b: "))
c=int(input("enter value c: "))

#defining the value of d
d=(b**2)-(4*a*c)

#defining sol1 and sol2 using cmath and sqrt
sol1=(-b-cmath.sqrt(d))/(2*a)
sol2=(-b+cmath.sqrt(d))/(2*a)

#printing solutions
print(f"the solution are {sol1} and {sol2}") 