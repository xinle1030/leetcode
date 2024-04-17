def merge(arr1, arr2):
    i = 0
    j = 0
    ret = []

    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            ret.append(arr1[i])
            i += 1
        else:
            ret.append(arr2[j])
            j += 1
    
    if i < len(arr1):
        ret += arr1[i:]
    if j < len(arr2):
        ret += arr2[j:]
    
    return ret

def merge_sort(arr):
    if len(arr) > 1:
        m = len(arr) // 2

        arr1 = merge_sort(arr[:m])
        arr2 = merge_sort(arr[m:])
        
        return merge(arr1, arr2)
    else:
        return arr

arr = [5, 2, 8, 6, 2]
print(merge_sort(arr))