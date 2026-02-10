# Quick Sort implementation with line-by-line comments for learning

def quick_sort(arr):  # Public wrapper that sorts the whole list
    
    _quick_sort_recursive(arr, 0, len(arr) - 1)  # Sort from first to last index
    return arr  # Return the now-sorted list


def _quick_sort_recursive(arr, low, high):  # Sort the subarray from low to high
    if low < high:  # Only sort if there are at least 2 elements
        # pi is the partition index; arr[pi] is in its final correct position
        pi = _partition(arr, low, high)  # Rearrange around pivot and get pivot index

        # Recursively sort left side (elements <= pivot)
        _quick_sort_recursive(arr, low, pi - 1)  # Sort subarray before the pivot
        # Recursively sort right side (elements > pivot)
        _quick_sort_recursive(arr, pi + 1, high)  # Sort subarray after the pivot


def _partition(arr, low, high):  # Move smaller values left, bigger values right
    i = (low - 1)  # i tracks the end of the "<= pivot" region
    pivot = arr[high]  # Choose the last element as the pivot

    for j in range(low, high):  # Scan from low up to high - 1
        # If current element is smaller than or equal to pivot
        if arr[j] <= pivot:  # This element should go to the left side
            i = i + 1  # Expand the "<= pivot" region
            arr[i], arr[j] = arr[j], arr[i]  # Swap current into the left region

    arr[i + 1], arr[high] = arr[high], arr[i + 1]  # Place pivot in final position
    return (i + 1)  # Return the pivot's final index


# Example usage:
my_list = [10, 7, 8, 9, 1, 5]  # Create a sample list
sorted_list = quick_sort(my_list)  # Sort the list in place
print("Sorted list is:", sorted_list)  # Display the result
