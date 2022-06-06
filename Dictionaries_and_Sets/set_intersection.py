evens = set(range(0,50, 2))
multiple_threes = set(range(0,50, 6))

print(evens)
print(multiple_threes)

# set intersection down below


new_set_method_intersection = evens.intersection(multiple_threes) # with the set.intersection() method
print(new_set_method_intersection)

print()

new_set_operator_intersection = evens & multiple_threes # with the set intersection operator
print(new_set_operator_intersection)

# advantages of the set intersection methods over the set intersection operators
# set intersection method can be used with iterables, despite set intersection operator which can only be used with sets

new_set_advantage = evens.intersection(set(range(0,10,1)))
print(new_set_advantage)