



def search_f(arr, target):
    for a in arr:
        #print(a)
        #print(target)
        if a == target :
            print("found: {target}")
            return a
    return +1


abc = [5,9,7,21,1]
ddd = search_f(abc, 7)

print(ddd)

"""
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

linear_search(abc, 8)
"""
