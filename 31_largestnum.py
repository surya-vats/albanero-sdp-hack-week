def Largestofarray(a):
    max=[0][0]
    row =len(a)
    colm=len(a[0])
    for i in range (0,row):
        for j in range(0,colm):
            if (a[i][j]>max):
                max=a[i][j]
    return max

  
print(Largestofarray([[3,6,9],[5,7,2],[22,9,2]]))