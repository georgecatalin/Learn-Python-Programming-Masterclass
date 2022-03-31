parrot = "Norwegian Blue"

# this is negative indexing: starts from the end of the string
print(parrot[-1])  # e
print(parrot[-2])  # u

print(parrot[3])    # -11
print(parrot[4])    # -10
print(parrot[9])    # -5
print(parrot[3])    # -11
print(parrot[6])    # -8
print(parrot[8])  # -6

print("********************")
print(parrot[-11])
print(parrot[-10])
print(parrot[-5])
print(parrot[-11])
print(parrot[-8])
print(parrot[-6])

print("*******************")
print(parrot[3 - 14])   # length of the string is 14
print(parrot[4 - 14])
print(parrot[9 - 14])
print(parrot[3 - 14])
print(parrot[6 - 14])
print(parrot[8 - 14])