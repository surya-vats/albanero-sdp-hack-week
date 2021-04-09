def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)
 

def staircase(s):
    return fib(s + 1)
 

s = 4
print(staircase(s))