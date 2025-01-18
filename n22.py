class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        def rec(prefix: str, left: int, right: int) -> None:
            if left > 0:
                rec(prefix + "(", left - 1, right + 1)
            if right > 0:
                rec(prefix + ")", left, right - 1)
            if (left == 0) and (right == 0):
                result.append(prefix)
        
        rec("", n, 0)
        return result
