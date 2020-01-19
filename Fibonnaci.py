def fib_iter(n):
    a, b = 0, 1

    for i in range(n):

        a, b = b, a+b
    
    return a

def fib_rec(n):

    cache = [None]*(n+1)

    if n==0 or n==1:
        return n

    if cache[n] != None:
        return cache[n]

    cache[n] = fib_rec(n-1) + fib_rec(n-2)

    return cache[n]

print(fib_rec(10))