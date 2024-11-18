class Solution(object):
   def twoSum(self, nums, target):
       pairs = dict((val, idx) for idx, val in enumerate(nums))
       for idx, val in enumerate(nums):
           if (target - val in pairs) and (idx != pairs[target - val]):
               return [idx, pairs[target - val]]
