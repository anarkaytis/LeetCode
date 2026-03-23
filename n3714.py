class Solution:
    def longestSingle(self, s: str) -> int:
        n = len(s)
        result = 1
        cnt = 1

        for i in range(1, n):
            if s[i] != s[i - 1]:
                cnt = 0
            cnt += 1
            result = max(result, cnt)

        return result
    
    def longestDuo(self, s: str, increase: str, exclude: str) -> int:
        n = len(s)
        level = 0
        result = 0
        firstSeen = {}
        firstSeen[level] = -1

        for i in range(n):
            if s[i] == exclude:
                level = 0
                firstSeen = {}
                firstSeen[level] = i  
            else:
                if s[i] == increase:
                    level += 1
                else:
                    level -= 1
                if level not in firstSeen:
                    firstSeen[level] = i
                else:
                    result = max(result, i - firstSeen[level])

        return result

    def longestTriple(self, s: str) -> int:
        n = len(s)
        result = 0
        level = (0, 0)
        firstSeen = {}
        firstSeen[level] = -1

        for i in range(n):
            if s[i] == 'a':
                level = (level[0] + 2, level[1])
            elif s[i] == 'b':
                level = (level[0] - 1, level[1] + 1)
            else:
                level = (level[0] - 1, level[1] - 1)
            if level not in firstSeen:
                firstSeen[level] = i
            else:
                result = max(result, i - firstSeen[level])

        return result

    def longestBalanced(self, s: str) -> int:
        return max(self.longestSingle(s), self.longestTriple(s),
        self.longestDuo(s, 'a', 'b'), self.longestDuo(s, 'b', 'c'), self.longestDuo(s, 'c', 'a'))
