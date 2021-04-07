from array import*
ar_nm = array('i',[])
n=int(input('enter number of element:'))
for i in range(n):
    ele =int(input())
    ar_nm.append(ele)
print(ar_nm)
psum =0
nsum =0
for i in range(n):
    if(ar_nm[i]>0):
        psum += ar_nm[i]
    elif(ar_nm[i]<=0):
        nsum += ar_nm[i]
        
print("sum of positive element:",psum)
print("sum of negative element:",nsum)