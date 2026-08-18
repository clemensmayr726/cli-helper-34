
def factorial(n: int) -> int:
    """
    Calculate the factorial of a non-negative integer.
    
    Args:
        n (int): A non-negative integer whose factorial is to be calculated.
    
    Returns:
        int: The factorial of the given integer.
    """
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def is_prime(num: int) -> bool:
    """
    Check if a number is prime.
    
    Args:
        num (int): The number to check for primality.
    
    Returns:
        bool: True if the number is prime, False otherwise.
    """
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def fibonacci(n: int) -> list[int]:
    """
    Generate a list of Fibonacci numbers up to the n-th term.
    
    Args:
        n (int): The number of terms to generate.
    
    Returns:
        list[int]: A list containing the Fibonacci sequence up to the n-th term.
    """
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    fib_sequence = [0, 1]
    for i in range(2, n):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence
