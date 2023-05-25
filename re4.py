import re
str='mat,cat,dog,mak,can,fan'
res=re.match(r'm\w\w',str)
print(res.group())