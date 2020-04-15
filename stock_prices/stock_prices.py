#!/usr/bin/python
# ([10, 7, 5, 8, 11, 9]), 6)
# write function "find_max_profit" that receives list of prices
# should return maximum profit made from ONE sell
# maximum difference between the smallest and largest prices in the list of prices  - note: buy must come BEFORE sell
# keep track of `current_min_price_so_far` and the `max_profit_so_far`?  # as you go down the list

import argparse

def find_max_profit(prices):
    # keep track of current min price and max profit so far
    # current_min_price = prices[0]
      # max profit = price - lowest price
      # current_min_price = prices[0]
      # current_max_profit = prices[1] - current_min_price
      current_min_price = prices[0]
      current_max_profit = prices[1] - current_min_price
    # loop through prices
      for i in range(1, len(prices)):
        if prices[i] < current_min_price:
          current_min_price = prices[i]
        elif current_max_profit < prices[i] - current_min_price:
          current_max_profit = prices[i] - current_min_price
    # conditional - if current_min price > arr[i]
    # set current_min_price = arr[i]
      return current_max_profit

prices = [10, 7, 5, 8, 11, 9] # must equal 6
print(find_max_profit(prices))

if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))



