class Solution:
    def mySqrt(self, x: int) -> int:
        min_b = 0
        max_b = x + 1
        while max_b - min_b > 1:
            mid = (min_b + max_b) // 2
            if mid * mid < x:
                min_b = mid
            elif mid * mid > x:
                max_b = mid
            else:
                return mid
        return min_b
