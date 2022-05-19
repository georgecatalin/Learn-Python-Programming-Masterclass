computer_parts = {
    "1": "processor",
    "2": "RAM Memory",
    "3": "Hard Disk",
    "4": "Keyboard",
    "5": "Mouse",
}

choice_option = None

new_dictionary = {}     # this way to create a new dictionary

while choice_option != 0:
    if choice_option in computer_parts:
        choice_value = computer_parts[choice_option]
        print(f"Adding {choice_option}")

        if choice_option in new_dictionary:
            print(f"Removing {new_dictionary[choice_option]}")
            new_dictionary.pop(choice_option)
        else:
            print(f"Adding {choice_value} to the new dictionary")
            new_dictionary[choice_option] = choice_value

    print(f"At this moment, the content of the new dictionary is {new_dictionary}")

    choice_option = input("> ")