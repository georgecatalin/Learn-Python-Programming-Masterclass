choice = "-"

while choice != "0":
    if choice in set("12345"):
        print("You chose {}".format(choice))
    else:
        print("Please choose your option from the list below:")
        print("1:\t Learn Python")
        print("2:\t Learn Java")
        print("3.\t Go swimming")
        print("4:\t Have dinner")
        print("5:\t Go to bed")
        print("0:\t Exit")

    choice = input()