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

