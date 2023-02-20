def squares(a,b):
    while a<b:
        yield a**2
        a+=1
a=int(input("a: "))
b=int(input("b: "))
for a in squares(a,b):
    print(a)