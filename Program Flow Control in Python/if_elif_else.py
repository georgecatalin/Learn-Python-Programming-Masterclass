answer = 5

print("Add a number to guess")
guess = int(input())

if guess > 5:
    print("You need to guess lower.")
elif guess < 5:
    print("You need to guess higher")
else:
    print("You guessed the number, brother")
