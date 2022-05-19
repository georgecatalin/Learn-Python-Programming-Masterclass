computer_parts = {
        "1": "processor",
        "2": "hard disk",
        "3": "keyboard",
        "4": "mouse",
        "5": "RAM memory",
}

choice_option = None
while choice_option != 0:
    if choice_option in computer_parts:
        element_in_dictionary = computer_parts[choice_option]
        print(f"You have selected {element_in_dictionary}")

    choice_option = input("> ")