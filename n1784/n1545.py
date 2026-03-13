class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        cnt = 0
        while k != 1:
            cnt += 1
            if k & (k - 1) == 0:
                break
            k = (1 << k.bit_length()) - k
        return str(cnt & 1)
