# Binary Search Lesson

Binary Search is a more efficient search algorithm than Linear Search. It works by repeatedly dividing the search space in half until the target element is found or the search space becomes empty.

**Crucially, Binary Search only works on lists that are already sorted.**

## How it Works

1.  **Start at the middle:** Find the middle element of the sorted list.
2.  **Compare:** Compare the middle element with the target value.
3.  **Check for Match:** If the middle element matches the target, return its index.
4.  **Narrow the search:**
    - If the target is **greater** than the middle element, it must be in the right half of the list. Continue the search in the right half.
    - If the target is **less** than the middle element, it must be in the left half of the list. Continue the search in the left half.
5.  **Repeat:** Repeat steps 1-4 with the new half-sized search area.
6.  **End of list:** If the search space becomes empty without finding the target, return -1.

## Visualization

Searching for `20` in `[1, 5, 8, 12, 15, 20, 25, 30]`:

```text
Step 1: [1, 5, 8, 12, 15, 20, 25, 30]  (low=0, high=7)
                  ^ mid=3 (val=12)
        Target 20 > 12, search right half.

Step 2: [15, 20, 25, 30] (low=4, high=7)
              ^ mid=5 (val=20)
        Target 20 == 20, Match Found! Return index 5.
```

## Why is it Logarithmic?
Every step in Binary Search reduces the search area by half. If you have $n$ elements, after one step you have $n/2$, then $n/4$, then $n/8$, and so on. The number of steps required to reach 1 is the power to which 2 must be raised to get $n$. This is the definition of $\log_2 n$.

- For **1,000** elements: ~10 steps
- For **1,000,000** elements: ~20 steps
- For **1,000,000,000** elements: ~30 steps

This is incredibly powerful!

## Pseudocode

```
procedure binarySearch(sortedList, target)
  low = 0
  high = length(sortedList) - 1
  
  while low <= high
    mid = (low + high) / 2
    if sortedList[mid] == target
      return mid
    else if sortedList[mid] < target
      low = mid + 1
    else
      high = mid - 1
    end if
  end while
  
  return -1
end procedure
```

## Python Implementation

Here is how you can implement the Binary Search algorithm in Python:

```python
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        
        # If the element is found at mid
        if arr[mid] == target:
            return mid
        # If the target is greater than mid, ignore the left half
        elif arr[mid] < target:
            low = mid + 1
        # If the target is smaller than mid, ignore the right half
        else:
            high = mid - 1
            
    # If the element is not found, return -1
    return -1

# Example usage:
my_sorted_list = [1, 5, 8, 12, 15, 20, 25, 30]
target_val = 20
result = binary_search(my_sorted_list, target_val)

if result != -1:
    print(f"Element found at index: {result}")
else:
    print("Element not found in the list.")
# Output: Element found at index: 5
```

## Complexity Analysis

Binary Search is significantly faster than Linear Search for large datasets.

### Time Complexity
- **Best Case: $O(1)$** - The target element is found at the middle of the array on the very first try.
- **Average Case: $O(\log n)$** - On average, the search space is halved $\log_2 n$ times.
- **Worst Case: $O(\log n)$** - The target element is at the far ends of the array or not present at all.

### Space Complexity
- **Iterative Approach: $O(1)$** - Only a few variables (`low`, `high`, `mid`) are used regardless of the input size.
- **Recursive Approach: $O(\log n)$** - Due to the call stack depth in recursion.

## Binary Search vs. Linear Search

| Feature | Linear Search | Binary Search |
| :--- | :--- | :--- |
| **Prerequisite** | None (can be unsorted) | Must be **Sorted** |
| **Worst-case Time** | $O(n)$ | $O(\log n)$ |
| **Best-case Time** | $O(1)$ | $O(1)$ |
| **Approach** | Sequential | Divide and Conquer |
| **Efficiency** | Better for small lists | Better for large lists |

## Recursive Implementation

While the iterative version is often preferred for its space efficiency, the recursive version is a classic example of the "Divide and Conquer" strategy.

```python
def binary_search_recursive(arr, target, low, high):
    if low > high:
        return -1
    
    mid = (low + high) // 2
    
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, high)
    else:
        return binary_search_recursive(arr, target, low, mid - 1)

# Example usage:
# result = binary_search_recursive(my_list, target, 0, len(my_list) - 1)
```

## Exercise

1.  Given the sorted list `[10, 20, 30, 40, 50, 60, 70, 80, 90]`, trace the Binary Search for target `70`. Write down the values of `low`, `high`, and `mid` for each step.
2.  What is the time complexity of Binary Search in the best, average, and worst cases? (Hint: How many times can you halve a number before it reaches 1?)
3.  Why can't Binary Search be used on an unsorted list?
