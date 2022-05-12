def my_function(a, b=10):
    """
    This function computes the product of the two arguments.
    :param a: is the first argument
    :param b: is the second argument and defaults to 10
    :return: the product of the two arguments
    """
    return a * b


print(my_function(5))
print(my_function(5,12))