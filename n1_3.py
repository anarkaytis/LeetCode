class Solution(object):
   def twoSum(self, nums, target):
       indexed = sorted([(val, idx) for idx, val in enumerate(nums)])
       l = 0
       r = len(indexed) - 1
       while l < r:
           diff = indexed[l][0] + indexed[r][0] - target
           if diff == 0:
               return [indexed[l][1], indexed[r][1]]
           elif diff < 0:
               l += 1
           else:
               r -= 1
