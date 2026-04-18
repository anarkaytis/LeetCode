class Solution:
    def isBalanced(self, num: str) -> bool:
        n = len(num)
        cnt = [0, 0]
        for i in range(n):
            cnt[i & 1] += int(num[i]) 
        return cnt[0] == cnt[1]
