def bubble_sort(arr):

    for i in range(len(arr)):
        for j in range(len(arr) - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    
    return arr

arr = [5, 2, 8, 6, 2]
print(bubble_sort(arr))

def bubble_sort_better(arr):
    n = len(arr)

    for mark in range(n - 1, 0, -1):
        swapped = False
        
        for i in range(mark):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
            
        if not swapped:
            break
    
    return arr

arr = [5, 2, 8, 6, 2]
print(bubble_sort_better(arr))