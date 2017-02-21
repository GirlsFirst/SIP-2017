'''
The code below represents one way that one might hard-code recipes into a recipe box, but does not offer
solutions to the extensions.
'''

# Recipe adapted from http://www.oliviascuisine.com/new-york-style-bacon-egg-and-cheese/
# New York-Style Bacon, Egg and Cheese Sandwich

bec_name = 'New York-Style Bacon, Egg and Cheese Sandwich'
bec_ingredients = {'Sesame, Everything or Whole Wheat Bagel': '1', 'Butter': '3 tsp', 'Cooked Bacon':'2 slices', 'Eggs':'2', 'American Cheese':'2 slices', 'Salt and Pepper': 'to taste' }

bec_instructions = []
bec_instructions.append('1. Slice bagel in half and spread the butter on the cut sides.')
bec_instructions.append('2. Pre-heat your cast iron pan (or griddle) over medium heat. Once hot, toast the bagels until golden brown.')
bec_instructions.append('3. Add the remaining tablespoon of butter and, once melted, crack both eggs in the pan. As soon as the whites start to set, puncture the yolks gently and spread them over the whites. Season with salt and pepper.')
bec_instructions.append('4. Layer the cheese and bacon on top of one of the eggs and use a spatula to flip the other egg on top o fthe bacon. Cook for a few extra seconds, until the cheese is melted')
bec_instructions.append('5. Once the cheese is melted, transfer the eggs to the bagel bottom and top the sandwich with the bagel top.')
bec_instructions.append('6. Serve immediately!')

# Create list of qualities that designate a recipe.
bec = [bec_name, bec_ingredients, bec_instructions]


# Recipe adapted from http://www.foodnetwork.com/recipes/ree-drummond/macaroni-and-cheese-recipe
# Macaroni and Cheese

mc_name = 'Macaroni and Cheese'
mc_ingredients = {'Dried Macaroni':'4 cups', 'Egg':'1', 'Butter':'1/2 stick','All-purpose Flour':'1/4 cup', 'Whole Milk':'2 1/2 cups', 'Dry Mustard':'2 tsp', 'Cheddar Cheese':'1 pound', 'Salt':'to taste', 'Black Pepper':'1/2 tsp', 'Optional spices':'cayanne pepper, paprika, thyme'}

mc_instructions = []
mc_instructions.append('1. Pre-heat the oven to 350 degrees F.')
mc_instructions.append('2. Grate the Cheddar Cheese.')
mc_instructions.append('3. Cook the macaroni until slightly firm. Drain and set aside.')
mc_instructions.append('4. In a small bowl, beat the egg. In a large pot, melt the butter and sprinkle in the flour. Whisk together over a medium-low heat. Cook for a couple of minutes, whisking constantly. Do not let it burn!')
mc_instructions.append('5. Pour the milk into the pot. Add the mustard and whisk until smooth. Cook until very thick; about 5 minutes. Reduce the heat to low.')
mc_instructions.append('6. Take 1/4 cup of the sauce and slowly pour it into the beaten egg, whisking constantly to avoid cooking the eggs. Whisk this together until smooth.')
mc_instructions.append('7. Pour the egg-sauce mixture back into the large pot, whisking constantly. Stir until smooth.')
mc_instructions.append('8. Add the cheese and stir to melt.')
mc_instructions.append('9. Add the salt, pepper, and other speices if desired. Taste the sauce and add more salt as needed.')
mc_instructions.append('10. Pour the drained, cooked macaroni into the sauce. Stir to combine.')
mc_instructions.append('11. Serve immediately, or pour into a buttered baking dish, top with extra cheese, and bake until bubbly and golden (approximately 20-25 minutes).')

# Create list of qualities that designate a recipe.
mc = [mc_name, mc_ingredients, mc_instructions]

# Add recipes to the recipe box, or list of recipes.
recipebox =[mc, bec]

# Print all recipes.
for recipe in recipebox:

    #Print Recipe name
    print("")
    print(recipe[0])
    print("")

    # Print ingredients
    print('Ingredients')
    ingredients = recipe[1]
    for item, amount in ingredients.items():
        print(item, amount)
    print("")

    #Print instructions
    print("Instructions")
    for step in recipe[2]:
        print(step)

    print("")
    print("")
