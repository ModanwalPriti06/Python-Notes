try:
	 x=int(input('Enterd the number'))
	 assert x>=5 and x<=5
	 print("the enterd num is:",x)
except AssertionError:
     print("This is conditio  is not fullfilled")
print('Rest f the code')