from array import*
stu_roll = array('i',[])
n=int(input('enter number of element:'))
for i in range(n):
    ele =int(input())
    stu_roll.append(ele)
print(stu_roll)
for i in range(n):
     if (i%2)==0:
         print(i)
