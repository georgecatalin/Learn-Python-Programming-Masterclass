filename = "Jabberwocky.txt"
with open(filename) as my_read:
    my_line = my_read.readline()

print(my_line)

print("*" * 80)
print("Using removeprefix() only happens in Python 3.9+")
print()
no_prefix = my_read.removeprefix("'Twas")
print(no_prefix)

print()
no_suffix = my_read.removesuffix("toves")
print(no_suffix)