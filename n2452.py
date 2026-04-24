class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        result = []
        for q in queries:
            for word in dictionary:
                cnt = sum(a != b for a, b in zip(q, word))
                if cnt <= 2:
                    result.append(q)
                    break
        return result
