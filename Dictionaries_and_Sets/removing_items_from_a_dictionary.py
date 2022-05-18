car_brands = {
    'blue': 'Dacia Logan 1.5dCi',
    'white': 'Skoda Octavia 1,2',
    'red': 'Renault Megane 1.6dCi',
    'green': 'Mercedes E-Class 2,2dCi',
    'black': 'Ford Focus 1.6d',
}

# remove an item from a dictionary using the del() method , same as in lists sequence types
del car_brands["white"]
for key, value in car_brands.items():
    print(key)


print()

# remove an item from a dictionay using the pop() method

result = car_brands.pop("blue")
print(result) # pop() method returns the element that was removed
for key, value in car_brands.items():
    print(key)

print("+" * 100)

# remove an item from a dictionary that does not exist using the pop() method
result_does_not_exist = car_brands.pop("maroon", None) # returns None instead of an error
print(result_does_not_exist)
for key, value in car_brands.items():
    print(key)

print("+" * 100)

result_does_not_exist_2 = car_brands.pop("crimson", "You wish you had it!") # if the key does not exist, return the 2nd argument
print(result_does_not_exist_2)
for key, value in car_brands.items():
    print(key)

print("+" * 100)

result_exists_even_if_specify_2nd_argument = car_brands.pop("green", "Good for you.")
print(result_exists_even_if_specify_2nd_argument)
for key, value in car_brands.items():
    print(key)
