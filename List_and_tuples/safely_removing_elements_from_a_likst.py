numbers = [4, 5, 67, 1102, 221, 102, 344, 455, 322, 663]

min_value = 100
max_value = 500

# safely removing the items until the stop
stop = 0

for index, value in enumerate(numbers):
    if value >= min_value :
        del(numbers[:index]) # delete from element at index 0, up to but not including index
        stop = index
        break

print("The index to stop at is " +str(stop))
print(numbers)