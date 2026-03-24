# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def treeWalk(self, root: Optional[TreeNode], level: int, allLevels: List[int]) -> None:
        if root is None:
            return

        if len(allLevels) <= level:
            allLevels.append(root.val)
        else:
            allLevels[level] += root.val
        
        self.treeWalk(root.left, level + 1, allLevels)
        self.treeWalk(root.right, level + 1, allLevels)

    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        allLevels = []
        self.treeWalk(root, 0, allLevels)
        maxIdx = 0
        n = len(allLevels)
        for i in range(n):
            if allLevels[maxIdx] < allLevels[i]:
                maxIdx = i
        return maxIdx + 1
