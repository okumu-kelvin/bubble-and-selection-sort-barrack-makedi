def selection_sort(arr):
    n = len(arr)
    
    for i in range(n):
        minpos = i
        for j in range(i + 1, n):
            if arr[j] < arr[minpos]:
                minpos = j
        
        # Swap only if needed
        if minpos != i:
            arr[i], arr[minpos] = arr[minpos], arr[i]
    
    print("Selection sort is done")
arr = [6, 1, 0, 8, 7, 4]
selection_sort(arr)
print(arr) 
