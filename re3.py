import re
str='man,run,dog,mas,cat,mat'
res=re.findall(r'm\w\w',str)
print(res)