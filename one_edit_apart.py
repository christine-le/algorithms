class Solution(object):
  def oneEditApart(self, word1, word2):
    if len(word1) > len(word2):
      longerWord, shorterWord = word1, word2
    else:
      longerWord, shorterWord = word2, word1
      
    lengthDiff = len(longerWord) - len(shorterWord)
    
    if lengthDiff > 1: 
      return False
    elif lengthDiff == 1:
      for i in range(0, len(longerWord)):
        if i == len(longerWord)-1 or longerWord[i] != shorterWord[i]:
          longerWord = longerWord[:i] + longerWord[i+1:]
          
          if longerWord == shorterWord:
            return True
          else:
            return False
    else:
      oneDiff = 0;
      for i in range(0, len(longerWord)):
        if longerWord[i] != shorterWord[i]:
          oneDiff = oneDiff + 1
          if oneDiff > 1:
            return False
            
      return True

    
solution = Solution()
print solution.oneEditApart("cat", "dog") # false
print solution.oneEditApart("cat", "cats") #true
print solution.oneEditApart("cat", "cut") # true
print solution.oneEditApart("cat", "cast") # true
print solution.oneEditApart("cat", "at") # true
print solution.oneEditApart("cata", "aact") # false

# Pseudocode
# if lengthDiff > 1:
#   return
# if lengthDiff == 1:
#   remove the character from larger string
# if lengthDiff == 0:
#   loop through word1 and compare against word2
  
  
