class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        for idx in range(len(strs[0])):
            for word in strs:
                if (idx >= len(word)) or (word[idx] != strs[0][idx]):
                    return prefix
            prefix += strs[0][idx]
        return prefix   
