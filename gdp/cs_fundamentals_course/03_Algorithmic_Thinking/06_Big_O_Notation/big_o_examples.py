# big_o_examples.py

# O(1) - Constant Time Example
def access_element(arr, index):
    """
    Accessing an element in an array by its index.
    Time Complexity: O(1)
    """
    if 0 <= index < len(arr):
        return arr[index]
    else:
        return "Index out of bounds"

# O(n) - Linear Time Example
def linear_search(arr, target):
    """
    Searches for a target element in an array.
    Time Complexity: O(n)
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# O(n^2) - Quadratic Time Example
def bubble_sort(arr):
    """
    Sorts an array using the Bubble Sort algorithm.
    Time Complexity: O(n^2)
    """
    n = len(arr)
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# O(log n) - Logarithmic Time Example (Binary Search)
def binary_search(arr, target):
    """
    Searches for a target element in a sorted array using Binary Search.
    Time Complexity: O(log n)
    """
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# O(n log n) - Linearithmic Time Example (Merge Sort - simplified conceptual)
# Note: A full implementation of Merge Sort is more complex and typically involves
# recursion and additional space. This is a conceptual representation.
def merge_sort_conceptual(arr):
    """
    Conceptual representation of an O(n log n) algorithm like Merge Sort.
    Actual Merge Sort implementation is more involved.
    Time Complexity: O(n log n)
    """
    if len(arr) <= 1:
        return arr

    # Divide step (log n)
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Conquer step (n operations for merging at each level)
    # The actual merge_sort would call itself recursively on left_half and right_half
    # followed by a merge operation.
    # For simplicity, we just return a sorted version for this example.
    # In a real merge sort, the merging step takes O(n) time.
    return sorted(arr) # Python's Timsort is O(n log n)

# O(2^n) - Exponential Time Example (Recursive Fibonacci - naive)
def fibonacci_exponential(n):
    """
    Calculates the nth Fibonacci number using a naive recursive approach.
    Time Complexity: O(2^n)
    """
    if n <= 1:
        return n
    else:
        return fibonacci_exponential(n-1) + fibonacci_exponential(n-2)

# O(n!) - Factorial Time Example (Permutations - conceptual)
# Generating all permutations of a list. This is a highly conceptual example
# as a full implementation is quite involved and rarely used for large n.
def factorial_permutations_conceptual(arr):
    """
    Conceptual representation of an O(n!) algorithm.
    Generates all permutations of a list.
    Time Complexity: O(n!)
    """
    import itertools
    # itertools.permutations is highly optimized, but conceptually, generating
    # all permutations of length n involves n! operations.
    return list(itertools.permutations(arr))

if __name__ == "__main__":
    my_list = [10, 4, 8, 2, 6, 1, 9, 3, 7, 5]
    sorted_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    print("--- O(1) Constant Time ---")
    print(f"Access element at index 3 in {my_list}: {access_element(my_list, 3)}")
    print(f"Access element at index 9 in {my_list}: {access_element(my_list, 9)}")
    print(f"Access element at index 10 (out of bounds) in {my_list}: {access_element(my_list, 10)}")

    print("
--- O(n) Linear Time ---")
    print(f"Linear search for 6 in {my_list}: {linear_search(my_list, 6)}")
    print(f"Linear search for 100 in {my_list}: {linear_search(my_list, 100)}")

    print("
--- O(n^2) Quadratic Time ---")
    print(f"Bubble sort {list(my_list)}: {bubble_sort(list(my_list))}") # Pass a copy

    print("
--- O(log n) Logarithmic Time ---")
    print(f"Binary search for 7 in {sorted_list}: {binary_search(sorted_list, 7)}")
    print(f"Binary search for 100 in {sorted_list}: {binary_search(sorted_list, 100)}")

    print("
--- O(n log n) Linearithmic Time (Conceptual) ---")
    print(f"Merge Sort Conceptual {list(my_list)}: {merge_sort_conceptual(list(my_list))}") # Pass a copy

    print("
--- O(2^n) Exponential Time ---")
    # WARNING: This will be very slow for n > 20-25
    print(f"Fibonacci (exponential) for 5: {fibonacci_exponential(5)}")
    print(f"Fibonacci (exponential) for 10: {fibonacci_exponential(10)}")

    print("
--- O(n!) Factorial Time (Conceptual) ---")
    # WARNING: This will be very slow for n > 10
    small_list = [1, 2, 3]
    print(f"Permutations of {small_list}: {factorial_permutations_conceptual(small_list)}")
    # larger_list = [1, 2, 3, 4]
    # print(f"Permutations of {larger_list}: {factorial_permutations_conceptual(larger_list)}") # Uncomment with caution
