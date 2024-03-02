from functools import cache

@cache # This decorator caches the results of the function, so that it doesn't have to be recalculated every time it's called with the same arguments
# cache can only be used with functions that have no side effects (i.e. they don't change anything outside of their scope) aka pure functions
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def print_fibonacci_sequence(n, current=0):
    if current < n:
        print(fibonacci(current))
        print_fibonacci_sequence(n, current + 1)

# Example usage: Print the first 10 Fibonacci numbers
print_fibonacci_sequence(10)
