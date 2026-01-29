#          0, 1, 2,  3, 4
my_list  = ["d", "b", "F", "c", "a"]



def insertion_sort(arr):
    #print(len(arr))
    for i in range(1, 5):
        print(i) #2
        key = arr[i]
        #arr[j]
        
        #print(key) #4

        j = i -1

        #print(arr[j])
        #print(j) 1
        while j >= 0 and key.lower() < arr[j].lower() :
            arr[j+1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

ll = insertion_sort(my_list)
print(ll)




#ord('a')  checking the unicode (ascii)
#char(97)  checking the number 