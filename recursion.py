# Print array elements recursively
def print_array(arr):
  if len(arr) == 0:
    return
  else:
    print arr.pop()
    print_array(arr)
    
  
print_array([1,2,3,4])