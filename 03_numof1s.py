#a=[[1,0,0],[0,1,1],[1,0,0]]
def countofone(a):
     count1s =0
     rows = len(a)
     cols = len(a[0])
     for i in range(0,rows):
        for j in range(0,cols):
          if(a[i][j]==1):
            count1s = count1s +1
     return count1s

a=[[1,0,0],[1,1,1],[1,0,0]]   
print(countofone(a))
