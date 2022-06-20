import csv

file_name = "country_info.txt"

with open(file_name,encoding="utf-8", newline="") as file_reader:
    sample = ""
    for row in range(3):
        sample += file_reader.readline() # this is much more efficient as it studies the structure of only first 3 lines in the csv
    csv_dialect = csv.Sniffer().sniff(sample)
    file_reader.seek(0)
    csv_reader = csv.reader(file_reader, dialect=csv_dialect)
    for line in csv_reader:
        print(line)