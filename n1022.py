# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def walk(self, root: Optional[TreeNode], soFar: int) -> None:
        if root is None:
            return
        soFar = (soFar << 1) | root.val
        if (root.left is None) and (root.right is None):
            self.result += soFar
            return 
        self.walk(root.left, soFar)
        self.walk(root.right, soFar)

    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        self.result = 0
        self.walk(root, 0)
        return self.result
