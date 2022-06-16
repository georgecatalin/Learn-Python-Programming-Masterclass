with open("Jabberwocky.txt", "r") as my_read:
    for line in my_read:
        print(line.rstrip())


# the 'where' keyword does the file close automatically by Python