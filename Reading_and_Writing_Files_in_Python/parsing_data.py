this_filename = "country_info.txt"

with open(this_filename)  as file_read_from:
    for row in file_read_from:
        data = row.strip("\n").split("|")
        print(data)
