##list1 = ['red', 'green','black', 'blue', 'orange', 'black','green', 'gray', 'green','black','red', 'green', 'blue', 'orange', 'green', 'gray', 'green',
##         'black','red', 'green', 'blue','black', 'orange','black', 'green', 'gray', 'green']
##
###count =[print(list1.count(item), item) for item in set(list1)]
##
##count = [print(list1.count(item), item) for item in set(list1)]



##a=['ali',"4th grade","seven","9 years","Nasra school"]
##try:
##    name, Class, siblings, age, school= a
##    print(b)
##
##except ValueError:
##    print('correct the values then try again')
##
import math
print("                     Solution Set of Quadratic Equation")
print('\n')


a= int(input("Enter a number A𝑥^2: "))
b= int(input("Enter a number B𝑥: "))
c= int(input("Enter a number C: "))

print('\n')

print("                     acc. to formula")
print("                     -b +or- √(b^2) - 4(a)(c) / 2(a)")
print('\n')

if (a>0):
        ac=4*a*c
        s=(math.pow(b,2))-ac
        d=math.sqrt(s)
##        print("sqroot is ", d)
        numi= -b + d
        den= 2*a
        res= numi /den
##        print(res)
        numi2= -b - d
        res2= numi2 / den
        print("(",res, "  ,", res2,")")
        
        
##        print(math.pow(c,d))
