def is_palindrom(string):
    backwards = string[::-1]
    return backwards.casefold() == string.casefold()


word = input("Enter the word to check if it is a palindrome: ")
if is_palindrom(word):
    print("{} is a palindrome.".format(word))
else:
    print("{} is not a palindrome.".format(word))