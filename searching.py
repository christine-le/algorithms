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
print 'binary_search: ', binary_search(my_array, 0, len(my_array)-1, 10)

# Count number of paths from the root that sum to target.
# Target: 5
#      2
#     / \
#    3 -3
#  /   / \
# 0   8   6
# Return Val: 2

#       2
#     /  \
#    1   -3
#  /  \   / \
# 0    1  8   6
#     /
#    1
class Node(object):
    def __init__ (self, data):
        self.data = data
        self.left = None
        self.right = None
        
node = Node(2)
node.left = Node(3)
node.right = Node(-3)
node.left.left = Node(1)
node.right.left = Node(8)
node.right.right = Node(6)

# node = Node(2)
# node.left = Node(1)
# node.right = Node(-3)
# node.left.left = Node(0)
# node.left.right = Node(1)
# node.left.right.left = Node(1)
# node.right.left = Node(8)
# node.right.right = Node(6)

def count(root, target, sum, cnt):
    if root == None:
        return 0
    else:
        sum = root.data + sum

        if (sum == 5):
            cnt += 1

        if root.left and sum < 5:
            cnt = count(root.left, target, sum, cnt)

        if root.right and sum < 5:
            cnt = count(root.right, target, sum, cnt)
        
        return cnt

print 'count: \n', count(node, 5, 0, 0)

    
