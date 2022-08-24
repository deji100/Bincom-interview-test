def recursive_search(arr, low, high, x):
    if high >= low:
 
        mid = (high + low) // 2
 
        if arr[mid] == x:
            return mid
 
        elif arr[mid] > x:
            return recursive_search(arr, low, mid - 1, x)

        else:
            return recursive_search(arr, mid + 1, high, x)
    
    else:
        return -1
    
 
arr = [ 2, 3, 4, 10, 40 ]
x = 10
 
result = recursive_search(arr, 0, len(arr), x)
 
if result != -1:
    print()
    print("Element is present at index", str(result))
    print()
else:
    print()
    print("Element is not present in array")
    print()
