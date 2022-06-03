from prescription_data import patients

trial_patients = {"Denise", "Eddie", "Frank", "Georgia", "Kenny"}

while trial_patients:
    this_patient=trial_patients.pop()  # the pop() method removes a random item from a set and selects it
    print(this_patient, end=": ")
    this_prescription = patients[this_patient]
    print(this_prescription)