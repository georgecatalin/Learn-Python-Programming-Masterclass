menu=[
    ["dacia" , "renault"],
    ["skoda", "honda", "BMW"],
    ["mercedes" , "saab", "dacia", "renault"],
    ["audi", "dacia", "mercedes ", "volvo"]
]

# for car_brand in menu:
#    if "dacia" not in car_brand:
#       print(car_brand)

for car_brand_2 in menu:
    for index in range(len(car_brand_2)-1, -1, -1):
        if car_brand_2[index] == "dacia":
            del car_brand_2[index]
    print(car_brand_2)
