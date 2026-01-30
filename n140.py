class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.Leaf = None

class Solution:
    def bt(self, s: str, idx: int, root: TrieNode, head: TrieNode, soFar: str, result: List[str]) -> None:
        if (idx == len(s)) and (head == root):
            result.append(soFar)
            return
        if idx == len(s):
            return
        if (head == root) and (idx != 0):
            soFar += " "

        head = head.children[ord(s[idx]) - ord('a')]
        if head is None:
            return
        
        if head.Leaf is not None:
            self.bt(s, idx + 1, root, root, soFar + head.Leaf, result)
        self.bt(s, idx + 1, root, head, soFar, result)


    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        # create trie
        # recursive + backtracking

        root = TrieNode()
        for word in wordDict:
            curr = root
            for c in word:
                idx = ord(c) - ord('a')
                if curr.children[idx] is None:
                    curr.children[idx] = TrieNode()
                curr = curr.children[idx]
            curr.Leaf = word
        
        result = []
        self.bt(s, 0, root, root, "", result)
        return (result)
