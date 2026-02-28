import sys

# 1. Basic Generator Function (using 'yield')
# Generators are functions that return an iterator, yielding values one by one.
def countdown(n):
    print(f"Counting down from {n}...")
    while n > 0:
        yield n
        n -= 1
    print("Countdown finished.")

print("--- 1. Basic Generator ---")
gen = countdown(3)
for val in gen:
    print(val)

# 2. Lazy Evaluation & Memory Efficiency
# A list stores everything in memory at once; a generator computes values on-the-fly.
def get_large_list(n):
    return [i * i for i in range(n)]

def get_large_gen(n):
    for i in range(n):
        yield i * i

print("\n--- 2. Memory Efficiency ---")
n = 1000000
my_list = get_large_list(n)
my_gen = get_large_gen(n)

print(f"List size (in bytes): {sys.getsizeof(my_list)}")
print(f"Generator size (in bytes): {sys.getsizeof(my_gen)}")

# 3. Generator Expressions
# This is a concise syntax for creating generators, using parentheses ().
print("\n--- 3. Generator Expressions ---")
square_gen = (x**2 for x in range(5))
for square in square_gen:
    print(square)

# 4. Working with Infinite Sequences
# Generators can generate an infinite series without crashing.
def fibonacci_gen():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

print("\n--- 4. Infinite Sequence (Fibonacci) ---")
fib = fibonacci_gen()
for _ in range(8):
    print(next(fib))

# 5. Advanced: send() and throw()
# Generators can also receive values using 'send()'.
def echoing_gen():
    print("Generator started.")
    while True:
        received = yield "Ready"
        if received == "stop":
            print("Stopping generator.")
            break
        print(f"Generator received: {received}")

print("\n--- 5. Interacting with send() ---")
echo = echoing_gen()
# Must 'prime' the generator by calling next() or send(None)
print(next(echo))
print(echo.send("Hello"))
print(echo.send("Python"))
try:
    echo.send("stop")
except StopIteration:
    print("Generator terminated.")

# 6. Delegation with 'yield from'
# 'yield from' allows you to yield from another generator directly.
def internal_gen():
    yield "A"
    yield "B"

def wrapper_gen():
    yield "Start"
    yield from internal_gen()
    yield "End"

print("\n--- 6. yield from Delegation ---")
for char in wrapper_gen():
    print(char)
