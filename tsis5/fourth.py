import re
txt=input()
x=re.search("[A-Z]_[a-z]+",txt)
if x:
    print("Yes")
else:
    print("No")