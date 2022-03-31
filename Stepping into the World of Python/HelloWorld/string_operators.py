string1 = "Today is "
string2 = "Thursday "
string3 = "and "
string4 = "it is a "
string5 = "day"

print(string1 + string2 + string3 + string4 + string5)  # concatenation
print("This is" " a perfect " "Thursday " " today") # this is also a concatenation of strings, but i prefer the first

print("Hello " * 8) # string multiplication

print("Hello " * (8+1))
print("Hello " * 5 + "7")


#   find substring in string
today = "Friday"
print("day" in today)    # true
print("Fri" in today)   # true
print("Thu" in today)   # false
print("Merc" in "edes")     # false


