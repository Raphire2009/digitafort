
#create the function
# check the length of the array we are sorting 
# make sure the element is a unit in the arr
#create a split in the middle and make sure nothing is remaining
def merge_sort(arr):
    size_of_the_element = len(arr)
    if size_of_the_element > 1:
        mid = size_of_the_element // 2 
        left = arr[:mid]
        print(f"THIS IS THE LEFT",left)
        right = arr[mid:]

        merge_sort(left)#

        merge_sort(right)
        i = j= k = 0  #i is for left index , j is for right index, k is for k index 

        while i < len(left)  and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j +=1
            k += 1
        
        while i < len(left):
            arr[k] = left[i]
            i += 1
            j += 1
        
        while j < len(right):
            arr[k] = right[j]
            j += 1
            i += 1
            
    return arr 

        
        
    



my_list = [12, 11, 13, 5, 6, 7]
sorted_list = merge_sort(my_list)