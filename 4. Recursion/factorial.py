def factorial(n, result=1):
    # Base case: if n is 0 or 1, print the result
    if n == 0 or n == 1:
        print(result)
    else:
        # Recursive case: multiply the result by n and call the function with n - 1
        factorial(n - 1, result * n)

# Example usage:
N = 4
factorial(N)