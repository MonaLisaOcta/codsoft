def addition(xyz,abc):
    return xyz+abc
def substraction(xyz,abc):
    return xyz-abc
def multiplication(xyz,abc):
    return xyz*abc
def division(xyz,abc):
    return xyz/abc

print("pick out the calculation")
print("A.addition")
print("S.substract")
print("M. multiplication")
print("D.division")

preference=int(input("give the preference(A/S/M/D): "))

value_1=int(input("enter the first figure: "))
value_2=int(input("enter the second figure: "))
    
if preference=="A":
    print(value_1,"+",value_2,"=",addition(value_1,value_2))
elif preference=="S":
    print(value_1,"-",value_2,"=",substraction(value_1,value_2)) 
elif preference=="M":
    print(value_1,"*",value_2,"=",multiplication(value_1,value_2))
elif preference=="D":
    print(value_1,"/",value_2,"=",division(value_1,value_2))
else:
    print("not valid")