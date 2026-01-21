# Radix Sort Lesson

Radix Sort is a non-comparative sorting algorithm. It avoids comparison by creating and distributing elements into buckets according to their radix. For elements with more than one significant digit, this bucketing process is repeated for each digit, while preserving the ordering of the prior step, until all digits have been considered.

## How it Works

Radix sort can be applied to data that can be sorted lexicographically, be they integers, words, or even email addresses.

1.  **Find the maximum:** Find the largest element in the list. This is done to determine the number of digits in the largest number.
2.  **Sort by digit:** Starting from the least significant digit (LSD) to the most significant digit (MSD), sort the list based on that digit. A stable sorting algorithm, like Counting Sort, is typically used for this step.
3.  **Repeat:** Repeat the process for all the digits.

## Textual Diagram

Let's trace Radix Sort on the list `[170, 45, 75, 90, 802, 24, 2, 66]`.

The maximum number is 802, which has 3 digits. So, we will have 3 passes.

### Pass 1: Sort by the least significant digit (1s place)

- `170` -> bucket 0
- `90` -> bucket 0
- `802` -> bucket 2
- `2` -> bucket 2
- `24` -> bucket 4
- `45` -> bucket 5
- `75` -> bucket 5
- `66` -> bucket 6

List after pass 1: `[170, 90, 802, 2, 24, 45, 75, 66]`

### Pass 2: Sort by the 10s place digit

- `170` -> bucket 7
- `90` -> bucket 9
- `802` -> bucket 0
- `2` -> bucket 0
- `24` -> bucket 2
- `45` -> bucket 4
- `75` -> bucket 7
- `66` -> bucket 6

List after pass 2: `[802, 2, 24, 45, 66, 170, 75, 90]`

### Pass 3: Sort by the 100s place digit

- `802` -> bucket 8
- `2` -> bucket 0
- `24` -> bucket 0
- `45` -> bucket 0
- `66` -> bucket 0
- `170` -> bucket 1
- `75` -> bucket 0
- `90` -> bucket 0

List after pass 3: `[2, 24, 45, 66, 75, 90, 170, 802]`

The list is now sorted.

## Pseudocode

```
procedure radixSort(list)
  max = findMax(list)
  exp = 1
  while max / exp > 0
    countingSort(list, exp)
    exp = exp * 10
  end while
end procedure

procedure countingSort(list, exp)
  n = length(list)
  output = new array of size n
  count = new array of size 10, initialized to 0

  // Store count of occurrences in count[]
  for i from 0 to n - 1
    index = (list[i] / exp)
    count[index % 10] = count[index % 10] + 1
  end for

  // Change count[i] so that count[i] now contains actual
  // position of this digit in output[]
  for i from 1 to 9
    count[i] = count[i] + count[i - 1]
  end for

  // Build the output array
  i = n - 1
  while i >= 0
    index = (list[i] / exp)
    output[count[index % 10] - 1] = list[i]
    count[index % 10] = count[index % 10] - 1
    i = i - 1
  end while

  // Copy the output array to list[], so that list[] now
  // contains sorted numbers according to current digit
  for i from 0 to n - 1
    list[i] = output[i]
  end for
end procedure
```

## Python Implementation

```python
def radix_sort(arr):
    # Find the maximum number to know number of digits
    max1 = max(arr)

    # Do counting sort for every digit. Note that instead
    # of passing digit number, exp is passed. exp is 10^i
    # where i is current digit number
    exp = 1
    while max1 / exp > 0:
        counting_sort(arr, exp)
        exp *= 10
    return arr

def counting_sort(arr, exp1):
    n = len(arr)
    # The output array elements that will have sorted arr
    output = [0] * (n)
    # initialize count array as 0
    count = [0] * (10)

    # Store count of occurrences in count[]
    for i in range(0, n):
        index = (arr[i] / exp1)
        count[int(index % 10)] += 1

    # Change count[i] so that count[i] now contains actual
    # position of this digit in output array
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Build the output array
    i = n - 1
    while i >= 0:
        index = (arr[i] / exp1)
        output[count[int(index % 10)] - 1] = arr[i]
        count[int(index % 10)] -= 1
        i -= 1

    # Copying the output array to arr[],
    # so that arr now contains sorted numbers
    i = 0
    for i in range(0, len(arr)):
        arr[i] = output[i]

# Example usage:
my_list = [170, 45, 75, 90, 802, 24, 2, 66]
sorted_list = radix_sort(my_list)
print("Sorted list is:", sorted_list)
# Output: Sorted list is: [2, 24, 45, 66, 75, 90, 170, 802]
```

## Exercise

1.  Radix Sort can be implemented to start from the most significant digit (MSD) instead of the least significant digit (LSD). How would the algorithm differ?
2.  What is the time and space complexity of Radix Sort? How does it depend on the number of digits?
3.  Can Radix Sort be used to sort a list of floating-point numbers? If so, how?
