# Algorithm:  Repeatedly finds the min element in the unsorted portion of the array
# and swaps with the last unsorted element in array
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

# Algorithm:  Iterate through aray and insert current element from the unordered portion 
# of the array into the ordered portion of the array
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
  
print "insertion sort: ", str(insertion_sort([3,2,6,1]))

# Algorithm:  Use a divide and conquer method to continually divide each half of array
# and sort.  Merge each sorted sub-arrays with each iteration.
def merge_sort(arr):
    if len(arr) == 1:
        return arr

    new_array = []
    half = len(arr)/2
    arr1 = merge_sort(arr[0:half])
    arr2 = merge_sort(arr[half:])

    new_array = []
    i =  j = 0
    while i < len(arr1) or j < len(arr2):
        if arr1[i] < arr2[j]:
            new_array.append(arr1[i])
            i += 1
        else:
            new_array.append(arr2[j])
            j += 1

        if i == len(arr1):
            new_array = new_array + arr2[j:]
            break
        if j == len(arr2):
            new_array = new_array + arr1[i:]
            break

    return new_array
    
    # return merge(arr1, arr2)
    

# def merge(arr1, arr2):
#     new_array = []
#     i =  j = 0

#     while i < len(arr1) or j < len(arr2):
        
#         print 'comparing', str(arr1[i]), '<', str(arr2[j])
#         if arr1[i] < arr2[j]:
#             new_array.append(arr1[i])
#             i += 1
#         else:
#             new_array.append(arr2[j])
#             j += 1

#         if i == len(arr1):
#             new_array = new_array + arr2[j:]
#             break
#         if j == len(arr2):
#             new_array = new_array + arr1[i:]
#             break

#     return new_array
    

print "merge sort on [7,8,5,4,9,2,1,3]: \n", str(merge_sort([7,8,5,4,9,2,1,3]))
# print "merge sort: \n", str(merge_sort([4,1,7,3]))