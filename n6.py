class Solution:
   def convert(self, s: str, numRows: int) -> str:
       result = ""
       cycle = 2 * numRows - 2
       if cycle == 0:
           return s
       for i in range(0, len(s), cycle):
           result += s[i]
       for j in range(1, numRows - 1):
           for i in range(0, len(s), cycle):
               if i + j < len(s):
                   result += s[i + j]
               if i + cycle - j < len(s):
                   result += s[i + cycle - j]
       for i in range(0, len(s), cycle):
           if i + numRows - 1 < len(s):
               result += s[i + numRows - 1]
       return result
