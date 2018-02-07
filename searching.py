# Simple recursive binary search algorithm
# Passes in upper and lower bounds to avoid creating multiple sub-arrays
def binary_search(arr, lower, upper, target):
    mid = lower + (upper - lower) / 2

    if lower > upper:
    	return -1
    elif arr[mid] == target:
    	return mid
    else:
	    if arr[mid] > target:
	    	upper = mid - 1
	    else:
	    	lower = mid + 1
	    return binary_search(arr, lower, upper, target)

my_array = [1,2,3,4,5,6,7,8,9,10]
print binary_search(my_array, 0, len(my_array)-1, 10)
