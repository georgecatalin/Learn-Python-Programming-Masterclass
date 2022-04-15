shopping_list = ["paine", "zahar", "faina", "sare"]
another_shopping_list = shopping_list

print(id(shopping_list)) # list is an immutable object
print(id(another_shopping_list))

shopping_list += ["prajituri", "cartofi"] # concatenation of a list
print(shopping_list)
print(id(shopping_list)) # the id of the object did not change, because the list object was a mutable object
print(id(another_shopping_list))