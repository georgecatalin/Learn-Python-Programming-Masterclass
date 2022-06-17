import json

languages = [
    ('ABC', 1987),
    ('Algol 68', 1968),
    ('APL', 1962),
    ('C', 1973),
    ('Haskell', 1990),
    ('Lisp', 1958),
    ('Modula-2', 1977),
    ('Perl', 1987),
]

with open("test.json", "w", encoding="utf-8") as my_file:
    json.dump(languages,my_file)

# tuples do not exist in other languages, hence they are serialized as arrays in JSON, same as lists