list =[]
n=int(input("Enter number of elements:"))
for i in range (0,n):
    ele = int (input())

    list.append(ele)
print(list)
#list1=[10,21,4,45,66,93]
for num in list:
    if num%2==0 :
        print(num,end = " ")