import  json

json_data_source = "temperature_anomaly.json"

with open(json_data_source, encoding="utf-8") as my_file:
    anomaly = json.load(my_file)

print(anomaly["description"])
print(anomaly["citation"])

for year, value in anomaly["data"].items():
    year = int(year)
    value = float(value)
    print(f"{year}...{value:6.3f}")
