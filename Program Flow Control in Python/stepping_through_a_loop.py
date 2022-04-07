series = "2,33,4545,3425 55: 45454;323"
separators = ""

for character in series:
    if not character.isnumeric():
        separators = separators + character

print(separators)

print("-" * 80)