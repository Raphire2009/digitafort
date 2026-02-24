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

# Comprehensive test cases
def test_binary_search():
    my_sorted_list = [1, 5, 8, 12, 15, 20, 25, 30]
    
    # Test iterative version
    print("Testing iterative binary search...")
    assert binary_search(my_sorted_list, 20) == 5
    assert binary_search(my_sorted_list, 1) == 0
    assert binary_search(my_sorted_list, 30) == 7
    assert binary_search(my_sorted_list, 8) == 2
    assert binary_search(my_sorted_list, 10) == -1
    
    # Edge cases for iterative
    assert binary_search([], 5) == -1           # Empty list
    assert binary_search([10], 10) == 0         # Single element (found)
    assert binary_search([10], 5) == -1          # Single element (not found)
    
    # Test recursive version
    print("Testing recursive binary search...")
    assert binary_search_recursive(my_sorted_list, 20, 0, 7) == 5
    assert binary_search_recursive(my_sorted_list, 1, 0, 7) == 0
    assert binary_search_recursive(my_sorted_list, 30, 0, 7) == 7
    assert binary_search_recursive(my_sorted_list, 8, 0, 7) == 2
    assert binary_search_recursive(my_sorted_list, 10, 0, 7) == -1
    
    # Edge cases for recursive
    assert binary_search_recursive([], 5, 0, -1) == -1
    assert binary_search_recursive([10], 10, 0, 0) == 0
    assert binary_search_recursive([10], 5, 0, 0) == -1
    
    print("All Binary Search tests passed!")

if __name__ == "__main__":
    test_binary_search()
