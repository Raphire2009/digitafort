# Python Functional Programming Examples (map, filter, reduce, lambda)
from functools import reduce

# --- Lambda Functions ---
# A simple lambda function that adds 10 to a number
add_ten = lambda x: x + 10
print(f"15 + 10 = {add_ten(15)}")

# A lambda function that multiplies two numbers
multiply = lambda x, y: x * y
print(f"5 * 6 = {multiply(5, 6)}")

print("-" * 20)

# --- Map ---
# Using map to square all numbers in a list
numbers = [1, 2, 3, 4, 5]
squared_numbers = map(lambda x: x**2, numbers)
print(f"Squared numbers: {list(squared_numbers)}")

print("-" * 20)

# --- Filter ---
# Using filter to get all even numbers from a list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = filter(lambda x: x % 2 == 0, numbers)
print(f"Even numbers: {list(even_numbers)}")

print("-" * 20)

# --- Reduce ---
# Using reduce to find the sum of all numbers in a list
numbers = [1, 2, 3, 4, 5]
sum_of_numbers = reduce(lambda x, y: x + y, numbers)
print(f"Sum of numbers: {sum_of_numbers}")
