car_brands=["Dacia", "Renault", "VW", "Audi", "Seat", "Skoda"]

del car_brands[4:] # delete all elements from the list starting from element index 4 till the end
print(car_brands)

readings = [4, 6, 102, 233, 435, 554, 211, 111]

min_value = 200
max_value = 500

for index,element in enumerate(readings):
    if (element < min_value) or (element > max_value): # this deletion will not work
        del readings[index]   # note: be careful when deleting from an iterable which affects also the indexing
print(readings)