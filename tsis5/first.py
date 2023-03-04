import re
txt="allbf"
x=re.search("a(b*)",txt)
if x:
    print("Yes")
else:
    print("No")