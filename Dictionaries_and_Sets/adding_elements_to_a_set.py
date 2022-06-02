my_set={*""} # one version to create a set
my_new_set = set()

# add elements to set
my_new_set.add("Cornel")
print(my_new_set)

while len(my_new_set) < 4:
    new_item=input("Enter the new element")
    my_new_set.add(new_item)

print(my_new_set)
