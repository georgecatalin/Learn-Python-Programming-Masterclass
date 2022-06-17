import json
import urllib.request

json_source_file = "https://www.ncdc.noaa.gov/cag/time-series/global/globe/land_ocean/ytd/12/1880-2021/data.json"

with urllib.request.urlopen(json_source_file) as source_url:
    data = source_url.read().decode("utf-8")
    anomaly = json.loads(data)

print(anomaly["description"])

for key, value in anomaly["data"].items():
    key, value = int(key), float(value)
    print(f"{key}...{value:4.2f}")

print("*" * 60)