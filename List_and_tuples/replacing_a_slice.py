car_brands = ["Dacia", "Renault", "VW", "Audi", "Mercedes", "BMW"]

print(car_brands)
car_brands[1] = "Honda" # this replaces the element of the list at a certain index
print(car_brands)

car_brands[2:]=["Volvo", "Rolls-Royce"] # this replaces the elements of a slice in a list with the elements of an iterable
print(car_brands)