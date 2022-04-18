pangram = "The quick brown fox jumps over the lazy dog."
#pangram contains all the letters of the alphabet at least once


sorted_pangram = sorted(pangram)
print(sorted_pangram)

another_string = pangram
print(pangram)

print(pangram)
print(another_string)


my_list = [3.44, 4.45, 6.5, 4.22]
my_other_list = sorted(my_list)
print(my_other_list)
print(my_list)

another_list = my_list.sort()  # result is None cause it does not create a new list, but modifies the existing list
print(another_list)
print(my_list)

