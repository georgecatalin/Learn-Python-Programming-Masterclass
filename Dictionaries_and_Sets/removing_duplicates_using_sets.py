my_set = set()
print(my_set,type(my_set))

# how to use sets to remove duplicate use of data
data = ["red", "blue", "white", "blue", "white", "green"]

print()
print()
unique_data_version_1=set(data)
print(unique_data_version_1)

unique_data_sorted_alphabetically=sorted(set(data)) #sorted() creates always a function
print(unique_data_sorted_alphabetically)

unique_data_sorted_with_dictionary = list(dict.fromkeys(data))
print(unique_data_sorted_with_dictionary)

print()
print()
print(dict.fromkeys(data))