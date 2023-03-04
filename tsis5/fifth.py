import re
txt=input()
x=re.search("a+[\w]+b+",txt)
if x:
    print("Yes")
else:
    print("No")