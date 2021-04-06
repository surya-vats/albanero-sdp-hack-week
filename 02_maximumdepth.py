def maxDepth(s):
    current_max =0
    max=0
    n=len(s)
    for i in range(n):
        if s[i] == '(':
            current_max +=1
            if current_max > max:
                max=current_max
            elif s[i] == ')':
                if current_max >0:
                    current_max -= 1
                else:
                    return -1
    if current_max!=0:
        return -1
    
    return max

s = "( ((x)) (((y))) )"
print(maxDepth(s))