panagram = "The quick fox jumps over the lazy dog"

words=panagram.split()
print(words)

numbers=['233','4','566','235','353','356456']
print(numbers)

int_numbers = []

for i in range(len(numbers)-1):
    int_numbers.append(int(numbers[i]))

print(int_numbers)

chapter ="Over the years, the Mastering Swift book has established itself amongst developers as a popular choice as an in-depth and practical guide to the Swift programming language. The latest edition is fully updated and revised to cover the new version: Swift 5"
print(chapter.split(" "))