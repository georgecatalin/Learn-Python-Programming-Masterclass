from prescription_data import  *

trial_patients = ["Denise", "Eddie", "Frank", "Georgia", "Kenny"]


for my_patient in trial_patients:
    this_prescription = patients[my_patient]
    if warfarin in this_prescription:
        this_prescription.remove(warfarin)
        this_prescription.add(edoxaban)
    else:
        print(f"The patient {my_patient} is not taking warfarin")

    print(f"{my_patient}:{this_prescription}")