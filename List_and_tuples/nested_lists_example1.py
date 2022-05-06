
odd = [1, 3, 5, 7, 9]
even = [0, 2, 4, 6, 8]

empty_list = [odd, even]
print(empty_list)

for number_list in empty_list:
    print(number_list)
    for value in number_list:
        print(value)
