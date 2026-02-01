class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.Leaf = None

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        root = TrieNode()
        for word in dictionary:
            curr = root
            for c in word:
                idx = ord(c) - ord('a')
                if curr.children[idx] is None:
                    curr.children[idx] = TrieNode()
                curr = curr.children[idx]
            curr.Leaf = word
        result = []
        for word in sentence.split(" "):
            curr = root
            add_word = True
            for c in word:
                idx = ord(c) - ord('a')
                curr = curr.children[idx]
                if curr is None:
                    result.append(word)
                    add_word = False
                    break
                if curr.Leaf is not None:
                    result.append(curr.Leaf)
                    add_word = False
                    break
            if add_word:
                result.append(word)
        return " ".join(result)
