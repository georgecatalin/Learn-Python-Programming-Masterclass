available_exists = [ "north", "south", "east", "west"]

chosen_exit = ""
while chosen_exit.casefold() not in available_exists:
    chosen_exit = input("Enter your choice to proceed: ")
    if chosen_exit.casefold() == "quit":
        print("Game Over")
        break

print("Aren't you glad that you made it out of the bloody trap?")