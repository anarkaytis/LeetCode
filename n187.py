class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        repository = {}
        result = []
        for i in range(len(s) - 9):
            seq = s[i : (i + 10)]
            repository[seq] = repository.get(seq, 0) + 1
        for seq, cnt in repository.items():
            if cnt > 1:
                result.append(seq)
        return result
