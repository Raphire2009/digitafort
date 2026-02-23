def linear_search(arr, target):
    # Iterate through the array
    for i in range(len(arr)):
        # If the element is found, return its index
        if arr[i] == target:
            return i
    # If the element is not found, return -1
    return -1

# Simple test cases
def test_linear_search():
    assert linear_search([10, 5, 20, 15, 30], 20) == 2
    assert linear_search([10, 5, 20, 15, 30], 10) == 0
    assert linear_search([10, 5, 20, 15, 30], 30) == 4
    assert linear_search([10, 5, 20, 15, 30], 100) == -1
    print("Linear Search tests passed!")

if __name__ == "__main__":
    test_linear_search()
