def getParity( n ):
    parity = 0
    while n:
        parity = ~parity
        n = n & (n - 1)
    return parity
  
n = int(input("enter the value of n:"))
print ("Parity of no ", n," = ",( "odd" if getParity(n) else "even"))
 