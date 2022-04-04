my_age = 43

print("My age is " + str(my_age) + " years old.")  # the int variable is coerced into a string here

print()

# here follows how to print strings with the replacement fields introduced with Python 3
print("There are {0} days in {1}".format(28, "January"))

print("There are {0} days in {1}, {2}, {3}, {4}, {5}, {6}."
      .format(31, "January", "March", "May", "June", "August", "October"))


print("There are {2} days in January, {0} days in February and {1} days in April"
      .format(28, 30, 31))   # the order in the format property matters

print(""" There are {0} days in
{1}
{2}
{3}
{4}
""".format(31, "January", "March", "May", "July"))
