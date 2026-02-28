import functools
import time

# --- Part 1: Generators ---

# Exercise 1: Fibonacci Generator
# Create a generator function that yields Fibonacci numbers indefinitely: 0, 1, 1, 2, 3, 5, 8, 13...
def fibonacci_generator():
    """
    Yields Fibonacci sequence starting from 0, 1.
    """
    # YOUR CODE HERE
    pass

# Exercise 2: Prime Number Filter
# Create a generator function that takes an iterable and yields only the prime numbers from it.
def prime_filter(iterable):
    """
    Yields only prime numbers from the given iterable.
    """
    # YOUR CODE HERE
    pass


# --- Part 2: Function-Based Decorators ---

# Exercise 3: Timer Decorator
# Create a decorator function that prints the time it took for the decorated function to run.
def timer(func):
    """
    Prints the execution time of the decorated function in seconds.
    """
    # YOUR CODE HERE
    pass

@timer
def heavy_calculation():
    time.sleep(1)
    return sum(range(1000000))

# Exercise 4: Cache (Memoization) Decorator
# Create a decorator function that stores results of function calls to avoid recalculating for the same arguments.
def cache(func):
    """
    Caches function results based on arguments.
    """
    # YOUR CODE HERE
    pass

@cache
def slow_square(n):
    time.sleep(1)
    return n * n

# --- Main Testing Area ---

if __name__ == "__main__":
    print("--- Testing Exercise 1: Fibonacci ---")
    # fib = fibonacci_generator()
    # for _ in range(10):
    #     print(next(fib), end=" ")
    # print()

    print("\n--- Testing Exercise 2: Prime Filter ---")
    # nums = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    # print(list(prime_filter(nums)))

    print("\n--- Testing Exercise 3: Timer ---")
    # heavy_calculation()

    print("\n--- Testing Exercise 4: Cache ---")
    # start = time.perf_counter()
    # print(f"Result: {slow_square(5)}")
    # print(f"Time: {time.perf_counter() - start:.4f}s")
    
    # start = time.perf_counter()
    # print(f"Result (cached): {slow_square(5)}")
    # print(f"Time (cached): {time.perf_counter() - start:.4f}s")
