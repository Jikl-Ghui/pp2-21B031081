import re
txt="kidkLOpdpskakLKdjksJidnn Ndsjn ndJsd"
x=re.findall("[A-Z][^A-Z]*",txt)
for i in x:
    print(i, end=" ")
