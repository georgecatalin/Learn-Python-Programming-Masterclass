print("*" * 80)
print("Read a file using readlines()")
print()

with open("Jabberwocky.txt") as my_read:
    lines = my_read.readlines() # creates a list with the lines

print(lines)
print(lines[-1:])
for line in reversed(lines):
    print(line, end="")


print("*" * 80)
print("Read a file using read into a whole string")
print()

with open("Jabberwocky.txt")  as my_read:
    my_text = my_read.read()

print(len(my_text))
print(my_text)

for character in reversed(my_text.rstrip()):
    print(character, end="")

print()
print("*" * 80)
print("Read a file using readline()")
print()

with open("Jabberwocky.txt") as my_read:
    while True:
        my_line = my_read.readline() # it reads one line at a time
        print(my_line,end="")
        if 'rested' in my_line.casefold():
            break
