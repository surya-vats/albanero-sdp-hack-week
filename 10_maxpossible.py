def maxPossiblesum(a):
    a.sort()
    a.reverse()
    print(a[0]+a[1]+a[2]+a[3]+a[4])

a=[5,5,5,5,5,0,0,0,0,0,0]
maxPossiblesum(a)