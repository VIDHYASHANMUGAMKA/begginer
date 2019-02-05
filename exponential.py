import math 
def power(base,exp):
    if(exp==1):
        return(base)
        print("power value:",power(base,exp))
    if(exp!=1):
        return(math.pow(base, power))
        return(base*power(base,exp-1))
base=int(input("Enter base: "))
exp=int(input("Enter exponential value: "))
power=int(input("Enter the power value:"))
print("power value:",math.pow(base, power))
print("exponential value:",math.exp( base ))
