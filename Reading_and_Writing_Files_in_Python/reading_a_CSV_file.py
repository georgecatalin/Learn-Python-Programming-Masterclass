import csv

csv_filename = "OlympicMedals_2020.csv"

with open(csv_filename,encoding="utf-8", newline='') as csv_file_object:
    my_heading = csv_file_object.readline().strip("\n").split(",")
    print(f"csv heading is {my_heading}")
    my_reader = csv.reader(csv_file_object)
    for row in my_reader:
        print(row)
