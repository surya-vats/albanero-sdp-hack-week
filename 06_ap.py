first=int(input('Enter the first number of AP :'))
diff =int(input('Enter the comman difference of an AP:'))
n = int(input('Enter the number of terms of Ap:'))
 
for i in range(1,n+1):
    tm=first+(i-1)*diff
    print(tm)
