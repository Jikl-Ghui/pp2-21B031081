def generat(n):
    v=0
    while n>v:
        yield n
        n-=1
n=int(input())
for n in generat(n):
    print(n)