# Heap Sort Lesson

Heap Sort is a comparison-based sorting technique based on a Binary Heap data structure. It is similar to selection sort where we first find the maximum element and place the maximum element at the end. We repeat the same process for the remaining elements.

Heap sort is an in-place algorithm but it is not a stable sort.

## How it Works

Heap sort can be divided into two parts:
1.  **Heapify:** In this step, we build a heap from the input array. We can use a max-heap to sort in ascending order and a min-heap to sort in descending order. A max-heap is a complete binary tree in which the value in each internal node is greater than or equal to the values in the children of that node.
2.  **Extraction:** After building the heap, the largest item is stored at the root of the heap. We swap it with the last item of the heap and reduce the size of the heap by one. Finally, we heapify the root of the tree. We repeat this process until all the items of the list are sorted.

## Textual Diagram

Let's trace Heap Sort with the example `[4, 10, 3, 5, 1]`.

### 1. Build Max-Heap

We start from the last non-leaf node and `heapify` it. The array represents a nearly complete binary tree.

Initial Array: `[4, 10, 3, 5, 1]`
Tree representation:
```
      4
     / \
    10   3
   / \
  5   1
```

- **Heapify index 1 (value 10):** Compare 10 with its children (5, 1). 10 is the largest. No change.
- **Heapify index 0 (value 4):** Compare 4 with its children (10, 3). 10 is largest. Swap 4 and 10.
  - Array becomes `[10, 4, 3, 5, 1]`
  - Now, we must recursively heapify the affected sub-tree, starting at index 1 (the new position of 4).
  - Compare 4 with its children (5, 1). 5 is largest. Swap 4 and 5.
  - Array becomes `[10, 5, 3, 4, 1]`

The max-heap is built. The array is `[10, 5, 3, 4, 1]`.

### 2. Sort by Extraction

Now, we repeatedly swap the root (the max element) with the last element of the unsorted section and heapify the root.

- **Pass 1:**
  - Swap `10` and `1`. Array: `[1, 5, 3, 4, 10]`. Sorted part: `[10]`
  - Heapify the root (`1`). Swap with `5`. Array becomes `[5, 4, 3, 1, 10]`.

- **Pass 2:**
  - Swap `5` and `1`. Array: `[1, 4, 3, 5, 10]`. Sorted part: `[5, 10]`
  - Heapify the root (`1`). Swap with `4`. Array becomes `[4, 1, 3, 5, 10]`.

- **Pass 3:**
  - Swap `4` and `3`. Array: `[3, 1, 4, 5, 10]`. Sorted part: `[4, 5, 10]`
  - Heapify the root (`3`). It is in the correct place.

- **Pass 4:**
  - Swap `3` and `1`. Array: `[1, 3, 4, 5, 10]`. Sorted part: `[3, 4, 5, 10]`
  - Heapify the root (`1`). It is in the correct place.

The final sorted array is `[1, 3, 4, 5, 10]`.

## Pseudocode

```
procedure heapSort(arr)
    n = length(arr)

    // Build a maxheap.
    for i from n / 2 - 1 down to 0
        heapify(arr, n, i)
    end for

    // One by one extract elements
    for i from n - 1 down to 0
        swap(arr[0], arr[i])
        heapify(arr, i, 0)
    end for
end procedure

procedure heapify(arr, n, i)
    largest = i  // Initialize largest as root
    left = 2 * i + 1
    right = 2 * i + 2

    // See if left child of root exists and is greater than root
    if left < n and arr[i] < arr[left]
        largest = left
    end if

    // See if right child of root exists and is greater than root
    if right < n and arr[largest] < arr[right]
        largest = right
    end if

    // Change root, if needed
    if largest != i
        swap(arr[i], arr[largest])
        // Heapify the root.
        heapify(arr, n, largest)
    end if
end procedure
```

## Python Implementation

```python
def heap_sort(arr):
    n = len(arr)

    # Build a maxheap.
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # One by one extract elements
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        heapify(arr, i, 0)
    return arr

def heapify(arr, n, i):
    largest = i  # Initialize largest as root
    l = 2 * i + 1  # left = 2*i + 1
    r = 2 * i + 2  # right = 2*i + 2

    # See if left child of root exists and is greater than root
    if l < n and arr[i] < arr[l]:
        largest = l

    # See if right child of root exists and is greater than root
    if r < n and arr[largest] < arr[r]:
        largest = r

    # Change root, if needed
    if largest != i:
        arr[i], arr[l] = arr[l], arr[i]  # swap

        # Heapify the root.
        heapify(arr, n, largest)

# Example usage:
my_list = [12, 11, 13, 5, 6, 7]
sorted_list = heap_sort(my_list)
print("Sorted list is:", sorted_list)
# Output: Sorted list is: [5, 6, 7, 11, 12, 13]

```

## Exercise

1.  What is a binary heap? Explain the difference between a min-heap and a max-heap.
2.  Trace the execution of Heap Sort on the list `[4, 10, 3, 5, 1]`. Show the state of the array after the initial heapify and after each extraction.
3.  The `heapify` function is a key part of the Heap Sort algorithm. What is its time complexity and why?
