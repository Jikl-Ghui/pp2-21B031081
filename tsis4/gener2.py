def gener2(n):
    v=0
    while v<n:
        yield v
        v+=2
inp=int(input())
for v in gener2(inp):
    print(v)
