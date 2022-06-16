my_read = open("Jabberwocky.txt", "r")

for line in my_read:
    print(line, end="")
    # print(len(line))

my_read.close()