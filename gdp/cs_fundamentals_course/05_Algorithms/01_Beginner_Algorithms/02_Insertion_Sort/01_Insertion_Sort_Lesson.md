# Insertion Sort Lesson

Insertion Sort is a simple sorting algorithm that builds the final sorted array one item at a time. It is much less efficient on large lists than more advanced algorithms such as quicksort, heapsort, or merge sort. However, it has several advantages:
- Simple implementation
- Efficient for (quite) small data sets
- Efficient for data sets that are already substantially sorted
- More efficient in practice than most other simple quadratic (i.e., O(n^2)) algorithms such as selection sort or bubble sort

## How it Works

The algorithm divides the input list into two parts: a sorted sublist of items which is built up from left to right and a sublist of the remaining unsorted items.

1.  **Start with the second element:** Assume the first element is already sorted.
2.  **Pick the next element:** Take the next unsorted element (the "key").
3.  **Compare and Shift:** Compare the key with the elements in the sorted sublist, moving from right to left. If the key is smaller than an element in the sorted sublist, shift that element to the right to make space.
4.  **Insert the key:** Once you find the correct position for the key (either at the beginning of the list or after an element that is smaller than it), insert the key into that position.
5.  **Repeat:** Repeat steps 2-4 until the entire list is sorted.

## Diagram

Here is a visual representation of Insertion Sort.

![Insertion Sort Diagram](02_Insertion_Sort_Diagram.gif)

## Pseudocode

```
procedure insertionSort(list)
  for i from 1 to length(list)-1
    key = list[i]
    j = i - 1
    while j >= 0 and list[j] > key
      list[j+1] = list[j]
      j = j - 1
    end while
    list[j+1] = key
  end for
end procedure
```

## Python Implementation

```python
def insertion_sort(arr):
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        key = arr[i]
        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Example usage:
my_list = [5, 1, 4, 2, 8]
sorted_list = insertion_sort(my_list)
print("Sorted list is:", sorted_list)
# Output: Sorted list is: [1, 2, 4, 5, 8]
```

## Exercise

1.  Take the list `[12, 11, 13, 5, 6]` and manually trace the Insertion Sort algorithm, showing the state of the list after each insertion.
2.  Explain why Insertion Sort might be a good choice for a list that is already "almost sorted".
3.  Modify the Python `insertion_sort` function to sort a list of strings alphabetically.
