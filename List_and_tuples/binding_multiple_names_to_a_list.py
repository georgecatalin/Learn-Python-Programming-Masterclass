shopping_list = ["bread", "butter", "sugar", "oil", "flour"]
another_shopping_list = shopping_list

print(shopping_list)
print(another_shopping_list)
print(id(shopping_list))
print(id(another_shopping_list))

a = b = c = d = another_shopping_list # binding multiple names to a list
print(a)
print(id(a))

print("Adding cream to the list")
b.append("cream")

print(b)
print(id(b))

print(c)
print(id(c))
print(d)
print(id(d))