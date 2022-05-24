import copy

animals = {
    "lion": ["scary", "powerful", "unmerciful"],
    "elephant": ["scary", "powerful", "unmerciful"],
    "teddy": ["cute", "cuddling"],
}

# creating a shallow copy => it copies the reference to the same object,hence the id of the object is the same
print()
things_shallow_copy = animals.copy()
print(id(animals["teddy"]), animals["teddy"])
print(id(things_shallow_copy["teddy"]), things_shallow_copy["teddy"])

animals["teddy"].append("smart")
print("`animals` dictionary =>", animals["teddy"])
print("`things_shallow_copy` dictionary =>", things_shallow_copy["teddy"])

# creating a deep copy of the objects, it effectively copies the objects, hence different ids
print()
things_deep_copy = copy.deepcopy(animals)
print(id(animals["teddy"]),animals["teddy"])
print(id(things_deep_copy["teddy"]), things_deep_copy["teddy"])

animals["teddy"].append("Romanian")
print(animals["teddy"])
print(things_deep_copy["teddy"])

