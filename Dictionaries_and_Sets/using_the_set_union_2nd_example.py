from prescription_data import adverse_interactions

complete_interactions = set()

for element in adverse_interactions:
    # complete_interactions = complete_interactions.union(element)
      complete_interactions = complete_interactions | element

print(sorted(complete_interactions))