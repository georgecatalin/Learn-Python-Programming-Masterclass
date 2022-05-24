animals = {
    "lion" : "scary",
    "elephant": "big",
    "teddy": "cuddling",
}

print()
beings = animals # references to
animals["teddy"] = "cute"
print(animals)
print(beings) # prints out the same thing since both variable objects point to the same thing

print()
new_beings = animals.copy() # creates a copy of the object, not a reference to the object
animals["teddy"] = "blue"
print(animals)
print(new_beings) # prints out two different things since the two variables are not referencing the same thing

animals_with_lists = {
    "lion": ["scary", "powerful", "unmerciful"],
    "elephant": ["big", "intelligent", "smart"],
    "teddy": ["cute", "cuddling"],
}

print()
new_beings_Lists = animals_with_lists
animals_with_lists["teddy"].append("beautiful")
print(animals_with_lists)
print(new_beings_Lists)

print()
new_beings_lists_copy = animals_with_lists.copy()
animals_with_lists["teddy"].append("blue")
print(animals_with_lists)
print(new_beings_lists_copy) # prints out the same thing