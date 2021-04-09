def SubSequence(st1, st2, m, n):
    if m == 0:
        return True
    if n == 0:
        return False
 
    if st1[m-1] == st2[n-1]:
        return SubSequence(st1, st2, m-1, n-1)
 
    # If last characters are not matching
    return SubSequence(st1, st2, m, n-1)
 
 
st1 = "sur"
st2 = "suryaprakash"
 
if SubSequence(st1, st2, 0, 0):
    print("Yes")
else:
    print("no")