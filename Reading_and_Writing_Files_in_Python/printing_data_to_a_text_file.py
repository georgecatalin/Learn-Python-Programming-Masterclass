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

write_to_file = "printo_file.txt"

with open(write_to_file, "w") as new_file:
    for plant in data:
        print(plant, file=new_file)

# here read to a new list to demonstrate the proper printing to text file
new_list = []
with open(write_to_file) as new_file:
    for row in new_file:
        data = row.strip()
        new_list.append(data)
        
print(new_list)