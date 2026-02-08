# Big O Notation - Take-Home Exercises

These exercises are designed to solidify your understanding of Time and Space Complexity using Big O Notation. Work through them to practice analyzing algorithms and comparing their efficiency.

## Exercise 1: Identify Time Complexity

For each of the following code snippets, determine its **Time Complexity** using Big O Notation. Assume `n` is the size of the input array or list.

### Problem 1.1

```python
def sum_array(arr):
    total = 0
    for x in arr:
        total += x
    return total
```

### Problem 1.2

```python
def print_pairs(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n):
            print(arr[i], arr[j])
```

### Problem 1.3

```python
def find_in_sorted_array(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return False
```

### Problem 1.4

```python
def process_data(data):
    # Part 1: Linear scan
    for item in data:
        if item == "special":
            print("Found special item!")
            break

    # Part 2: Another linear scan
    for i in range(len(data)):
        data[i] = data[i] * 2
    return data
```

### Problem 1.5

```python
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
```

## Exercise 2: Identify Space Complexity

For each of the following code snippets, determine its **Space Complexity** using Big O Notation. Assume `n` is the size of the input array or list.

### Problem 2.1

```python
def reverse_array_in_place(arr):
    left, right = 0, len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr
```

### Problem 2.2

```python
def create_new_array(arr):
    new_arr = []
    for x in arr:
        new_arr.append(x * 2)
    return new_arr
```

### Problem 2.3

```python
def fibonacci_memoized(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci_memoized(n - 1, memo) + fibonacci_memoized(n - 2, memo)
    return memo[n]
```

## Exercise 3: Algorithm Comparison and Best Choice

Consider a scenario where you need to search for an element within a dataset of `N` items.

### Problem 3.1

You have an unsorted list of `N` integers. You need to find if a specific integer `X` exists in this list.
*   What is the best possible Time Complexity for this operation?
*   What is the typical Time Complexity if you iterate through the list?

### Problem 3.2

You have a *sorted* list of `N` integers. You need to find if a specific integer `X` exists in this list.
*   What is the most efficient search algorithm you can use?
*   What is its Time Complexity? Justify your answer.

### Problem 3.3

You need to sort a list of `N` items. You can choose between an algorithm with `O(N^2)` complexity (e.g., Bubble Sort) and an algorithm with `O(N log N)` complexity (e.g., Merge Sort).
*   Which algorithm would you choose for very large `N` (e.g., `N = 1,000,000`)?
*   Explain *why* your chosen algorithm is better for large `N`, referring to how their growth rates differ.

## Exercise 4: Real-World Scenario

Imagine you are building a social media application. One feature is to show a user all posts made by their friends.

### Problem 4.1

If a user has `F` friends, and each friend has `P` posts, describe an approach to gather all posts from all friends.
*   What would be the Time Complexity of this operation in terms of `F` and `P`?
*   What assumptions are you making about how posts are retrieved (e.g., direct lookup, iterating through all posts)?

### Problem 4.2

Now, imagine you need to find the 10 most recent posts from *all* friends combined.
*   Briefly describe an efficient approach to do this.
*   What might be the Time Complexity of this optimized approach, and why?

---

**Remember to:**
*   Clearly state your Big O answer (e.g., `O(n)`, `O(log n)`, `O(1)`, `O(n^2)`).
*   Provide a brief justification or explanation for your answer, especially for the comparison and scenario-based questions.
