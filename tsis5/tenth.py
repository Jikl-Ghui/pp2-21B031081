import re
txt=input()
x=re.findall("[A-Z][a-z]*",txt)
print("_".join(x).lower())
