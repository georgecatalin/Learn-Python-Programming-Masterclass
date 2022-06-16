my_file =  "Jabberwocky.txt"
with open(my_file) as my_read:
    my_line = my_read.readline().rstrip()

print(my_line)

char = "'"
print(my_line.strip(char))

char = "'Thwas"
print(my_line.strip(char))

char = "'Thwasev"
print(my_line.strip(char)) # it removes ' and T h w a s and finds space which does not exist in char and he considers done stripping left handside, moves to righthand side
                           # it finds s right handside from the char , it finds e and it stops when it finds o which does not exists in the char

char = "'"
print(my_line.strip(char))