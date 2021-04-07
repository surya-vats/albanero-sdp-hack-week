list=[]
n=int(input("Enter number of elements:"))
for i in range (0,n):
    ele = int(input())

    list.append(ele)
    list.sort()
    if (list ==0):
        print("empty array")
print(list)