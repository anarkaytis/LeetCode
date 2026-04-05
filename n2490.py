class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        n = len(sentence)
        if sentence[n - 1] != sentence[0]:
            return False
        for i in range(1, n - 1):
            if sentence[i] == " ":
                if sentence[i + 1] != sentence[i - 1]:
                    return False
        return True
