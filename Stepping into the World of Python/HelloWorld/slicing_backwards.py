letters = "abcdefghijklmnopqrstuvwxyz"

print(letters[25:0:-1])     # up to, but not including the last 'a'


print(letters[25::-1])  # prints out in reverse order anything, including 'a' which is the last character
print(letters[::-1])    # prints out in reverse order anything, including 'a' which is the last character

# this is the challenge
first_slice=letters[16:13:-1] #qpo
second_slice=letters[4::-1] #edcba
third_slice=letters[25:17:-1]

print(first_slice)
print(second_slice)
print(third_slice)