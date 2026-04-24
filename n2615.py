class Solution:
    def update(self, num: int, idx: int) -> int:
        if not num in self.d:
            self.d[num] = {"cnt" : 0, "sum" : 0, "idx" : 0}
        self.d[num]["sum"] += abs(idx - self.d[num]["idx"]) * self.d[num]["cnt"]
        self.d[num]["cnt"] += 1
        self.d[num]["idx"] = idx
        return self.d[num]["sum"]

    def distance(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n
        self.d = {}
        for i in range(n):
            result[i] += self.update(nums[i], i)
        self.d = {}
        for i in range(n - 1, -1, -1):
            result[i] += self.update(nums[i], i)
        return result
