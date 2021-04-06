list = [5,8,9,6]
total=0
for ele in range(0,len(list)):
 total= total+list[ele]
if((total%2==0) or (total==0)):
     print("Even")  
else:
    print("odd")

#print("sum of arry is :",total)