#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution
def eating_cookies(n, cache=None):
    if cache is None:
        cache = [0] * (n + 1)
    if n <= 1:
        cache[n] = 1
    elif n == 2:
        cache[n] = 2
    elif cache[n] == 0:
        cache[n] = eating_cookies(n - 1, cache) + eating_cookies(n - 2, cache) + eating_cookies(n - 3, cache)
    return cache[n]

# MORE PERFORMANT SOLUTION ABOVE
# def eating_cookies(n, cache=None):
#   if n <= 1:
#     return 1
#   elif n == 2:
#     return 2
#   else: 
#     return eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3)
  
  # how many possible ways can i eat n numbers of cookies by eating 0, 1, 2, or 3  cookies at once?
  # bascially, what are the combinations of the above that add up to n



if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')