class Solution:
    def lexSmallestNegatedPerm(self, n: int, target: int) -> List[int]:
        result = []
        sum = n * (n + 1) // 2
        if (abs(target) > sum) or ((sum - target) & 1 == 1):
            return result

        while sum - 2 * n >= target:
            result.append(-n)
            sum -= 2 * n
            n -= 1
            if n == 0:
                break

        num = (sum - target) // 2
        if num != 0:
            result.append(-num)
        for i in range(1, n + 1):
            if i != num:
                result.append(i)
                
        return result
