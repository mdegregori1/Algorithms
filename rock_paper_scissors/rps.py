import sys
import math 
# possible plays in game
# n is number of plays per round
# Your output should be a list of lists containing strings. Each inner list should have length equal to the input n.
# something to store new combinations in 
def rock_paper_scissors(n):
  # set empty list to append to 
  # set list [[]] for base case 0
  # set rps for base case 1
  empty = [[]]
  rps = [['rock'], ['paper'], ['scissors']]
  total_moves = []
  # set up base cases
  if n == 0:
    return empty
  if n == 1:
    return rps 
  # now, loop through func(n-1) (recursive) to get rps combinations at n-1
  for x in rock_paper_scissors(n-1):
    # loop through rps to get additional # for combination
    for y in rps:
      # print(f"x:{x} + y:{y}")
      total_moves.append(x + y)

  return total_moves

  
# rock_paper_scissors(4)

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')