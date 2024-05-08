import json

datapath = "data/recipes.txt"
outputpath = "outputs/recipe-index.json"

def load_data(datapath):
    print(f"Reading in recipes from file...")
    with open(datapath, 'r') as f:
        # Read the file into a list
        recipes = []
        for line in f:
            line = line.strip()
            recipes.append(line)        
    return recipes

def index_recipes_by_ingredient(recipes):
    print(f"Indexing recipes by ingredient...")
    # create an empty dictionary to hold the index
    recipe_index = {}

    # go through the recipes
    for recipe in recipes:

        # (the key(s) is/are: ingredients)
        # (the value(s) is/are: recipe names)
        # (parse out the keys and values you want to index from the item if necessary)
        
        # first let's split it into recipe name and list of ingredients
        recipe_name, ingredients = recipe.split(" | ")
        
        # WE NEED TO GET RID OF THE INGREDIENTS word at the beginning
        ingredients = ingredients.replace("Ingredients: ", "")

        # get each individual ingredient
        ingredient_list = ingredients.split(",")

        # now we can index each individual ingredient, which is our key
        for this_ingredient in ingredient_list:

            # clean the ingredient string
            this_ingredient = this_ingredient.strip()
        
            # GET the current value associated with the key in the index
            these_recipes = recipe_index.get(this_ingredient, [])
        
            # UPDATE the value
            these_recipes.append(recipe_name)
            
            # UPDATE the index with the key and its updated value
            recipe_index.update({this_ingredient: these_recipes})
    
    return recipe_index

# LOAD THE RECIPES
recipes = load_data(datapath)
print(f"Successfully read in {len(recipes)} recipes from file!")

# INDEX THE RECIPES
recipe_index = index_recipes_by_ingredient(recipes)
print(f"Successfully indexed recipes for {len(recipe_index)} ingredients!")
print(f"Here is a sample for 3 ingredients:")
for ingredient in list(recipe_index.keys())[:3]:
    print(f"Recipes that use {ingredient}: {recipe_index.get(ingredient)}")

# SAVE THE INDEX
print(f"Now saving index to {outputpath}...")
# use json library to convert the index into a json we can write to file in a nice format (with indentation)
json_recipe_index = json.dumps(recipe_index, indent=4)
# write to file
with open(outputpath, "w") as f:
    f.write(json_recipe_index)


