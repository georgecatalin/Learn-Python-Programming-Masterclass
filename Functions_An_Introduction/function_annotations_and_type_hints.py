def multiply(x : float, y : float ) -> float :
    result = x * y
    return  result


def is_palindrome(string : str) -> bool:
    if string[::-1].casefold() == string.casefold():
        return  True
    else:
        return False


def add(x : int = 11, y : int = 43) -> int:
    result = x + y
    return result


print(is_palindrome("Radar"))
print(multiply(4,5))
print(add())