class Solution(object):
  def buildString(self, input):
    newString = ''
    count = 1
    curr = input[0]
    
    for next in range(1, len(input)):
      if input[next] == curr:
        count = count + 1
      else:
        newString += str(count) + curr
        count = 1
        
      curr = input[next]
    
    newString += str(count) + curr
    count = 1
    return newString
  
  def countAndSay(self, n):
    
    if n == 1: return '1'
    result = self.buildString('1')
    
    for _ in range(2, n):
      result = self.buildString(result)
      
    return result
    
solution = Solution()
print solution.countAndSay(2)
