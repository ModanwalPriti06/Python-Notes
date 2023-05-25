import re
str='This?is the:"core"Python\'book'
res=re.split(r'\W+',str)
print(res)