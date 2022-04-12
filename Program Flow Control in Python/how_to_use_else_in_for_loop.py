

for i in range(1,7):
    print("the number is now {}".format(i))
    if i % 8 == 0:
        break
else: # executes only when the code did not break
    print("I have found no multiple of 8")