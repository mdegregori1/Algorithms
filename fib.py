# counter = 0
# def fib(n):
#     # base case
#     print(n)
#     global counter
#     counter += 1
#     # print(counter)
#     if n <= 2:
#         return 1
#     # recursive call
#     return fib(n-1) + fib(n-2)

# fib(30)

def fib(n, cache=None):
    if cache is None:
        cache = {}
    # Base case
    if n <= 2:
        return 1
    elif n in cache:
        return cache[n]
    else:
        answer = fib(n-1, cache) + fib(n-2, cache)
        cache[n] = answer
        # Recursive call, should move toward base case
        return answer
