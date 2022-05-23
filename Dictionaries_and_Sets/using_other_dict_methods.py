my_dictionary = {
    0: "white",
    1: "blue",
    2: "red",
    3: "yellow",
    4: "maroon",
    5: "black",
    6: "orange",
}

food = ["pizza", "coca-cola", "pepsi-cola", "vodka"]

new_dictionary = dict.fromkeys(food) # creates a new dictionary using the keys from the iterable object 'food' with None as values
print(new_dictionary)

new_other_dictionary = dict.fromkeys(food, 0) # creates a new dictionary using the keys from the iterable object 'food' with values default 0
print(new_other_dictionary)

for item in my_dictionary:
    print(f"{item}") # prints the key of the dictionary
print()
for item in my_dictionary.keys():
    print(f"{item}")