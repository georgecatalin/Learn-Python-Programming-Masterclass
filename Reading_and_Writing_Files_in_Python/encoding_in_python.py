with open("Jabberwocky.txt", encoding="utf-8") as my_file: # always specify explicitly the encoding when opening the text files
    for row in my_file:
        print(row.strip())
