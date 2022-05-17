my_tuple = (1953, 1954, 1978, 1977, 2011)

# print the tuple
print(my_tuple, sep=";") # the separator has no effect cause it is only one element printed out

# print the tuple unpacked
print(*my_tuple,sep=":")

# print the values with separator between
print(0, 1, 2 , 4, sep=":")


def my_function(*arguments):
    print(arguments)
    for i in arguments:
        print(i)


my_function(2, 45 , 66)
print()
my_function()