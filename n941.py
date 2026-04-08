class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        n = len(arr)
        if (n < 3) or (arr[0] >= arr[1]) or (arr[n - 1] >= arr[n - 2]):
            return False
        i = 0
        for i in range(1, n - 1):
            if arr[i] <= arr[i - 1]:
                break
        for i in range(i + 1, n - 1):
            if arr[i] >= arr[i - 1]:
                return False
        return True
