my_list = []
odd =[1, 3, 5, 7, 9]
even = [2, 4, 6, 8, 0]

numbers = odd + even # create a list by concatenating two existing lists
print(numbers)


sorted_numbers =sorted(numbers)  # create a new list using the function sorted()
print(sorted_numbers)
print(numbers)

new_sorted_numbers = sorted("45235453461")
print(new_sorted_numbers) # the new  list contains the same type of elements as in the initial list

print(numbers.sort()) # it does not create a new list


another_sorted_numbers = list(numbers)  # create a new list using the list() function
another_sorted_numbers_slice = numbers[:] # create a new list using the slice, comes from Python 2.0
another_sorted_numbers_copy = numbers.copy() # create a new list using the copy() function

print(another_sorted_numbers)
print(another_sorted_numbers is numbers) # compares if the objects are exactly the same : False
print(another_sorted_numbers == numbers) # compares if the content of the objects is the same : True

print(another_sorted_numbers_slice)
print(another_sorted_numbers_copy)
