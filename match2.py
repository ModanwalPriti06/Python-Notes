import re
str="Hello World!"
res=re.search(r'World$',str)
if(res):
     print("string end with World")
else:
     print("not end with World")
