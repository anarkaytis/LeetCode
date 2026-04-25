class Solution:
    def largestOddNumber(self, num: str) -> str:
        result = ""
        n = len(num)
        idx = -1
        for i in range(n - 1, -1 , -1):
            if int(num[i]) & 1 == 1:
                idx = i
                break
        return num[: idx + 1] 
