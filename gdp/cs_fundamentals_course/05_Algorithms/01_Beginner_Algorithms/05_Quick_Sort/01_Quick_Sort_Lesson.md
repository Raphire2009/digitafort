# Quick Sort Lesson

Quick Sort is a highly efficient, in-place, and comparison-based sorting algorithm. It is a divide and conquer algorithm. Quick sort is not a stable sort, meaning that the relative order of equal sort items is not preserved.

## One-Sentence Idea

Pick a **pivot**, put everything smaller on the left and everything larger on the right, then do the same thing to each side.

## Why It Works (Intuition)

After you partition around the pivot:
- Everything left of the pivot is **smaller**.
- Everything right of the pivot is **larger**.
- So the pivot is already in its **final, correct position**.

Now you only need to sort the left and right sides. Keep repeating until each side has 0 or 1 element (already sorted).

## Kid-Friendly Picture

Imagine a line of kids by height and you choose one kid as the **pivot**.
- All shorter kids go to the left.
- All taller kids go to the right.
- The pivot kid is now standing exactly where they belong.

Then you do the same thing to the left group and the right group until each group has 0 or 1 kid.

## Tiny Example (Super Small)

List: `[3, 1, 2]`  
Pivot = `2` (last element)

- Put numbers smaller than `2` on the left.
- Put numbers bigger than `2` on the right.

Result after partition: `[1, 2, 3]`  
Now the pivot `2` is done, and both sides are already size 1.

## How it Works

Quick Sort works by selecting a 'pivot' element from the array and partitioning the other elements into two sub-arrays, according to whether they are less than or greater than the pivot. The sub-arrays are then sorted recursively.

1. **Choose a Pivot:** Select an element from the array. This can be the first element, the last element, the middle element, or a random element.
2. **Partitioning:** Reorder the array so that all elements with values less than the pivot come before the pivot, while all elements with values greater than the pivot come after it. After this partitioning, the pivot is in its final position. This is called the partition operation.
3. **Recursive Sort:** Recursively apply the above steps to the sub-array of elements with smaller values and separately to the sub-array of elements with greater values.

The base case of the recursion is an array of size zero or one, which are sorted by definition.

## Step-by-Step Walkthrough (Small Example)

We will use the **last element as the pivot** (Lomuto partition):

List: `[7, 2, 1, 6, 8, 5, 3, 4]`
- Pivot = `4`

Partitioning process (conceptual):
- Scan from left to right.
- Keep a boundary of items <= pivot.
- Swap items to keep smaller values on the left.

After partitioning around `4`, one possible result is:

`[2, 1, 3, 4, 8, 5, 7, 6]`

Now `4` is in its final position.

Recursively sort the left side `[2, 1, 3]` and the right side `[8, 5, 7, 6]`.

Repeat until all subarrays are size 0 or 1.

### Partition Walkthrough (First Pass Only)

We use two pointers:  
- `j` scans the list  
- `i` marks the end of the "smaller or equal to pivot" section

Start: `i = -1`, pivot = `4`  

| j value | arr[j] | Action | Array after action |
| --- | --- | --- | --- |
| 0 | 7 | 7 > 4, do nothing | `[7, 2, 1, 6, 8, 5, 3, 4]` |
| 1 | 2 | 2 <= 4, i = 0, swap | `[2, 7, 1, 6, 8, 5, 3, 4]` |
| 2 | 1 | 1 <= 4, i = 1, swap | `[2, 1, 7, 6, 8, 5, 3, 4]` |
| 3 | 6 | 6 > 4, do nothing | `[2, 1, 7, 6, 8, 5, 3, 4]` |
| 4 | 8 | 8 > 4, do nothing | `[2, 1, 7, 6, 8, 5, 3, 4]` |
| 5 | 5 | 5 > 4, do nothing | `[2, 1, 7, 6, 8, 5, 3, 4]` |
| 6 | 3 | 3 <= 4, i = 2, swap | `[2, 1, 3, 6, 8, 5, 7, 4]` |

Final swap: swap pivot with `arr[i + 1]`  
Result: `[2, 1, 3, 4, 8, 5, 7, 6]`

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

## Performance (What to Remember)

- **Average time**: O(n log n)
- **Worst time**: O(n^2) if the pivot is always the smallest or largest
- **Space**: O(log n) recursion stack (average)

## Common Confusions (Cleared Up)

- **“Is it sorting while partitioning?”**
  Partitioning only guarantees the pivot is correct. The sides still need sorting.

- **“Why does recursion stop?”**
  A list of size 0 or 1 is already sorted, so no work is needed.

- **“Why can equal values move?”**
  Because swaps do not preserve order. That makes it **not stable**.

## Exercise

1. Trace the execution of Quick Sort on the list `[7, 2, 1, 6, 8, 5, 3, 4]` using the last element as the pivot.
2. The choice of pivot is crucial to the performance of Quick Sort. What happens if you consistently choose the smallest or largest element as the pivot? What is the time complexity in this worst-case scenario?
3. Implement a version of Quick Sort that uses a random element as the pivot.
