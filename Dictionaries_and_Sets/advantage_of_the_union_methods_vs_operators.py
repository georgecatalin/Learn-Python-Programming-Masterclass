from prescription_data import adverse_interactions

complete_set_adverse_interactions = set()

# complete_set_adverse_interactions.update(adverse_interactions[0], adverse_interactions[1],adverse_interactions[2])

# unpack the list
complete_set_adverse_interactions.update(*adverse_interactions)

print(complete_set_adverse_interactions)