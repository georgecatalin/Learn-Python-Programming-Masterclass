import csv

file_name ="country_info.txt"

with open(file_name, encoding="utf-8", newline="")  as file_reader:
    csv_reader = csv.reader(file_reader, delimiter= "|")
    for line in csv_reader:
        print(line)