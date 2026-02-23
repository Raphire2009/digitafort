# Linear Search Lesson

Linear Search is the simplest search algorithm. It works by checking every element in a list one by one from the beginning until the target element is found or the end of the list is reached.

While not very efficient for large datasets, Linear Search is easy to understand and can be used on unsorted lists, unlike Binary Search.

## How it Works

1.  **Start at the first element:** Begin at index 0 of the list.
2.  **Compare:** Compare the current element with the target value.
3.  **Check for Match:** If the current element matches the target, return its index.
4.  **Move to next:** If it doesn't match, move to the next index in the list.
5.  **Repeat:** Repeat steps 2-4 until the target is found or you reach the end of the list.
6.  **End of list:** If you reach the end of the list without finding the target, return a value indicating the element is not present (usually -1).

## Pseudocode

```
procedure linearSearch(list, target)
  for each index i from 0 to length(list) - 1
    if list[i] == target
      return i
    end if
  end for
  return -1
end procedure
```

## Python Implementation

Here is how you can implement the Linear Search algorithm in Python:

```python
def linear_search(arr, target):
    # Iterate through the array
    for i in range(len(arr)):
        # If the element is found, return its index
        if arr[i] == target:
            return i
    # If the element is not found, return -1
    return -1

# Example usage:
my_list = [10, 5, 20, 15, 30]
target_val = 20
result = linear_search(my_list, target_val)

if result != -1:
    print(f"Element found at index: {result}")
else:
    print("Element not found in the list.")
# Output: Element found at index: 2
```

## Exercise

1.  Given the list `[4, 8, 15, 16, 23, 42]`, trace the Linear Search for target `23`. How many comparisons were made?
2.  What is the time complexity of Linear Search in the best, average, and worst cases?
3.  Why is Linear Search necessary for unsorted lists?
