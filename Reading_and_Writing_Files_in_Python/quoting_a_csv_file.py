import csv

csv_file_name = "cereal_grains.csv"

with open(csv_file_name, encoding="utf-8", newline="")  as csv_reader:
    my_reader = csv.reader(csv_reader, quoting = csv.QUOTE_NONNUMERIC)  # by letting know the quotation exists around strings, all un-quoted values from the csv are parsed as floats
    for row in my_reader:
        print(row)