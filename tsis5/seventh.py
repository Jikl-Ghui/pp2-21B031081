import re
txt="kele_zhatyr"
x=re.sub("['_']",' ',txt)
y=re.sub("\s",'',x.title())
print(x)
print(y)