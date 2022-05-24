lion_list = ["scary", "powerful", "unmerciful"]
elephant_list = ["big", "intelligent", "smart"]
teddy_list = ["cute", "cuddling"]

animals_with_lists = {
    "lion": lion_list,
    "elephant": elephant_list,
    "teddy": teddy_list,
}

print()
new_beings_Lists = animals_with_lists
animals_with_lists["teddy"].append("beautiful")
print(animals_with_lists)
print(new_beings_Lists) # prints the same thing because each dictionary stores references to the same lists

print()
new_beings_lists_copy = animals_with_lists.copy()
animals_with_lists["teddy"].append("blue")
print(animals_with_lists)
print(new_beings_lists_copy) # prints the same thing because each dictionary stores references to the same lists

print()
new_beings_lists_copy = animals_with_lists.copy()
teddy_list.append("funny")
print(animals_with_lists)
print(new_beings_lists_copy) # prints the same thing because each dictionary stores references to the same lists

print()
new_beings_lists_copy = {
    "lion": lion_list,
    "elephant": elephant_list,
    "teddy": teddy_list,
}

teddy_list.append("funky")
print(animals_with_lists)
print(new_beings_lists_copy) # prints the same thing because each dictionary stores references to the same lists