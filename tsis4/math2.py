import math
def pol(n,l):
    a=l/(2*math.tan(180/n))
    return n*l*a*0.5
n=int(input())
l=int(input())
print(poly=pol(n,l))
