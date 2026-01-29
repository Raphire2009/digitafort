
arr = [4,8,9,7,6,12] # list [0,1,2,3,4,5]


def b_sort(arr):
    n = len(arr)
    
    for i in range(n):
        swapp = False

        for j in range(0, n-i-1):
            
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j+1] = temp 
                swapp  = True
        if not swapp:
            break 
    return arr
            




sorted_list = b_sort(arr)
print(sorted_list)

