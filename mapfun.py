def mapfun(n):
	 return n*10
my_dict={2,3,4,5,6,7,8,9}
filter = map (mapfun,my_dict)
print(filter)
print(list(filter))