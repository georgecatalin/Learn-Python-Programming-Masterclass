from contents import pantry, recipes


# print the dictionaries to demonstrate they were imported properly

# print(pantry)
# print(recipes)


display_dictionary = {}
for index, key in enumerate(recipes):
    # print(f"{index}: {key}")
    display_dictionary[str(index+1)] = key

# print(display_dictionary)

while True:
    print()
    print("Choose from the menu:")
    print("=====================")
    choice = input("> ")

    for key, value in display_dictionary.items():
        print(f"{key} - {value}")

    if choice == 0:
        break
    elif choice in display_dictionary:
        selected_option = display_dictionary[choice]
        print(f"You have selected {selected_option}")
        print("Checking ingredients...")
        print(recipes[selected_option])