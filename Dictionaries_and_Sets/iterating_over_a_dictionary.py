car_park = {
    'blue': 'Dacia Logan 1.5dCi',
    'white': 'Skoda Octavia 1,2',
    'red': 'Renault Megane 1.6dCi',
    'green': 'Mercedes E-Class 2,2dCi',
    'black': 'Ford Focus 1.6d',
}

# this is the first manner of iterating
for key in car_park:
    print(key, car_park[key],sep="; ")

# this is the second possibility to use of iterating through a dictionary and far more efficient
print("*" * 50)
for key,value in car_park.items():
    print(key, value, sep="; ")