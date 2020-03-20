#!/usr/bin/python

import sys


#  1. We can make change for 10 cents using 10 pennies
#  2. We can use 5 pennies and a nickel
#  3. We can use 2 nickels
#  4. We can use a single dime


def making_change(amount, denominations):
  # if the amount is 1 or 0, then you can only use a penny for count
  if amount <= 1:
    return 1

  cache = [0] * (amount+1)
  cache[0] = 1

  #loop through all of the coins
  for coin in denominations:
    #look for higher value
    for high_amt in range(coin, amount+1):
      difference = high_amt - coin
      combinations = cache[difference]
      cache[high_amt] += combinations

  return cache[amount]


if __name__ == "__main__":
  # Test our your implementation from the command line
  # with `python making_change.py [amount]` with different amounts
  if len(sys.argv) > 1:
    denominations = [1, 5, 10, 25, 50]
    amount = int(sys.argv[1])
    print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
  else:
    print("Usage: making_change.py [amount]")