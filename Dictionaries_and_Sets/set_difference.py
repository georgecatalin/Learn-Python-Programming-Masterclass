my_set = set(range(0,50,2))
my_set_2 = set(range(10))

my_difference_set_with_method = my_set.difference(my_set_2)
print(my_difference_set_with_method)

print()

my_difference_set_with_operator = my_set - my_set_2
print(my_difference_set_with_operator)

# the advantage of the set difference method is the fact the with the set difference method can be used iterables, opposite to set difference operators which accepts only sets
print("The advantage of the set difference method")
my_difference = my_set.difference(set(range(0,20)))
print(my_difference)