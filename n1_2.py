class Solution(object):
   def twoSum(self, nums, target):
       pairs = {}
       for idx, val in enumerate(nums):
           if target - val in pairs:
               return [idx, pairs[target - val]]
           pairs[val] = idx
