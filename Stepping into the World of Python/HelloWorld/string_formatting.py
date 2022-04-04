for i in range(1, 15):
    print("No. {0} square is  {1} and cube is {2}".format(i, i ** 2, i ** 3))

print()

for i in range(1, 15):
    print("No. {0:2} square is  {1:3} and cube is {2:4}".format(i, i ** 2, i ** 3)) # right aligned numbers

print()

for i in range(1, 15):
    print("No. {0:<2} square is  {1:<3} and cube is {2:<4}".format(i, i ** 2, i ** 3)) # left aligned numbers

print()
print("printing without specifying the index of the format specifier")

# printing without specifying the index of the format specifier
for i in range(1, 15):
    print("No. {} square is  {} and cube is {:4}".format(i, i ** 2, i ** 3))
    # right aligned numbers , the order matters

# printing floats
print()
print("The value of PI is {0:12}".format(22 / 7)) #12 digits for the whole number
print("The value of PI is {0:12.50f}".format(22 / 7)) #12 digits for the whole number, but 50 digits after decimal
print("The value of PI is {0:51.50f}".format(22 / 7)) #51 digits for the whole number, but 50 digits after decimal
print("The value of PI is {0:72.50f}".format(22 / 7)) #72 digits for the whole number, but 50 digits after decimal
   # aligned to right

print("The value of PI is {0:<72.50f}".format(22 / 7)) #72 digits for the whole number, but 50 digits after decimal
# aligned to left
