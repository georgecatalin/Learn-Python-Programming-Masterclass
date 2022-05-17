def calculate_fibonacci(n):
    '''Returns the `n` the Fibonacci number , after feeding with a positive `n` '''
    if 0 <= n <= 1:
        return n

    n_minus_1 = 1
    n_minus_2 = 0

    result = None

    for fibonacci in range(n):
        result = n_minus_1 + n_minus_2
        n_minus_2 = n_minus_1
        n_minus_1 = result

    return result

i = int(input("Enter your number to calculate its Fibonacci: "))

for number in range(i):
    print(number, "===>", calculate_fibonacci(number))