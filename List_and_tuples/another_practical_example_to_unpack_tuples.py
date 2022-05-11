# the function enumerate() returns a tuple made of index, character
for index, character in enumerate("Cornel is king"):
    print(index, character)

# what does enumerate() function returns as a result?
print("What does enumerate() function return?")
for t in enumerate("Cornel is king"):
    print(t)

# explained more clearly
print("Explain the unpacking more clearly")
for t in enumerate("Dacia Duster is great for light offroad"):
    index, value = t
    print(index, value)