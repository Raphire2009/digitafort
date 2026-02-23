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

# Simple test cases
def test_binary_search():
    my_sorted_list = [1, 5, 8, 12, 15, 20, 25, 30]
    assert binary_search(my_sorted_list, 20) == 5
    assert binary_search(my_sorted_list, 1) == 0
    assert binary_search(my_sorted_list, 30) == 7
    assert binary_search(my_sorted_list, 8) == 2
    assert binary_search(my_sorted_list, 10) == -1
    print("Binary Search tests passed!")

if __name__ == "__main__":
    test_binary_search()
