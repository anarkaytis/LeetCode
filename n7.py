class Solution:
   def reverse(self, x: int) -> int:
       is_negative = False
       if x < 0:
           is_negative = True
           x = -x
       reverse = 0
       while x != 0:
           reverse = reverse * 10 + x % 10
           x //= 10
       if is_negative:
           reverse = -reverse
       if (reverse < -(1 << 31)) or (reverse > (1 << 31) - 1):
           reverse = 0
       return reverse 
