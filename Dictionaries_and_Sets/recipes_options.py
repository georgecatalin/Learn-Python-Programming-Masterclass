# nest list of tuples
recipes_tuple = {
    "Chicken and chips": [
        ("chicken", 100),
        ("potatoes", 3),
        ("salt", 1),
        ("malt vinegar", 5),
    ]
}

# nested dictionaries
recipes_dictionary = {
    "Chicken and chips": {
        "chicken": 100,
        "potatoes": 3,
        "salt": 1,
        "malt vinegar": 5,
    }
}

# list the quantities in the version of list of tuples
for recipe, ingredients in recipes_tuple.items():
    print(f"Ingredients for this recipe called {recipe}")
    print("***********************************")
    for ingredient, quantity in ingredients:
        print(f"{ingredient} in quantity of {quantity}")

# list the quantities when data is presented as a nested dictionary inside a dictionary
for recipe, ingredients in recipes_dictionary.items():
    print(f"Ingredients of the {recipe} are: ")
    print("==================================")
    for ingredient, quantity in ingredients.items():
        print(ingredient, quantity, sep="; ")