d = {
    0: "white",
    1: "green",
    2: "red",
    3: "blue",
    4: "crimson",
    5: "black",
    6: "magenta",
}

v = d.values()
print(v)

print()
print("black" in v)
print("maroon" in v)

print()
keys = list(d.keys())
values = list(d.values())

for item in values:
    if item == "green":
        pos = values.index(item)
        key = keys[pos]
        print(key, values[pos], sep=" =>")

# the 2nd method to do the same thing
for key, value in d.items():
    if value == "green":
        print(key, value, sep="==>")