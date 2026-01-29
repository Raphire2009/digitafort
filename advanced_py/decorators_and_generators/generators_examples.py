# Python Generators Example

def my_generator():
    n = 1
    print('This is printed first')
    # Generator function contains yield statements
    yield n

    n += 1
    print('This is printed second')
    yield n

    n += 1
    print('This is printed at last')
    yield n

# Using the generator
a = my_generator()
print(next(a))
print(next(a))
print(next(a))
# The following line would raise a StopIteration exception
# print(next(a))

print("-" * 20)

# Generator for generating squares
def squares(n=10):
    for i in range(1, n + 1):
        yield i * i

# Using the squares generator
for i in squares(5):
    print(i)
