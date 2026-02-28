# Python Mastery: Generators and Decorators (Function-Based)

Welcome to this in-depth guide. This course focuses on two of Python's most powerful features: **Generators** for efficient data processing and **Decorators** for elegant, reusable logic. 

Both features rely heavily on Python's functional programming capabilities, specifically **first-class functions** and **closures**.

---

## 1. Generators: Memory-Efficient Iteration

Generators are functions that allow you to declare a function that behaves like an iterator. They are the primary tool for "Lazy Evaluation" in Python.

### How They Work Under the Hood
Normally, when a function returns, it loses all its local variables. A generator function, however, uses the `yield` keyword. When `yield` is encountered:
1. The function's state is **suspended**.
2. The value is returned to the caller.
3. The function's local variables and execution pointer are **saved**.
4. When the caller asks for the next value, the function resumes exactly where it left off.

### The Iteration Protocol
A generator automatically implements the Python iterator protocol:
- It has a `__next__()` method (called via `next(gen)`).
- It has an `__iter__()` method (so you can use it in `for` loops).
- It raises `StopIteration` automatically when the function finishes.

### Why Use Generators?
- **Massive Data**: Processing a 10GB log file? A list would crash your RAM. A generator reads it line-by-line, using only a few KBs.
- **Infinite Streams**: You can represent infinite sequences (like the Fibonacci series or a real-time sensor feed) that would be impossible to store in a list.
- **Pipelining**: You can "chain" generators together to create data processing pipelines.

**Explore: [generators_examples.py](./generators_examples.py)**

---

## 2. Decorators: The Power of Closures

A decorator is a function that takes another function and extends its behavior without explicitly modifying it. 

### The Foundation: Closures
To understand decorators, you must understand **Closures**. A closure is a function object that remembers values in enclosing scopes even if they are not present in memory.
```python
def outer(message):
    def inner():
        print(message) # 'inner' remembers 'message' from the outer scope
    return inner
```

### The Anatomy of a Decorator
When you see `@my_decorator`, it is actually "syntactic sugar" for:
`my_function = my_decorator(my_function)`

The execution flow looks like this:
1. **Definition Time**: The decorator wraps the original function.
2. **Call Time**: You call the wrapper, which performs "pre-work," then calls the original function, then performs "post-work."

### Decorator Stacking (Chaining)
You can apply multiple decorators to a single function:
```python
@decorator_one
@decorator_two
def my_func():
    pass
```
This is equivalent to: `my_func = decorator_one(decorator_two(my_func))`. The decorators are applied from the **bottom up**.

### Common Real-World Uses:
- **Logging**: Automatically log every time a specific function is called.
- **Timing**: Measure how long a database query or a heavy calculation takes.
- **Authorization**: Check if a user has permission before running a sensitive function.
- **Caching**: Store the results of expensive function calls (Memoization).

**Explore: [decorators_examples.py](./decorators_examples.py)**

---

## 3. Advanced Comparison: List vs. Generator

| Feature | List / Collection | Generator |
| :--- | :--- | :--- |
| **Storage** | Entire collection in RAM | Only the logic to generate the next item |
| **Access** | Indexing (e.g., `data[5]`) | Sequential only (`next()`) |
| **Speed** | Faster if you need to access items repeatedly | Faster for the first item, better for one-time passes |
| **Infinite?** | No | Yes |

---

## 4. Learning Path & Exercises

1. **Step 1**: Study `generators_examples.py` to see lazy evaluation in action.
2. **Step 2**: Study `decorators_examples.py` to understand wrappers and closures.
3. **Step 3**: Open `practice_exercises.py` and try to implement the missing logic.

### Exercises Overview:
- **Fibonacci Generator**: Handle an infinite mathematical sequence.
- **Prime Filter**: Process an iterable and yield results on-the-fly.
- **Timer Decorator**: Wrap functions to profile their performance.
- **Cache Decorator**: Use a dictionary inside a closure to save states.

**Let's get started!**
