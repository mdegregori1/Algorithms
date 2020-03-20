#!/usr/bin/python

import sys

def rock_paper_scissors(n):
  #set an empty array to add all plays
  total_plays = []
  def rps_plays(total_plays, plays, n):
    rps = ['rock', 'paper', 'scissors']
    # if the length of arrays equal the input, then add plays to total plays array
    if len(plays) == n:
      total_plays.append(plays)
    #if not, loops through rps array and add new element to new plays 
    else:
      for g in rps:
        new_plays = plays.copy()
        new_plays.append(g)
        rps_plays(total_plays, new_plays, n)

  rps_plays(total_plays, [], n)
  return total_plays


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')