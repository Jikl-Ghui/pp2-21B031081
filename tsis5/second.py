import re
txt="abb"
x=re.search("(a(b{2,3}))",txt)
if x:
    print("Yes")
else:
    print("No")