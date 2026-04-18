class Solution:
    def minOperations(self, nums: List[int]) -> int:
        stack = []
        result = 0
        for num in nums:
            while len(stack) != 0:
                if stack[-1] <= num: 
                    break
                stack.pop()
                result += 1
            if (num != 0) and ((len(stack) == 0) or (stack[-1] < num)):
                stack.append(num)
        return result + len(stack)
