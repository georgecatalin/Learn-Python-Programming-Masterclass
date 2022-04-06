name = input("Please enter your name, alligator:")
age = int(input("Please enter your age , {0} :".format(name)))

if age >= 18:
    print("Good news. You are good enough to watch X-rated movies.")
    print("Fill an X in that box")
else:
    print("Come back in {0} years , my friend. It's not for you".format(18 - age))

