import re
txt="al_b"
x=re.search("[a-z]+_[a-z]",txt)
if x:
    print("Yes")
else:
    print("No")