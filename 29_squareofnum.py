def Findsquare(num):
    r = ''
    for i in str(num):
        r= r+str((int(i))**2)

    return int(r)

num = input("enter the number:")
print(Findsquare(num))



 