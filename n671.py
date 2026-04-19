# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse(self, node: Optional[TreeNode]) -> None:
        if node is None:
            return
        self.traverse(node.left)
        self.traverse(node.right)
        if node.val != self.min:
            self.result = min(self.result, node.val)
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        self.min = root.val
        self.result = 1 << 31
        self.traverse(root)
        return self.result if self.result != (1 << 31) else -1
