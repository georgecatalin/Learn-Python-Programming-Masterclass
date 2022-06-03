my_set_1 = {"Dacia", "Renault", "VW", "Skoda", "Peugeot"}
my_set_2 = {"Ferrari", "Maseratti", "Lamborghini", "Porsche"}

all_set_form_1=my_set_1.union(my_set_2)
print(all_set_form_1)

print()
all_set_form_2 = my_set_2.union(my_set_1)
print(all_set_form_2)

print()
all_set_form_3 = my_set_1 | my_set_2
print(all_set_form_3)