import hashlib

# print(sorted(hashlib.algorithms_available))
# print(sorted(hashlib.algorithms_guaranteed

python_string = """"for i in range(10)
print(i)
"""


# print the  bytearray for the string
for j in python_string.encode('utf8'):
    print(j, chr(j)) # chr(j) means the character encoded with j


old_sha256 = hashlib.sha256(python_string.encode('utf8'))
print(old_sha256.hexdigest())

python_string += """
print('code was changed')
"""
print()
print(python_string)

new_sha256= hashlib.sha256(python_string.encode('utf8'))
print(new_sha256.hexdigest())

if old_sha256 == new_sha256:
    print("The file has integrity.")
else:
    print("The file has been tampered with.")