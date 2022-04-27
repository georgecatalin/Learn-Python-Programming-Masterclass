numbers = [4, 5, 104, 105, 110, 120, 130, 130, 150, 160, 170, 183, 185, 187, 188, 191, 350, 360]

min_value = 100
max_value = 200

# safely removing the items until the stop
stop = 0

for index, value in enumerate(numbers):
    if value >= min_value :
        stop = index
        break

print("The index to stop at is " +str(stop))
del(numbers[:index]) # delete from element at index 0, up to but not including index
print(numbers)

# removing the highest values
start = 0
for index in range(len(numbers)-1, -1, -1): # up to element with index -1, but not including it. So the last is index 0
    if numbers[index] <= max_value:
        start = index + 1
        break

print("The start index is {0}".format(start))
del numbers[start:]  # delete from index start till the end of the iterable (list)
print(numbers)