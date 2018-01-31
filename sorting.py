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


def insertion_sort(arr):
  for i in range(1, len(arr)):
    for curr in range(i, 0, -1):
      if arr[curr] < arr[curr-1]:
        arr.insert(curr-1, arr.pop(curr))
    
  return arr
  
print insertion_sort([3,2,6,1])

