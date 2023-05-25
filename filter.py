a = [100,46,73,62,45,28,43,22,47,89]
def fun(n):
    if n>=50:
        return True
result=list(filter(fun,a))
print(result)
print(type(result))                     #define the type of vlaue
for i in result:
    print(i)   
#=========================================================

a = [100,46,73,62,45,28,43,22,47,89]
result=list(filter(lambda n: n>=60,a))
print(result)
for i in result:
    print(i)