def costpayforstair(cost, n):
    arr = [None]*n
    if n == 1:
        return cost[0]
    arr[0] = cost[0]
    arr[1] = cost[1]

    for i in range(2, n):
        arr[i] = min(arr[i - 1],
                    arr[i - 2]) + cost[i]
 
    # return the minimum
    return min(arr[n - 2], arr[n - 1])

a = [10,15,20]
n = len(a)
print(costpayforstair(a, n))