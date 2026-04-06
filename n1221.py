class Solution:
    def balancedStringSplit(self, s: str) -> int:
        level = 0
        result = 0
        for letter in s:
            if letter == "R":
                level += 1
            else:
                level -= 1
            if level == 0:
                result += 1 
        return result
