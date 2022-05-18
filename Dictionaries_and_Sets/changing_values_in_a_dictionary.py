car_brands = {
    'blue': 'Dacia Logan 1.5dCi',
    'white': 'Skoda Octavia 1,2',
    'red': 'Renault Megane 1.6dCi',
    'green': 'Mercedes E-Class 2,2dCi',
    'black': 'Ford Focus 1.6d',
    'red': 'VW Passat 2.0',
}

car_brands["blue"] = "Dacia Duster 1.5dCi"
for key, value in car_brands.items():
    print(key, value, sep="; ")