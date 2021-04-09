lst = []

n = 2
for i in range(0, n):
    ele = int(input("enter any two number:"))
  
    lst.append(ele) 
      
print(lst)

for i in lst:
    sum = 0
    while (i != 1):
 
        sum = sum + int(n % 10)
        n = int(n/10)
 
for i in lst :
            sum1=0
            while(i!=2):
                sum1 =sum+int(n%10)
                n=int(n/10)
if (sum==sum1):
    print("true")
else:
    print("false")
    
