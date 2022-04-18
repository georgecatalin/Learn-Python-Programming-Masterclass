available_options = ["computer", "hard drive", "processor", "mouse", "keyboard"]

available_choices = []
for i in range(1, len(available_options) + 1):
    available_choices.append(str(i))

print(f"These are the available choices : {available_choices}")

choice_made = "-"
current_list = []

while choice_made != "0":
    if choice_made in available_choices:
        print("Adding {0} to list".format(choice_made))
        index = int(choice_made) - 1
        current_list.append(available_options[index])
    else:
        print("Add your option below:")
        for part in available_options:
            print("{0} : {1}".format(available_options.index(part) +1,part))

    choice_made = input()

print("The list now is:")
print(current_list)