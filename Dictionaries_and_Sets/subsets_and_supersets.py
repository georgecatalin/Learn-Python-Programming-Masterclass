animals = {"tigru", "leu", "urs", "delfin", "vultur", "soim", "ciocanitoare"}
pasari = {"vultur", "soim", "ciocanitoare"}

print(f"The animals set is a super set of pasari set : {animals.issuperset(pasari)}")
print(f"The pasari set is a subset of the animals set : {pasari.issubset(animals)}")
print(f"The animals set is a subset of pasari set : {animals.issubset(pasari)}")

print("*" * 50)
print(f"The animals set is a superset of pasari set : {animals >= pasari}")
print(f"The animals set is a proper superset of pasari set : {animals >  pasari}")

print("*" * 50)
print(f"The pasari set is a subset of animals set : {pasari <= animals}")
print(f"The pasari set is a proper subset of animals set : {pasari < animals}")