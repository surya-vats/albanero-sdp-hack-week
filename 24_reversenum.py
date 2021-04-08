def reversematrix(a):
     rows = len(a)
     cols = len(a[0])
     reversea =[]
     for i in range(0,rows):
        for j in range(0,cols):
          if(a[i][j]==1):
            reversea.append(0)
          elif (a[i][j]==0):
              reversea.append(1)

     return reversea

a=[[1,0,0]
,[1,1,1]
,[1,0,0]]   
print(reversematrix(a))