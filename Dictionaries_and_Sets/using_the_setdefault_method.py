from contents_dictionaries import pantry

paprika_quantity = pantry.setdefault("paprika", 0)
print(paprika_quantity)

# if the key does not exist in the dictionary, the setdefault() method adds it to the dictionary
# In case that the key="ketchup" does not exist, the default value would be 0
ketch_up_quantity = pantry.setdefault("ketchup", 0)
print(ketch_up_quantity)

# similarly, the get() method can retrieve the default value for a non-existing key, but it does not add it to the dictionary
potatoes_quantity = pantry.get("potatoes", 0)
print(potatoes_quantity)


print()
print("The content of the 'pantry' is :")
for key, value in sorted(pantry.items()):
    print(f"{key} : {value}")