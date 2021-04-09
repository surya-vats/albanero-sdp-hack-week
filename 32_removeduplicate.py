def removeDulipcates(arr):
   
    # convert the arr into set and then into list
    return list(set(arr))
 
arr = [1, 22, 5, 1, 7, 2, 4, 21]
 
# Function call
arr = [1, 22, 5, 1, 7, 2, 4, 21]
print(removeDulipcates(arr))