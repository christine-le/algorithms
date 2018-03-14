n = 1
arr = [[-1 for col in range(n)] for row in range(n)]

curr, row, col = 1, 0, 0
while curr <= n * n:
  while col < n and arr[row][col] == -1:   # move right
    arr[row][col] = curr
    curr = curr + 1
    col = col + 1 
  
  col = col - 1
  row = row + 1
    
  while row < n and arr[row][col] == -1:   # move down
    arr[row][col] = curr
    curr = curr + 1
    row = row + 1
  
  row = row - 1
  col = col - 1
  
  while col >= 0 and arr[row][col] == -1:   # move left
    arr[row][col] = curr
    col = col - 1
    curr = curr + 1
  
  row = row - 1
  col = col + 1
    
  while arr[row][col] == -1:               # move up
    arr[row][col] = curr
    row = row - 1
    curr = curr + 1
  
  row = row + 1
  col = col + 1
    
print arr