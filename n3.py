class Solution:
   def lengthOfLongestSubstring(self, s: str) -> int:
       l = 0
       unique = set()
       res = 0
       for r in range(len(s)):
           if s[r] not in unique:
               unique.add(s[r])
           else:
               while s[l] != s[r]:
                   unique.remove(s[l])
                   l += 1
               l += 1
           res = max(res, r - l + 1) 
       return res
