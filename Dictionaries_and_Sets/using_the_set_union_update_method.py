from prescription_data import adverse_interactions

# unlike set.union() method, the update() method does not create a new set, but it updates the old one
# unlike the union operator, the |= operator updates the existing set

complete_antagonist_medicines_set = set()

for medicine in adverse_interactions:
    # complete_antagonist_medicines_set.update(medicine)
    complete_antagonist_medicines_set |= medicine

print(complete_antagonist_medicines_set)