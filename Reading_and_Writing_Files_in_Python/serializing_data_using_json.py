import json

languages = [
    ['ABC', 1987],
    ['Algol 68', 1968],
    ['APL', 1962],
    ['C', 1973],
    ['Haskell', 1990],
    ['Lisp', 1958],
    ['Modula-2', 1977],
    ['Perl', 1987],
]


# This is how to serialize the data to json
with open("test.json", "w", encoding="utf-8") as my_file:
    json.dump(languages, my_file)

# This is how to deserialize the data from the json file
with open("test.json", "r", encoding="utf-8") as my_file:
    data = json.load(my_file)

print(data)
print(data[1])