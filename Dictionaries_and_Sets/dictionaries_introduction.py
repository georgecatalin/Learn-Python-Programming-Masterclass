car_brands = {
    'blue': 'Dacia Logan 1.5dCi',
    'white': 'Skoda Octavia 1,2',
    'red': 'Renault Megane 1.6dCi',
    'green': 'Mercedes E-Class 2,2dCi',
    'black': 'Ford Focus 1.6d',
}

# elements stored in a dictionary can be accessed either via index, or using the .get() method

# accessing the elements of the dictionary via index
my_car = car_brands['red']
print(my_car)

other_car = car_brands['green']
print(other_car)

# accessing the elements of the dictionary using the .get() method
economic_car = car_brands.get("blue")
print(economic_car)

hipster_car = car_brands.get("black")
print(hipster_car)