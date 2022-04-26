data = [104, 101, 4, 105, 308, 103, 5, 107, 100, 306, 106, 102, 108]

min_valid = 100
max_valid = 200

for index in range(len(data)-1, -1, -1):
    print(f"The index is {index} and the value is {data[index]}. ")
    if (data[index] < min_valid) or (data[index] > max_valid):
        print(f"to remove >>> the index is {index} and its value is {data[index]}")
        del data[index]

print(f"The list now is {data}")