def meanofdigit(num):
    nbr = str(num)
    lst = list(nbr)
    sum =0
    count =0
    for i in lst:  
        k=int(i)
        sum = k+sum
    for i in lst:
        count += 1
    mean =(sum/count)
    return mean
      
    

num = 575
print(meanofdigit(num))