'''
Pete likes to bake some cakes. He has some recipes and ingredients. 
Unfortunately he is not good in maths. 
Can you help him to find out, how many cakes he could bake considering his recipes?

Write a function cakes(), which takes the recipe (object) and the available ingredients (also an object) 
and returns the maximum number of cakes Pete can bake (integer). 
For simplicity there are no units for the amounts (e.g. 1 lb of flour or 200 g of sugar are simply 1 or 200). 
Ingredients that are not present in the objects, can be considered as 0.

Examples:
# must return 2
cakes({flour: 500, sugar: 200, eggs: 1}, {flour: 1200, sugar: 1200, eggs: 5, milk: 200})
# must return 0
cakes({apples: 3, flour: 300, sugar: 150, milk: 100, oil: 100}, {sugar: 500, flour: 2000, milk: 2000})
'''

recipe = {
    "flour": 500,
    "sugar": 200,
    "eggs": 1,
}

available = {
    "flour": 1200,
    "sugar": 1200,
    "eggs": 5,
    "milk": 2000
}

r1 = {'apples': 3, 'flour': 300, 'sugar': 150, 'milk': 100, 'oil': 100}
a1 = {'sugar': 500, 'flour': 2000, 'milk': 2000}

def loop(r, a):
    
    cake = []

    for recipe_ing, recipe_how_much in r.items():

        if recipe_ing in a.keys():
            print(recipe_ing, 'is available')
            cake.append(a[recipe_ing] // recipe_how_much)
             
        else:
           print(recipe_ing, 'is not available')
           return 0
    
    return min(cake)

def cakes(recipe, available):
    
    min_cake = []

    for i, how_much in recipe.items():
        if not i in available.keys(): 
            return 0
        else:
            min_cake.append(available[i] // how_much)
    
    return min(min_cake)

print(cakes(recipe, available))
print(cakes(r1, a1))