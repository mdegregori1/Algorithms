#!/usr/bin/python

import argparse

def find_max_profit(prices):
  #set a minimum price at index zero 
  #set a current profit function where you have [1] - [0]
  #^ this is because profit is max - min, and max has to be after min 0 
  current_min_price = prices[0]
  current_profit = prices[1] - prices[0]
  # now, we have to loop through the array to get all of the elements 
  # start at 1, as 0 is where your min price is
  for x in range(0, len(prices)):
    # if current minimum price is greater than prices[x], that means that prices x is lower. So, it should now #be the lower price
    if current_min_price > prices[x]:
      current_min_price = prices[x]
    # if the current profit is less than prices[x] minus minimum profit, then profit is not maximized. So, it #should now be set to current_profit
    elif current_profit < prices[x] - current_min_price:
      current_profit = prices[x] - current_min_price

  return current_profit 


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))



