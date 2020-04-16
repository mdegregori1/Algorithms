#!/usr/bin/python

# receives recipes and needed ingredients for that recipe in the form of a dicionary (key value)
# that key in kv pair is ingredient names, value is amount
# function should output (return ) the max number of whole batches


import math

def recipe_batches(recipe, ingredients):
  # define empty list to append to 
  # can call key or item without looping
  recipes_to_make = None
  # if keys are not the same, then return 0 or null (don't have #necessary ingregredients)
  if recipe.keys() != ingredients.keys():
    return 0
  else:
    # if keys are the same, then you can compare the values 
    for a,b in (recipe.items()):
      for k,v in (ingredients.items()):
        batches_possible = ingredients[k] // v
        # print("recipe:", f"key: {a}, value: {b}")
        # print("ingredients:", f"key: {k}, value: {v}")
        if recipes_to_make is None:
          recipes_to_make = batches_possible
        elif batches_possible < recipes_to_make:
          recipes_to_make = batches_possible
    
    return recipes_to_make
  #     divide = ingredients[x] // recipe[x] 
  #     if divide > 1:
  #       recipes_to_make.append(divide) 
  # return recipes_to_make
    
 





if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
