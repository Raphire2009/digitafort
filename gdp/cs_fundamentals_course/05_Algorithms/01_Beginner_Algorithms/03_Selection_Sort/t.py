arr = [43, 41, 23,57,45,12]

def selection_sort(arr):
    for i in range(len(arr)):
        print(i)
        min_idx = i
        #arr[min_idx] = 43
        #
        for j in range(i + 1, len(arr)):
            if arr[min_idx] > arr[j]:
                 min_idx =  j
        arr[min_idx], arr[j]  = arr[j], arr[min_idx]

selection_sort(arr)


