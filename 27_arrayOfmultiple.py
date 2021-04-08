def arrayOfmuliple (num,length):
    result_arr = []
    for i in range(1,(length+1)):
        result_arr.append(i*num)
    return result_arr

num =int(input("enter any number:"))
length = int(input("enter the length of multiple:"))
print(arrayOfmuliple(num,length))