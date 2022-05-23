my_dictionary = {
    0: "white",
    1: "red",
    2: "blue",
    3: "orange",
    4: "magenta",
    5: "crimson",
    6: "black",
}

my_list = ["chips", "food", "coca-cola", "pepsi-cola"]

my_dictionary_2 = {
    3: "another white",
    6: "another black",
    10: "new ten",
}


my_dictionary.update(my_dictionary_2)  # the update keeps the position of the key, but updates the value
for key, value in my_dictionary.items():
    print(f"{key} : {value}")

my_dictionary.update(enumerate(my_list)) # updates the values for the keys 0...3 corresponding with the values in the my_list
for key, value in my_dictionary.items():
    print(key, value, sep="; ")