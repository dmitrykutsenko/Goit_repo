def get_recipe(path, search_id):

    with open(path, 'r') as file:
        for line in file:
            recipe = line.strip().split(',')
            if recipe[0] == search_id:
                return {
                    "id": recipe[0],
                    "name": recipe[1],
                    "ingredients": recipe[2:]
                }
    return None

# This function takes two parameters: `path`, which is the path to the file containing the recipes, and `search_id`, which is the MongoDB primary key for the recipe you want to search.

# The function uses a context manager (`with open(...) as file`) to read from the file. It then iterates over each line in the file, splitting the line by commas to extract the recipe details. If the first element of the split line matches the `search_id`, it returns a dictionary with the recipe information in the specified format. If no matching recipe is found, it returns `None`.

# For example, calling `get_recipe("./data/ingredients.csv", "60b90c3b13067a15887e1ae4")` with the provided file would return the following dictionary:

# python
# {
#    "id": "60b90c3b13067a15887e1ae4",
#    "name": "Watermelon Cucumber Salad",
#    "ingredients": [
#        "1 large seedless watermelon",
#        "12 leaves fresh mint",
#        "1 cup crumbled feta cheese"
#    ]
#}

# Please make sure to replace `"./data/ingredients.csv"` with the actual path to your file.