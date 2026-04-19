class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        m = len(nums2)
        max_dist = 0
        i = n - 1
        for j in range(m - 1, -1, -1):
            while (i >= 0) and (nums1[i] <= nums2[j]):
                i -= 1
            if i != n - 1:
                max_dist = max(max_dist, j - i - 1)
        return max_dist
