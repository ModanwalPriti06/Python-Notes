import re
str="kumbh mela is condected an Ahemdabad in India"
res=re.sub(r'Ahemdabad','Allahabad',str)
print(res)