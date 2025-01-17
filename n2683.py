class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        state = 1
        for num in derived:
            state ^= num
        return state == 1
