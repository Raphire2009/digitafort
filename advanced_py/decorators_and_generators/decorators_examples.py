import functools
import time

# 1. Basic Decorator (The Anatomy)
# A decorator is a function that takes a function, defines a wrapper, and returns it.
def my_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"--- Calling {func.__name__} ---")
        result = func(*args, **kwargs)
        print(f"--- {func.__name__} finished ---")
        return result
    return wrapper

@my_decorator
def greet(name):
    """Greets the user."""
    print(f"Hello, {name}!")

print("1. Basic Function-Based Decorator")
greet("Pythonista")

# 2. Decorators with Arguments
# To pass arguments TO the decorator itself, you need three levels of nesting.
def repeat(times):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(times):
                value = func(*args, **kwargs)
            return value
        return wrapper
    return decorator_repeat

@repeat(times=3)
def say_hello():
    print("Hello!")

print("\n2. Decorator with Arguments")
say_hello()

# 3. Stateful Decorators (Function-based)
# You can maintain state within a decorator using closures.
def count_calls(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.num_calls += 1
        print(f"Call {wrapper.num_calls} of {func.__name__}")
        return func(*args, **kwargs)
    wrapper.num_calls = 0  # Initializing state on the function object
    return wrapper

@count_calls
def simple_task():
    print("Task performed.")

print("\n3. Stateful Decorator (using function attributes)")
simple_task()
simple_task()

# 4. Real-world: Authorization Simulation
# Decorators are often used to check permissions.
def require_admin(func):
    @functools.wraps(func)
    def wrapper(user_role, *args, **kwargs):
        if user_role != "admin":
            print(f"Access Denied for {user_role}. Admin required.")
            return None
        return func(user_role, *args, **kwargs)
    return wrapper

@require_admin
def delete_database(role):
    print("Database deleted successfully!")

print("\n4. Authorization Decorator")
delete_database("guest")
delete_database("admin")

# 5. Chaining Decorators
# Decorators are applied from bottom to top.
@my_decorator
@repeat(times=2)
def chained_greet():
    print("Chained Greet!")

print("\n5. Chaining Decorators")
chained_greet()
