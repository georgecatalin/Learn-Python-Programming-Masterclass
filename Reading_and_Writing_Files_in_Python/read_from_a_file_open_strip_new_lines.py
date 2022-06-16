my_read = open("Jabberwocky.txt", "r")

for line in my_read:
    print(line.strip()) # strips the line from the empty spaces characters tab, space and new line
    # there exists also lstrip() and rstrip() methods depending upon which side of the string you wish to strip

my_read.close()