pangram = "The quick brown fox jumps over the lazy dog."
#pangram contains all the letters of the alphabet at least once


sorted_pangram = sorted(pangram, key = str.casefold)
print(sorted_pangram)

my_string = sorted("The quick brown fox jumps over the lazy dog.",key = str.casefold)
print(my_string)

names = [ "George", "Alex", "cornel", "pavel"]

names.sort(reverse=True, key=str.casefold)
print(names)