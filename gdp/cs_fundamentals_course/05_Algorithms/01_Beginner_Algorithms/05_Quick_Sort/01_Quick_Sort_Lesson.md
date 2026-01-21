# Quick Sort Lesson

Quick Sort is a highly efficient, in-place, and comparison-based sorting algorithm. It is a divide and conquer algorithm. Quick sort is not a stable sort, meaning that the relative order of equal sort items is not preserved.

## How it Works

Quick Sort works by selecting a 'pivot' element from the array and partitioning the other elements into two sub-arrays, according to whether they are less than or greater than the pivot. The sub-arrays are then sorted recursively.

1.  **Choose a Pivot:** Select an element from the array. This can be the first element, the last element, the middle element, or a random element.
2.  **Partitioning:** Reorder the array so that all elements with values less than the pivot come before the pivot, while all elements with values greater than the pivot come after it. After this partitioning, the pivot is in its final position. This is called the partition operation.
3.  **Recursive Sort:** Recursively apply the above steps to the sub-array of elements with smaller values and separately to the sub-array of elements with greater values.

The base case of the recursion is an array of size zero or one, which are sorted by definition.

## Diagram

Here is a visual representation of Quick Sort.

![Quick Sort Diagram](02_Quick_Sort_Diagram.gif)

## Pseudocode

There are many different versions of pseudocode for Quick Sort. Here is one common implementation (Lomuto partition scheme).

```
procedure quickSort(arr, low, high)
  if low < high
    // pi is partitioning index, arr[pi] is now at right place
    pi = partition(arr, low, high)

    // Recursively sort elements before partition and after partition
    quickSort(arr, low, pi - 1)
    quickSort(arr, pi + 1, high)
  end if
end procedure

procedure partition(arr, low, high)
  // pivot (Element to be placed at right position)
  pivot = arr[high]

  i = (low - 1)  // Index of smaller element

  for j from low to high - 1
    // If current element is smaller than or equal to pivot
    if arr[j] <= pivot
      i = i + 1
      swap(arr[i], arr[j])
    end if
  end for
  swap(arr[i + 1], arr[high])
  return (i + 1)
end procedure
```

## Python Implementation

```python
def quick_sort(arr):
    # This is a wrapper function for the recursive sort
    _quick_sort_recursive(arr, 0, len(arr) - 1)
    return arr

def _quick_sort_recursive(arr, low, high):
    if low < high:
        # pi is partitioning index, arr[p] is at the right place
        pi = _partition(arr, low, high)

        # Separately sort elements before partition and after partition
        _quick_sort_recursive(arr, low, pi - 1)
        _quick_sort_recursive(arr, pi + 1, high)

def _partition(arr, low, high):
    i = (low - 1)         # index of smaller element
    pivot = arr[high]     # pivot

    for j in range(low, high):
        # If current element is smaller than or equal to pivot
        if arr[j] <= pivot:
            # increment index of smaller element
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)

# Example usage:
my_list = [10, 7, 8, 9, 1, 5]
sorted_list = quick_sort(my_list)
print("Sorted list is:", sorted_list)
# Output: Sorted list is: [1, 5, 7, 8, 9, 10]
```

## Exercise

1.  Trace the execution of Quick Sort on the list `[7, 2, 1, 6, 8, 5, 3, 4]` using the last element as the pivot.
2.  The choice of pivot is crucial to the performance of Quick Sort. What happens if you consistently choose the smallest or largest element as the pivot? What is the time complexity in this worst-case scenario?
3.  Implement a version of Quick Sort that uses a random element as the pivot.
