# syntax= import module_name as alias_name
import cal as preeti
print(preeti.name)
a=preeti.add(5,3)
print(a)
b=preeti.sub(34,8)
print(b)


# syntax= import module_name 
import cal
print(cal.name)
a=cal.add(5,3)
print(a)
b=cal.sub(34,8)
print(b)


# Syntax= from module_name import *
from math import *
print(floor(4.3))
print(sqrt(49))
print(factorial(5))
print(pow(5,3))
