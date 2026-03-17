class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        reps = [(num.bit_count(), num) for num in arr]
        reps.sort()
        return [rep[1] for rep in reps]
