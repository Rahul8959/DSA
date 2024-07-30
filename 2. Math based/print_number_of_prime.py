import math

def primeNumbersTillN(N):
    # Function to check if a number is prime
    def isPrime(n):
        # 1 is not a prime number
        if n <= 1:
            return False
        # Check for factors from 2 to the square root of n
        limit = int(math.sqrt(n))
        for i in range(2, limit + 1):
            if n % i == 0:
                return False
        return True

    # Loop through numbers from 2 to N (inclusive)
    for i in range(2, N + 1):
        if isPrime(i):
            print(i)

# Example usage:
N = 30
primeNumbersTillN(N)
print(int(math.sqrt(2)))