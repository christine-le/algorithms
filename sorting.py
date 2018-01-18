def selection_sort(arr):
    for i in range(0, len(arr)):
        minIdx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[minIdx]:
                minIdx = j
        # Swap
        tmp = arr[i]
        arr[i] = arr[minIdx]
        arr[minIdx] = tmp
    return arr


print selection_sort([7,8,5,4,9,2])
