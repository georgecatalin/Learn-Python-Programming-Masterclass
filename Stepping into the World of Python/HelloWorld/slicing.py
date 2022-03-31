parrot = "Norwegian Blue"

print(parrot[0:6])  # starts at index 0, up to ,but not including position 6 'Norweg'
print(parrot[:6])   # it is the same thing as above

print(parrot[3:5])

print(parrot[9:14])
print(parrot[9:])   # it is the same thing as line 8, goes till the end of the string. Up to ,but not including index 14

print(parrot[:6] + parrot[6:])   # from the beginning up to , but not including index 6 + from index 6 till end
print(parrot[:])    # it is the same thing as line 11, it prints out the whole string

