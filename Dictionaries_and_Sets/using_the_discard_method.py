travel_mode = {"1": "car", "2": "plane"}

items = {
    "can opener",
    "fuel",
    "jumper",
    "knife",
    "matches",
    "razor blades",
    "razor",
    "scissors",
    "shampoo",
    "shaving cream",
    "shirts (3)",
    "shorts",
    "sleeping bag(s)",
    "soap",
    "socks (3 pairs)",
    "stove",
    "tent",
    "mug",
    "toothbrush",
    "toothpaste",
    "towel",
    "underwear (3 pairs)",
    "water carrier",
}

restricted_items = {
    "catapult",
    "fuel",
    "gun",
    "knife",
    "razor blades",
    "scissors",
    "shampoo",
}

mode = "-"
mode = input("Enter your choice: ")

while mode not in travel_mode:
    mode = input("> ")

print(f"You have chosen {mode} : {travel_mode[mode]}")

if mode =="2":
    for element in restricted_items:
         items.discard(element)
        # items.remove() returns error because it attempts to delete a non-existing item "catapult" from 'items' set
        # items.remove(element)

for element in items:
    print(f"{element}")