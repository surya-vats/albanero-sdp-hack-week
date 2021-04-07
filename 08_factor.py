n =int(input("Enter a number for find factor:"))
Factor =[]
for i in range(1,n+1):
    if (n%i)==0:
        Factor.append(i)


print(Factor)