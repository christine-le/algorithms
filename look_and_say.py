class Solution(object):
  def countAndSay(self, n):
    newString = ''
    count = 1
    curr = str(n)[0]
    input = str(n)
    
    for next in range(1, len(str(n))):
      if input[next] == curr:
        count = count + 1
      else:
        newString += str(count) + curr
        count = 1
        
      curr = input[next]
    
    newString += str(count) + curr
    count = 1
    
    return newString
    
    
solution = Solution()
print solution.countAndSay(1211)
# 111221

