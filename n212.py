class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.Leaf = None

class Solution:
    def dfs(self, board: List[List[str]], visited: List[List[bool]], x: int, y: int, trie: TrieNode, result: set) -> None:
        if (x < 0) or (x >= len(board)) or (y < 0) or (y >= len(board[0])):
            return

        if visited[x][y]:
            return

        trie = trie.children[ord(board[x][y]) - ord('a')]

        if trie is None:
            return

        if trie.Leaf is not None:
            result.add(trie.Leaf)

        visited[x][y] = True
        self.dfs(board, visited, x + 1, y, trie, result)
        self.dfs(board, visited, x - 1, y, trie, result)
        self.dfs(board, visited, x, y + 1, trie, result)
        self.dfs(board, visited, x, y - 1, trie, result)
        visited[x][y] = False

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for word in words:
            curr = root
            for c in word:
                idx = ord(c) - ord('a')
                if curr.children[idx] is None:
                    curr.children[idx] = TrieNode()
                curr = curr.children[idx]
            curr.Leaf = word
        
        result = set()
        m = len(board)
        n = len(board[0])
        visited = [[False] * n for _ in range(m)]
        for x in range(m):
            for y in range(n):
                self.dfs(board, visited, x, y, root, result)
        return list(result)   
