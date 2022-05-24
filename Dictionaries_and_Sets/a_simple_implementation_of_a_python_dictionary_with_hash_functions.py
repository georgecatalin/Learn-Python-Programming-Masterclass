dictionary_sample = {
    "dacia": "a cheap car, yet reliable and made in Romania",
    "renault": "a french flavour of the car",
    "mercedes": "the luxury and a lifetime brand",
}


def dummy_hash_function(string: str) -> int:
    '''
    An foolish representation of a hash function
    :param string:
    :return:
    '''

    hashed = ord(string[0])
    return hashed % 10


keys = [""] * 10
values = keys.copy()
print(id(keys), keys)
print(id(values), values)
print(id(keys[1]), keys[1], id(values[1]), values[1])

for key, value in dictionary_sample.items():
    h = dummy_hash_function(key)
    # h = hash(key)
    print(h,key, sep=": ")
    keys[h] = key
    values[h] = value

print()
print(keys)
print(values)