import numpy as np
k=2
array1 = [7,3,1,6]
print('intial array',array1)
array1.sort()
array1.insert(1,-1)
array1.insert(-1,1)
sum = 0
for i in range(0,len(array1)):
    sum = sum+array1[i]
    print(sum)
    

