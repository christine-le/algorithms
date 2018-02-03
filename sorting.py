# Time complexity: O(n^2)
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

print "selection sort: ", str(selection_sort([7,8,5,4,9,2]))

# Time Complexity: O(n^2)
def insertion_sort(arr):
    for i in range(1, len(arr)):
        curr = i
        val = arr[i]

        while val < arr[curr-1] and curr > 0:
            arr[curr] = arr[curr-1]
            curr -= 1

        arr[curr] = val

    return arr
  
print "insertion sort:", str(insertion_sort([3,2,6,1]))

