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

# Algorithm:  Uses a divide and conquer method to continually divide each half of array
# and sort.  Merge each sorted sub-arrays with each iteration.
# Time Complexity: (n log n)
def merge_sort(arr):
    if len(arr) == 1:
        return arr

    new_array = []
    half = len(arr)/2
    arr1 = merge_sort(arr[0:half])    # Continuously divides left half and sort
    arr2 = merge_sort(arr[half:])     # Continuously divides right half and sort

    # Sort and merge subarrays
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
    
print "merge sort: ", str(merge_sort([7,8,5,4,9,2,1]))

# Algorithm:  Uses a divide and conquer method to partition an array into two parts.
# Then sort each part in place.
# Time Complexity: O (n log n) average.  O(n^2) worse case
def quick_sort(arr, l, p):
    if l < p:
        p = partition(arr, l, p)
        
        quick_sort(arr, l, p-1)
        quick_sort(arr, p+1, len(arr) - 1)

    return arr

def partition(arr, l, p):
    for r in range(l, p):
        if arr[r] <= arr[p]:
            temp = arr[r]
            arr[r] = arr[l]
            arr[l] = temp
            l += 1

    # Lastly, swap current position with pivot
    temp = arr[l]
    arr[l] = arr[p]
    arr[p] = temp
    return l  # returns new pivot position

my_arr = [7,8,5,1,9,2,4]
print "quick sort: ", str(quick_sort(my_arr, 0, len(my_arr)-1))

######################################################################

def bucketSort(arr):
  buckets = [[], [], [], [], [], [], [], [], [], []]
  
  # insert into buckets
  for i in arr:
    if i < 10:
      bucket = buckets[i]
      bucket.append(i)
    else:
      bucket = buckets[i / 10]
      bucket.append(i)
      
  # sort each bucket
  sortedList = []
  for bucket in buckets:
    if len(bucket) > 1:
      bucket = insertSort(bucket)
    
    sortedList = sortedList + bucket
    
  return sortedList
  
def insertSort(arr):
  for i in range(1, len(arr)):
    curr = i
    val = arr[i]

    while val < arr[curr-1] and curr > 0:
      arr[curr] = arr[curr-1]
      curr -= 1

      arr[curr] = val

  return arr
    
print "bucket sort: ", bucketSort([12,25,54,31,60,78,45,33,40])
######################################################################
def bubbleSort(arr):
  for i in range(len(arr)):
    for j in range(len(arr) - i - 1):
      if arr[j] > arr[j + 1]:
        arr = swap(arr, j, j+1)
  return arr
  
def swap(arr, i, j):
  tmp = arr[i]
  arr[i] = arr[j]
  arr[j] = tmp
  
  return arr

print "bubble sort: ", bubbleSort([21,13,51,19,10,44])