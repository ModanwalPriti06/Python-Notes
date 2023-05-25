import time
initial=time.time()
k=0
while(k<10):
    print(k)
    k +=1
print("while loop in",time.time()-initial,"first")
initial2=time.time()
for i in range(10):
    print(i)  
print("for loop in",time.time()-initial2,"Seconds")