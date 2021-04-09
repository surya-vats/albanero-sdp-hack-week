from array import*
ar_nm = array('i',[])
n=int(input('enter number of element:'))
for i in range(n):
    ele =int(input())
    ar_nm.append(ele)
print(ar_nm)

def contigeous(arr,n):
    return(sum(arr))

arr=ar_nm
n =len(arr)
ans = contigeous(arr,n)
print(ans)
