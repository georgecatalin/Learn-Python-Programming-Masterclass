import csv

file_name = "country_info.txt"

with open(file_name, encoding="utf-8", newline="") as file_reader:
    sample = ""
    sample = file_reader.read()
    csv_dialect_object = csv.Sniffer().sniff(sample) # not that efficient taking into account that it reads the entire csv into a text
    file_reader.seek(0)
    csv_reader = csv.reader(file_reader, dialect=csv_dialect_object) # csv parser knows from examining itself the structure of the csv which is the delimiter , quoting etc
    for line in csv_reader:
        print(line)