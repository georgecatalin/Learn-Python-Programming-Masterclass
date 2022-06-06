my_set = {"Java", "C#", "C", "Lisp","Visual Basic"}
my_set_2 = {"Python", "Kotlin", "C++","Java","C"}

print("Symmetric difference with a method")
set_symmetric_difference = my_set.symmetric_difference(my_set_2)
print(set_symmetric_difference)

print("Symmetric difference with the operator")
set_symmetric_difference_with_operator = set(my_set) ^ set(my_set_2)
print(set_symmetric_difference_with_operator)