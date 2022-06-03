from prescription_data import adverse_interactions

complete_interactions = set()

for element in adverse_interactions:
    # complete_interactions = complete_interactions.union(element) # set.union() method creates a new set each time
      complete_interactions = complete_interactions | element # the union operator creates a new set each time

print(sorted(complete_interactions))