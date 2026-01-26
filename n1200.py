class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        diff = arr[1] - arr[0]
        for i in range(1, len(arr) - 1):
            diff = min(diff, arr[i + 1] - arr[i])
        result = []
        for i in range(len(arr) - 1):
            if arr[i + 1] - arr[i] == diff:
                result.append([arr[i], arr[i + 1]])
        return result
