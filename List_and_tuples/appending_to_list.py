choice_made = "-"
current_list = []

while choice_made != "0":
    if choice_made in "12345":
        print("Adding {0} to list".format(choice_made))
        if choice_made == "1":
            current_list.append("computer")
        elif choice_made == "2":
            current_list.append("hard drive")
        elif choice_made == "3":
            current_list.append("processor")
        elif choice_made == "4":
            current_list.append("mouse")
        else:
            current_list.append("keyboard")
    else:
        print("Add your option below:")
        print("1: computer")
        print("2: hard drive")
        print("3: processor")
        print("4: mouse")
        print("5: keyboard")
        print("0: exit application")

    choice_made = input()

print("The list now is:")
print(current_list)