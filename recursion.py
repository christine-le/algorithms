# Print array elements recursively
def print_array(arr):
  if len(arr) == 0:
    return
  else:
    print arr.pop()
    print_array(arr)
    
  
print_array([1,2,3,4])


# Recursively check if word is a palindrome
def is_palindrome(word):
  if len(word) == 0:
    return True

  else:
    if word[0] == word[len(word)-1]:
      word = word[1:len(word)-1]
      return is_palindrome(word)
    else:
      return False
  
print is_palindrome('tacocat')


# Write a recursive function that computes the sum of all numbers from 1 to n, where n is given as parameter.
# return the sum 1+ 2+ 3+ ...+ n
def sum(n):
  
  if n < 1:
    return 0
  else:
    return sum(n-1) + n
    
    
print sum(4)

# Write a recursive function that computes and returns the sum of all elements in an array
def find_sum(arr):
  if len(arr) == 1:
    return arr[0]
  else:
    num = arr.pop()
    return num + find_sum(arr)
  
print find_sum([2,5,1,6])

# Write a recursive function that finds and returns the minimum element in an array
def find_min(arr):
  if len(arr) == 1:
    return arr[0]
  else:
    num = arr.pop()
    min = find_min(arr)
    if num < min:
      return num
    else:
      return min
      

print find_min([2,5,3,6])
