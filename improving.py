# [0, 1, 1, 2, 3, 5, 8, 13, 21]

#added cache
cache = {0:1, 1:1}
def rec_fib(n):
    #base cases
    # if n == 0:
    #     return 0
    # if n == 1:
    #     return 1
    if n in cache:
        return cache[n]
    
    #if it's not in the cache, we must :
    # run the recursion, and add to the cache
    cache[n] = rec_fib(n-1) + rec_fib(n-2)
    
    return rec_fib(n-1) + rec_fib(n-2)
    #here, calculation the same thing a bunch of times

print(rec_fib(5))

