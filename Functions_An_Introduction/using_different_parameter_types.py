def my_function(param1, param2, *args, k, **kwargs):
    """
    Demonstrating the different types of parameters in Python functions
    Args:
        param1: a keyword or positional parameter
        param2: a keyword or positional parameter
        *args: variable positional *args
        k: keyword parameter
        **kwargs: var-keyword parameter
    Returns: None
    """
    print(f"This is a positional or keyword parameter ....{param1}")
    print(f"This is a positional or keyword parameter ...{param2}")
    print(f"This is a var-positional parameter (tuple) ...{args}")
    print(f"This is a keyword parameter ...{k}")
    print(f"This is a var-keyword parameter ...{kwargs}")


my_function(1953, 1954, 1978, 1977, 2011, k=1973, key1=2000, key2=1989, key3=2003)