#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  #initialize at no batches
  finished_batches = None

  for key, value in recipe.items():

    if key in ingredients.keys():
      batches_possible = ingredients[key] // value
      if finished_batches is None:
        finished_batches = batches_possible
      elif batches_possible < finished_batches:
        finished_batches = batches_possible
    else:
      finished_batches = 0

  return finished_batches

#rewrite when possible, a bit messy

if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))