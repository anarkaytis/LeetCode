class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {
            "(" : ")",
            "{" : "}",
            "[" : "]",
        }
        for char in s:
            if char in "({[":
                stack.append(char)
            else:
                if (not stack) or (pairs[stack.pop()] != char):
                    return False
        return (not stack)
