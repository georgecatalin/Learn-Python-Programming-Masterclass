my_tuple = "Dacia", 109, "1.5dCi"

print(my_tuple)
# printing individual elements of the tuple (ordered set of data) by the index
print(my_tuple[0])
print(my_tuple[1])
print(my_tuple[2])

# tuples are immutable, can not change their elements and this is an advantage of tuples over lists
# my_tuple[0] = "Renault"  # error

my_list = list(my_tuple) # function list() creates a list from an iterable object
print(my_list)
my_list[0] = "Audi"
print(my_list)