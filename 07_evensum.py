import sys
r =3
c =3
def sumEven(mat):
    sum =0
    for i in range(r+1):
        for j in range(c+1):
         if (mat[i][j]%2==0):
                sum += mat[i][j]
          return sum
mat = [[1,2,3],[3,7,5],[8,5,3]]
print(sumEven(mat))

