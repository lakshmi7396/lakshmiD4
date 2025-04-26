def gcd(a, b):
    """
    Compute the greatest common divisor (GCD) of two numbers using the Euclidean algorithm.
    :param a: first number (integer).
    :param b: second number (integer).
    :return: GCD of a and b.
    """
    while b != 0:
        a, b = b, a % b
    return abs(a)  # Ensure the GCD is always non-negative

# Example usage
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
result = gcd(num1, num2)
print(f"The GCD of {num1} and {num2} is: {result}")
