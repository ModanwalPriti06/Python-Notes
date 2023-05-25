import re
str="Hello World!"
res=re.search(r'^He',str)
if(res):
     print("string satrt with he")
else:
     ptint("not strat with he")
print(res)