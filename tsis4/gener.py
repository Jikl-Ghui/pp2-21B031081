import math
def generat(n):
    v=0
    while v<n:
        yield v**2
        v+=1

m=int(input())
for sq in generat(m):
    print(sq)