import re
str="100 dogs,34 cats,rabbit 3"
res=re.compile('\d+',str)
res.findall(str)
#res.sub('-',str)