car_brands = {
    'blue': 'Dacia Logan 1.5dCi',
    'white': 'Skoda Octavia 1,2',
    'red': 'Renault Megane 1.6dCi',
    'green': 'Mercedes E-Class 2,2dCi',
    'black': 'Ford Focus 1.6d',
}

car_brands["magenta"] = "Volvo 2.9"
car_brands["orange"] = "BMW 1.9"

for key, value in car_brands.items():
    print(key, value, sep="; ")