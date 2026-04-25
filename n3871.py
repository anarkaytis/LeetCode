class Solution:
    def countCommas(self, n: int) -> int:
        result = 0
        threshold = 1000
        while n >= threshold:
            result += n - threshold + 1
            threshold *= 1000
        return result 
