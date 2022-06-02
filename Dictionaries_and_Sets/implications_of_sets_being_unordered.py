my_python_set = {"Audi", "VW", "Renault", "Dacia", "Skoda"}
print(my_python_set)

for item in my_python_set:
    print(item)

my_new_python_set_differently_ordered = {"Dacia","Audi","Skoda","Renault", "VW"}

if my_python_set == my_new_python_set_differently_ordered:
    print("The two sets are the same")
else:
    print("No, these sets are different")