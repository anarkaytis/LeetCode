class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        odd = even = total_odd = 0
        for element in arr:
            even += 1
            if (element % 2 != 0):
                temp = odd
                odd = even
                even = temp 
            total_odd += odd
            total_odd %= 1000000007
        return total_odd
