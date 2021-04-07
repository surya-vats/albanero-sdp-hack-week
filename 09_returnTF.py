
def truefalse(a,n):
    for i in range(5):
       for j in range(i+1,6):
          if a[i]+a[j]==n :
            print("true")
            return
          else:
            print("false")

a=[10,12,4,7,9,11]
n=16
truefalse(a,n)