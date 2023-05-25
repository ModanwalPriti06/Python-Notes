n=['Pinky','Priti','Kirti','Manvi','Janhvi']
n.sort()
print(n)
#
n.sort(reverse=True)
print(n)
#
def myfun(e):
     return len(e)
n=['Pinky','Priti','Kirti','Manvi','Janhvi']
n.sort(key=myfun)
print(n)
