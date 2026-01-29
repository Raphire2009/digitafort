arr = [43, 41, 23,57,45,12]
def selection_sort(arr):
    for i in range(len(arr)):
       #print(i)
        min_idx  = i 
        for j in range(i + 1, len(arr)):
           #print(j)
            #print(arr[j])
            if arr[min_idx] > arr[j] :
                min_idx = j
                #print(min_idx)
        print(f"before swapp  {arr}")
        print("before adding it :",arr[min_idx])
        print("second add on :", arr[i])
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        print("after swapp:", arr)
    return arr 

selection_sort(arr)



"""
Pass 1 (i=0):
i = 0, min_idx = 0 (initially points to 43)
```
**Inner loop searches for minimum:**
```
j=1: arr[0]=43 > arr[1]=41? YES → min_idx = 1
j=2: arr[1]=41 > arr[2]=23? YES → min_idx = 2
j=3: arr[2]=23 > arr[3]=57? NO  → min_idx = 2
j=4: arr[2]=23 > arr[4]=45? NO  → min_idx = 2
j=5: arr[2]=23 > arr[5]=12? YES → min_idx = 5 ✅
```
**Result:** Minimum is 12 at index 5

**Swap:**
```
Before: [43, 41, 23, 57, 45, 12]
         ↑                   ↑
        i=0              min_idx=5

After:  [12, 41, 23, 57, 45, 43]
         ↑
       sorted
"""







"""
Pass 2 (i=1):

i = 1, min_idx = 1 (points to 41)
```

**Inner loop (only checks unsorted portion):**
```
Sorted: [12]
Unsorted: [41, 23, 57, 45, 43]
           ↑ start searching from here

j=2: arr[1]=41 > arr[2]=23? YES → min_idx = 2
j=3: arr[2]=23 > arr[3]=57? NO  → min_idx = 2
j=4: arr[2]=23 > arr[4]=45? NO  → min_idx = 2
j=5: arr[2]=23 > arr[5]=43? NO  → min_idx = 2 ✅
```

**Swap:**
```
Before: [12, 41, 23, 57, 45, 43]
             ↑   ↑
            i=1 min_idx=2

After:  [12, 23, 41, 57, 45, 43]
         -----  ↑
        sorted
"""


"""
pass 3 (i = 2)
i = 2, min_idx = 2 (points to 41)
```

**Inner loop:**
```
Sorted: [12, 23]
Unsorted: [41, 57, 45, 43]
           ↑

j=3: arr[2]=41 > arr[3]=57? NO  → min_idx = 2
j=4: arr[2]=41 > arr[4]=45? NO  → min_idx = 2
j=5: arr[2]=41 > arr[5]=43? NO  → min_idx = 2 ✅
```

**Swap (with itself):**
```
Before: [12, 23, 41, 57, 45, 43]
                 ↑
               i=2 (already minimum)

After:  [12, 23, 41, 57, 45, 43]
         ---------  ↑
          sorted
"""


"""
pass 4(i=3)
i = 3, min_idx = 3 (points to 57)
```

**Inner loop:**
```
Sorted: [12, 23, 41]
Unsorted: [57, 45, 43]
           ↑

j=4: arr[3]=57 > arr[4]=45? YES → min_idx = 4
j=5: arr[4]=45 > arr[5]=43? YES → min_idx = 5 ✅
```

**Swap:**
```
Before: [12, 23, 41, 57, 45, 43]
                     ↑       ↑
                    i=3   min_idx=5

After:  [12, 23, 41, 43, 45, 57]
         -------------  ↑
            sorted

"""


"""
pass 5(i=4)
i = 4, min_idx = 4 (points to 45)
```

**Inner loop:**
```
Sorted: [12, 23, 41, 43]
Unsorted: [45, 57]
           ↑

j=5: arr[4]=45 > arr[5]=57? NO → min_idx = 4 ✅
```

**Swap (with itself):**
```
After:  [12, 23, 41, 43, 45, 57]
         -----------------  ↑
              sorted
"""


"""

pass 6(i=5)
i = 5, min_idx = 5 (points to 57)
```

**Inner loop doesn't run** (j starts at 6, which is >= len(arr))

**Already sorted!**
```
Final:  [12, 23, 41, 43, 45, 57]
         ----------------------
           fully sorted ✅
"""