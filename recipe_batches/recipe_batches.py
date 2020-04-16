#!/usr/bin/python

# receives recipes and needed ingredients for that recipe in the form of a dicionary (key value)
# that key in kv pair is ingredient names, value is amount
# function should output (return ) the max number of whole batches


import math

def recipe_batches(recipe, ingredients):
    possible_batches = []
    # must compare keys to see if they match
    # loop through the items in both recipe and ingredients
    # if keys are the same, then run look to compare
    if recipe.keys() != ingredients.keys():
      return 0
    else:
      for i in recipe:
        # print('recipe:',recipe[i])
        # print('ingredients:',ingredients[i])
        if recipe[i] > ingredients[i]:
          return 0
        else:
          #here, we're assuming that there are enough ingredients for the recipe. so, we have to determine how many we can make given the ingredients
          divide = ingredients[i] // recipe[i]
          print('division happens here',divide)
          possible_batches.append(divide)

        return max(possible_batches)





if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
