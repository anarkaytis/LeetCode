class Solution:
    def match0(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        n = len(mat)
        for i in range(n):
            for j in range(n):
                if mat[i][j] != target[i][j]:
                    return False
        return True
    
    def match90(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        n = len(mat)
        for i in range(n):
            for j in range(n):
                if mat[i][j] != target[j][n - 1 - i]:
                    return False
        return True
    
    def match180(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        n = len(mat)
        for i in range(n):
            for j in range(n):
                if mat[i][j] != target[n - 1 - i][n - 1 - j]:
                    return False
        return True

    def match270(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        n = len(mat)
        for i in range(n):
            for j in range(n):
                if mat[i][j] != target[n - 1 - j][i]:
                    return False
        return True

    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        if self.match0(mat, target):
            return True
        if self.match90(mat, target):
            return True
        if self.match180(mat, target):
            return True
        if self.match270(mat, target):
            return True
        return False
