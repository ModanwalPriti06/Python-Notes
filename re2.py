import re
prog=re.compile(r'm\w\w\w\w')
str='mamta,anju,kizie,manny,rocky'
res=prog.search(str)
print(res.group())