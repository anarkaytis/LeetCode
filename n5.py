class Solution:
   def longest_odd(self, s: str, idx: int) -> int:
       longest = 0
       for i in range(1, len(s)):
           if not ((idx - i >= 0) and (idx + i < len(s))):
               break
           if s[idx - i] != s[idx + i]:
               break
           longest = 2 * i + 1
       return longest


   def longest_even(self, s: str, idx: int) -> int:
       longest = 0
       for i in range(1, len(s)):
           if not ((idx + 1 - i >= 0) and (idx + i < len(s))):
               break
           if s[idx + 1 - i] != s[idx + i]:
               break
           longest = 2 * i
       return longest


   def longestPalindrome(self, s: str) -> str:
       max_pal = 1
       start = 0
       for i in range(len(s)):
           candidate = self.longest_odd(s, i)
           if max_pal < candidate:
               max_pal = candidate
               start = i - candidate // 2
           candidate = self.longest_even(s, i)
           if max_pal < candidate:
               max_pal = candidate
               start = i + 1 - candidate // 2
       return s[start : start + max_pal]
