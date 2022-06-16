data = [
    "Andromeda - Shrub",
    "Bellflower - Flower",
    "China Pink - Flower",
    "Daffodil - Flower",
    "Evening Primrose - Flower",
    "French Marigold - Flower",
    "Hydrangea - Shrub",
    "Iris - Flower",
    "Japanese Camellia - Shrub",
    "Lavender - Shrub",
    "Lilac- Shrub",
    "Magnolia - Shrub",
    "Peony - Shrub",
    "Queen Anne's Lace - Flower",
    "Red Hot Poker - Flower",
    "Snapdragon - Flower",
    "Sunflower - Flower",
    "Tiger Lily - Flower",
    "Witch Hazel - Shrub",
]

write_to_file = "writeto_file.txt"

with open(write_to_file,"w") as write_file:
    for plant in data:
        write_file.write(plant)
        string_representation = plant.__str__()
        print(type(string_representation))


# print() prints the __str__() representation of any object, whereas the write() method prints exactly what one asks it to

write_numbers_to_file = "write_numbers_to_file.txt"
with open(write_numbers_to_file,"w") as test:
    for i in range(100):
        print(i, file=test)

with open(write_numbers_to_file, "w") as test:
    for i in range(250):
        test.write(str(i)+"\n")