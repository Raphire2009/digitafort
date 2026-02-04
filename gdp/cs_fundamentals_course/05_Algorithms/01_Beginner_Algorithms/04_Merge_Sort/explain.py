#create the sort 
# count the list
# divide the list
# create the left list and right list
def merge_sort(arr):
    size_of_list = len(arr)
    #arr
    if size_of_list > 1 :
        middle = size_of_list  // 2
        left = arr[:middle]
        right = arr[middle:]
        merge_sort(left)
        merge_sort(right)

        i = j= k = 0

    """
     while i < len(left) and j < len(right) :
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else :
            arr[k] = right[j]
            j += 1
        k += 1 
    """
    """
    while i < len(left):
        arr[k] = left[i]
        i += 1 
        k += 1 
    """
    
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1 
    return arr 
    


my_list = [12, 11, 13, 5, 6, 7]
sorted_list = merge_sort(my_list)





