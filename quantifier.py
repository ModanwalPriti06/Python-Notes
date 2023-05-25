import re
str='Priti:245631789'
res=re.search(r'\d+',str)
print(res.group())