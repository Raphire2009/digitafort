def insertion_sort(arr):

    for i in range(1, len(arr)):
        key = arr[i] #1
        #print(key)
        #print(i)
    
        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i - 1
        #print(j)
        #j = O
        #key = 1
        #arr[j] = 5
        #arr[j + 1] = 1
        #arr[j + 1 ]  = arr[j] = 5

        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
            print(j)
        arr[j + 1] = key
    return arr
        # [0 ,1, 2, 3, 4]
my_list = [5, 1, 4, 2, 8]
sorted_list = insertion_sort(my_list)










