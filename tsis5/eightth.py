import re
txt="allbHijkaLolGuhkik"
x=re.findall("[A-Z][^A-Z]*",txt)
print(x)