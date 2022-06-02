my_set = set(range(21))
print(my_set, type(my_set))

# clear all the elements of the set with clear()
# my_set.clear()
print(my_set)

print()
print()
my_set.discard(17)  # removes element 17 , but does not return error if it does not exist
print(my_set)

print()
print()

my_set.remove(10)  # removes element 10, and it returns error if it does not exist
print(my_set)