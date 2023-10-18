

# bubble sort
def bubble(arr):
    l = len(arr)
    for i in range(l-1):
        for j in range(l-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# bubble sort (optimized)
def bubble_opt(arr):
    l = len(arr)
    for i in range(l-1):
        for j in range(l-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

